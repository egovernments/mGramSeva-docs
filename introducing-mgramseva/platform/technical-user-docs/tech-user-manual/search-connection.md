# Search Connection

## **Overview**

Users are redirected to this screen once they click on the Collect Payment card or the Update Consumer Details card or the Download Bills and Receipts card on the home screen. ​

**Link**&#x20;

→ {base url}/mgramseva/home/householdSearch?Mode=collect

&#x20;→ {base url}/mgramseva/home/consumersearchupdate?Mode=update

&#x20;→ {base url}/mgramseva/home/householdReceiptsSearch?Mode=receipts

![](<../../../../.gitbook/assets/image (48).png>)

## **User Interaction On Screen**

* Users can search the consumer/connection with their Mobile Number / Name / Old Connection ID / New Connection ID ( `Search with any one of these`)
* Click on Search to get the household details of the Consumer/Connection.

## **Files Path**

Primary Files:[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/SearchConnection.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/ConnectionResults/SearchConnection.dart)

## Field Validations

| Fields               | Validations                |
| -------------------- | -------------------------- |
| Owner Mobile Number  | `r'^(?:[+0]9)?[0-9]{10}$'` |
| Name of the Consumer | `r'^[A-Za-z ]'`            |
| Old Connection ID    | `No Validation`            |
| New Connection ID    | `No Validation`            |

## **API Details**

<table><thead><tr><th>End Point</th><th width="170">Request Method</th><th>Request Info</th></tr></thead><tbody><tr><td><code>/ws-services/wc/_search</code></td><td><code>POST</code></td><td><p>tenantId: {}</p><p>oldConnectionNumber: {}</p><p>name: {}</p><p>connectionNumber: {}</p><p>mobileNumber: {}</p></td></tr></tbody></table>

### Stack

1 → Home Screen. + Search Connection Screen

Pop → Home Screen

Widgets utilised from Library

| Widgets           | File Path                                                                                                                                                                                                                                                                   | Description |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `BuildTextField`  | [<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/TextFieldBuilder.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart) | Text Field  |
| `BottomButtonBar` | [<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/BottonButtonBar.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/BottonButtonBar.dart)   | Button      |

