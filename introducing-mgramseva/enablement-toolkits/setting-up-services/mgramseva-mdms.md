# mGramSeva MDMS

## Overview

mGramSeva's Master Data Management System ([MDMS](https://github.com/misdwss/mdms-mgramseva)) is organized into several folders, each containing essential JSON files that define various aspects of the application's configuration. This documentation provides an overview of the key folders and their respective files, along with a description of the data contained within each file.

## Steps

#### 1. [ACCESSCONTROL-ACTIONS-TEST](https://github.com/misdwss/mdms-mgramseva/tree/master/data/pb/ACCESSCONTROL-ACTIONS-TEST)

This folder contains the `actions-test.json` file, which defines various API endpoints along with their configurations.

{% code lineNumbers="true" %}
```json
{
  "id": 11,
  "name": "Employee Count",
  "url": "/egov-hrms/employees/_count",
  "parentModule": "egov-hrms",
  "displayName": "Employee Count",
  "orderNumber": 0,
  "enabled": false,
  "serviceCode": "egov-hrms",
  "code": "null",
  "path": ""
}

```
{% endcode %}

* `id`: Unique identifier for the API endpoint. Increase id with respect to id present in action-test.json file.
* `name`: Name of the endpoint.
* `url`: URL of the API endpoint.
* `Other things` : As per your specific requirements.

#### 2. [ACCESSCONTROL-ROLEACTIONS](https://github.com/misdwss/mdms-mgramseva/tree/master/data/pb/ACCESSCONTROL-ROLEACTIONS)

This folder contains the `roleactions.json` file, which associates roles with action IDs.

{% code lineNumbers="true" %}
```json
{
  "rolecode": "HRMS_ADMIN",
  "actionid": 11,
  "actioncode": "",
  "tenantId": "pb"
}

```
{% endcode %}

* `rolecode`: Code representing the role.
* `actionid`: Action ID associated with the role, linking to entries in actions-test.json.
* `actioncode`: Additional code for the action if needed.
* `tenantId`: Tenant ID associated with the role.

