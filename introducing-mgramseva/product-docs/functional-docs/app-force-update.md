# App Force Update

## Overview <a href="#overview" id="overview"></a>

Show Update App PopUp to end users in case there is a new release in the Google play store or IOS App Store.

## MDMS Configuration <a href="#mdms-configuration" id="mdms-configuration"></a>

Add the file (link below) in the common-masters MDMS -

[<img src="https://github.com/fluidicon.png" alt="" data-size="line">mdms-mgramseva/AppVersion.json at UAT · misdwss/mdms-mgramseva](https://github.com/misdwss/mdms-mgramseva/blob/UAT/data/pb/common-masters/AppVersion.json)

Whenever a new release is deployed to the play store or app store, update the version in the above-mentioned file.

{% hint style="info" %}
**Note: The version deployed in the Play Store and App Store should match the version in** [<img src="https://github.com/fluidicon.png" alt="" data-size="line">mdms-mgramseva/AppVersion.json at UAT · misdwss/mdms-mgramseva](https://github.com/misdwss/mdms-mgramseva/blob/UAT/data/pb/common-masters/AppVersion.json)
{% endhint %}

```
{  "tenantId": "pb", 
 "moduleName": "common-masters",  
"AppVersion": [    
{      
"latestAppVersion": "1.2.0",      
"packageName": "com.dwss.mgramseva"    
} ]  
}{  "tenantId": "pb", 
 "moduleName": "common-masters",  
"AppVersion": [    
{      
"latestAppVersion": "1.2.0",      
"packageName": "com.dwss.mgramseva"    
} ]  
}
```

**Logic implemented for version check:**&#x20;

```
commonProvider.getAppVersionDetails();
```

MDMS call is made every time a user opens the app.

In the landing page widget, afterViewBuild() returns a pop-up, validating if the package version matches the version in MDMS.

```
await commonProvider.getAppVersionDetails();
CommonMethods()
    .checkVersion(context, commonProvider.appVersion!.latestAppVersion);
```

```
CommonMethods()
    .checkVersion(context, commonProvider.appVersion!.latestAppVersion);
```

### Primary Files <a href="#primary-files" id="primary-files"></a>

[<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/main.dart at master · misdwss/punjab-mgramseva](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/main.dart)

[<img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/common\_methods.dart at master · misdwss/punjab-mgramseva](https://github.com/misdwss/punjab-mgramseva/blob/master/frontend/mgramseva/lib/utils/common\_methods.dart)
