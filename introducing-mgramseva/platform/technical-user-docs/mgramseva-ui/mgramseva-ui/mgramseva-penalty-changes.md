# mGramSeva Penalty Changes

## Overview

Water Connection Penalty changes are added to get the penalty amount after the due date. The due date is configurable and penalty enable and disable are also configurable. If we want to have the penalty we can enable or we can disable it through configuration.

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

## Key Functionalities

* Calculate water charges and taxes based on the billing slab.
* Calculate meter reading charge for water connection
* Generate demand for penalty feature
* Scheduler for generating the demand(for non-metered connection)

## Deployment Details

1. Deploy the latest version of ws-service and ws-calculator
2. Add water-persist.yml & water-meter.yml file in the config folder in git and add that path in persister. _(The file path is to be added in the environment yaml file in a param called_ persist-yml-path _)_

## Configuration Details

### MDMS Configuration

#### **Billing service tax head configuration**

```
 {
      "category": "PENALTY",
      "service": "WS",
      "name": "Penalty",
      "code": "10201",
      "isDebit": false,
      "isActualDemand": true,
      "order": "3",
      "isRequired": false,
      "IsBillamend": true
    },
     {
      "category": "TAX",
      "service": "WS",
      "name": "Water adhoc penalty",
      "code": "WS_TIME_ADHOC_PENALTY",
      "isDebit": false,
      "isActualDemand": true,
      "order": "6",
      "isRequired": false,
      "IsBillamend": false
    },
```

#### **ws-calculator penalty configuration:**

**Use case 1 : Fixed percentage on outstanding without penalty**\
**Use case 2 : Fixed percentage on current month**\
**Use case 3 : Fixed percentage on outstanding including penalty**

**Note : All above are applied to the running month only.**

Use case 4 : Fixed percentage on outstanding applied for every month on the outstanding amount respectively (not implemented)

**Tech configs:**

**Use case 1:**\
"type": "Fixed",\
&#x20;"subType": "outstandingWithoutPenalty"

**Use case 2:**\
"type": "Fixed",\
&#x20;"subType": "currentMonth",

**Use Case 3:**\
"type": "Fixed",\
&#x20;"subType": "outstanding",\
\
We have Total 4 types of penalty in the system:

**Fixed - Current month:** This type of penalty is applied to the current month's amount based on the rate (%) given in the configuration.\


```
{
  "tenantId": "pb",
  "moduleName": "ws-services-calculation",
  "Penalty": [
    {
      "type": "FIXED",
      "subType": "currentMonth",
      "rate": 10,
      "amount":null,
      "minAmount": null,
      "applicableAfterDays": 10,
      "flatAmount": null,
      "fromFY": "2022-23",
      "startingDay": "1/01/2022"
    }
  ]
}
```

**Fixed - outstanding:** This is the penalty applied on the total outstanding amount including previously applied penalties based on the rate (%) given in the configuration.

```
{
  "tenantId": "pb",
  "moduleName": "ws-services-calculation",
  "Penalty": [
    {
      "type": "FIXED",
      "subType": "outstanding",
      "rate": 10,
      "amount":null,
      "minAmount": null,
      "applicableAfterDays": 10,
      "flatAmount": null,
      "fromFY": "2022-23",
      "startingDay": "1/01/2022"
    }
  ]
}
```

**Fixed - outstandingWithoutPenalty:** This is the penalty applied on the total outstanding amount excluding previously applied penalties based on the rate (%) given in the configuration.

```
{
  "tenantId": "pb",
  "moduleName": "ws-services-calculation",
  "Penalty": [
    {
      "type": "FIXED",
      "subType": "outstandingWithoutPenalty",
      "rate": 10,
      "amount":null,
      "minAmount": null,
      "applicableAfterDays": 10,
      "flatAmount": null,
      "fromFY": "2022-23",
      "startingDay": "1/01/2022"
    }
  ]
```

**Flat - Current month:** This type of penalty is applied to the current month's amount based on the amount given in the configuration.

```
{
  "tenantId": "pb",
  "moduleName": "ws-services-calculation",
  "Penalty": [
    {
      "type": "FLAT",
      "subType": "currentMonth",
      "rate": null,
      "amount": 15,
      "minAmount": null,
      "applicableAfterDays": 10,
      "flatAmount": null,
      "fromFY": "2022-23",
      "startingDay": "1/01/2022"
    }
  ]
}
```

**Flat - outstanding:** This type of penalty applied to the total pending amount till the current month amount based on the amount given in the configuration.

```
{
  "tenantId": "pb",
  "moduleName": "ws-services-calculation",
  "Penalty": [
    {
      "type": "FLAT",
      "subType": "outstanding",
      "rate": null,
      "amount": 15,
      "minAmount": null,
      "applicableAfterDays": 10,
      "flatAmount": null,
      "fromFY": "2022-23",
      "startingDay": "1/01/2022"
    }
  ]
}
```

