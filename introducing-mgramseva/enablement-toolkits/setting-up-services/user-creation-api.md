# User creation API

The [CreateNovaildate](https://web.postman.co/workspace/My-Workspace\~9f040a08-ea42-45f5-8e7b-4e79ceae42c7/request/24183907-95666725-c68a-42fb-a891-678f6d4eb01b) API allows users to create a new user with specified details, including username, name, gender, mobile number, activation status, user type, tenant ID, and password. Additionally, users can be assigned specific roles based on their responsibilities.

### Request Parameters

1. **username (string):** User's unique username.
2. **name (string):** Full name of the user.
3. **gender (string):** Gender of the user.
4. **mobileno (string):** User's mobile number.
5. **active (boolean):** User's account status (true for active, false for inactive).
6. **type (string):** It will be EMPLOYEE only.
7. **tenantid (string):** User's tenant ID.
8. **password (string):** User's password.
9. **Roles**

Roles determine the permissions and responsibilities assigned to a user. The available roles are as follows:

#### Roles for Sarpanch

* COLLECTION\_OPERATOR
* EXPENSE\_PROCESSING
* BULK\_DEMAND\_PROCESSING
* DASHBOARD\_VIEWER
* GP\_ADMIN

#### Roles for Secretary

* EXPENSE\_PROCESSING
* BULK\_DEMAND\_PROCESSING
* DASHBOARD\_VIEWER
* GP\_ADMIN
* COLLECTION\_OPERATOR

#### Roles for Revenue Collector

* COLLECTION\_OPERATOR
* DASHBOARD\_VIEWER

#### Roles for Division User

* HRMS\_ADMIN
* DIVISION\_ADMIN

#### Roles for State User

* HRMS\_ADMIN
* STATE\_ADMIN

\
To assign roles to a user, include the desired roles in the `roles` section of the request.

PROFILE\_UPDATE role will be included for every user.

This documentation provides a comprehensive guide on using the CreateNovaildate API to create users with specific roles based on their responsibilities within the system. Adjust the parameters and roles as needed for your specific requirements.