3\. [**ACCESSCONTROL-ROLES**](https://github.com/misdwss/mdms-mgramseva/tree/master/data/pb/ACCESSCONTROL-ROLES)

This folder contains the `roles.json` file, defining roles in the system.

{% code lineNumbers="true" %}
```json
{
  "code": "ANONYMOUS",
  "name": "anonymous",
  "description": "anonymous user"
}

```
{% endcode %}

* `code`: Code representing the role.
* `name`: Name of the role.
* `description`: Description of the role.

#### 4. [BillingService](https://github.com/misdwss/mdms-mgramseva/tree/master/data/pb/BillingService)

This folder contains various JSON files related to billing services.

\
**4.1** **`BusinessService.json`**

Defines business services, such as expenses like electricity bills and salaries.

{% code lineNumbers="true" %}
```
{
  "businessService": "EXPENSE.ELECTRICITY_BILL",
  "code": "EXPENSE.ELECTRICITY_BILL",
  "collectionModesNotAllowed": [
    "DD"
  ],
  "partPaymentAllowed": true,
  "isAdvanceAllowed": false,
  "isVoucherCreationEnabled": true,
  "isActive": true,
  "type": "Adhoc"
}

```
{% endcode %}

* `businessService`: Identifier for the business service.
* `code`: Code representing the business service.
* `collectionModesNotAllowed`: Collection modes not allowed for the service.
* `partPaymentAllowed`: Indicates whether part payment is allowed.
* `isAdvanceAllowed`: Indicates whether advance payment is allowed.
* `isVoucherCreationEnabled`: Indicates whether voucher creation is enabled.
* `isActive`: Indicates whether the service is active.
* `type`: Type of the service.

#### 4.2 `PaymentService.json`

This file, located in the `billingservice` folder, provides configurations for payment services within the Billing Service module.

```json
{
  "tenantId": "pb",
  "moduleName": "BillingService",
  "PaymentService": [
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
      "billGineiURL": "egov-searcher/bill-genie/waterbills/_get",
      "isBillAmendmentEnabled": true
    }
  ]
}

```

* `tenantId`: The identifier for the tenant associated with the configuration.
* `moduleName`: The name of the module, in this case, "BillingService."
* `PaymentService`: An array containing configurations for different payment services.

**Payment Service Configuration:**

* `businessService`: Identifier for the business service.
* `code`: Code representing the payment service.
* `collectionModesNotAllowed`: Array specifying modes of payment not allowed for this service.
  * `"DD"`: Demand Draft
  * `"CHEQUE"`: Cheque
  * `"CARD"`: Card
  * `"OFFLINE_NEFT"`: Offline NEFT
  * `"OFFLINE_RTGS"`: Offline RTGS
  * `"POSTAL_ORDER"`: Postal Order
  * `"ONLINE"`: Online
* `partPaymentAllowed`: Indicates whether part payment is allowed for this service.
* `isAdvanceAllowed`: Indicates whether advance payment is allowed for this service.
* `demandUpdateTime`: Time interval (in milliseconds) for updating demands.
* `isVoucherCreationEnabled`: Indicates whether voucher creation is enabled for this service.
* `billGineiURL`: URL for generating bills using Bill Genie.
* `isBillAmendmentEnabled`: Indicates whether bill amendment is enabled for this service.

This configuration specifies the payment modes not allowed for the "ws-services-calculation" business service, whether part payment and advance payment are allowed, the demand update time, voucher creation status, Bill Genie URL, and bill amendment status.

#### 4.3 `TaxHeadMaster.json`

This file is responsible for defining the various charges and taxes which are going to be configured in the application.

#### 4.4 `TaxPeriod.json`

This file is used to define the number of financial years which are supported in each tax head.

5. [**ws-services-masters**](https://github.com/misdwss/mdms-mgramseva/tree/master/data/pb/ws-services-masters)

This folder contains various JSON files related to ws-services-masters.

&#x20; 6\. [**ws-services-calculation**](https://github.com/misdwss/mdms-mgramseva/tree/master/data/pb/ws-services-calculation)\
\
This folder contains various JSON files related to ws-services-calculations.

7. [**PropertyTax**](https://github.com/misdwss/mdms-mgramseva/tree/master/data/pb/PropertyTax)

This folder contains various JSON files related to property tax.

8. [**ExpenseType**](https://github.com/misdwss/mdms-mgramseva/blob/master/data/pb/Expense/ExpenseType.json)

This folder contains expense type in JSON format.

All (1 to 8 points) are state-level changes.

9\. [**Tenant**](https://github.com/misdwss/mdms-mgramseva/tree/master/data/pb/aassalhihjag)[ **Folder**](https://github.com/misdwss/mdms-mgramseva/tree/master/data/pb/aassalhihjag) **(City level changes for every city there is one folder in MDMS)**

For each tenant, there is a unique folder containing three subfolders, each with its specific configuration files.

#### 1. `businessservice.json` - Billing Service Configuration

This file, located in the `billing service` folder, provides tenant-specific configurations for the Billing Service module. It is similar to the global `BusinessService.json` configuration but is specific to the tenant.

#### 2. `boundary-data.json` - Location Boundary Data Configuration

This file, located in the `egov-location` folder contains boundary data specific to the tenant.

Details of the structure and content of this file would be specific to the actual data in the system. Please refer to the specific `boundary-data.json` file for detailed information.

#### 3. `WCBillingSlab.json` - Water Connection Billing Slab Configuration

This file, found in the `ws-services-calculation` folder defines billing slabs for water connection based on building type and connection type.

{% code lineNumbers="true" %}
```json
{
  "id": "1",
  "buildingType": "RESIDENTIAL",
  "connectionType": "Metered",
  "calculationAttribute": "Water consumption",
  "minimumCharge": 100,
  "slabs": [
    {
      "from": 0,
      "to": 1000000,
      "charge": 2,
      "meterCharge": 50
    }
  ]
}

```
{% endcode %}

* `id`: Unique identifier for the billing slab.
* `buildingType`: Type of the building (e.g., RESIDENTIAL).
* `connectionType`: Type of connection (e.g., Metered).
* `calculationAttribute`: Attribute used for calculation (e.g., Water consumption).
* `minimumCharge`: Minimum charge for the billing slab.
* `slabs`: Array defining the billing slabs, including `from`, `to`, `charge`, and `meterCharge`.

This configuration is used to determine rates for water consumption based on the specified billing slab criteria.

There is a [tenant](https://github.com/misdwss/mdms-mgramseva/tree/master/data/pb/tenant) folder in the MDMS which contains all tenants in [tenants.json ](https://github.com/misdwss/mdms-mgramseva/blob/master/data/pb/tenant/tenants.json)file.
