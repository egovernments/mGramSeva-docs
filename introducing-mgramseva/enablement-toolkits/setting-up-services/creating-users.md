---
description: >-
  This doc provides the steps to create and add users on mgramseva platform
  post-installation.
---

# Creating Users

## **Overview**

Follow the steps provided on this page to create and add users on the mGramSeva platform once the installation is complete.

## **Pre-requisites**

Ensure the Postman utility is installed to run the following scripts. If not, [Install Postman](https://www.postman.com/downloads/canary/) on the local machine.

## Create Users - Steps

There are two methods to create users - either through **API or** through **port-forwarding**. To create users through port-forwarding refer [here](https://core.digit.org/guides/data-setup-guide/user-module).&#x20;

Follow the steps given below to create different types of users through the API.

There are primarily three different types of users as listed below:

* Super User
* Anonymous User
* System User

**Super User** - A superuser is a privileged user account with elevated access rights in a computer system or application. It is typically reserved for administrators or trusted personnel and grants them full control and unrestricted access to all system resources. Superusers are necessary to manage and maintain the system, perform critical tasks, and troubleshoot issues efficiently.

A Superuser is created using the createnovaildate API. Below is the curl given for creating a superuser.&#x20;

Steps to follow:

1. Import the curl given below in Postman.
2. Refresh the authorisation token.
3. Provide User data as per requirements. **This API will create a Super User in production.** To add users in any other environment change the URL.

{% code lineNumbers="true" %}
```
curl --location 'https://mgramseva-dwss.punjab.gov.in/user/users/_createnovalidate' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJQQVlIQWZ1YXpiRFpadlVGdEJSdmFQOWxYaHROXzBUS2FzdUpxZWl3bW04In0.eyJleHAiOjE2NDA0MTM1MjMsImlhdCI6MTYzNzgyMTUyMywianRpIjoiZTZiNmQyNmQtY2EwYS00MDZmLTgxZGYtYTNiOTE0NGEzYTQ3IiwiaXNzIjoiaHR0cHM6Ly9pZml4LXVhdC5wc2Vncy5pbi9hdXRoL3JlYWxtcy9pZml4IiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImJhMDE1OGFiLWZlYTMtNDc5NC04ZDE3LTRiYjc4MjFhZmM2NyIsInR5cCI6IkJlYXJlciIsImF6cCI6ImlmaXgtdWF0IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZmlzY2FsLWV2ZW50LXByb2R1Y2VyIiwiZGVmYXVsdC1yb2xlcy1pZml4Il19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJlbWFpbCBwcm9maWxlIiwiY2xpZW50SG9zdCI6IjE5Mi4xNzIuMzIuODYiLCJjbGllbnRJZCI6ImlmaXgtdWF0IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJ0ZW5hbnRJZCI6InBiIiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LWlmaXgtdWF0IiwiY2xpZW50QWRkcmVzcyI6IjE5Mi4xNzIuMzIuODYifQ.Wemcw5vLajX77GnHJmLq3-NhoEaBcySUyNQCpzfglBojTfF9-7xTk7ripf-VxlR3H5AsULIOsw1vRjTW255_3v-MwlYgRML4YE-d-Bt54v1SVnZ77NQsGRmmZ2UQ4wTwIhYQi2jaqzfTeAdU0fJAQTqo7POpTUcChTz_L6O7MQbVVpDJ3BRoWa5XX-BE6MYqZR1tBrLimvJEUWneohUEpPNncszmUAKEZkhEaiUhh8AzSJA3KtP18JOFC8KOCi7ErL-Vf-bJ928tpsNOMmFM2Syjxnqwu2rHE1ZPLdPUxGt6PGI9oJR7PEShakne0p9Fx-PLP8NxCPFCErq87U6zag' \
--data-raw '{
    "RequestInfo": {
        "api_id": "1",
        "ver": "1",
        "ts": null,
        "action": "create",
        "did": "",
        "key": "",
        "msg_id": "",
        "requester_id": "",
        "authToken": "7d2b5b4f-6053-4633-941c-d30d67bc52b8",
        "token_type": "bearer"
    },
    "User": {
        "userName": "9399998206",                
        "name": "Test",
        "gender": "male",
        "mobileNumber": "9399998206",
        "active": true,
        "type": "EMPLOYEE",
        "tenantId": "pb",
        "password": "eGov@123",
        "roles": [
            {
                "name": "Super User",
                "code": "SUPERUSER",
                "tenantId": "pb"
            }
        ]
    }
}'
```
{% endcode %}

The parameters - userName , name , gender, mobileNumber , tenantId , and password can be changed as per requirements.

**Anonymous User** -An anonymous user is a generic or unauthenticated user account that does not require login credentials to access certain parts of a system or website. These accounts are essential for providing basic access to public information or services without requiring user registration. They are commonly used to ensure accessibility for a wide audience and encourage user interaction while preserving user privacy. These are used when the system is accessing non-authentication links such as bills and payment receipts.

Creating an anonymous user is the same as creating a superuser. The only difference is to change the name and code in roles. **The API below is used to create an Anonymous User in production.**

{% code lineNumbers="true" %}
```
curl --location 'https://mgramseva-dwss.punjab.gov.in/user/users/_createnovalidate' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJQQVlIQWZ1YXpiRFpadlVGdEJSdmFQOWxYaHROXzBUS2FzdUpxZWl3bW04In0.eyJleHAiOjE2NDA0MTM1MjMsImlhdCI6MTYzNzgyMTUyMywianRpIjoiZTZiNmQyNmQtY2EwYS00MDZmLTgxZGYtYTNiOTE0NGEzYTQ3IiwiaXNzIjoiaHR0cHM6Ly9pZml4LXVhdC5wc2Vncy5pbi9hdXRoL3JlYWxtcy9pZml4IiwiYXVkIjoiYWNjb3VudCIsInN1YiI6ImJhMDE1OGFiLWZlYTMtNDc5NC04ZDE3LTRiYjc4MjFhZmM2NyIsInR5cCI6IkJlYXJlciIsImF6cCI6ImlmaXgtdWF0IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvZmZsaW5lX2FjY2VzcyIsInVtYV9hdXRob3JpemF0aW9uIiwiZmlzY2FsLWV2ZW50LXByb2R1Y2VyIiwiZGVmYXVsdC1yb2xlcy1pZml4Il19LCJyZXNvdXJjZV9hY2Nlc3MiOnsiYWNjb3VudCI6eyJyb2xlcyI6WyJtYW5hZ2UtYWNjb3VudCIsIm1hbmFnZS1hY2NvdW50LWxpbmtzIiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJlbWFpbCBwcm9maWxlIiwiY2xpZW50SG9zdCI6IjE5Mi4xNzIuMzIuODYiLCJjbGllbnRJZCI6ImlmaXgtdWF0IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJ0ZW5hbnRJZCI6InBiIiwicHJlZmVycmVkX3VzZXJuYW1lIjoic2VydmljZS1hY2NvdW50LWlmaXgtdWF0IiwiY2xpZW50QWRkcmVzcyI6IjE5Mi4xNzIuMzIuODYifQ.Wemcw5vLajX77GnHJmLq3-NhoEaBcySUyNQCpzfglBojTfF9-7xTk7ripf-VxlR3H5AsULIOsw1vRjTW255_3v-MwlYgRML4YE-d-Bt54v1SVnZ77NQsGRmmZ2UQ4wTwIhYQi2jaqzfTeAdU0fJAQTqo7POpTUcChTz_L6O7MQbVVpDJ3BRoWa5XX-BE6MYqZR1tBrLimvJEUWneohUEpPNncszmUAKEZkhEaiUhh8AzSJA3KtP18JOFC8KOCi7ErL-Vf-bJ928tpsNOMmFM2Syjxnqwu2rHE1ZPLdPUxGt6PGI9oJR7PEShakne0p9Fx-PLP8NxCPFCErq87U6zag' \
--data-raw '{
    "RequestInfo": {
        "api_id": "1",
        "ver": "1",
        "ts": null,
        "action": "create",
        "did": "",
        "key": "",
        "msg_id": "",
        "requester_id": "",
        "authToken": "7d2b5b4f-6053-4633-941c-d30d67bc52b8",
        "token_type": "bearer"
    },
    "User": {
        "userName": "9399998206",
        "name": "Test",
        "gender": "male",
        "mobileNumber": "9399998206",
        "active": true,
        "type": "EMPLOYEE",
        "tenantId": "pb",
        "password": "eGov@123",
        "roles": [
            {
                "name": "anonymous",
                "code": "ANONYMOUS",
                "tenantId": "pb"
            }
        ]
    }
}'
```
{% endcode %}

**System User** - Creating a system user is the same as creating a superuser and anonymous user. The only difference is to change the name and code in roles.

{% hint style="info" %}
While creating any user make sure your roles are present in [ACCESSCONTROL-ROLES](https://github.com/misdwss/mdms-mgramseva/tree/master/data/pb/ACCESSCONTROL-ROLES).

Here, 'pb' is used as tenantId since we are creating users at the state-level.
{% endhint %}

