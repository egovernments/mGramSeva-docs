# Collect Payment

## Overview

The Revenue Collector uses the Collect Payment screen to collect payment against the demand generated for metered and non-metered connections or any arrears.  &#x20;

Collect Payment card is available on the home screen to the user role having the `COLLECTION_OPERATOR` permission.

**Link** → {base url}/mgramseva/household/details/collectPayment

![](<../../../../.gitbook/assets/image (107).png>)

## **User Interaction On Screen**

* Users can pay the total due amount that is set by default.
* Or, users can also pay an advance amount or partial amount by changing the value in the payment amount field to a higher or lower value. If a partial amount is to be paid, then users need to provide a lower amount than the total due amount. If the advance amount is to be paid, users need to provide a higher amount than the total due amount.
* Clicking on Collect Payment opens a confirmation popup to confirm if the amount entered is correct.
* Clicking on Confirm navigates the user to the Payment Success screen. The user can download the receipt or share the receipt for the collected amount.
* Users can also print mini receipts with the help of Bluetooth thermal printers by selecting the [Print mini receipt](bluetooth-thermal-printer-integration.md) option.

## **Logic Implemented For Advance**

`billing-service/demand/_search` API is used to calculate the advance amount for the current bill.  The advance amount is fetched from the logic - if `taxHeadMasterCode` is `'WS_ADVANCE_CARRYFORWARD'.` This has two properties - collection amount and tax amount. The tax amount is the advance amount that is added to the system and the collection amount is the amount utilised from the total advance amount. We can get the current advance from the `taxAmount - collectionAmount.`

## **Logic Implemented For Time Penalty**

`ws-calculator/waterCalculator/_getPenaltyDetails` API is used to calculate the Time Penalty amount. The time penalty amount is fetched from the logic - if `taxHeadMasterCode`  is`'WS_TIME_PENALTY'.` The time penalty amount is retrieved from the tax amount property of the latest demand.

The due date is calculated by adding the `billexpirtyDate` days to the demand generation date.

If the due date is crossed, `billing-service/demand/_search` API gives the Time Penalty applied.

## **Logic Implemented For First Demand Penalty**

`billing-service/demand/_search` API gives the Normal Penalty. The Penalty placeholder in the bill details is visible if it is the first demand and has the `taxHeadMasterCode` as `10201.`

## **Logic Implemented For Arrears Breakup**

The arrears are broken into 'BL\_(TaxHeadCode)' fetched from Bill Details-->Bill Account Details --> Tax Head Code. The amount of particular arrears is similar to the Bill Details--> Amount from the Fetch Bill API.

![](<../../../../.gitbook/assets/image (149).png>)

(For instance, `if there are two bills with tax head codes is 10101 and 10102, then arrears break up is represented as BL_10101(Water Charges) with the corresponding amount and BL_10102(Water Charges-Arrears) with the corresponding amount`).

{% hint style="info" %}
**Note:**

* The “Penalty” details displayed under “Bill Details“ section is displayed only if the config flag “Penalty enabled” is set as true. If it is set as false, then the penalty details is not displayed.
* The “Advance” details displayed under “Bill Details“ section is displayed only if the config flag “Advance enabled” is set as true. If it is set as false, then the advance details is not displayed.
{% endhint %}

## **Files Path**

Primary Files: [https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/screeens/common/collect\_payment.dart](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/screeens/common/collect\_payment.dart)

## **Field Validations**

| Fields                                           | Validations                  |
| ------------------------------------------------ | ---------------------------- |
| Partial Amount (`If Partial Amount is selected`) | `r'^[0-9]+$' , Can not be 0` |
| Payment Method                                   | **Defaulted to Cash**        |

## **API Details**

| **API EndPoint**                                  | **Input Params (Modules)**                                                                                                                                                                                   | **Description**                                                                      |   |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | - |
| <p>egov-mdms-service/v1/_search</p><p> </p>       |  \[{"moduleName":"BillingService","masterDetails":\[{"name":"BusinessService","filter":"\[?(@.code=='WS')]"}]}]                                                                                              | To get the billGeneiURL, Calculation of Water services and collectionModesNotAllowed |   |
| billing-service/bill/v2/\_fetchbill               | <p>consumerCode : {}</p><p>businessService : WS</p><p>tenantId : {}</p>                                                                                                                                      | To fetch the bills of the connection/Consumer                                        |   |
| billing-service/demand/\_search                   | consumerCode, businessService, tenantId                                                                                                                                                                      | To Fetch Demand Details                                                              |   |
| ws-calculator/waterCalculator/\_getPenaltyDetails | <p>{ "tenantId": "", "consumerCodes": "", "isGetPenaltyEstimate": "true"},</p><p>{</p><p>"GetBillCriteria":</p><p>{"tenantId": "", "isGetPenaltyEstimate": true, "consumerCodes": [""] }</p><p>}</p><p> </p> | To get the Time Penalty Amount                                                       |   |

**Stack**

1 → Home Screen. + Search Connection Screen + Household Results + Household Details Screen + Collect Payment Screen

Pop → Household Details Screen

Widgets utilised from Library

| **Widgets**       | **File Path**                                                                                                                                                                                                                              | **Description**                                                |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| BuildTextField    | [https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart)               | Text Field                                                     |
| BottomButtonBar   | [https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/BottonButtonBar.dart](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/BottonButtonBar.dart)                 | Button                                                         |
| RadioButtonField  | [https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/RadioButtonFieldBuilder.dart](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/RadioButtonFieldBuilder.dart) | Radio Buttons for options                                      |
| ConfirmationPopUp | [https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/ConfirmationPopUp.dart](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/ConfirmationPopUp.dart)             | Dialog box to confirm and proceed to next step                 |
| CustomDetailsCard | [https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/CustomDetails.dart](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/CustomDetails.dart)                     | Secondary theme color Card to display Details Eg. Penalty Card |

