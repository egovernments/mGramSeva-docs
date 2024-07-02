# Billing Service

## **Overview**

The main objective of the billing module is to serve the Bill for all revenue Business services. To serve the Bill, Billing-Service requires demand. Demands will be prepared by Revenue modules and stored by billing based on which it will generate the Bill.

## **Pre-requisites**

1. Prior knowledge of Java/J2EE.
2. Prior knowledge of Spring Boot.
3. Prior knowledge of KAFKA
4. Prior knowledge of REST APIs and related concepts like path parameters, headers, JSON, etc.
5. Prior knowledge of the demand-based systems.
6. The following services should be up and running:
   * user
   * MDMS
   * Id-Gen
   * URL-Shortening
   * notification-sms

## **Key Functionalities**&#x20;

* **eGov** billing service creates and maintains demands.
* Generates bills based on demands.
* Updates the demands from payment when the collection service takes a payment.

## **Deployment Details**

* Deploy the latest image of the billing service available.

## **Configuration Details**

In the MDMS data configuration, the following master data is needed for the functionality of billing

### **MDMS Configuration**

Business Service JSON

```
{
  "tenantId": "pb",
  "moduleName": "BillingService",
  "BusinessService": [
    {
      "businessService": "PropertyTax",
      "code": "PT",
      "isBillAmendmentEnabled":"true",
      "collectionModesNotAllowed": [
        "DD","OFFLINE_NEFT","OFFLINE_RTGS","POSTAL_ORDER"
      ],
      "partPaymentAllowed": true,
      "minAmountPayable":100,
      "isAdvanceAllowed": false,
      "demandUpdateTime": 86400000,
      "isVoucherCreationEnabled": true,
      "billGineiURL" : "egov-searcher/bill-genie/billswithaddranduser/_get"
    },
    {
      "businessService": "WaterCharges",
      "code": "WC",
      "isBillAmendmentEnabled":"true",
      "collectionModesNotAllowed": [
        "DD","OFFLINE_NEFT","OFFLINE_RTGS","POSTAL_ORDER"
      ],
      "partPaymentAllowed": false,
      "isAdvanceAllowed": true,
      "demandUpdateTime": 86400000,
      "isVoucherCreationEnabled": false
    },
    {
      "businessService": "TradeLicense",
      "code": "TL",
      "collectionModesNotAllowed": [
        "DD","OFFLINE_NEFT","OFFLINE_RTGS","POSTAL_ORDER"
      ],
      "partPaymentAllowed": false,
      "isAdvanceAllowed": false,
      "demandUpdateTime": 604800000,
      "isVoucherCreationEnabled": true
    }
  ]
}
```

TAX-Head JSON

```
{
  "tenantId": "pb",
  "moduleName": "BillingService",
  "TaxHeadMaster": [
    {
      "category": "ADVANCE_COLLECTION",
      "service": "PT",
      "name": "Pt advance carry forward",
      "code": "PT_ADVANCE_CARRYFORWARD",
      "isDebit": true,
      "isActualDemand": false,
      "order": "0",
      "isRequired": false
    },
    {
      "category": "TAX",
      "service": "PT",
      "name": "Pt owner exemption",
      "code": "PT_OWNER_EXEMPTION",
      "isDebit": true,
      "isActualDemand": true,
      "order": "5",
      "isRequired": false
    },
    {
      "category": "TAX",
      "service": "PT",
      "name": "Pt time rebate",
      "code": "PT_TIME_REBATE",
      "isDebit": true,
      "isActualDemand": true,
      "order": "2",
      "isRequired": false
    },
    {
      "category": "TAX",
      "service": "PT",
      "name": "Pt unit usage excemption",
      "code": "PT_UNIT_USAGE_EXEMPTION",
      "isDebit": true,
      "isActualDemand": true,
      "order": "6",
      "isRequired": false
    },
    {
      "category": "TAX",
      "service": "PT",
      "name": "Pt adhoc penalty",
      "code": "PT_ADHOC_PENALTY",
      "isDebit": false,
      "isActualDemand": false,
      "order": "1",
      "isRequired": false
    },
    {
      "category": "TAX",
      "service": "PT",
      "name": "propertytax",
      "code": "PT_TAX",
      "isDebit": false,
      "isActualDemand": true,
      "order": "0",
      "isRequired": false
    },
    {
      "category": "TAX",
      "service": "PT",
      "name": "Pt fire cess",
      "code": "PT_FIRE_CESS",
      "isDebit": false,
      "isActualDemand": true,
      "order": "7",
      "isRequired": false
    }
  ]
}
```

Tax-Period JSON

