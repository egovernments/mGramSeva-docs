# Localisation Module

## Overview

Localization is the process of adapting a software application, website, or content to different languages and regions, making it accessible and user-friendly for diverse audiences. It involves translating text, adapting graphics, and configuring settings to suit the cultural and linguistic preferences of a specific locale.

### Search API For Localization In mGramSeva

To retrieve localization messages in mGramSeva, use the Search API given below. This API allows you to search for messages based on parameters like locale, tenantId, and apiId. Here is an example using cURL:

You can customize the parameters such as locale (en\_IN, hi\_IN, pn\_IN) and tenantId to search for messages in different languages and environments. Change the URL to search in any other environment. The current API is specific for UAT environment.

{% code lineNumbers="true" %}
```
curl --location 'https://mgramseva-uat.psegs.in/localization/messages/v1/_search?locale=en_IN&tenantId=pb' \
--header 'authority: mgramseva-dwss.punjab.gov.in' \
--header 'accept: */*' \
--header 'accept-language: en-GB,en;q=0.9' \
--header 'content-type: application/json; charset=utf-8' \
--header 'cookie: _ga=GA1.1.748766720.1676369982; _ga_DDHVQCKC6W=GS1.1.1676369981.1.0.1676369984.0.0.0' \
--header 'origin: https://mgramseva-dwss.punjab.gov.in' \
--header 'referer: https://mgramseva-dwss.punjab.gov.in/mgramseva/selectLanguage' \
--header 'sec-ch-ua: "Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"' \
--header 'sec-ch-ua-mobile: ?1' \
--header 'sec-ch-ua-platform: "Android"' \
--header 'sec-fetch-dest: empty' \
--header 'sec-fetch-mode: cors' \
--header 'sec-fetch-site: same-origin' \
--header 'user-agent: Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36' \
--data '{
    "apiId": "mgramseva",
    "ver": 1,
    "ts": "",
    "action": "_search",
    "did": 1,
    "key": "",
    "msgId": "20170310130900|en_IN",
    "authToken": "",
    "userInfo": null
}'
```
{% endcode %}

### Upsert API For Localization In mGramSeva

The Upsert API allows users to update or insert new localization messages into mGramSeva. This involves refreshing the authentication token and providing details like code, message, module, and locale. Here is an example using cURL:

In this example, you can customize the "code," "message," "module," and "locale" parameters to specify the localization details you want to upsert. Make sure to update the authentication token for security purposes.

{% code lineNumbers="true" %}
```
curl --location 'https://mgramseva-uat.psegs.in/localization/messages/v1/_upsert' \
--header 'Content-Type: application/json' \
--data '{
    "RequestInfo": {
        "apiId": "Mihy",
        "ver": "1.0",
        "ts": "",
        "action": "create",
        "did": "1",
        "key": "abcdkey",
        "msgId": "20170310130900",
        "requesterId": "",
        "authToken": "7d569ce1-4b5c-4f4c-be93-4af7265890f3"
    },
    "tenantId": "pb",
    "messages": [
         {
            "code": "CORE_DOWNLOAD",
            "message": "Download",
            "module": "mgramseva-common",
            "locale": "en_IN"
        }
    ]
}'
```
{% endcode %}

{% hint style="info" %}
Note: The provided APIs are for the UAT environment, and you may need to modify the URLs accordingly for other environments.
{% endhint %}

