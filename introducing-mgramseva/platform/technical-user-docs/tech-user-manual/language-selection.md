# Language Selection

## Overview <a href="#link" id="link"></a>

Users land on the Language Selection screen.

Link → {base url}/mgramseva/selectLanguage

![App - initial screen](https://238770250-files.gitbook.io/\~/files/v0/b/gitbook-legacy-files/o/assets%2F-Mfb8ehcimjt6ER7QOME%2F-MkMbL3y8YcH5PxpU1GS%2F-MkMeKA4SjNd5S-OpRgR%2Fimage.png?alt=media\&token=3b886a41-753d-4592-8379-5aaed539ed53)

## User Interaction On Screen <a href="#user-interaction-on-screen" id="user-interaction-on-screen"></a>

* Users can switch to different languages that the application supports.
* Click on [Continue](login.md) to navigate to the next screen.

## File Path  <a href="#data-storage" id="data-storage"></a>

Primary files:&#x20;

{% embed url="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/SelectLanguage/languageSelection.dart" %}

Secondary files:&#x20;

{% embed url="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/SelectLanguage/DesktopView.dart" %}

{% embed url="https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/SelectLanguage/MobileView.dart" %}

## Data Storage

LocalStorage

| Key                         | Stored Data                             |
| --------------------------- | --------------------------------------- |
| `states_key`                | State Information for From MDMS Service |
| ex :`pn_IN`,`en_IN`,`hi_IN` | Localization codes                      |

## **API Details**

| API EndPoint                                                         | Input Params (Modules)                                   | Description                                                                                                                            |
| -------------------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `egov-mdms-service/v1/_search`                                       | `common-masters tenant`                                  | To fetch details              State info                        Logo background          Image                     Languages supported |
| `localization/messages/v1/_search?module`={}`locale`={}`tenantId`={} | ALL the necessary Modules, with locale key and tenant Id | To Load the Localized data                                                                                                             |

### Stack

0 → Language selection screen

Pop → Application closes

Widgets utilized from library

| Widgets Library |
| --------------- |
| Button Bar      |

