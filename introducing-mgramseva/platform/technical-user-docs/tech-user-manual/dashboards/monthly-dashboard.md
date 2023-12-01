# Monthly Dashboard

## Overview

Users are redirected to this screen if they select the GPWSC Dashboard option on the home screen.

**Link** → {base url}/mgramseva/home/dashboard

## **User Interaction On Screen**

![](<../../../../../.gitbook/assets/image (23).png>)

* Users can select the year from the drop-down which contains the list of the last 5 Financial years, on tap of any year respective months will be displayed.
* Users can see the user satisfaction average scores of the selected month.
* Users can see the Trend line graph plotted based on both Revenue and Expenditure.
* By selecting any Month from the table, users are navigated to the [Expenditure](https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/1926791281) and [Revenue](https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/1926824058) Dashboard screen.
* Users can see the WhatsApp Share button, by tapping on it users can share the Monthly dashboard as a screenshot via WhatsApp.

## **Files Path**

Primary Files:

{% embed url="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/dashboard/Dashboard.dart" %}

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/dashboard/revenue_dashboard/revenue_charts.dart" %}

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/dashboard/revenue_dashboard/revenue_dashboard.dart" %}

Secondary Files:&#x20;

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/dashboard/revenue_dashboard/revenue.dart" %}

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/components/Dashboard/nested_date_picker.dart" %}

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/components/Dashboard/DashboardCard.dart" %}

## **API Details**

| End Point                                             | Request Method | Request Info                                                                                                                                           |
| ----------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `dashboard-analytics/dashboard/getChartV2`            | POST           | <p><code>aggregationRequestDto</code> : {}</p><p><code>requestDate</code> : {}</p><p><code>headers</code> : {}</p><p><code>RequestInfo</code> : {}</p> |
| `ws-services/wc/_revenueCollectionData`               | POST           | <p>tenantId : {}<br>fromDate : {}<br>toDate : {}</p><p><code>RequestInfo</code> : {}</p>                                                               |
| `echallan-services/eChallan/v1/_chalanCollectionData` | POST           | <p>tenantId : {}<br>fromDate : {}<br>toDate : {}</p><p><code>RequestInfo</code> : {}</p>                                                               |
| `/filestore/v1/files`                                 | POST           | <p><code>tenantId</code> : {}</p><p><code>module</code> : {}</p>                                                                                       |
| `/egov-url-shortening/shortener`                      | POST           | `url` : {}                                                                                                                                             |

**Stack**

1 → Home Screen + Monthly Dashboard + Revenue Dashboard + update connection screen

Pop → Revenue Dashboard screen → Home Screen

2 → Home Screen + Monthly Dashboard + Expenditure Dashboard + update expenditure screen

Pop → Expenditure Dashboard Screen → Home Screen

3 → Home Screen + Monthly Dashboard + Revenue Dashboard + update connection screen + Update Success

Pop → Home Screen

4 → Home Screen + Monthly Dashboard + Expenditure Dashboard + update expenditure screen + Update Success

Pop → Home Screen

Widgets utilised from Library

| Widgets            | File Path                                                                                                                                                                                                                                                        | Description        |
| ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `Pagination`       | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/pagination.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/pagination.dart)                                     | Pagination         |
| `BuildTextField`   | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart)                         | Text Field         |
| `BillsTable`       | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/components/Dashboard/BillsTable.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/components/Dashboard/BillsTable.dart)           | Table              |
| `LabelText`        | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/LabelText.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/LabelText.dart)                                       | Subtitle           |
| `NestedDatePicker` | [https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/components/Dashboard/nested\_date\_picker.dart](https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/components/Dashboard/nested\_date\_picker.dart) | Nested Date Picker |

## **Role Access Mapping**

```
case Routes.DASHBOARD:
  return ['SUPERUSER', 'DASHBOARD_VIEWER'];
```

## **Files Path**

Model →&#x20;

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/model/dashboard/revenue_chart.dart" %}

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/model/dashboard/revenue_dashboard.dart" %}

View →

{% embed url="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/dashboard/Dashboard.dart" %}

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/dashboard/revenue_dashboard/Custom%20Label%20widget/custom_tooltip_label_render.dart" %}

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/dashboard/revenue_dashboard/revenue_charts.dart" %}

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/dashboard/revenue_dashboard/revenue_dashboard.dart" %}

Controller →

{% embed url="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/providers/dashboard_provider.dart" %}

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/providers/revenuedashboard_provider.dart" %}

