# Property Services

## **Overview**

One of the major applications of the eGov stack is that it helps municipalities and citizens handle property tax payments and other related functions on the property such as assessments, mutation, and so on.

## **Pre-requisites**

* Prior knowledge of Java/J2EE
* Prior knowledge of Spring Boot
* Prior knowledge of REST APIs and related concepts like path parameters, headers, JSON etc.
* Prior knowledge of Git
* Prior knowledge of the demand-based systems
* The following services should be up and running:
  * user
  * MDMS
  * Persister
  * Location
  * Localization
  * Id-Gen
  * Billing-service
  * URL-shortener

## **Key Functionalities**

The Property Service provides multiple functionalities starting from serving as a central repository where property information is registered for reference of citizens and other municipality-provided services such as water connection and sewerage management.\
An assessment can be done to calculate and pay tax on the property. The different services provided by the property services are -

Property Registry

Assessment

Mutation

Bifurcation

consolidation

**Registry Explanation**

* The registry flow helps the citizen/Employee to create a property in the system with the minimal information required.
* Other workflows such as assessment or mutation can be triggered on the existing ACTIVE Property in the registry.
* The property can be created, updated, cancelled, and searched followed by the process of Mutation and Assessment.
* The same entry in the registry can be referred to by other modules for various business purposes (Water charges).

## **Configuration Details**

