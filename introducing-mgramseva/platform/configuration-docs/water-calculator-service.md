# Water Calculator Service

## Overview

Water Calculator Service is used to create meter readings, search meter readings, update existing meter readings, calculate water charges, generate demand, notify ULB officials using SMS & email on-demand generation and estimation of water charges (one-time cost) which involves costs like road-cutting charge, form fee, scrutiny fee, etc.

## Pre-requisites

Before you proceed with the documentation, make sure the following pre-requisites are met -

1. _Java 8_
2. The Kafka server is up and running
3. egov-persister service is running and has the water service persister configs path added to it
4. PSQL server is running and a database is created to store water connection/application data
5. The following services should be up and running:
   * egov-perister
   * egov-mdms
   * ws-services
   * billing-service

## Key Functionalities

* Calculate water charges and taxes based on the billing slab
* Calculate meter reading charge for water connection
* Generate demand
* Scheduler for generating the demand (for non-metered connection)

## Deployment Details

1. Deploy the latest version of ws-service and ws-calculator
2. Add water-persist.yml & water-meter.yml files in the config folder in git and add that path in persister. _(_Add the file path to the environment YAML file under a parameter named "persist-yml-path"_)._

## Configuration Details

### MDMS Configuration

#### **Billing Slabs**

Criteria

1. connection type
2. building type
3. calculation attribute
4. property usage type

