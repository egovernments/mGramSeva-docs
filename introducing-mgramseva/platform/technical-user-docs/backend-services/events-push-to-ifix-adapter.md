# Events Push To IFIX Adapter

## Overview <a href="#overview" id="overview"></a>

Events push is used to manually push data from the mGramSeva Adapter to the iFIX Adapter. Make sure the existing events are cleared or deleted to ensure reliable data transfer. Refer to the documentation here to find details on how to clean up the event data - [IFIX-Core Data Clean-Up v2.0](https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/2075918384). Post events clean up the system loads the project code for all the tenants. Then it pushes the data to the iFIX adapter.

## **Pre-requisites**

* Access to Kubectl of the environment targetted
* Postman scripts

The Postman script fetches the data from the existing mGramSeva database and passes it to the mGramSeva adapter, from where it is pushed to the iFIX adapter.

### Payments Curl

Pass the offset and limits based on the total transactions present in the database.

{% code lineNumbers="true" %}
```
curl --location --request POST 'http://localhost:8084/mgramseva-ifix-adapter/mGramsevaAdopter/v1/_paymentdatatransfer?tenantId=pb.massewal&businessService=WS&limit=1000&offset=0' 
--header 'Content-Type: application/json' 
--data-raw '{
"RequestInfo": {
"apiId": "Rainmaker",
"ver": ".01",
"ts": null,
"action": "",
"did": "1",
"key": "",
"msgId": "20170310130900|en_IN",
"authToken": null,
"correlationId": null,
"userInfo": {
"id": 1238,
"userName": "230566|6nazOXejetsSwLcRS5aclEJD/4e7SzmimN4=",
"name": "230566|kBzPQAXbCiQzR3NUY/cLPTzdnmw63ho=",
"type": "SYSTEM",
"mobileNumber": "230566|6nazOXejetsSwLcRS5aclEJD/4e7SzmimN4=",
"emailId": null,
"roles": [
{
"id": null,
"name": "Employee",
"code": "EMPLOYEE",
"tenantId": "pb"
},
{
"id": null,
"name": "System user",
"code": "SYSTEM",
"tenantId": "pb"
}
],
"tenantId": "pb.lodhipur",
"uuid": "47ff55dc-c9d0-4f86-8f82-b4d7a24ba59e"
}
}
}'
```
{% endcode %}

Here, TenantId is mandatory. Limit and offset can vary based on the requirement. Business service is not required.

This fetches all payment records irrespective of tenant based on the limit and offset. The data is passed to the IFIX adapter one after the other.

### Demand / Bill Curl

{% code lineNumbers="true" %}
```
curl --location --request POST 'http://localhost:8084/mgramseva-ifix-adapter/mGramsevaAdopter/v1/_legacydatatransfer?businessService=WS' \
--header 'Content-Type: application/json' \
--data-raw '{
"RequestInfo": {
"apiId": "Rainmaker",
"ver": ".01",
"ts": null,
"action": "",
"did": "1",
"key": "",
"msgId": "20170310130900|en_IN",
"authToken": null,
"correlationId": null,
"userInfo": {
"id": 1238,
"userName": "230566|6nazOXejetsSwLcRS5aclEJD/4e7SzmimN4=",
"name": "230566|kBzPQAXbCiQzR3NUY/cLPTzdnmw63ho=",
"type": "SYSTEM",
"mobileNumber": "230566|6nazOXejetsSwLcRS5aclEJD/4e7SzmimN4=",
"emailId": null,
"roles": [
{
"id": null,
"name": "Employee",
"code": "EMPLOYEE",
"tenantId": "pb"
},
{
"id": null,
"name": "System user",
"code": "SYSTEM",
"tenantId": "pb"
}
],
"uuid": "47ff55dc-c9d0-4f86-8f82-b4d7a24ba59e"
}
},
"tenantIds": ["pb.lodhipur","pb.baruwal"]
}'
```
{% endcode %}

The above curl fetches the demands based on the tenant ID and business service passed.\
Business service can be ‘WS' or ‘EXPENSE.SALARY’ or 'EXPENSE.MISC’ or 'EXPENSE.OM’ etc.\
For WS it is saved as demand and for EXPENSE it is saved as bill.
