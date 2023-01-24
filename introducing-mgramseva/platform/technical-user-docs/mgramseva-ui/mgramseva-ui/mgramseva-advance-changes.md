# mGramSeva - Advance Changes

## **Overview**

Water Connection advance changes are added to allow the customer to pay advance amount. This amount is adjusted when a new demand is generated. We can enable or disable advance based on the configuration.

## Pre-requisites

Before you proceed with the documentation, make sure the following pre-requisites are met -

* _Java 8_
* Kafka server is up and running
* egov-persister service is running and has the water service persister configs path added to it
* PSQL server is running and a database is created to store water connection/application data
* The following services should be up and running:
  * egov-persister
  * egov-mdms
  * ws-services
  * billing-service
  * ws-calculator
  * egov-apportion-service

## Key Functionalities

* Accepts advance amount during water connection creation and while collecting payment
* Creates demand for consumer-type water connection-advance
* Adjusts the new demand with existing advance with apportion service

## Deployment Details

Deploy the latest version of ws-service, ws-calculator, billing-service, egov-apportion-service

## MDMS Configuration

**Billing service tax head configuration**

```
{
      "businessService": "ws-services-calculation",
      "code": "WS",
      "collectionModesNotAllowed": [
        "DD",
        "CHEQUE",
        "CARD",
        "OFFLINE_NEFT",
        "OFFLINE_RTGS",
        "POSTAL_ORDER",
        "ONLINE"
      ],
      "partPaymentAllowed": true,
      "isAdvanceAllowed": true,
      "demandUpdateTime": 86400000,
      "isVoucherCreationEnabled": false,
      "billGineiURL" : "egov-searcher/bill-genie/waterbills/_get",
      "isBillAmendmentEnabled":true
    }
```

**Tax head master service configuration**

```
{
      "category": "ADVANCE_COLLECTION",
      "service": "WS",
      "name": "Ws advance carry forward",
      "code": "WS_ADVANCE_CARRYFORWARD",
      "isDebit": true,
      "isActualDemand": false,
      "order": "0",
      "isRequired": true,
      "IsBillamend": false
    },
```

### **Existing service code changes**

#### **Billing service changes:**

* Creating a new bill for the advance amount in BillServiceV2.\
  Removing the following line while adding the bill objects to the list\
  if (billAmount.compareTo(BigDecimal.ZERO) >= 0)
* Passing Active status filter for demand search during apportioning in DemandService.\
  DemandCriteria searchCriteria = DemandCriteria.builder().tenantId(tenantId)\
  .status(Demand.StatusEnum.ACTIVE.toString()).consumerCode(Collections.singleton(consumerCode)). businessService(businessService).build();
* New Demand audit history API in Demandcontroller.\
  An API that returns the audit history of demandDetails. demand/\_history

#### **Water service changes:**

* Create water connection API:\
  Adding a check for payment type advance. If advance, passing a boolean isAdvanceCollection to calculationRequest to water calculator service.
* Update water connection API:\
  Adding a check for payment type advance. If advance, passing a boolean isAdvanceCollection to calculationRequest to water calculator service.\
  Adding a check for advance in validateUpdate method to set the current demand to CANCELLED.

#### **Water calculator service changes:**

* Calling estimation service getEstimationMap based on isAdvanceCalculation boolean. If true, reading taxAmount from criteria.getWaterConnection().getAdvance();
* Changes in getEstimatesForTax for a new taxHeadCode ADVANCE\_COLLECTION with value WS\_ADVANCE\_CARRYFORWARD
* Getting the advance amount in getCalculation with taxHeadCode ADVANCE\_COLLECTION\
  4.Calling generateDemand method based on isAdvanceCalculation. If true, create a demand object with consumerType “waterConnection-advance“.\
  \
  \
  \
