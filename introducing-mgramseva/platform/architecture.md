---
description: mGramSeva architecture details
---

# Architecture

## Service Architecture

mGramSeva is built on top of the [DIGIT ](https://docs.digit.org/)Platform. It consists of distinct layers listed below.​

**Back End**

* Core Services
  1. ​[User Services ](https://core.digit.org/platform/core-services/user-services)(egov-user)
  2. [​User OTP](https://core.digit.org/platform/core-services/user-otp-service) (user-otp)
  3. ​[Access Control](https://core.digit.org/platform/core-services/access-control-services) (access-control)
  4. ​[MDMS](https://core.digit.org/platform/core-services/mdms-master-data-management-service)
  5. [​ID Generation Service](https://core.digit.org/platform/core-services/id-generation-service) (id-gen)
  6. ​[Payment Gateway](https://core.digit.org/platform/core-services/payment-gateway-service) (pg-service)
  7. ​[Workflow Service](https://core.digit.org/platform/core-services/workflow-service) (wf-service)
  8. ​[Persister](https://core.digit.org/platform/core-services/persister-service)
  9. ​[Indexer](https://core.digit.org/platform/core-services/indexer-service)
  10. ​[Encryption Service](https://core.digit.org/platform/core-services/encryption-service) (data-encryption-service)
  11. ​[Localization Servic](https://core.digit.org/platform/core-services/localization-service)e (localization-service)
  12. ​[Boundary Servic](https://core.digit.org/platform/core-services/location-services#api-list)e (location-service)
  13. ​[URL Shortening Service](https://core.digit.org/platform/core-services/url-shortening-service) (url-shortening-service)
  14. ​[PDF Generation Service](https://core.digit.org/platform/core-services/pdf-generation-service) (pdf-generator)
  15. ​[SMS Notifications](https://core.digit.org/platform/core-services/sms-notification-service) (notification-sms)
  16. [Email Notifications](https://core.digit.org/platform/core-services/email-notification-service) (notification-email)
  17. ​[Filestore](https://core.digit.org/platform/core-services/filestore-service)
  18. ​[API Gateway](https://digit-discuss.atlassian.net/wiki/spaces/EPE/pages/36700192/API-Gateway)​
* Business Services
  1. ​[Billing Service​](configure-mgramseva/billing-service.md)
  2. ​[Collection service​](https://core.digit.org/platform/api-specifications/collection)
  3. ​[Apportioning Service​](configure-mgramseva/apportion-service.md)
  4. ​[Dashboard Ingest​](https://core.digit.org/platform/core-services/national-dashboard-ingest)
  5. ​[Dashboard Analytic](https://core.digit.org/focus-areas/analytics)s (DSS)
* Municipal Services
  1. ​[Property Service](configure-mgramseva/property-services.md) (property-services)
  2. ​[Water Service Calculator](configure-mgramseva/water-calculator-service.md) (ws-calculator)
  3. ​[Water Service](configure-mgramseva/water-calculator-service.md) (ws-service)
  4. ​[eChallan](configure-mgramseva/echallans-service.md) (echallan)
  5. ​[User Events](configure-mgramseva/user-events-service.md) (user-event)
  6. ​[Vendor](configure-mgramseva/vendor-registry-service.md)​
  7. ​[IFIX Adaptor Integration Service](https://ifix.digit.org/exemplar/mgramseva/user-manual/backend-services/ifix-adapter-integration-service)​

<div align="left">

<img src="https://238770250-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FS0VW1NVyguqXxlketbHB%2Fuploads%2FqWk2FvJIJ8btK9FcE15A%2FeGov_MgramSeva_Architecture.png?alt=media&#x26;token=9b7d18b6-fbed-49a6-b258-da64785a7689" alt="">

</div>

## mGramSeva Architecture Diagram

The sequence diagram below illustrates a typical interaction between the various services.

![Sample sequence diagram for a typical flow of DIGIT Microservices](https://238770250-files.gitbook.io/\~/files/v0/b/gitbook-legacy-files/o/assets%2F-Mfb8ehcimjt6ER7QOME%2F-MjIgmisnHwIZtDsYSNe%2F-MjIjnn2orGB4euQEf7C%2Fdigit\_sequence\_diagram.png?alt=media\&token=2d3fda64-eb5a-4281-bc77-5a64dee5a7d7)

