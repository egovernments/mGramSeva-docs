# Water Calculator Service

### Overview

Water Calculator Service is used for creating meter reading, searching meter reading, updating existing meter reading, calculation of water charge, demand generation, SMS & email notification to ULB officials on-demand generation and estimation of water charge(one-time cost) which involves cost like road-cutting charge, form fee, scrutiny fee, etc.

### Pre-requisites

Before you proceed with the documentation, make sure the following pre-requisites are met -

* _Java 8_
* Kafka server is up and running
* egov-persister service is running and has water service persister configs path added in it
* PSQL server is running and database is created to store water connection / application data
* Following services should be up and running:
  * egov-perister
  * egov-mdms
  * ws-services
  * billing-service

### Key Functionalities

* Calculate water charge and taxes based on billing slab.
* Calculate meter reading charge for water connection
* Generate demand
* Scheduler for generating the demand(for non metered connection)

### Deployment Details

1. Deploy the latest version of ws-service and ws-calculator
2. Add water-persist.yml & water-meter.yml file in config folder in git and add that path in persister . _(The file path is to be added in environment yaml file in param called_ persist-yml-path _)_

### Configuration Details

#### MDMS Configuration

#### **Billing Slabs:**

Criteria :

1. connection type
2. building type
3. calculation attribute
4. property usage type

