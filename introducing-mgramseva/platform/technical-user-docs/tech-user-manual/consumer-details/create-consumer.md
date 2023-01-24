# Create Consumer

## Overview

Enables employees to create new Consumers or Connections - The process of onboarding the end-users.

**Link**

→ {base url}/mgramseva/home/consumercreate

![](<../../../../../.gitbook/assets/image (31).png>)

The Create Consumer card is available on the home screen as per the defined user role.

Click on the Consumer Create card navigates the user to the consumer creation screen.

Users enter the required details for the creation of a consumer.

If a user logs in for the first time then a walkthrough is populated following the same logic as in the home screen.

## File Path

Primary Files -[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/WalkFlowContainer.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/ConsumerDetails/ConsumerDetailsWalkThrough/WalkFlowContainer.dart) ,[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/walkthrough.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/ConsumerDetails/ConsumerDetailsWalkThrough/walkthrough.dart)

| **Fields**             | **Validations** |
| ---------------------- | --------------- |
| consumer Name\*        | `[A-Za-z ]`     |
| Gender\*               | None            |
| Spouse/Parent’s Name\* | `[A-Za-z ]`     |
| Phone Number\*         | `[0-9]`         |
| Old Connection No      | None            |
| Category               | None            |
| Sub Category           | None            |
| Door Number            | None            |
| Street Name/Number     | None            |
| Gram Panchayat Name\*  | None- Disabled  |
| Propert Type\*         | None            |
| Service Type\*         | None            |
| Meter Id               | `[a-zA-Z0-9]`   |
| Meter Reading          | `[0-9]`         |
| Billing Cycle          | None            |
| Arrears                | `[0-9.]`        |
| Advance                | `[0-9.]`        |
| Penalty                | `[0-9.]`        |

{% hint style="info" %}
**Note**: All fields are validated on Submit except the Phone number which gets validated on change.
{% endhint %}

## **API Details**

| API                                             | Params                                                                                                                                                                                                                                                                                                                    | Description                                                                         |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `/egov-mdms-service/v1/_search`                 | `[{"moduleName":"ws-services-masters","masterDetails":[{"name":"connectionType"}]},{"moduleName":"PropertyTax","masterDetails":[{"name":"PropertyType"}]},{"moduleName":"BillingService","masterDetails":[{"name":"TaxPeriod","filter":"[?(@.service=='WS' && @.fromDate <= 1631989800000 && @.toDate >= 1631989800000)]` | To get the Property Type and service Type and billing cycle values for the Dropdown |
| `egov-location/location/v11/boundarys/_search?` | `hierarchyTypeCode=REVENUE&boundaryType=Locality&tenantId={tenantID}`                                                                                                                                                                                                                                                     | To get the values for Locality DropDow                                              |

## Process Details

Consumer creation involves 2 sequential processes

1. Property Creation
2. Water connection Creation

After creating a property, the Property ID is linked to the WaterConnection Request JSON.

Water connection creation is of two types:

A metered connection that requires Meter ID and meter installation Date/ Last Meter Reading Date and an optional field to capture meter reading**.**

****![](<../../../../../.gitbook/assets/image (65).png>)****

Non-Metered Connection which requires the last billing cycle as mandatory params captured in the field as shown below.

![](<../../../../../.gitbook/assets/image (22).png>)

Users can switch between connection types by selecting a desired value from the **Service Type** DropDown.

![](<../../../../../.gitbook/assets/image (24).png>)



**Advance and Penalty**

![](<../../../../../.gitbook/assets/image (17).png>)

* For consumers, users can give either Advance or Arrears along with a Penalty by selecting the respective option using the radio buttons. If a user selects Advance, the field is shown or else Arrears and Penalty will be shown where the user can enter the required amount.
* The radio button “Advance” will be displayed only if the config flag “Advance enabled” is activated in the MDMS billing service.
* The “Penalty” field (displayed along with arrears) on selecting the Arrears radio button, will be displayed only if the config flag “Penalty enabled” is activated in the MDMS billing service. The user will be able to see the arrears field and can enter the arrears amount.

### **Logic Implemented For Advance**

billing-service/demand/\_search API is used for calculating the advance amount for the current bill. We can get the advance amount if taxHeadMasterCode contains 'WS\_ADVANCE\_CARRYFORWARD'. Here we have two properties - collection amount and tax amount. The tax amount is the advance amount that is added to the system and the collection amount is how much we utilised from the total advance amount. We can get the current advance from the `taxAmount - collectionAmount`

### **Logic Implemented For Time Penalty**

billing-service/demand/\_search API is used to calculate the Penalty amount. We can get the penalty amount if taxHeadMasterCode contains 'WS\_TIME\_ADHOC\_PENALTY'. We get the penalty amount from the tax amount property.

The due date is calculated by adding the billexpirtyDate days with the demand generation date.

### **Logic Implemented For First Demand Penalty**

If it is the first demand and it is having the taxHeadMasterCode 10201, we show the Penalty place holder in the bill details.

| API                                  | Description                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `property-services/property/_create` | <p>Property Creation Request JSON</p><p>defined in<a href="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/model/connection/property.dart"> <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/property.dart at develop · egovernments/punjab-mgramseva</a></p> |
| `ws-services/wc/_create`             | Water Connection Request JSON defined in[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/water\_connection.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/model/connection/water\_connection.dart)        |

## **Role Access Mapping**

```
    case Routes.CONSUMER_CREATE:
        return ['GP_ADMIN', 'SUPERUSER'];
```

## **Files Path**

**Model** →[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/property.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/model/connection/property.dart) ,[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/water\_connection.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/model/connection/water\_connection.dart)

**View** →[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/ConsumerDetails.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/ConsumerDetails/ConsumerDetails.dart)

**Controller** →[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/consumer\_details\_repo.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/repository/consumer\_details\_repo.dart) ,[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/consumer\_details\_provider.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/providers/consumer\_details\_provider.dart)

Components utilised from **Widgets Library**

| **Components**            | **File Path**                                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TextField Builder         | [https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart)                 |
| RadioButtonField Builder  | [https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/RadioButtonFieldBuilder.dart](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/RadioButtonFieldBuilder.dart)   |
| SearchSelectField Builder | [https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/SearchSelectFieldBuilder.dart](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/SearchSelectFieldBuilder.dart) |
| DatePicker Builder        | [https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/DatePickerFieldBuilder.dart](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/DatePickerFieldBuilder.dart)     |

****
