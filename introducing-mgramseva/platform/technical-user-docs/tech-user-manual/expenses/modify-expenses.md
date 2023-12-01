# Modify Expenses

## Overview

Enables employees to modify/edit the expenses based on the status of the payment.

![](<../../../../../.gitbook/assets/image (71).png>)

**Link** → {base url}/mgramseva/home/searchExpense/result/updateExpense

Update Expenses card is visible on the home screen for defined user roles that have EXPENSE PROCESSING permission. Clicking on the Update Expenditure card in the expense search results screen navigates the user to the Edit Expense Bills screen.

Users can edit the previously populated expense details for the vendors.

Clicking on the Submit button navigates the users to the Modified Expenditure Success screen.

## **Logic Implemented For Paid Or Unpaid Bills**

**Use Case1:** When the status is “Unpaid”

Allows modification of all the details except the Bill Id. Users can Mark the Bill as “Cancelled” by checking on the option.

**Use Case2:** When the status is “Paid”

Cannot modify any details. But the users can Mark the Bill as “Cancelled” by checking the option.

![](<../../../../../.gitbook/assets/image (1).png>)

## File Path

Primary Files -[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/ExpenseDetails.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/AddExpense/ExpenseDetails.dart)

## **Field Validations**

| Fields                      | Validations                                                                        |
| --------------------------- | ---------------------------------------------------------------------------------- |
| Vendor Name\*               | `[A-Za-z ]`                                                                        |
| Mobile Number\*             | `[0-9] & is mandatory only if a new vendor is added`                               |
| Type of Expense\*           | None                                                                               |
| Amount\*                    | `[0-9]`                                                                            |
| Bill Date\*                 | Before Current Date and after party Bill Date                                      |
| Party Bill Date             | `Should be before the Bill Date`                                                   |
| Bill Paid                   | None                                                                               |
| Paid Date                   | After Bill date and less than current Date                                         |
| Attach Documents            | Option to upload a single document, Supported files - PDF, JPEG, PNG (maximum 5MB) |
| Mark this Bill as Cancelled | None                                                                               |

## **API Details**

| API                             | Params                                                                                                                                                                                   | Description                                                                                 |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `/egov-mdms-service/v1/_search` | `[{"moduleName": "Expense", "masterDetails": [{"name": "ExpenseType"},]}, {"moduleName": "BillingService", "masterDetails": [{"name": "BusinessService"}, {"name": "TaxHeadMaster"},]}]` | To get the Expense Type for the Dropdown                                                    |
| `egov.org.in/vendor/v1/_search` | `tenantId: {}`                                                                                                                                                                           | To get the list of vendors in the selected tenant for the suggestion text box - Vendor Name |

**Stack**

1 → Home Screen. + Search Expense Screen + Expense Results Screen + Edit Expense Bills Screen

Pop → Expense Results Screen

Widgets utilised from Library

| Widgets                                                                                                                                                                                       | File Path                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| `BuildTextField`                                                                                                                                                                              | [**https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart**](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart)                                                                                                                                                                                                                                                                                              | Text Field            |
| `AutoCompleteView`                                                                                                                                                                            | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/auto\_complete.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/auto\_complete.dart)                                                                                                                                                                                                                                                                                                      | Suggestion Text Field |
| <p></p><ul><li><code>SelectFieldBuilder</code></li></ul><p><strong>(Primary File)</strong></p><ul><li><code>SearchSelectFieldBuilder</code></li></ul><p><strong>(Secondary File)</strong></p> | <p><a href="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/SelectFieldBuilder.dart">https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/SelectFieldBuilder.dart</a> </p><p><a href="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/SearchSelectFieldBuilder.dart">https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/SearchSelectFieldBuilder.dart</a></p> | Searchable Drop down  |
| `DatePickerFieldBulder`                                                                                                                                                                       | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/DatePickerFieldBuilder.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/DatePickerFieldBuilder.dart)                                                                                                                                                                                                                                                                                      | Date Picker           |
| `CommonSuccessPage`                                                                                                                                                                           | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/CommonSuccessPage.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/CommonSuccessPage.dart)                                                                                                                                                                                                                                                                                                | Success Screen        |
| `BottomButtonBar`                                                                                                                                                                             | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/BottonButtonBar.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/BottonButtonBar.dart)                                                                                                                                                                                                                                                                                                    | Button                |
