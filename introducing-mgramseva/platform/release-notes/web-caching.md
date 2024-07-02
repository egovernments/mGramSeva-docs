---
description: Steps to remove the cache data whenever a new build is deployed
---

# Web Caching

## **Package Used**

```
package_info_plus: ^1.3.0
```

The build number of the application is compared every time we hit the URL. If the build number is not present in the local storage or the build number does not match the existing build number then the local storage cache is deleted.

## Build number

```
1.2.0+17 
```

Here, 17 is the build number.

{% hint style="info" %}
**Note: Add all localizations to the respective environment, before deploying the build to any environment.**
{% endhint %}

If we add new localizations after deploying the build, we need to increment the build version and deploy a new build to reflect those localizations. The previous web cache validates the build number check and does not delete the localization messages stored in the local storage.