MDMS CONFIG: [https://github.com/egovernments/egov-mdms-data/tree/DEV/data/pb/PropertyTax](https://github.com/egovernments/egov-mdms-data/tree/DEV/data/pb/PropertyTax)

### **Persister File Configuration**

The persister file configuration for property services can be found in the Config repo of eGov Git, which needs to be added in the persister service - [property-services-registry.yml](https://github.com/egovernments/configs/blob/master/egov-persister/property-services-registry.yml)

### **Workflow Configurations**

Each flow in property has a workflow associated with it, which can be controlled by the following configurations.

The Boolean field can enable/disable Workflow - the same field controls the update and creates the workflow.

| name                                                                                  | value         | description                                                                |
| ------------------------------------------------------------------------------------- | ------------- | -------------------------------------------------------------------------- |
| **is.workflow.enabled**                                                               | true/false    | enable disbale workflow                                                    |
| [**property.workflow.name**](http://property.workflow.name)                           | **PT.CREATE** | the name should match the config name in the workflow businessservice JSON |
| [**property.legacy.entry.workflow.name**](http://property.legacy.entry.workflow.name) | **PT.LEGACY** |                                                                            |
| [**property.update.workflow.name**](http://property.update.workflow.name)             | **PT.UPDATE** |                                                                            |

Workflow configuration for a property is created if the source is from the **WATER CONNECTION** module.

For the creation of property from the water and sewerage module, as per the use case mentioned in this [ticket](https://digit-discuss.atlassian.net/browse/RAIN-1772), a different workflow configuration is used.\
For each use case, to identify which workflow to use can be identified from this [mdms file](https://github.com/egovernments/egov-mdms-data/blob/DEV/data/pb/PropertyTax/PTWorkflow.json).

```
{
 "tenantId": "pb",
 "moduleName": "PropertyTax",
 "PTWorkflow":[
     {
         "businessService":"PT.CREATEWITHWNS",
         "initialAction":"OPEN",
         "inWorkflowStatusAllowed":false,
         "enable":false
     },
     {
      "businessService":"PT.CREATE",
      "initialAction":"open",
      "inWorkflowStatusAllowed":true,
      "enable":true
  }
     
 ]
}
```

Use Case 1, which involves property creation from the Water and Sewerage module, necessitates a single-step workflow. In the MDMS file mentioned above, ensure that the businessService with PT.CREATEWITHWNS object is enabled, allowing the field to be set as true. Property creation from the Water and Sewerage module will feature a one-step workflow, for properties in an ACTIVE state.

**Fields in the above MDMS file:**

<table><thead><tr><th width="244">MDMS Fields</th><th>Description</th></tr></thead><tbody><tr><td><strong>businessService</strong></td><td>Name of workflow config</td></tr><tr><td><strong>initialAction</strong></td><td>Indicate the start(initial) action of the particular workflow mention in businessService.</td></tr><tr><td><strong>inWorkflowStatusAllowed</strong></td><td>This field indicate whether the property with application status as “<strong>inWorkflow</strong>” can be use with water and sewerage connection creation.<br>If this field is true then for that particular use case, the property with “<strong>inWorkflow</strong>” status can be use with water and sewerage connection creation and vice versa</td></tr><tr><td><strong>enable</strong></td><td>If this filed is set as true, then the other fields associate with the particular object is use for property creation.</td></tr></tbody></table>

<mark style="color:red;">Note: Each object mentioned above represents a specific use case outlined in this ticket. Therefore, only one object (use case) enable field should be set to true at any given time.</mark>

Sample workflow config for use case 1 where property creation is from water and sewerage module with one-step workflow

```
{
    "BusinessServices": [
      {
        "tenantId": "pb",
        "businessService": "PT.CREATEWITHWNS",
        "business": "PT",
        "businessServiceSla": null,
        "states": [
          {
            "sla": null,
            "state": null,
            "applicationStatus": "INWORKFLOW",
            "docUploadRequired": false,
            "isStartState": true,
            "isTerminateState": false,
            "isStateUpdatable": false,
            "actions": [
              {
                "action": "OPEN",
                "nextState": "INITIATED",
                "roles": [
                  "CITIZEN",
                  "WS_CEMP",
                  "SW_CEMP"
                ]
              }
            ]
          },
          {
            "sla": null,
            "state": "INITIATED",
            "applicationStatus": "INWORKFLOW",
            "docUploadRequired": false,
            "isStartState": true,
            "isTerminateState": false,
            "isStateUpdatable": true,
            "actions": [
              {
                "action": "SUBMIT",
                "nextState": "APPROVED",
                "roles": [
                  "EMPLOYEE",
                  "CITIZEN",
                  "SW_CEMP",
                  "WS_CEMP"
                ]
              },
              {
                "action": "BACK",
                "nextState": "INWORKFLOW",
                "roles": [
                  "EMPLOYEE",
                  "CITIZEN",
                  "SW_CEMP",
                  "WS_CEMP"
                ]
              }
            ]
          },
          {
            "sla": null,
            "state": "INWORKFLOW",
            "applicationStatus": "INWORKFLOW",
            "docUploadRequired": false,
            "isStartState": true,
            "isTerminateState": false,
            "isStateUpdatable": true,
            "actions": [
              {
                "action": "SUBMIT",
                "nextState": "APPROVED",
                "roles": [
                  "EMPLOYEE",
                  "CITIZEN",
                  "SW_CEMP",
                  "WS_CEMP"
                ]
              }
            ]
          },
          {
            "sla": null,
            "state": "APPROVED",
            "applicationStatus": "ACTIVE",
            "docUploadRequired": false,
            "isStartState": false,
            "isTerminateState": true,
            "isStateUpdatable": false,
            "actions": null
          }
        ]
      }
    ]
  }
```

Sample workflow config - (The same PT.CREATE can be used for update workflow also since both involve the same functionality)

```
 {
  "RequestInfo": {
    "apiId": "Rainmaker",
    "action": "",
    "did": 1,
    "key": "",
    "msgId": "20170310130900|en_IN",
    "requesterId": "",
    "ts": 1513579888683,
    "ver": ".01",
    "authToken": "b39181b1-5c6b-484a-b825-6be2f62012b8"
  },
 "BusinessServices": [
  {
    "tenantId": "pb",
    "businessService": "PT.CREATE",
    "business": "PT",
    "businessServiceSla": null,
    "states": [
        {
            "tenantId": "pb",
            "sla": null,
            "state": null,
            "applicationStatus": "INWORKFLOW",
            "docUploadRequired": false,
            "isStartState": true,
            "isTerminateState": false,
            "actions": [
                {
                    "tenantId": "pb",
                    "action": "OPEN",
                    "nextState": "OPEN",
                    "roles": [
                        "CITIZEN",
                        "EMPLOYEE"
                    ]
                }
            ]
        },
        {
            "tenantId": "pb",
            "sla": null,
            "state": "OPEN",
            "applicationStatus": "INWORKFLOW",
            "docUploadRequired": false,
            "isStartState": true,
            "isTerminateState": false,
            "actions": [
                {
                    "tenantId": "pb",
                    "action": "VERIFY",
                    "nextState": "DOCVERIFIED",
                    "roles": [
                        "PT_DOC_VERIFIER"
                    ]
                },
                {
                  "tenantId": "pb",
                  "action": "REJECT",
                  "nextState": "REJECTED",
                  "roles": [
                      "PT_DOC_VERIFIER"
                  ]
              },
              {
                "tenantId": "pb",
                "action": "SENDBACKTOCITIZEN",
                "nextState": "CORRECTIONPENDING",
                "roles": [
                    "PT_DOC_VERIFIER"
                ]
            }
            ]
        },
        {
            "tenantId": "pb",
            "sla": null,
            "state": "DOCVERIFIED",
            "applicationStatus": "INWORKFLOW",
            "docUploadRequired": false,
            "isStartState": false,
            "isTerminateState": false,
            "actions": [
                {
                    "tenantId": "pb",
                    "action": "FORWARD",
                    "nextState": "FIELDVERIFIED",
                    "roles": [
                        "PT_FIELD_INSPECTOR"
                    ]
                }
            ]
        },
        {
            "tenantId": "pb",
            "sla": null,
            "state": "FIELDVERIFIED",
            "applicationStatus": "INWORKFLOW",
            "docUploadRequired": false,
            "isStartState": false,
            "isTerminateState": false,
            "actions": [
                {
                    "tenantId": "pb",
                    "action": "APPROVE",
                    "nextState": "APPROVED",
                    "roles": [
                        "PT_APPROVER"
                    ]
                },
                {
                    "tenantId": "pb",
                    "action": "REJECT",
                    "nextState": "REJECTED",
                    "roles": [
                        "PT_APPROVER"
                    ]
                }
            ]
        },
        {
            "tenantId": "pb",
            "sla": null,
            "state": "REJECTED",
            "applicationStatus": "INACTIVE",
            "docUploadRequired": false,
            "isStartState": false,
            "isTerminateState": true,
            "actions": null
        },
        {
            "tenantId": "pb",
            "sla": null,
            "state": "APPROVED",
            "applicationStatus": "ACTIVE",
            "docUploadRequired": false,
            "isStartState": false,
            "isTerminateState": true,
            "actions": null
        },
        {
          "tenantId": "pb",
          "sla": null,
          "state": "CORRECTIONPENDING",
          "applicationStatus": "INWORKFLOW",
          "docUploadRequired": false,
          "isStartState": false,
          "isTerminateState": false,
          "isStateUpdatable": true,
          "actions": [
              {
                  "tenantId": "pb",
                  "action": "REOPEN",
                  "nextState": "OPEN",
                  "roles": [
                    "CITIZEN",
                    "PT_CEMP"
                  ]
              },
              {
                  "tenantId": "pb",
                  "action": "REJECT",
                  "nextState": "REJECTED",
                  "roles": [
                    "CITIZEN",
                    "PT_CEMP"
                  ]
              }
          ]
      }
    ]
}
  ]
}	
```

**PT.LEGACY workflow config**

```
{
    "RequestInfo": {
      "apiId": "Rainmaker",
      "action": "",
      "did": 1,
      "key": "",
      "msgId": "20170310130900|en_IN",
      "requesterId": "",
      "ts": 1513579888683,
      "ver": ".01",
      "authToken": "{{authToken_amritsar}}"
    },
    "BusinessServices": [
      {
        "tenantId": "pb",
        "businessService": "PT.LEGACY",
        "business": "PT",
        "businessServiceSla": null,
        "states": [
          {
            "tenantId": "pb",
            "sla": null,
            "state": null,
            "applicationStatus": "INWORKFLOW",
            "docUploadRequired": false,
            "isStartState": true,
            "isTerminateState": false,
            "actions": [
              {
                "tenantId": "pb",
                "action": "OPEN",
                "nextState": "APPROVALPENDING",
                "roles": [
                  "CITIZEN",
                  "EMPLOYEE"
                ]
              }
            ]
          },
          {
            "tenantId": "pb",
            "sla": null,
            "state": "APPROVALPENDING",
            "applicationStatus": "INWORKFLOW",
            "docUploadRequired": false,
            "isStartState": true,
            "isTerminateState": false,
            "actions": [
              {
                "tenantId": "pb",
                "action": "APPROVE",
                "nextState": "APPROVED",
                "roles": [
                  "EMPLOYEE"
                ]
              },
              {
                "tenantId": "pb",
                "action": "REJECT",
                "nextState": "REJECTED",
                "roles": [
                  "EMPLOYEE"
                ]
              }
            ]
          },
          {
            "tenantId": "pb",
            "sla": null,
            "state": "REJECTED",
            "applicationStatus": "INACTIVE",
            "docUploadRequired": false,
            "isStartState": false,
            "isTerminateState": true,
            "actions": null
          },
          {
            "tenantId": "pb",
            "sla": null,
            "state": "APPROVED",
            "applicationStatus": "INACTIVE",
            "docUploadRequired": false,
            "isStartState": false,
            "isTerminateState": true,
            "actions": null
          }
        ]
      }
    ]
  }
```

Notifications :

To enable or disable notifications\
**notif.sms.enabled**=true

\#notif urls - makes use of the UI app host in notification service\
**egov.notif.commonpay =** citizen/egov-common/pay?consumerCode={CONSUMERCODE}\&tenantId={TENANTID}\
**egov.notif.view.property** = citizen/property-tax/my-properties/property/{PROPERTYID}/{TENANTID}\
**egov.notif.view.mutation** = citizen/pt-mutation/search-preview?applicationNumber={APPID}\&tenantId={TENANTID}

The current localization messages for notification -

```
[
        {
            "code": "PT_NOTIF_WF_STATE_LOCALE_OPEN",
            "message": "Open",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_STATE_LOCALE_DOCVERIFIED",
            "message": "Document Verified",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_STATE_LOCALE_FIELDVERIFIED",
            "message": "Field verified",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_STATE_LOCALE_APPROVED",
            "message": "Approved",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_STATE_LOCALE_REJECTED",
            "message": "Rejected",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_STATE_LOCALE_PAID",
            "message": "Paid",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_MT_OPEN",
            "message": "Dear {OWNER_NAME}, Your application to edit ownership details of property ID {PROPERTYID} has been submitted successfully. Your application no. for future reference is {APPID}. You can track your application on the link given below - {MTURL} Thank you",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_MT_STATE_CHANGE",
            "message": "Dear {OWNER_NAME}, Status for your application no. {APPID} for property {PROPERTYID} to edit ownership has been changed to {STATUS}. You can track your application on the link given below - {MTURL} Thank you",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_MT_PAYMENT_PENDING",
            "message": "Dear {OWNER_NAME}, Payment is pending for your application no. {APPID} for property ID {PROPERTYID} to edit ownership. You can pay your mutation fee on the below link - {PAYLINK} or visit your ULB to pay your dues. Thank you",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_MT_PAID",
            "message": "Dear {OWNER_NAME}, You’ve successfully paid mutation fee - INR {AMOUNT} for application no. {APPID} for property ID {PROPERTYID}. You can download your receipt on the below link - {MTURL} Thank you ",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_MT_APPROVED",
            "message": "Dear {OWNER_NAME}, Your property ownership has been changed as per the application no. {APPID} for property {PROPERTYID}. You can download your mutation certificate on the below link - {MTURL} Thank you",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_MT_NONE",
            "message": "Dear {OWNER_NAME}, Your property with property-id {PROPERTYID} has been mutated. You can view your property on the link given below - {MTURL} Thank you",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_OPEN",
            "message": "Dear {OWNER_NAME}, Your application to {updated/created} property with Id {PROPERTYID} has been submitted successfully. Your application no. for future reference is {APPID}. You can track your application on the link given below - {PTURL} Thank you",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_STATUS_CHANGE",
            "message": "Dear {OWNER_NAME}, Status for your application no. {APPID} for property {PROPERTYID} to {updated/created} property has been changed to {STATUS}. You can track your application on the link given below - {PTURL} Thank you",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_APPROVED",
            "message": "Dear {OWNER_NAME}, Your property has been {updated/created} as per the application no. {APPID} for property {PROPERTYID}. You can view your property on the link given below - {PTURL} Thank you",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        },
        {
            "code": "PT_NOTIF_WF_UPDATE_NONE",
            "message": "Dear {OWNER_NAME}, Your property with property-id {PROPERTYID} has been {updated/created}. You can view your property on the link given below - {PTURL} Thank you",
            "module": "rainmaker-pt",
            "locale": "en_IN"
        }
    ]
```

Configs in App.props

<table><thead><tr><th width="294">name</th><th>value</th></tr></thead><tbody><tr><td>egov.idgen.ack.format</td><td>PB-AC-[cy:yyyy-MM-dd]-[SEQ_EG_PT_ACK]</td></tr><tr><td>egov.idgen.mutation.format</td><td>PB-MT-[CITY]-[SEQ_EG_PT_MUTATION]</td></tr><tr><td>egov.idgen.assm.format</td><td>PB-AS-[cy:yyyy-MM-dd]-[SEQ_EG_PT_ASSM]</td></tr><tr><td>egov.idgen.ptid.format</td><td>PB-PT-[cy:yyyy-MM-dd]-[SEQ_EG_PT_PTID]</td></tr><tr><td>citizen.allowed.search.params</td><td>accountId,ids,propertyDetailids,mobileNumber,oldpropertyids</td></tr><tr><td>employee.allowed.search.params</td><td>accountId,ids,propertyDetailids,mobileNumber,oldpropertyids</td></tr></tbody></table>

## Integration Details

### Integration Scope

Property service can be integrated with any organization or system that wants to maintain a record of the property and collect taxes with ease.

### Integration Benefits

* Easy to create and simple process of self-assessment to avoid the hassle.
* Helps maintain property data which can be used in the integration of other essential services like asset management, water connection and so on.
* provides additional functionalities like mutation and assessment of properties.

### Integration Steps

1. Customers can create a property using the /property/\_create
2. Search the property using /property/\_searchendpoint
3. /property/\_update endpoint to update the property demand as needed.
4. Mutation can be carried out with the help of /property/\_update itself, no extra API is required.

## **Reference Docs**

**Doc Links**

<table data-header-hidden><thead><tr><th width="202"></th><th></th></tr></thead><tbody><tr><td><strong>Title</strong> </td><td><strong>Link</strong></td></tr><tr><td>USER Service</td><td><a href="https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/669450371">https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/669450371</a></td></tr><tr><td>url-shortening</td><td> <a href="https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/896892936">https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/896892936</a></td></tr><tr><td> MDMS</td><td> <a href="https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/723189807">https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/723189807</a></td></tr><tr><td>Billing-service</td><td><a href="https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/1620672528">https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/1620672528</a></td></tr><tr><td>Location</td><td><a href="https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/664338482">https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/664338482</a></td></tr><tr><td>Workflow</td><td><a href="https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/664174657">https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/664174657</a></td></tr><tr><td>Persister</td><td></td></tr><tr><td>Localization</td><td></td></tr><tr><td> Id-Gen service</td><td></td></tr></tbody></table>

**API LIST**

<table data-header-hidden><thead><tr><th width="214"></th><th></th></tr></thead><tbody><tr><td><strong>Title</strong> </td><td><strong>Link</strong></td></tr><tr><td> /Property/_create</td><td><a href="https://www.getpostman.com/collections/02d01e7b46c79c140863">https://www.getpostman.com/collections/02d01e7b46c79c140863</a></td></tr><tr><td> /Property/_update</td><td><a href="https://www.getpostman.com/collections/02d01e7b46c79c140863">https://www.getpostman.com/collections/02d01e7b46c79c140863</a></td></tr><tr><td>/property/_search</td><td><a href="https://www.getpostman.com/collections/02d01e7b46c79c140863">https://www.getpostman.com/collections/02d01e7b46c79c140863</a></td></tr></tbody></table>
