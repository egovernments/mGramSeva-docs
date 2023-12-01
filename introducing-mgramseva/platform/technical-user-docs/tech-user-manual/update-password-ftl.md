# Update Password FTL

## **Overview**

Users are redirected to the Update Password screen once they log in successfully the first time.

**Link:** → {base url}/mgramseva/selectLanguage/login/`updatepassword`

![](<../../../../.gitbook/assets/image (143).png>)

## **User Interaction On Screen**

* Enter the OTP sent on the user’s 10-digit mobile number.
* Set the new password for logging into the application.
* Click on Change Password to apply new password credentials for the user.
* Users can see the allocated Gram Panchayat name and code in the table.

## **Password Hint Card**

This feature helps match the user’s password and check if the password contains

* Minimum 6 digits
* At least one special character ( !#$%^&...)
* At least one letter
* At least one number

## **Files Path**

Primary Files

{% embed url="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/ResetPassword/Updatepassword.dart" %}

## **Logic For Tenant Filtration**

Fetch the tenants from MDMS, based on the user roles in the user request filtering the tenants by comparing tenant Id.

## **Field Validations**

| Fields                 | Validations                                                |
| ---------------------- | ---------------------------------------------------------- |
| Enter the OTP sent \*  | `r'^[0-9]+$'` , 6 digit                                    |
| Enter a New Password\* | `r'^(?=.*?[A-Za-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,}$'` |
| Confirm New Password   | Match with New Password                                    |

## API Details

| End Point                       | Request Method | Request Info                                                                                                                                                               |
| ------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `user/password/nologin/_update` | `POST`         | <p>"otpReference": {},<br>"userName": {},<br>"newPassword": {},<br>"tenantId": {},<br>"type": “Employee”</p>                                                               |
| `egov-mdms-service/v1/_search`  | POST           | <p>"MdmsCriteria": {<br>"tenantId": tenantId,<br>"moduleDetails": [<br>{<br>"moduleName": "tenant",<br>"masterDetails": [<br>{"name": "tenants"}<br>],<br>},<br>]<br>}</p> |

### **Stack**

1 → Language selection screen + Login screen + Update password + Update password success

Pop → Login

Widgets utilized from library

| Widgets           | File Path                                                                                                                                                                                                                                | Description        |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BuildTextField`  | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart) | Text Field         |
| `BottomButtonBar` | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/BottonButtonBar.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/BottonButtonBar.dart)   | Button             |
| `PasswordHint`    | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/PasswordHint.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/PasswordHint.dart)         | Password Hint Card |

## **Files Path**

View →&#x20;

{% embed url="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/ResetPassword/Updatepassword.dart" %}

Controller →

{% embed url="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/repository/tendants_repo.dart" %}