The above combination is used to define the billing slab. Billing Slab is defined in MDMS under the ws-services-calculation folder with the [WCBillingSlab](https://github.com/egovernments/mdms-mgramseva/blob/DEV/data/pb/ws-services-calculation/WCBillingSlab.json). Find below a sample slab.

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

Depending on the matching criteria for the water connection, the calculation applies the specified slab.

#### **Estimation:**

For the one-time fee application, the estimation will return all related tax heads based on criteria. All configurations for estimation are present in ws-services-calculation.

1. [FeeSlab.json](https://github.com/egovernments/egov-mdms-data/blob/master/data/pb/ws-services-calculation/FeeSlab.json)
2. [PlotSizeSlab.json](https://github.com/egovernments/egov-mdms-data/blob/master/data/pb/ws-services-calculation/PlotSizeSlab.json)
3. [RoadType.json](https://github.com/egovernments/egov-mdms-data/blob/master/data/pb/ws-services-calculation/RoadType.json)

The above master configuration is used for estimation.

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

The billing slab determines the water charges. Water application charges are based on the slab and tax calculations are based on the master configuration.

**Interest:**

Below is a sample of the master data JSON for interest :

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

Below is a sample of the master data JSON for penalty:

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

If the fraction is greater than equal to 0.5 the number is rounded up else it’s rounded down. For example, 100.4 is rounded to 100 while 100.6 is rounded to 101.

### Actions & Role Action Mapping

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

**Role Action Mapping**

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

### Demand Generation

Once water is sent to the calculator, its tax estimates are calculated. Using these tax head estimates, demand details are created. For every tax head, the estimated demand generates a corresponding demand detail.

When the `_calculate` API is called, demand is first searched based on the connection number or application number and the demand period. If demand already exists, it is updated with the new information. Otherwise, a new demand is generated for the financial year period.

During an update, if the tax head estimates change, the difference in amount for that tax head is added as a new demand detail. For example, if the initial demand has one demand detail with WATER\_CHARGE equal to 120.

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

Round-off in the bill is based on the total amount, ensuring that the payable amount is a whole number. Each WS\_ROUNDOFF in the demand detail can be greater than 0.5, but the sum of all WS\_ROUNDOFF values is always less than 0.5.

### Scheduler for generating the demand (For non metered connection):

_**Description:**_

To generate demand for non-metered connections, we have a feature for batch demand generation. The scheduler is responsible for generating demand based on the tenant.

* The scheduler can be triggered using the scheduler API, scheduled as a cron job, or configured in Kubectl to hit the scheduler based on the configuration.
* After the scheduler is triggered, we can search for the list of tenants (cities) in the database.
* After obtaining the list of tenants, iterate through the list and generate the demand for specific tenants.
* Load the consumer codes for the tenant and push the calculation criteria to Kafka. The calculation criteria contain minimal information, including the consumer code and one boolean variable.
* After pushing the data into Kafka, the system consumes the records based on the batch configuration. For example, if the batch configuration is set to 50, the system will consume 50 calculation criteria at a time.
* After consuming the records (calculation criteria), the system processes the batch to generate the demand. If the batch processing is successful, the processed consumer codes are logged.
* If some records fail in the batch, the system pushes the batch into the dead letter batch topic. From there, the batch is processed one record at a time.
* If the record is successful, the system logs the consumer code. If the record fails, the data is pushed into a dead-letter single topic.
* Dead letter single topic contains information about failure records in Kafka.

_**Use cases:**_

1. If the same job triggers multiple times what will happen?

If the same job triggers multiple times the system processes it again as mentioned above but at the demand level, it checks the demand based on consumer code and billing period. In case the demand already exists then it updates the demand or else creates the demand.

1. Are we maintaining success or failure status anywhere?

Currently, we are maintaining the status of failed records in Kafka.

_**Configuration:**_

We need to configure the batch size for Kafka consumers. This configuration determines how much data is processed at a time.

```
ws.demand.based.batch.size=10
```

## Integration Details

### Integration Scope

The ws-calculator is integrated with ws-service. ws-services internally invoke the ws-calculator service to calculate and generate demand for the charges.

### Integration Benefits

WS calculator application is used to calculate the water application one-time fees and meter reading charges based on the different billing slabs. That's why the calculation and demand generation logic is separated from the WS service.\
So in future, if calculation logic requires modification the changes can be carried out for each implementation without modifying the WS service.

### Integration Steps

1. Once the water connection is activated for the metered connection, the employee can add meter reading details using the API - /ws-calculator/meterConnection/\_create. This generates the demand. For non-metered connections, the scheduler APIs should be called periodically to generate the demand.
2. For the metered connection service, the /meterConnection/\_search API is used to get the previous meter reading,
3. To activate the Water Service application, the user has to pay the ONE\_TIME\_FEE for the connection. To calculate this fee, the ONE\_TIME\_FEE /waterCalculator/\_estimate API is used.
4. To generate the demand for metered or non-metered water connection /waterCalculator/\_calculate API is used.
5. Users can pay partial/full/advance amounts for the metered or non-metered connection bill. In such cases, the billing service would call back /waterCalculator/\_updateDemandAPI to update the demand-generated details.
6. /waterCalculator/\_jobscheduler API is used to generate demand for non-metered connections. This API can be called periodically.
7. /waterCalculator/\_applyAdhocTax API is used to add a Rebate or Penalty on any bill and based on that the bill amount is adjusted.

## Reference Docs

#### Doc Links

<table data-header-hidden><thead><tr><th width="226"></th><th></th></tr></thead><tbody><tr><td><strong>Title</strong> </td><td><strong>Link</strong></td></tr><tr><td>API Swagger Contract</td><td><a href="https://editor.swagger.io/?url=https://raw.githubusercontent.com/egovernments/DIGIT-OSS/master/municipal-services/docs/water-sewerage-services.yaml#!/">https://editor.swagger.io/?url=https://raw.githubusercontent.com/egovernments/DIGIT-OSS/master/municipal-services/docs/water-sewerage-services.yaml#!/</a></td></tr><tr><td>Water Service Document</td><td><a href="https://digit-discuss.atlassian.net/l/c/VDfAnLVt">Water Service</a></td></tr></tbody></table>

#### API List

<table data-header-hidden><thead><tr><th width="322"></th><th></th></tr></thead><tbody><tr><td><h4><strong>Title</strong> </h4></td><td><strong>Link</strong></td></tr><tr><td>/ws-calculator/meterConnection/_create</td><td><a href="https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d">https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d</a></td></tr><tr><td>/ws-calculator/meterConnection/_search</td><td><a href="https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d">https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d</a></td></tr><tr><td>/waterCalculator/_estimate</td><td><a href="https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d">https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d</a></td></tr><tr><td>/waterCalculator/_calculate</td><td><a href="https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d">https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d</a></td></tr><tr><td>/waterCalculator/_updateDemand</td><td><a href="https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d">https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d</a></td></tr><tr><td>/waterCalculator/_jobscheduler</td><td><a href="https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d">https://www.getpostman.com/collections/7ca1fb4384cf83c40c9d</a></td></tr></tbody></table>

_(Note: All the APIs are in the same Postman collection therefore the same link is added in each row)._\