#### Curl to create:

```
curl --location --request POST 'http://localhost:8090/ws-services/wc/_create' \
--header 'authority: mgramseva-qa.egov.org.in' \
--header 'accept: */*' \
--header 'accept-language: en-GB,en-US;q=0.9,en;q=0.8' \
--header 'content-type: application/json; charset=utf-8' \
--header 'cookie: _ga_MY9HZBBBC8=GS1.1.1646915127.24.1.1646915152.0; _ga=GA1.1.1108799280.1643257024; _ga_8H6W5DYGX0=GS1.1.1655294682.124.0.1655294682.0' \
--header 'origin: https://mgramseva-qa.egov.org.in' \
--header 'referer: https://mgramseva-qa.egov.org.in/mgramseva/home/consumercreate' \
--header 'sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "Linux"' \
--header 'sec-fetch-dest: empty' \
--header 'sec-fetch-mode: cors' \
--header 'sec-fetch-site: same-origin' \
--header 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36' \
--data-raw '{
    "RequestInfo": {
        "apiId": "mgramseva",
        "ver": 1,
        "ts": "",
        "action": "_create",
        "did": 1,
        "key": "",
        "msgId": "20170310130900|en_IN",
        "authToken": "cded20ed-d1f7-40ca-bd8e-978e319fdcea",
        "userInfo": {
            "id": 705,
            "uuid": "36b747f4-bd94-4be7-b0cc-e59af2ff970b",
            "userName": "8122091926",
            "name": "Vasanthi",
            "mobileNumber": "8122091926",
            "emailId": "vasanth.arun.95@gmail.com",
            "locale": null,
            "type": "EMPLOYEE",
            "roles": [
                {
                    "name": "GP Admin",
                    "code": "GP_ADMIN",
                    "tenantId": "pb.lodhipur"
                },
                {
                    "name": "Bulk Demand Processing",
                    "code": "BULK_DEMAND_PROCESSING",
                    "tenantId": "pb.dabourupper"
                },
                {
                    "name": "Super User",
                    "code": "SUPERUSER",
                    "tenantId": "pb.dabourupper"
                },
                {
                    "name": "Profile update",
                    "code": "PROFILE_UPDATE",
                    "tenantId": "pb.lalpur"
                },
                {
                    "name": "Dashbaord Viewer",
                    "code": "DASHBOARD_VIEWER",
                    "tenantId": "pb.dabourupper"
                },
                {
                    "name": "Expense Processing",
                    "code": "EXPENSE_PROCESSING",
                    "tenantId": "pb.dabourupper"
                },
                {
                    "name": "Dashbaord Viewer",
                    "code": "DASHBOARD_VIEWER",
                    "tenantId": "pb.lodhipur"
                },
                {
                    "name": "Expense Processing",
                    "code": "EXPENSE_PROCESSING",
                    "tenantId": "pb.lodhipur"
                },
                {
                    "name": "GP Admin",
                    "code": "GP_ADMIN",
                    "tenantId": "pb.lalpur"
                },
                {
                    "name": "GP Admin",
                    "code": "GP_ADMIN",
                    "tenantId": "pb.dabourlower"
                },
                {
                    "name": "Profile update",
                    "code": "PROFILE_UPDATE",
                    "tenantId": "pb.massewal"
                },
                {
                    "name": "Bulk Demand Processing",
                    "code": "BULK_DEMAND_PROCESSING",
                    "tenantId": "pb.lodhipur"
                },
                {
                    "name": "Profile update",
                    "code": "PROFILE_UPDATE",
                    "tenantId": "pb.dabourupper"
                },
                {
                    "name": "Profile update",
                    "code": "PROFILE_UPDATE",
                    "tenantId": "pb.lodhipur"
                },
                {
                    "name": "Employee",
                    "code": "EMPLOYEE",
                    "tenantId": "pb.dabourupper"
                },
                {
                    "name": "Employee",
                    "code": "EMPLOYEE",
                    "tenantId": "pb.lodhipur"
                },
                {
                    "name": "Collection Operator",
                    "code": "COLLECTION_OPERATOR",
                    "tenantId": "pb.dabourlower"
                },
                {
                    "name": "Employee",
                    "code": "EMPLOYEE",
                    "tenantId": "pb.massewal"
                },
                {
                    "name": "Bulk Demand Processing",
                    "code": "BULK_DEMAND_PROCESSING",
                    "tenantId": "pb.dabourlower"
                },
                {
                    "name": "Bulk Demand Processing",
                    "code": "BULK_DEMAND_PROCESSING",
                    "tenantId": "pb.lalpur"
                },
                {
                    "name": "Collection Operator",
                    "code": "COLLECTION_OPERATOR",
                    "tenantId": "pb.lalpur"
                },
                {
                    "name": "Employee",
                    "code": "EMPLOYEE",
                    "tenantId": "pb.lalpur"
                },
                {
                    "name": "Dashbaord Viewer",
                    "code": "DASHBOARD_VIEWER",
                    "tenantId": "pb.lalpur"
                },
                {
                    "name": "Super User",
                    "code": "SUPERUSER",
                    "tenantId": "pb.dabourlower"
                },
                {
                    "name": "Dashbaord Viewer",
                    "code": "DASHBOARD_VIEWER",
                    "tenantId": "pb.massewal"
                },
                {
                    "name": "Expense Processing",
                    "code": "EXPENSE_PROCESSING",
                    "tenantId": "pb.dabourlower"
                },
                {
                    "name": "Expense Processing",
                    "code": "EXPENSE_PROCESSING",
                    "tenantId": "pb.massewal"
                },
                {
                    "name": "Dashbaord Viewer",
                    "code": "DASHBOARD_VIEWER",
                    "tenantId": "pb.dabourlower"
                },
                {
                    "name": "Bulk Demand Processing",
                    "code": "BULK_DEMAND_PROCESSING",
                    "tenantId": "pb.massewal"
                },
                {
                    "name": "GP Admin",
                    "code": "GP_ADMIN",
                    "tenantId": "pb.dabourupper"
                },
                {
                    "name": "Super User",
                    "code": "SUPERUSER",
                    "tenantId": "pb.lodhipur"
                },
                {
                    "name": "GP Admin",
                    "code": "GP_ADMIN",
                    "tenantId": "pb.massewal"
                },
                {
                    "name": "Expense Processing",
                    "code": "EXPENSE_PROCESSING",
                    "tenantId": "pb.lalpur"
                },
                {
                    "name": "Collection Operator",
                    "code": "COLLECTION_OPERATOR",
                    "tenantId": "pb.massewal"
                },
                {
                    "name": "Profile update",
                    "code": "PROFILE_UPDATE",
                    "tenantId": "pb.dabourlower"
                },
                {
                    "name": "Super User",
                    "code": "SUPERUSER",
                    "tenantId": "pb.massewal"
                },
                {
                    "name": "Employee",
                    "code": "EMPLOYEE",
                    "tenantId": "pb.dabourlower"
                },
                {
                    "name": "Super User",
                    "code": "SUPERUSER",
                    "tenantId": "pb.lalpur"
                },
                {
                    "name": "Collection Operator",
                    "code": "COLLECTION_OPERATOR",
                    "tenantId": "pb.dabourupper"
                },
                {
                    "name": "Collection Operator",
                    "code": "COLLECTION_OPERATOR",
                    "tenantId": "pb.lodhipur"
                }
            ],
            "active": true,
            "tenantId": "pb",
            "permanentCity": null
        }
    },
    "WaterConnection": {
        "id": null,
        "connectionNo": null,
        "propertyId": "PB-PT-2022-06-15-1722",
        "applicationNo": null,
        "tenantId": "pb.lodhipur",
        "action": "SUBMIT",
        "status": null,
        "meterInstallationDate": 1651343400000,
        "documents": null,
        "proposedTaps": 1,
        "noOfTaps": 1,
        "paymentType":"arrears",
        "arrears": 112,
        "penalty":50,
        "connectionType": "Metered",
        "oldConnectionNo": "",
        "meterId": "121212",
        "propertyType": "RESIDENTIAL",
        "previousReadingDate": 1651343400000,
        "previousReading": 56,
        "proposedPipeSize": 10,
        "connectionHolders": [
            {
                "id": null,
                "uuid": null,
                "userName": null,
                "password": null,
                "aadhaarNumber": null,
                "permanentAddress": null,
                "permanentCity": null,
                "permanentPinCode": null,
                "correspondenceCity": null,
                "correspondencePinCode": null,
                "correspondenceAddress": null,
                "pwdExpiryDate": null,
                "accountLocked": null,
                "active": null,
                "type": null,
                "tenantId": null,
                "altContactNumber": null,
                "ownerInfoUuid": null,
                "isPrimaryOwner": null,
                "ownerShipPercentage": null,
                "institutionId": null,
                "designation": null,
                "emailId": null,
                "isCorrespondenceAddress": null,
                "mobileNumber": "9182541372",
                "fatherOrHusbandName": "Sravan",
                "name": "Sravani",
                "status": null,
                "gender": "FEMALE",
                "ownerType": "NONE",
                "documents": null,
                "roles": null
            }
        ],
        "additionalDetails": {
            "initialMeterReading": 56,
            "meterReading": 56,
            "locality": "WARD1",
            "category": null,
            "subCategory": null,
            "aadharNumber": null,
            "propertyType": "RESIDENTIAL",
            "street": "",
            "doorNo": "",
            "collectionAmount": null,
            "collectionPendingAmount": null,
            "action": null
        },
        "processInstance": {
            "action": "SUBMIT"
        }
    }
}'
```
