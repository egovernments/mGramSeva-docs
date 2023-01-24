# Search Expense Bills

## Overview

Users are redirected to this screen by selecting the Update Expense card on the home screen.

Update Expenses card is available on the home screen for defined roles that have EXPENSE PROCESSING permission.

**Link** → {base url}/mgramseva/home/searchExpense

![](<../../../../../.gitbook/assets/image (99).png>)

## **User Interaction On Screen**

* Users can search the expense bills with the Vendor Name / Type of Expense / Bill ID ( `Search with any one of these criteria` )
* Click on Search navigates the user to the expense results screen which lists the expenditure bills matching the search criteria.

## **File Path**

Primary Files:

[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/search\_expense.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/expense/search\_expense.dart)&#x20;

[<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/expense\_results.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/expense/expense\_results.dart)

![](<../../../../../.gitbook/assets/image (7).png>)

## **Field Validations**

| Fields               | Validations                |
| -------------------- | -------------------------- |
| Owner Mobile Number  | `r'^(?:[+0]9)?[0-9]{10}$'` |
| Name of the Consumer | `r'^[A-Za-z ]'`            |
| Old Connection ID    | `No Validation`            |
| New Connection ID    | `No Validation`            |

## **API Details**

| API                             | Params                                                                                                                                                                                   | Description                              |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| `/egov-mdms-service/v1/_search` | `[{"moduleName": "Expense", "masterDetails": [{"name": "ExpenseType"},]}, {"moduleName": "BillingService", "masterDetails": [{"name": "BusinessService"}, {"name": "TaxHeadMaster"},]}]` | To get the Expense Type for the Dropdown |

**Stack**

1 → Home Screen. + Search Expense Bills Screen

Pop → Home Screen

Widgets utilised from Library

| Widgets                                                                                                                                                                                       | File Path                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Description          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| `BuildTextField`                                                                                                                                                                              | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart)                                                                                                                                                                                                                                                                                                  | Text Field           |
| <p></p><ul><li><code>SelectFieldBuilder</code></li></ul><p><strong>(Primary File)</strong></p><ul><li><code>SearchSelectFieldBuilder</code></li></ul><p><strong>(Secondary File)</strong></p> | <p><a href="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/SelectFieldBuilder.dart">https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/SelectFieldBuilder.dart</a> </p><p><a href="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/SearchSelectFieldBuilder.dart">https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/SearchSelectFieldBuilder.dart</a></p> | Searchable Drop down |
| `BottomButtonBar`                                                                                                                                                                             | ****[**https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/BottonButtonBar.dart**](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/BottonButtonBar.dart)****                                                                                                                                                                                                                                                                                        | Button               |

