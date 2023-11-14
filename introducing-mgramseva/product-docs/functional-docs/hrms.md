# HRMS

Backend Code Git Repo\
[<img src="https://github.githubassets.com/favicon.ico" alt="" data-size="line">https://github.com/egovernments/punjab-mgramseva/tree/master/business-services/egov-hrms](https://github.com/egovernments/punjab-mgramseva/tree/master/business-services/egov-hrms)

Connect to your GitHub account and navigate to the config /persister repo: [https://github.com/misdwss/config-mgramseva/blob/UAT/egov-persister/hrms-employee-persister.yml](https://github.com/misdwss/config-mgramseva/blob/UAT/egov-persister/hrms-employee-persister.yml)\
DevOps repo: [<img src="https://github.githubassets.com/favicon.ico" alt="" data-size="line">https://github.com/misdwss/iFix-DevOps/tree/mgramseva/deploy-as-code/helm/charts/business-services/egov-hrms](https://github.com/misdwss/iFix-DevOps/tree/mgramseva/deploy-as-code/helm/charts/business-services/egov-hrms)Connect your Github account

There is the concept of hierarchy in mGramSeva :\
1\. State-level user → one who can create a Division user\
2\. Div level user → one who can create the employees like Sarpanch for mgramseva\
\
List of changes done in the user service and HRMS service to adapt HRMS in mGramSeva:\
[<img src="https://github.com/fluidicon.png" alt="" data-size="line">Pfm 1419 user search by debasishchakraborty-egovt · Pull Request #610 · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/pull/610/files)

1. Modified the search API of user service to do role based search of users based on the tenants it is mapped to and show the list in all cities where it is mapped to.\
   State-level users can search for division users. Division users are created and mapped to pb as the base tenants and roles HRMS\_ADMIN, and DIV\_ADMIN to the concerned cities. Division users can search users based on roles like - SYSTEM,+GP\_ADMIN,+COLLECTION\_OPERATOR,+PROFILE\_UPDATE,+DASHBOAD\_VIEWER within the GPWSC it is currently logged into.
2. Modified the count API to search for users based on the role and the mapped tenant.
3. MDMS changes: [<img src="https://github.com/fluidicon.png" alt="" data-size="line">PFM-1419 : HRMS mdms Changes by debasishchakraborty-egovt · Pull Request #312 · misdwss/mdms-mgramseva](https://github.com/misdwss/mdms-mgramseva/pull/312/files)\
   [<img src="https://github.com/fluidicon.png" alt="" data-size="line">Update master-config.json by debasishchakraborty-egovt · Pull Request #314 · misdwss/mdms-mgramseva](https://github.com/misdwss/mdms-mgramseva/pull/314/files)

{% hint style="info" %}
**Note:** Division users are mapped to PB as BASE TENANT. GP\_ADMIN and other users are mapped to one city as BASE TENANT from where the user is created. \
BASE TENANT cannot be removed from the user.  To modify the Base tenant, deactivate that user and create a new user.\

{% endhint %}

### APIs

Count API\
1\. Count Normal Employee API

{% code lineNumbers="true" %}
```
curl --location 'http://localhost:8080/egov-hrms/employees/v1/_count?tenantId=pb.baruwal&_=1697534837504&roles=SYSTEM%2C%20GP_ADMIN%2C%20COLLECTION_OPERATOR%2C%20PROFILE_UPDATE%2C%20DASHBOAD_VIEWER&isStateLevelSearch=true' \
--header 'Accept: application/json, text/plain, */*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Connection: keep-alive' \
--header 'Content-Type: application/json;charset=UTF-8' \
--header 'Origin: http://localhost:3000' \
--header 'Referer: http://localhost:3000/mgramseva-web/employee' \
--header 'Sec-Fetch-Dest: empty' \
--header 'Sec-Fetch-Mode: cors' \
--header 'Sec-Fetch-Site: same-origin' \
--header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' \
--header 'sec-ch-ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "Windows"' \
--data '{
    "RequestInfo": {
        "apiId": "Rainmaker",
        "authToken": "28ee5e63-8150-48cf-a0b2-26212a450d18",
        "userInfo": {
            "id": 878469,
            "uuid": "b5bcbe8d-5410-4548-8b94-ee638d409f63",
            "userName": "9502410535",
            "name": "Rakesh",
            "mobileNumber": "9502410535",
            "emailId": null,
            "locale": null,
            "type": "EMPLOYEE",
            "roles": [
                {
                    "name": "HRMS_ADMIN",
                    "code": "HRMS_ADMIN",
                    "tenantId": "pb.baruwal"
                },
                {
                    "name": "DIVISION ADMIN",
                    "code": "DIV_ADMIN",
                    "tenantId": "pb.baruwal"
                },
                {
                    "name": "Employee",
                    "code": "EMPLOYEE",
                    "tenantId": "pb.baruwal"
                }
            ],
            "active": true,
            "tenantId": "pb.baruwal",
            "permanentCity": null
        },
        "msgId": "1697534837504|en_IN",
        "plainAccessRequest": {}
    }
}'


```
{% endcode %}

2. Count Division User

{% code lineNumbers="true" %}
```
curl --location 'http://localhost:8080/egov-hrms/employees/v1/_count?tenantId=pb&_=1697534837504&roles=DIV_ADMIN%2CHRMS_ADMIN&isStateLevelSearch=true' \
--header 'Accept: application/json, text/plain, */*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Connection: keep-alive' \
--header 'Content-Type: application/json;charset=UTF-8' \
--header 'Origin: http://localhost:3000' \
--header 'Referer: http://localhost:3000/mgramseva-web/employee' \
--header 'Sec-Fetch-Dest: empty' \
--header 'Sec-Fetch-Mode: cors' \
--header 'Sec-Fetch-Site: same-origin' \
--header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' \
--header 'sec-ch-ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "Windows"' \
--data '{
    "RequestInfo": {
        "apiId": "Rainmaker",
        "authToken": "28ee5e63-8150-48cf-a0b2-26212a450d18",
        "userInfo": {
            "id": 878469,
            "uuid": "b5bcbe8d-5410-4548-8b94-ee638d409f63",
            "userName": "9502410535",
            "name": "Rakesh",
            "mobileNumber": "9502410535",
            "emailId": null,
            "locale": null,
            "type": "EMPLOYEE",
            "roles": [
                {
                    "name": "HRMS_ADMIN",
                    "code": "HRMS_ADMIN",
                    "tenantId": "pb.baruwal"
                },
                {
                    "name": "DIVISION ADMIN",
                    "code": "DIV_ADMIN",
                    "tenantId": "pb.baruwal"
                },
                {
                    "name": "Employee",
                    "code": "EMPLOYEE",
                    "tenantId": "pb.baruwal"
                }
            ],
            "active": true,
            "tenantId": "pb.baruwal",
            "permanentCity": null
        },
        "msgId": "1697534837504|en_IN",
        "plainAccessRequest": {}
    }
}'
```
{% endcode %}

Search APIs

3. Search Normal Employee

{% code lineNumbers="true" %}
```
curl --location 'http://mgramseva-uat.psegs.in/egov-hrms/employees/_search?tenantId=pb.baruwal&isStateLevelSearch=false&limit=200&offset=0&sortOrder=ASC&roles=SYSTEM%2C%2BGP_ADMIN%2C%2BCOLLECTION_OPERATOR%2C%2BPROFILE_UPDATE%2C%2BDASHBOAD_VIEWER&_=1697180313780' \
--header 'Accept: application/json, text/plain, */*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Connection: keep-alive' \
--header 'Content-Type: application/json;charset=UTF-8' \
--header 'Origin: http://localhost:3000' \
--header 'Referer: http://localhost:3000/mgramseva-web/employee/hrms/inbox' \
--header 'Sec-Fetch-Dest: empty' \
--header 'Sec-Fetch-Mode: cors' \
--header 'Sec-Fetch-Site: same-origin' \
--header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' \
--header 'sec-ch-ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "Windows"' \
--data '{
    "RequestInfo": {
        "apiId": "Rainmaker",
        "authToken": "ab731e06-b758-47fb-8642-a598daf51d72",
        "userInfo": {
            "id": 4659,
            "uuid": "6736c66c-3091-45d4-9aa0-43dcffa914fc",
            "userName": "5000000001",
            "name": "DIVSION-ADMIN-TESTING",
            "mobileNumber": "5000000001",
            "emailId": null,
            "locale": null,
            "type": "EMPLOYEE",
            "roles": [
                {
                    "name": "HRMS_ADMIN",
                    "code": "HRMS_ADMIN",
                    "tenantId": "pb.lodhipur"
                },
                {
                    "name": "DIVISION ADMIN",
                    "code": "DIV_ADMIN",
                    "tenantId": "pb.lodhipur"
                }
            ],
            "active": true,
            "tenantId": "pb.massewal",
            "permanentCity": null
        },
        "msgId": "1697180313780|en_IN",
        "plainAccessRequest": {}
    }
}'



```
{% endcode %}

4. Search Division User

{% code lineNumbers="true" %}
```
curl --location 'http://mgramseva-uat.psegs.in/egov-hrms/employees/_search?tenantId=pb&isStateLevelSearch=true&limit=200&offset=0&sortOrder=ASC&roles=DIV_ADMIN%2CHRMS_ADMIN&_=1697180313780' \
--header 'Accept: application/json, text/plain, */*' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Connection: keep-alive' \
--header 'Content-Type: application/json;charset=UTF-8' \
--header 'Origin: http://localhost:3000' \
--header 'Referer: http://localhost:3000/mgramseva-web/employee/hrms/inbox' \
--header 'Sec-Fetch-Dest: empty' \
--header 'Sec-Fetch-Mode: cors' \
--header 'Sec-Fetch-Site: same-origin' \
--header 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' \
--header 'sec-ch-ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"' \
--header 'sec-ch-ua-mobile: ?0' \
--header 'sec-ch-ua-platform: "Windows"' \
--data '{
    "RequestInfo": {
        "apiId": "Rainmaker",
        "authToken": "ab731e06-b758-47fb-8642-a598daf51d72",
        "userInfo": {
            "id": 4659,
            "uuid": "6736c66c-3091-45d4-9aa0-43dcffa914fc",
            "userName": "5000000001",
            "name": "DIVSION-ADMIN-TESTING",
            "mobileNumber": "5000000001",
            "emailId": null,
            "locale": null,
            "type": "EMPLOYEE",
            "roles": [
                {
                    "name": "HRMS_ADMIN",
                    "code": "HRMS_ADMIN",
                    "tenantId": "pb.lodhipur"
                },
                {
                    "name": "DIVISION ADMIN",
                    "code": "DIV_ADMIN",
                    "tenantId": "pb.lodhipur"
                }
            ],
            "active": true,
            "tenantId": "pb.massewal",
            "permanentCity": null
        },
        "msgId": "1697180313780|en_IN",
        "plainAccessRequest": {}
    }
}'
```
{% endcode %}