The combination of the above can be used to define the billing slab. Billing Slab is defined in mdms under ws-services-calculation folder with the [WCBillingSlab](https://github.com/egovernments/mdms-mgramseva/blob/DEV/data/pb/ws-services-calculation/WCBillingSlab.json). The following is the sample slab.

```
  {
      "id": "1",
      "buildingType": "RESIDENTIAL",
      "connectionType": "Metered",
      "calculationAttribute": "Water consumption",
      "minimumCharge": 100,
      
      "slabs": [
        {
          "from": 0,
          "to": 10,
          "charge": 2,
          "meterCharge": 50
        },
        {
          "from": 10,
          "to": 20,
          "charge": 2.5,
          "meterCharge": 50
        },
        {
          "from": 20,
          "to": 30,
          "charge": 8,
          "meterCharge": 150
        },
        {
          "from": 30,
          "to": 40,
          "charge": 12,
          "meterCharge": 150
        },
        {
          "from": 40,
          "to": 1000000000,
          "charge": 15,
          "meterCharge": 150
        }
      ]
    },
    {
      "id": "5",
      "buildingType": "RESIDENTIAL",
      "calculationAttribute": "No. of taps",
      "connectionType": "Non Metered",
      
      "minimumCharge": 100,
      "slabs": [
        {
          "from": 0,
          "to": 1000000000,
          "charge": 100
        }
      ]
    },
```

If all criteria will match for that water connection this slab will use for calculation.

#### **Estimation:**

For application one-time fee, the estimation will return all the related tax head based on criteria. For estimation, all configuration is present in ws-services-calculation.

1. [FeeSlab.json](https://github.com/egovernments/egov-mdms-data/blob/master/data/pb/ws-services-calculation/FeeSlab.json)
2. [PlotSizeSlab.json](https://github.com/egovernments/egov-mdms-data/blob/master/data/pb/ws-services-calculation/PlotSizeSlab.json)
3. [RoadType.json](https://github.com/egovernments/egov-mdms-data/blob/master/data/pb/ws-services-calculation/RoadType.json)

All the above master configuration is used for estimation.

Following are the exemptions and taxes that are calculated:

* Form fee
* Scrutiny fee
* Meter charge (For metered connection)
* Other charges
* Road cutting charges
* One time fee
* Security charges
* Tax and cess

#### Water Charge and Tax:

Water charge is based on billing slab, for water application charge will be based on slab and tax based on master configuration.

**Interest:**

Below is a sample of master data JSON for interest :

```
{
  "tenantId": "pb",
  "moduleName": "ws-services-calculation",
  "Interest": [
    {
      "rate": 5,
      "minAmount": null,
      "applicableAfterDays":0,
      "flatAmount": null,
      "maxAmount": null,
      "fromFY": "2019-20",
      "startingDay": "1/01/2019"
    }
  ]
}
```

**Penalty:**

Below is a sample of master data JSON for penalty :

```
{
  "tenantId": "pb",
  "moduleName": "ws-services-calculation",
  "Penalty": [
    {
      "rate": 10,
      "minAmount": null,
      "applicableAfterDays": 0,
      "flatAmount": null,
      "fromFY": "2019-20",
      "startingDay": "1/01/2019"
    }
  ]
}
```

**Round Off:**

If the fraction is greater than equal to 0.5 the number is round up else it’s round down. eg: 100.4 will be rounded to 100 while 100.6 will be rounded to 101.

#### Actions & Role Action Mapping

\
**Actions**

```
[
  {
      "id": {{PLACEHOLDER1}},
      "name": "Bulk Demand Generation",
      "url": "/ws-calculator/waterCalculator/_bulkDemand",
      "parentModule": "",
      "displayName":"Bulk Demand Generation",
      "orderNumber": 1,
      "enabled": false,
      "serviceCode": "ws-services",
      "code": "null",
      "path": ""
    },
    {
      "id": {{PLACEHOLDER2}},
      "name": "Demand Calculation",
      "url": "/ws-calculator/waterCalculator/_calculate",
      "parentModule": "",
      "displayName": "Demand Calculation",
      "orderNumber": 2,
      "enabled": false,
      "serviceCode": "ws-services",
      "code": "null",
      "path": ""
    },
    {
      "id": {{PLACEHOLDER3}},
      "name": "Meter Demand Calculation",
      "url": "/ws-calculator/meterConnection/_create",
      "parentModule": "",
      "displayName": "Meter Demand Calculation",
      "orderNumber": 3,
      "enabled": false,
      "serviceCode": "ws-services",
      "code": "null",
      "path": ""
    },
    {
      "id": {{PLACEHOLDER4}},
      "name": "Meter Demand search",
      "url": "/ws-calculator/meterConnection/_search",
      "parentModule": "",
      "displayName": "Meter Demand search",
      "orderNumber": 3,
      "enabled": false,
      "serviceCode": "ws-services",
      "code": "null",
      "path": ""
    },
    {
      "id": {{PLACEHOLDER5}},
      "name": "Demand Estimate",
      "url": "/ws-calculator/waterCalculator/_estimate",
      "parentModule": "",
      "displayName": "Demand Estimate",
      "orderNumber": 2,
      "enabled": false,
      "serviceCode": "ws-services",
      "code": "null",
      "path": ""
    }
]

```

\
**Role Action Mapping**\


```
[
    {
      "rolecode": "BULK_DEMAND_PROCESSING",
      "actionid": {{PLACEHOLDER1}},
      "actioncode": "",
      "tenantId": "pb"
    },
    {
      "rolecode": "BULK_DEMAND_PROCESSING",
      "actionid": {{PLACEHOLDER2}},
      "actioncode": "",
      "tenantId": "pb"
    },
    {
      "rolecode": "BULK_DEMAND_PROCESSING",
      "actionid": {{PLACEHOLDER3}},
      "actioncode": "",
      "tenantId": "pb"
    },
    {
      "rolecode": "BULK_DEMAND_PROCESSING",
      "actionid": {{PLACEHOLDER4}},
      "actioncode": "",
      "tenantId": "pb"
    },
    {
      "rolecode": "COLLECTION_OPERATOR",
      "actionid": {{PLACEHOLDER4}},
      "actioncode": "",
      "tenantId": "pb"
    },
    {
      "rolecode": "GP_ADMIN",
      "actionid": {{PLACEHOLDER4}},
      "actioncode": "",
      "tenantId": "pb"
    },
    {
      "rolecode": "GP_ADMIN",
      "actionid": {{PLACEHOLDER5}},
      "actioncode": "",
      "tenantId": "pb"
    }
]
```

\


### Demand Generation:

Once water is sent to calculator it’s tax estimates are calculated. Using this tax head estimates demand details are created. For every tax head, estimate demand generates function will create a corresponding demand detail.

Whenever \_calculate API is called demand is first searched based on the connection no or application no and the demand from and to period. If demand already exists the same demand is updated else new demand is generated with consumer code as connection no or application no and demand from and to a period equal to financial year start and end period.

In case of the update if the tax head estimates change, the difference in amount for that tax head is added as new demand detail. For example, if the initial demand has one demand detail with WATER\_CHARGE equal to 120

```
"demandDetails": [
                {
                    "id": "77ba1e93-a535-409c-b9d1-a312c409bd45",
                    "demandId": "687c3176-305b-461d-9cec-2fa26a30c88f",
                    "taxHeadMasterCode": "WATER_CHARGE",
                    "taxAmount": 120,
                    "collectionAmount": 120,
                    "additionalDetails": null,
                    "auditDetails": {
                        "createdBy": "04956309-87cd-4526-b4e6-48123abd4f3d",
                        "lastModifiedBy": "04956309-87cd-4526-b4e6-48123abd4f3d",
                        "createdTime": 1583675275873,
                        "lastModifiedTime": 1583675298705
                    },
                    "tenantId": "pb.amritsar"
                }
            ],
```

After updating if the WATER\_CHARGE increases to 150 we add one more demand detail to account for the increased amount. The demand detail will be updated to:

```
"demandDetails": [
                {
                    "id": "77ba1e93-a535-409c-b9d1-a312c409bd45",
                    "demandId": "687c3176-305b-461d-9cec-2fa26a30c88f",
                    "taxHeadMasterCode": "WATER_CHARGE",
                    "taxAmount": 120,
                    "collectionAmount": 0,
                    "additionalDetails": null,
                    "auditDetails": {
                        "createdBy": "04956309-87cd-4526-b4e6-48123abd4f3d",
                        "lastModifiedBy": "04956309-87cd-4526-b4e6-48123abd4f3d",
                        "createdTime": 1583675275873,
                        "lastModifiedTime": 1583675298705
                    },
                    "tenantId": "pb.amritsar"
                },
                {
                    "id": "0d83f4b0-6442-11ea-bc55-0242ac130003 ",
                    "demandId": "687c3176-305b-461d-9cec-2fa26a30c88f",
                    "taxHeadMasterCode": "WATER_CHARGE",
                    "taxAmount": 30,
                    "collectionAmount": 0,
                    "additionalDetails": null,
                    "auditDetails": {
                        "createdBy": "04956309-87cd-4526-b4e6-48123abd4f3d",
                        "lastModifiedBy": "04956309-87cd-4526-b4e6-48123abd4f3d",
                        "createdTime": 1583675275873,
                        "lastModifiedTime": 1583675298705
                    },
                    "tenantId": "pb.amritsar"
                }
            ],
```

RoundOff is bill based i.e every time bill is generated round off is adjusted so that payable amount is the whole number. Individual WS\_ROUNDOFF in demand detail can be greater than 0.5 but the sum of all WS\_ROUNDOFF will always be less than 0.5.

### Scheduler for generating the demand(For non metered connection):

_**Description :**_

For generating the demand for non metered connection we have a feature for generating the demand in batch. The scheduler is responsible for generating the demand based on the tenant.

* The scheduler can be hit by scheduler API or we can schedule cron job or we can put config to kubectl which will hit scheduler based on config.
* After the scheduler been hit we will search the list of the tenant (city) present in the database.
* After getting the tenants we will pickup tenant one by one and generate the demand for that tenant.
* We will load the consumer codes for the tenant and push the calculation criteria to Kafka. Calculation criteria contain minimal information (We are not pushing large data to Kafka), calculation criteria contain consumer code and one boolean variable.
* After pushing the data into Kafka we are consuming the records based on the batch configuration. Ex:-> if the batch configuration is 50 so we will consume the 50 calculation criteria at a time.
* After consuming the record(Calculation criteria) we will process the batch for generating the demand. If the batch is successful so will log the consumer codes which have been processed.
* If some records failed in batch so we will push the batch into dead letter batch topic. From the dead letter batch topic, we will process the batch one by one.
* If the record is successful we will log the consumer code, If the record is failed so we will push the data into a dead letter single topic.
* Dead letter single topic contains information about failure records in Kafka.

_**Use cases:**_

1. If the same job trigger multiple time what will happen?

If the same job triggers multiple times we will process again as mentioned above but at the demand level we will check the demand based on consumer code and billing period, If demand already exists then we will update the demand otherwise we will create the demand.

1. Are we maintaining success or failure status anywhere?

Currently, we are maintaining the status of failed records in Kafka.

_**Configuration :**_

We need to configure the batch size for Kafka consumer. This configuration is for how much data will be processed at a time.

```
ws.demand.based.batch.size=10
```

### Integration

#### Integration Scope

ws-calculator will be integrated with ws-service. ws-services internally invoke the ws-calculator service to calculate and generate demand for the charges.

#### Integration Benefits

WS calculator application is used to calculate the water application one time Fees and meter reading charges based on the different billing slabs that's why the calculation and demand generation logic will be separate out from WS service.\
So in future, if calculation logic need to modify then changes can be carry out for each implementation without modifying the WS service.

#### Steps to Integration

1. Once the water connection is activated for metered-connection, employee can add meter reading details using this API - /ws-calculator/meterConnection/\_createwhich in-turn will generate the demand. For the Non-Metered connections, the scheduler APIs need to be called periodically to generate the demand.
2. For the Metered Connection service, to get the previous meter reading /meterConnection/\_search API is use.
3. To Activate the Water Service application, the user needs to pay the ONE\_TIME\_FEE for the connection. To calculate the ONE\_TIME\_FEE /waterCalculator/\_estimate API is use.
4. To generate the demand for metered or non-metered water connection /waterCalculator/\_calculate API is use.
5. User can pay partial / full / advance amount for the Metered or Non-Metered connection bill. In these cases, Billing service would call back /waterCalculator/\_updateDemandAPI to update the details of the demand generated.
6. /waterCalculator/\_jobscheduler API is use to generate demand for Non-metered connections. This API can be called periodically.
7. /waterCalculator/\_applyAdhocTax API is use to add Rebate or Penalty on any bill and based on that the bill amount will be adjusted.

### Reference Docs

#### Doc Links

| **Title**              | **Link**                                                                                                                                                                                                                                                                                                         |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API Swagger Contract   | [https://editor.swagger.io/?url=https://raw.githubusercontent.com/egovernments/DIGIT-OSS/master/municipal-services/docs/water-sewerage-services.yaml#!/](https://editor.swagger.io/?url=https://raw.githubusercontent.com/egovernments/DIGIT-OSS/master/municipal-services/docs/water-sewerage-services.yaml#!/) |
| Water Service Document | [Water Service](https://digit-discuss.atlassian.net/l/c/VDfAnLVt)                                                                                                                                                                                                                                                |

#### API List

| <h4><strong>Title</strong> </h4>        | **Link**                                                                                                                   |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| /ws-calculator/meterConnection/\_create | [https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d](https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d) |
| /ws-calculator/meterConnection/\_search | [https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d](https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d) |
| /waterCalculator/\_estimate             | [https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d](https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d) |
| /waterCalculator/\_calculate            | [https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d](https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d) |
| /waterCalculator/\_updateDemand         | [https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d](https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d) |
| /waterCalculator/\_jobscheduler         | [https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d](https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d) |

_(Note: All the API’s are in the same postman collection therefore same link is added in each row)_\
