# Expenditure Dashboard

## Overview

Users are redirected to this screen when they select the GPWSC Dashboard option on the home screen.

**Link** → {base url}/mgramseva/home/dashboard?tab=1

![](<../../../../../.gitbook/assets/image (1).png>)

## **User Interaction On Screen**

* Users can select the year from the drop-down which contains the list of financial years.
* From the text field, users can search for the expenses using Bill ID or vendor name.
* Users can see the expense data for paid and pending with respective tabs.
* Initially, only 10 expenses are loaded for the selected tab. The pagination dropdown and right arrow click enable the user to load and view more expense records.
* Selecting any Bill ID navigates the users to the [Expense update screen](https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/1927348594).

## **Files Path** <a href="#files-path" id="files-path"></a>

Primary Files:[<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/Dashboard.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/dashboard/Dashboard.dart)​[<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/search\_expense.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/dashboard/search\_expense.dart)

## **API Details**

| End Point                                | Request Method | Request Info                                                                                                                                                                                                                                       |
| ---------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /`echallan-services/eChallan/v1/_create` | POST           | <p>tenantId : {}<br>offset ; {}<br>limit : {}<br>fromDate : {}<br>toDate : {}<br>vendorName : {}<br>challanNo : {}<br>toDate : {}<br>freeSearch : {}<br>status : {}<br>isBillCount : {}</p><p>sortOrder ; {}<br>sortBy : {}<br>isBillPaid : {}</p> |

**Stack**

1 → Home Screen. + Dashboard expenditure screen + update expense screen

Pop → Dashboard expenditure screen → Home Screen

2 → Home Screen. + Dashboard expenditure screen + update expense screen + expense update success

Pop → Home Screen

Widgets utilised from Library

| Widgets          | File Path                                                                                                                                                                                                                                              | Description |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `Pagination`     | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/pagination.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/pagination.dart)                           | Pagination  |
| `BuildTextField` | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart)               | Text Field  |
| `BillsTable`     | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/components/Dashboard/BillsTable.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/components/Dashboard/BillsTable.dart) | Table       |
| `LabelText`      | ****[https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/LabelText.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/LabelText.dart)                         | Subtitle    |

## **Role Access Mapping**

```
case Routes.DASHBOARD:
  return ['SUPERUSER', 'DASHBOARD_VIEWER'];
```

## **Files Path**

Model →[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/expenses\_details.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/model/expensesDetails/expenses\_details.dart)

View →[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/Dashboard.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/dashboard/Dashboard.dart)&#x20;

[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/search\_expense.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/dashboard/search\_expense.dart)

Controller →[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/dashboard\_provider.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/providers/dashboard\_provider.dart)&#x20;

[<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/expenses\_repo.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/repository/expenses\_repo.dart)

