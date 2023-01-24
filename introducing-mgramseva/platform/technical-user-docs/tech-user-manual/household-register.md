# Household Register

## **Overview**&#x20;

Users are redirected to this screen once they select the Household Register tile/card on the home screen.

The Household Register tile/card is displayed to the user with `COLLECTION_OPERATOR` role.

**Link** → {base url}/mgramseva/home/householdRegister

<figure><img src="../../../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

## **User Interaction On Screen**

* From the text field, users can search for connections by using the connection ID.
* Users can see all the connections data of the selected tenant till the current date based on their payment status (Ex: All, Paid, Pending).
* Initially, only 10 connections are loaded for the selected tab. The pagination drop-down and right arrow click enable users to view more connections.
* Selecting any connection ID redirects users to the View Consumer Details screen.
* Click on the Download button to get all the household records in PDF format.
* Click on Share to share the PDF on Whats App.

![](<../../../../.gitbook/assets/image (75).png>)

## **File Path**

Primary Files:

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/HouseholdRegister/HouseholdRegister.dart" %}

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/HouseholdRegister/HouseholdSearch.dart" %}

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/HouseholdRegister/HouseholdList.dart" %}

{% embed url="https://github.com/misdwss/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/HouseholdRegister/household_pdf.dart" %}

## **API Details**

| End Point                        | Request Method | Request Info                                                                                                                                                                                                                                                                                                                 |
| -------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| /`ws-services/wc/_search`        | POST           | <p><code>tenantId</code> : {}<br><code>offset</code> ; {}<br><code>limit</code> : {}<br><code>toDate</code> : {}<br><code>isCollectionCount</code>: {}</p><p><code>isBillPaid</code><br><code>connectionNumber</code>: {}<br><code>freeSearch</code>: {}</p><p><code>sortOrder</code>: {}</p><p><code>sortBy</code> : {}</p> |
| `/filestore/v1/files`            | POST           | <p><code>tenantId</code> : {}</p><p><code>module</code> : {}</p>                                                                                                                                                                                                                                                             |
| `/egov-url-shortening/shortener` | POST           | `url` : {}                                                                                                                                                                                                                                                                                                                   |

**Stack**

1 → Home Screen. + Household Register Screen

Pop → Household Register Screen→ Home Screen

2 → Home Screen. + Household Register Screen + View Consumer Details Screen

Pop → View Consumer Details Screen → Household Register Screen

**Widgets used from Library**

| **Widgets**      | **File Path**                                                                                                                                                                                                                                                                                                                                                                                                    | **Description** |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| `Pagination`     | [<img src="https://github.com/fluidicon.png" alt="" data-size="line">](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/pagination.dart)****[**https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/pagination.dart**](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/pagination.dart)**** | Pagination      |
| `BuildTextField` | [<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/TextFieldBuilder.dart at master · misdwss/punjab-mgramseva](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart)                                                                                                                                                  | Text Field      |
| `BillsTable`     | [<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/BillsTable.dart at master · misdwss/punjab-mgramseva](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/components/Dashboard/BillsTable.dart)                                                                                                                                                 | Table           |
| `LabelText`      | [<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/LabelText.dart at master · misdwss/punjab-mgramseva](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/LabelText.dart)                                                                                                                                                                | Title           |
| `SubLabelText`   | [<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/SubLabel.dart at master · misdwss/punjab-mgramseva](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/widgets/SubLabel.dart)                                                                                                                                                                  | Subtitle        |

## **Role Access Mapping**

```
case Routes.HOUSEHOLD:
    return ['COLLECTION_OPERATOR', 'SUPERUSER'];
```

## **File Path**

**Model** → [<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/water\_connection.dart at master · misdwss/punjab-mgramseva](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/model/connection/water\_connection.dart) , [<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/water\_connections.dart at master · misdwss/punjab-mgramseva](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/model/connection/water\_connections.dart)

**View** → [https://github.com/misdwss/punjab-mgramseva/tree/master/frontend/mgramseva/lib/screeens/HouseholdRegister](https://github.com/misdwss/punjab-mgramseva/tree/master/frontend/mgramseva/lib/screeens/HouseholdRegister)

**Controller** -> [https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/providers/household\_register\_provider.dart](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/providers/household\_register\_provider.dart) , [https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/repository/search\_connection\_repo.dart](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/repository/search\_connection\_repo.dart)

