# Edit Profile

## **Overview**

Users are navigated to the Edit Profile screen once they click on the option on the sidebar app drawer.

**Link -** → {base url}/mgramseva/home/editProfile

![](<../../../../.gitbook/assets/image (79).png>)

## **User Interaction On Screen**

* User can change their profile name, gender and email on this screen
* Click on the Save button triggers a Details Saved Successfully message on the screen and saves the changes to the profile.

## **File Path**

Primary Files:[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/EditProfile.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/Profile/EditProfile.dart)

## **Field Validations**

| Fields   | Validations                                                                                                                                                          |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name     | `r'^[a-zA-Z ]+$'`                                                                                                                                                    |
| Email ID | `r'^$\|^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)\|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])\|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'` |

## **API Details**

| End Point               | Request Method | Request Info                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `/user/profile/_update` | `POST`         | <p>"user": {<br>"id": {},<br>"userName": {},<br>"salutation": null,<br>"name": {},<br>"gender": {},<br>"mobileNumber": "9191919146",<br>"emailId": {},<br>"altContactNumber": null,<br>"pan": null,<br>"aadhaarNumber": null,<br>"permanentAddress": null,<br>"permanentCity": null,<br>"permanentPinCode": null,<br>"correspondenceAddress": null,<br>"correspondenceCity": null,<br>"correspondencePinCode": null,<br>"active": true,<br>"locale": null,<br>"type": "EMPLOYEE",<br>"accountLocked": false,<br>"accountLockedDate": 0,<br>"fatherOrHusbandName": null,<br>"relationship": null,<br>"signature": null,<br>"bloodGroup": null,<br>"photo": null,<br>"identificationMark": null,<br>"createdBy": {},<br>"lastModifiedBy": {},<br>"tenantId": {},<br>"roles": [ {} ],<br>}</p> |

**Stack**

1 → Home Screen. + Edit Profile Screen

Pop → Home Screen

Widgets utilised from Library

| Widgets            | File Path                                                                                                                                                                                                                                              | Description               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| `BuildTextField`   | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/TextFieldBuilder.dart)               | Text Field                |
| `BottomButtonBar`  | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/BottonButtonBar.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/BottonButtonBar.dart)                 | Button                    |
| `RadioButtonField` | [https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/RadioButtonFieldBuilder.dart](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/widgets/RadioButtonFieldBuilder.dart) | Radio Buttons for options |

