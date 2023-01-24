# Forgot Password

## Overview

Users are redirected to this screen once they click on the Forgot Password link on the home screen.

![](<../../../../.gitbook/assets/image (62).png>)

## **OTP Request**

This feature allows users to request OTP by entering a valid (registered) mobile number.

Follow the steps below to set a new password -

* Click on the Forgot Password link visible on the login screen
* Enter the registered mobile number

The remaining steps are explained in the [Reset Password ](forgot-password.md#reset-password)section.

### **Files Path**

Primary Files[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/ForgotPassword.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/ForgotPassword/ForgotPassword.dart)

### **Field Validation**

| **Fields**     | **Validation** |
| -------------- | -------------- |
| Phone Number\* | `r'^[0-9]+$'`  |

### **API Details**

| End Point           | Request Method | Request Info                                                                                                         |
| ------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------- |
| `user-otp/v1/_send` | `POST`         | <p>"otp": {<br>"mobileNumber": {},<br>"tenantId": {},<br>"type": "passwordreset",<br>"userType": "Employee"<br>}</p> |

#### **Stack**

2 → Language Selection Screen. + Login Screen + ForgotPassword

Pop → Login Screen Screen

&#x20;Widgets utilised from Library

| Widgets          | File Path                                                                                                                                                                                                                                                                      | Description |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| `BuildTextField` | ​[​<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/TextFieldBuilder.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart)​ | Text Field  |
| `Button`         | ​[​<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/Button.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/Button.dart)​                     | Button      |

## Reset Password

Users are redirected to this screen once they click on the Continue button on Forgot Password screen.

**Link -** → {base url}/mgramseva/selectLanguage/login/forgotPassword/resetPassword &#x20;

![](<../../../../.gitbook/assets/image (44).png>)

### **User Interaction On Screen**

* Enter the OTP sent on the user’s 10-digit mobile number.
* Set the new password for logging into the application.
* Click on Change Password to apply new password credentials for the user.

### **Password Hint Card**

This feature helps to provide the users with a clear indication of what the password should contain. Acceptable passwords must contain -

* Minimum 6 digits
* At least one special character ( !#$%^&...)
* At least one letter
* At least one number

### **Files Path**

Primary Files[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/Resetpassword.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/ResetPassword/Resetpassword.dart)

### **Field Validations**

| Fields                 | Validations                                                |
| ---------------------- | ---------------------------------------------------------- |
| Enter the OTP sent \*  | `r'^[0-9]+$'` , 6 digit                                    |
| Enter a New Password\* | `r'^(?=.*?[A-Za-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,}$'` |
| Confirm New Password   | Match with New Password                                    |

### **API Details**

| End Point                       | Request Method | Request Info                                                                                                 |
| ------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------ |
| `user/password/nologin/_update` | `POST`         | <p>"otpReference": {},<br>"userName": {},<br>"newPassword": {},<br>"tenantId": {},<br>"type": “Employee”</p> |

#### **Stack**

1 → Language Selection Screen. + Login Screen + Forgot Password + Reset Password.

Pop → Forgot Password Screen.

Widgets utilised from Library

| Widgets           | File Path                                                                                                                                                                                                                                | Description        |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| `BuildTextField`  | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart) | Text Field         |
| `BottomButtonBar` | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/BottonButtonBar.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/BottonButtonBar.dart)   | Button             |
| `PasswordHint`    | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/PasswordHint.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/PasswordHint.dart)         | Password Hint Card |