```
{
  "tenantId": "pb",
  "moduleName": "BillingService",
  "TaxPeriod": [
    {
      "fromDate": 1554076799000,
      "toDate": 1585679399000,
      "periodCycle": "ANNUAL",
      "service": "PT",
      "code": "PTAN2019",
      "financialYear": "2019-20"
    },
    {
      "fromDate": 1522540800000,
      "toDate": 1554076799000,
      "periodCycle": "ANNUAL",
      "service": "PT",
      "code": "PTAN2018",
      "financialYear": "2018-19"
    },
    {
      "fromDate": 1491004800000,
      "toDate": 1522540798000,
      "periodCycle": "ANNUAL",
      "service": "PT",
      "code": "PTAN2017",
      "financialYear": "2017-18"
    },
    {
      "fromDate": 1459468800000,
      "toDate": 1491004799000,
      "periodCycle": "ANNUAL",
      "service": "PT",
      "code": "PTAN2016",
      "financialYear": "2016-17"
    },
    {
      "fromDate": 1522540800000,
      "toDate": 1554076799000,
      "periodCycle": "ANNUAL",
      "service": "TL",
      "code": "TLAN2018",
      "financialYear": "2018-19"
    }
  ]
}
```

|                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                  |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bs.businesscode.demand.updateurl         | <p>{</p><p>"PT":"<a href="http://pt-calculator-v2:8080/pt-calculator-v2/propertytax/_updatedemand%22,%22TL%22:%22%22%7D">http://pt-calculator-v2:8080/pt-calculator-v2/propertytax/_updatedemand",</a></p><p><a href="http://pt-calculator-v2:8080/pt-calculator-v2/propertytax/_updatedemand%22,%22TL%22:%22%22%7D">"TL":""</a></p><p><a href="http://pt-calculator-v2:8080/pt-calculator-v2/propertytax/_updatedemand%22,%22TL%22:%22%22%7D">}</a></p> | Each module’s application calculator should provide its own update URL. if not present then new bill will be generated without making any changes to the demand. |
| bs.bill.billnumber.format                | BILLNO-{module}-\[SEQ\_egbs\_billnumber{tenantid}]                                                                                                                                                                                                                                                                                                                                                                                                       | IdGen format for bill number                                                                                                                                     |
| bs.amendment.idbs.bill.billnumber.format | BILLNO-{module}-\[SEQ\_egbs\_billnumber{tenantid}]                                                                                                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                  |
| is.amendment.workflow.enabled            | true/false                                                                                                                                                                                                                                                                                                                                                                                                                                               | enable disable workflow of bill amendment                                                                                                                        |

## Integration Details

### Integration Scope

Billing service can be integrated with any organization or system that wants a demand-based payment system.

### Integration Benefits

* Easy to create and simple process of generating bills from demands
* The amalgamation of bills period-wise for a single entity like PT or Water connection.
* Amendment of bills in case of legal requirements.

### Integration Steps

1. Customers can create a demand using the /demand/\_create
2. Organizations or system can search the demand using /demand/\_searchendpoint
3. Once the demand is raised the system can call /demand/\_update endpoint to update the demand as per need.
4. Bills can be generated using, which is a self-managing API that generates a new bill only when the old one expires /bill/\_fetchbill.
5. Bills can be searched using /bill/\_search.
6. Amendment facility can be used in case of a legal issue to add values to existing demands using /amendment/\_create and /amendment/\_update can used to cancel the created ones or update workflow if configured.

### Interaction Diagram

**Interaction Diagram V1.1**

## **Reference Docs**

**Doc Links**

| **Title**       | **Link** |
| --------------- | -------- |
|  Id-Gen service |          |
| url-shortening  |          |
|  MDMS           |          |

**API List**

| **Title**                             | **Link**                                                                                                                   |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
|  /demand/\_create, \_update, \_search | [https://www.getpostman.com/collections/900d99a85d083fb2d377](https://www.getpostman.com/collections/900d99a85d083fb2d377) |
|  /bill/\_fetchbill, \_search          | [https://www.getpostman.com/collections/900d99a85d083fb2d377](https://www.getpostman.com/collections/900d99a85d083fb2d377) |
| /amendment/\_create, \_update         | [https://www.getpostman.com/collections/b195d3b1d354c767b6bd](https://www.getpostman.com/collections/b195d3b1d354c767b6bd) |

## **Apportioning**

**What is apportioning?**

Adjusting the receivable amount with the individual tax head.

**Types of apportioning V1.1:**

Default order-based apportioning(Based on apportioning order adjust the received amount with each tax head).V1.1

**Types of apportioning V1.2:**&#x20;

* Proportionate-based apportioning (Adjust total receivable with all the tax heads equally)
* Order & Percentage-based apportioning(Adjust total receivable based on order and the percentage which is defined for each tax head).

**Principle of apportioning:**

&#x20;The basic principle of apportioning is, that if the full amount is paid for any bill then each tax head should get nullified with their corresponding adjusted amount.

**Example**:\
**Case 1:** When there are no arrears all tax heads belong to their current purpose:\
&#x20;

<table data-header-hidden><thead><tr><th></th><th width="128"></th><th></th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>TaxHead</strong></td><td><strong>Amount</strong></td><td><strong>Order</strong></td><td><strong>Full Payment(2000)</strong></td><td><strong>Partial Payment1(1500)</strong></td><td><strong>Partial payment2(750)</strong></td><td><strong>Partial payment2 with rebate(500)</strong></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Pt_tax</td><td>1000</td><td>6</td><td>1000</td><td>1000</td><td>750</td><td>750</td></tr><tr><td>AdjustedAmt</td><td><br></td><td><br></td><td>1000</td><td>-250</td><td>-750</td><td>-750</td></tr><tr><td>RemainingAMTfromPayableAMT</td><td><br></td><td><br></td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Penality</td><td>500</td><td>5</td><td>500</td><td>500</td><td><br></td><td><br></td></tr><tr><td>AdjustedAmt</td><td><br></td><td><br></td><td>500</td><td>-500</td><td><br></td><td><br></td></tr><tr><td>RemainingAMTfromPayableAMT</td><td><br></td><td><br></td><td>1000</td><td>250</td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Interest</td><td>500</td><td>4</td><td>500</td><td>500</td><td><br></td><td><br></td></tr><tr><td>AdjustedAmt</td><td><br></td><td><br></td><td>500</td><td>-500</td><td><br></td><td><br></td></tr><tr><td>RemainingAMTfromPayableAMT</td><td><br></td><td><br></td><td>1500</td><td>750</td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Cess</td><td>500</td><td>3</td><td>500</td><td>500</td><td><br></td><td><br></td></tr><tr><td>AdjustedAmt</td><td><br></td><td><br></td><td>500</td><td>-500</td><td><br></td><td><br></td></tr><tr><td>RemainingAMTfromPayableAMT</td><td><br></td><td><br></td><td>2000</td><td>1250</td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Exm</td><td>-250</td><td>1</td><td>-250</td><td>-250</td><td><br></td><td><br></td></tr><tr><td>AdjustedAmt</td><td><br></td><td><br></td><td>-250</td><td>250</td><td><br></td><td><br></td></tr><tr><td>RemainingAMTfromPayableAMT</td><td><br></td><td><br></td><td>2250</td><td>1750</td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Rebate</td><td>-250</td><td>2</td><td>-250</td><td><br></td><td><br></td><td>-250</td></tr><tr><td>AdjustedAmt</td><td><br></td><td><br></td><td>-250</td><td><br></td><td><br></td><td>250</td></tr><tr><td>RemainingAMTfromPayableAMT</td><td><br></td><td><br></td><td>2500</td><td><br></td><td><br></td><td>750</td></tr></tbody></table>

**Case 2:** Apportioning with two years of arrear:\
If the current financial year is 2014-15. Below are the demands&#x20;

<table data-header-hidden><thead><tr><th width="155"></th><th width="95"></th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>TaxHead</strong></td><td><strong>Amount</strong></td><td><strong>TaxPeriodFrom</strong></td><td><strong>TaxPeriodTo</strong></td><td><strong>Order</strong></td><td><strong>Purpose</strong></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Pt_tax</td><td>1000</td><td>2014</td><td>2015</td><td>6</td><td>Current</td></tr><tr><td>AdjustedAmt</td><td>0</td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Penality</td><td>500</td><td>2014</td><td>2015</td><td>5</td><td>Current</td></tr><tr><td>AdjustedAmt</td><td>0</td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Interest</td><td>500</td><td>2014</td><td>2015</td><td>4</td><td>Current</td></tr><tr><td>AdjustedAmt</td><td>0</td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Cess</td><td>500</td><td>2014</td><td>2015</td><td>3</td><td>Current</td></tr><tr><td>AdjustedAmt</td><td>0</td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Exm</td><td>-250</td><td>2014</td><td>2015</td><td>1</td><td>Current</td></tr><tr><td>AdjustedAmt</td><td>0</td><td><br></td><td><br></td><td><br></td><td><br></td></tr></tbody></table>

If any payment is not done, and we generate demand in 2015-16 then the demand structure will be as follows:

<table data-header-hidden><thead><tr><th width="165"></th><th></th><th></th><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>TaxHead</strong></td><td><strong>Amount</strong></td><td><strong>TaxPeriodFrom</strong></td><td><strong>TaxPeriodTo</strong></td><td><strong>Order</strong></td><td><strong>Purpose</strong></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Pt_tax</td><td>1000</td><td>2014</td><td>2015</td><td>6</td><td>Arrear</td></tr><tr><td>AdjustedAmt</td><td>0</td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Pt_tax</td><td>1500</td><td>2015</td><td>2016</td><td>6</td><td> Current</td></tr><tr><td>AdjustedAmt</td><td>0</td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Penalty</td><td>600</td><td>2014</td><td>2015</td><td>5</td><td>Arrear</td></tr><tr><td>AdjustedAmt</td><td>0</td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Penalty</td><td>500</td><td>2015</td><td>2016</td><td>5</td><td>Current</td></tr><tr><td>AdjustedAmt</td><td>0</td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Interest</td><td>500</td><td>2014</td><td><br></td><td>4</td><td>Arrear</td></tr><tr><td>AdjustedAmt</td><td>0</td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Cess</td><td>500</td><td>2014</td><td><br></td><td>3</td><td>Arrear</td></tr><tr><td>AdjustedAmt</td><td>0</td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td><td><br></td></tr><tr><td>Exm</td><td>-250</td><td>2014</td><td><br></td><td>1</td><td>Arrear</td></tr><tr><td>AdjustedAmt</td><td>0</td><td><br></td><td><br></td><td><br></td><td><br></td></tr></tbody></table>

