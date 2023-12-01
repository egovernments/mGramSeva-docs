# Getting Started With DIGIT

## Overview

To enable any municipal service in a fresh environment and for the first time, we require a basic idea of what DIGIT does and the generic services required to set it up.&#x20;

DIGIT is an open-source, customizable platform that lends itself to extensibility. New modules can be built on top of the platform to suit new use-cases or existing modules can be modified or replaced. To enable this, in addition to deploying DIGIT, a CD/CI pipeline has to be set up. CD/CI pipelines enable the end users to automate & simplify the build/deploy process.&#x20;

Find more details on DIGIT and platform deployment [here](https://core.digit.org/guides/installation-guide/digit-deployment).&#x20;

## Core Services <a href="#hardbreak-core-services" id="hardbreak-core-services"></a>

DIGIT platform comprises several core services that serve as the platform backbone.\
Some of the key core services are listed below:

1. [Workflow Service](https://core.digit.org/platform/core-services/workflow-service)
2. [Location Service](https://core.digit.org/platform/core-services/location-services)
3. [User Service](https://core.digit.org/platform/core-services/user-services)
4. [Access Control Service](https://core.digit.org/platform/core-services/access-control-services)
5. [PDF Service](https://core.digit.org/platform/core-services/pdf-generation-service)
6. [Payment Service](https://core.digit.org/platform/core-services/payment-gateway-service)
7. [MDMS Service](https://core.digit.org/platform/core-services/mdms-master-data-management-service)
8. [Indexer Service](https://core.digit.org/platform/core-services/indexer-service)
9. [Persister Service](https://core.digit.org/platform/core-services/persister-service)
10. ..among [multiple others](https://core.digit.org/platform/core-services)

Each microservice has a distinct function explained in the provided documentation links.

Developers can activate specific municipal services easily once the platform and its terminologies are well understood.&#x20;

{% hint style="info" %}
NOTE - mGramSeva uses DIGIT core services and additional code is available in [municipal-services](https://github.com/egovernments/punjab-mgramseva/tree/master/municipal-services) and [business-services](https://github.com/egovernments/punjab-mgramseva/tree/master/business-services).
{% endhint %}
