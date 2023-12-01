# Change Password

## Overview

Users are redirected to this screen once they click on the Change Password option in the sidebar app drawer.

![](<../../../../.gitbook/assets/image (75).png>)

**Link** → {base url}/mgramseva/home/changepassword

## **User Interaction On Screen**

* Enter the Current Password
* Enter and Confirm a New Password to set the login credentials for the next time login
* Click the Change Password Button. The user login password is set to the new password.

## **Password Hint Card**

This feature helps match the user password to the requirements and checks if the password contains

* Minimum 6 digits
* At least one special character ( !#$%^&...)
* At least one letter
* At least one number

## **File Path**

Primary Files:[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/Changepassword.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/ChangePassword/Changepassword.dart)

## **Field Validations**

| Fields                 | Validation                                                 |
| ---------------------- | ---------------------------------------------------------- |
| Current Password\*     | No Validation                                              |
| Set a New Password\*   | `r'^(?=.*?[A-Za-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,}$'` |
| Confirm New Password\* | Match with New Password                                    |

## **API Details**

<table><thead><tr><th width="175.33333333333331">End Point</th><th>Request Method</th><th>Request Info</th></tr></thead><tbody><tr><td><code>user/password/_update</code></td><td><code>POST</code></td><td>"userName": {},<br>"existingPassword": {},<br>"newPassword": {},<br>"tenantId": {},<br>"type": {}</td></tr></tbody></table>

**Stack**

1 → Home Screen. + Change Password Screen

Pop → Home Screen

Widgets utilised from Library

| Widgets          | File Path                                                                                                                                                                                                                                | Description |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `BuildTextField` | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart) | Text Field  |
| `Button`         | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/Button.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/Button.dart)                     | Button      |



