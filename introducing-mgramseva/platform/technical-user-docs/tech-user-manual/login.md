# Login

## Overview <a href="#link" id="link"></a>

Users are redirected to this screen once they select the preferred language in the previous screen.

Link → {base url}/mgramseva/selectLanguage/login

![](https://238770250-files.gitbook.io/\~/files/v0/b/gitbook-legacy-files/o/assets%2F-Mfb8ehcimjt6ER7QOME%2F-MkMeYDtmbSGq9gFtUsn%2F-MkMeryxdSejVdCjRrGR%2Fimage.png?alt=media\&token=4b8bfe7a-be6b-4ced-bb1c-c5691816a7a4)

### User Interaction On Screen <a href="#user-interaction-on-screen" id="user-interaction-on-screen"></a>

* Users enter the registered Phone Number and Password.
* Click on Continue.
* First-time login users navigate to Reset Password Page.

**Log in with the default password**

YES → [Reset Password/ Update Password Screen](https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/1922662535)​

NO → [Home Screen](https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/1923416085)​

## File Path <a href="#files-path" id="files-path"></a>

Primary Files:

[<img src="https://github.com/fluidicon.png" alt="" data-size="line">](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/Login/Login.dart)[punjab-mgramseva/Login.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/Login/Login.dart)​

## Field Validations

| Fields         | Validations                                                |
| -------------- | ---------------------------------------------------------- |
| Phone Number\* | `r'^[0-9]+$'`                                              |
| Password\*     | `r'^(?=.*?[A-Za-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,}$'` |

### API Details <a href="#field-validations" id="field-validations"></a>

| End Point           | Request Method | Request Info                                                                                         |
| ------------------- | -------------- | ---------------------------------------------------------------------------------------------------- |
| `/user/oauth/token` | `POST`         | username: {} password:{}        scope: read grant\_type: password tenantId: {}    userType: EMPLOYEE |

**Stack**

1 → Language selection screen. + Login screen.

Pop → Language selection screen.

Widgets utilized from library

| Widgets          | File Path                                                                                                                                                                                                                                | Description |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `BuildTextField` | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart) | Text Field  |
| `Button`         | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/Button.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/Button.dart)                     | Button      |

****
