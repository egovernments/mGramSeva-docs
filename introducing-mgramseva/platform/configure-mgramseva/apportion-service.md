# Apportion Service

## Overview

Apportion service is used to apportion the amount paid against a bill among the different tax heads based on the implemented algorithm. The default algorithm uses the order of the tax head to apportion, the tax head with the lowest order is apportioned off first while the highest-order tax head is apportioned last.

## Pre-requisites

Before you proceed with the documentation, make sure the following pre-requisites are met -

* _Java 8_
* The Kafka server is up and running
* egov-persister service is running and has an apportioned persister configuration path added to it
* PSQL server is running and a database is created to store apportion audit data

## Key Functionalities

* Apportion payment in tax heads of bill
* Apportion advance amount in tax heads of demand during demand creation

| **Environment Variables**          | **Description**                                                                       |
| ---------------------------------- | ------------------------------------------------------------------------------------- |
| egov.apportion.default.value.order | If set to true will apportion of negative amount first irrespective of tax head order |

## Deployment Details

1. Deploy the latest version of the egov-apportion-service service
2. Add apportion persister yaml path in persister configuration

## Configuration Details

There is no separate configuration required. The TaxHead master that is configured in billing service is only used

## Integration Details

### Integration Scope

Any payment service which wants to divide the paid amount into different tax head buckets can integrate with the apportion service.

### Integration Benefits

* Apportions amount in tax heads

### Integration Steps

1. To integrate, the host of egov-apportion-service should be overwritten in the helm chart
2. /apportion-service/v2/bill/\_apportion should be called to apportion the bill
3. /apportion-service/v2/demand/\_apportion should be called to apportion advance amount in demands

## Reference Docs

#### Doc Links

<table data-header-hidden><thead><tr><th width="216"></th><th></th></tr></thead><tbody><tr><td><strong>Title</strong> </td><td><strong>Link</strong></td></tr><tr><td>Collection Service</td><td> <a href="https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/1620574288">https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/1620574288</a></td></tr><tr><td>Billing Service</td><td> <a href="https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/1620672528">https://digit-discuss.atlassian.net/wiki/spaces/DD/pages/1620672528</a></td></tr><tr><td>API Swagger Documentation</td><td></td></tr></tbody></table>

#### API List

<table data-header-hidden><thead><tr><th width="241"></th><th></th></tr></thead><tbody><tr><td><h4><strong>Title</strong> </h4></td><td><strong>Link</strong></td></tr><tr><td><em>/apportion-service/v2/bill/_apportion</em></td><td><a href="https://www.getpostman.com/collections/142983a40e95da157b45">https://www.getpostman.com/collections/142983a40e95da157b45</a></td></tr><tr><td><em>/apportion-service/v2/demand/_apportion</em></td><td> <a href="https://www.getpostman.com/collections/142983a40e95da157b45">https://www.getpostman.com/collections/142983a40e95da157b45</a></td></tr></tbody></table>

_(Note: All the APIs are in the same Postman collection therefore the same link is added in each row)_
