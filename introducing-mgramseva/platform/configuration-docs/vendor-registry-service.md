# Vendor Registry Service

## Overview

Vendor Registry is a system that enables ULBEmployees to create and search Vendors i.e. Desluding Operator (DSO) and driver entities with appropriate vehicle Entities for FSM Applications. This document contains details on how to set up the Vendor and describes the functionalities provided.

## Pre-requisites

Before you proceed with the configuration, make sure the following pre-requisites are met -

* _Java 8_
* The Kafka server is up and running
* egov-persister service is running and has a vendor-persister config path added to it
* PSQL server is running and a database is created to store FSM Application data
* The following services should be up and running:
  * egov-mdms-service
  * egov-user-service
  * boundary-service
  * vehicle

## Key Functionalities

1. Added payment payment preference and agency attributes for DSO
2. Added gender attribute in the create and update APIs for Vendor
3. Updated the Vendor search API to add vehicleCapacity in the search parameter to search all vendors matching the vehicle capacity specified in the search parameter.

### Deployment Details

1. Deploy the latest version of the vendor
2. Add vendor-persister.yml file in the config folder in git and add that path in persister. _(The file path is to be added in the environment yaml file in a param called_ persist-yml-path _) and restart_ egov-persister-service.
3.  Integrate the below changes in vendor-persister.yml

    [https://github.com/egovernments/configs/commit/95dd26f926ec44d07448926ee4b6b7e031847a57](https://github.com/egovernments/configs/commit/95dd26f926ec44d07448926ee4b6b7e031847a57)
4. [https://github.com/egovernments/configs/pull/2237/files](https://github.com/egovernments/configs/pull/2237/files)

## Configuration Details

### MDMS Configuration 

NA

### Business Service / Workflow Configuration

&#x20;

NA

### Actions & Role Action Mapping

After adding Actions and role-action mappings, restart the egov-mdms-service.

**Actions**

```
{
      "id": {{PLACEHOLDER1}},
      "name": "Create Vendor/DSO",
      "url": "/vendor/v1/_create",
      "displayName": "Create Vehicle",
      "orderNumber": 0,
      "enabled": false,
      "serviceCode": "vendor",
      "code": "null",
      "path": ""
    },
    {
      "id": {{PLACEHOLDER1}},
      "name": "Search Vendor/DSO",
      "url": "/vendor/v1/_search",
      "displayName": "Search  Vendor",
      "orderNumber": 1,
      "enabled": false,
      "serviceCode": "vendor",
      "code": "null",
      "path": ""
    },

```

**Role Action Mapping**

```
[
  {
    "rolecode": "FSM_ADMIN",
    "actionid": "{{PLACEHOLDER1}}",
    "actioncode": "",
    "tenantId": "pb"
  },
  {
    "rolecode": "FSM_ADMIN",
    "actionid": "{{PLACEHOLDER2}}",
    "actioncode": "",
    "tenantId": "pb"
  },
  {
    "rolecode": "FSM_DSO",
    "actionid": "{{PLACEHOLDER2}}",
    "actioncode": "",
    "tenantId": "pb"
  },
  {
    "rolecode": "FSM_EDITOR_EMP",
    "actionid": "{{PLACEHOLDER2}}",
    "actioncode": "",
    "tenantId": "pb"
  },
  {
    "rolecode": "FSM_VIEW_EMP",
    "actionid": "{{PLACEHOLDER2}}",
    "actioncode": "",
    "tenantId": "pb"
  },
  {
    "rolecode": "FSM_EMP_FSTPO",
    "actionid": "{{PLACEHOLDER2}}",
    "actioncode": "",
    "tenantId": "pb"
  },
  {
    "rolecode": "CITIZEN",
    "actionid": "{{PLACEHOLDER2}}",
    "actioncode": "",
    "tenantId": "pb"
  }
]

```

### **Infra Ops Configuration**

Configurations we can manage through values.yml of the vendor in the infra ops repo are as follows: values.yml for a vehicle can be found.

| Description                                               | name in values.yml                 | Current Value                            |
| --------------------------------------------------------- | ---------------------------------- | ---------------------------------------- |
| Kafka Consumer Group                                      | SPRING\_KAFKA\_CONSUMER\_GROUP\_ID | egov-vendor-services                     |
| kafka topic to which service push data to save new Vendor | PERSISTER\_SAVE\_VENDOR\_TOPIC     | save-vendor-application                  |
| mdms service host                                         | EGOV\_MDMS\_HOST                   | egov-mdms-service from egov-service-host |
| Vehicle Service host                                      | EGOV\_VEHICLE\_HOST                | vehicle from egov-service-host           |
| User service host                                         | EGOV\_USER\_HOST                   | egov-user-service from egov-service-host |
| Location Service Host                                     | EGOV\_LOCATION\_HOST               | egov-location from egov-service-host     |

**Configurations sample in Values.yml**

```
# Common Labels
labels:
  app: "vendor"
  group: "rainmaker"

# Ingress Configs
ingress:
  enabled: true
  zuul: true
  context: "vendor"

# Init Containers Configs
initContainers:
  dbMigration:
    enabled: true
    schemaTable: "vendor_schema"
    image:
      repository: "vendor-db"

# Container Configs
image:
  repository: "vendor"
replicas: "1"
healthChecks:
  enabled: true
  livenessProbePath: "/vendor/health"
  readinessProbePath: "/vendor/health"
appType: "java-spring"
tracing-enabled: true
heap: "-Xmx256m -Xms256m"
java-args: "-Dspring.profiles.active=monitoring"

# Additional Container Envs
env: |
  - name: EGOV_VEHICLE_HOST
    valueFrom:
      configMapKeyRef:
        name: egov-service-host
        key: vehicle
  - name: EGOV_MDMS_HOST
    valueFrom:
      configMapKeyRef:
        name: egov-service-host
        key: egov-mdms-service
  - name: EGOV_USER_HOST
    valueFrom:
      configMapKeyRef:
        name: egov-service-host
        key: egov-user
  - name: EGOV_LOCATION_HOST
    valueFrom:
      configMapKeyRef:
        name: egov-service-host
        key: egov-location
  - name: EGOV_HRMS_HOST
    valueFrom:
      configMapKeyRef:
        name: egov-service-host
        key: egov-hrms
  - name: SPRING_KAFKA_CONSUMER_GROUP_ID
    value: egov-vendor-services
  - name: PERSISTER_SAVE_VENDOR_TOPIC
    value: save-vendor-application
  - name: PERSISTER_UPDATE_VENDOR_TOPIC
    value: update-vendor-application
  - name: SPRING_KAFKA_PRODUCER_KEY_SERIALIZER
    value: org.apache.kafka.common.serialization.StringSerializer
  - name: SPRING_KAFKA_PRODUCER_VALUE_SERIALIZER
    value: org.springframework.kafka.support.serializer.JsonSerializer
  - name: JAVA_OPTS
    value: {{ index .Values "heap" | quote }}
  - name: JAVA_ARGS
    value: {{ index .Values "java-args" | quote }}
  - name: SERVER_PORT
    value: "8080"
  - name: SECURITY_BASIC_ENABLED
    value: "false"  
  - name: MANAGEMENT_SECURITY_ENABLED
    value: "false"
  {{- if index .Values "tracing-enabled" }}
  - name: TRACER_OPENTRACING_ENABLED
    value: "true" 
  {{- end }}
 
```

### Data Setup

DSO for FSM System is a vendor, For every city/ULB DSO should be created with the Representative details as owner, associated vehicles and drivers.

Sample Curl

```
curl --location --request POST 'https://dev.digit.org/vendor/v1/_create' \
--header 'Content-Type: application/json' \
--data-raw '{
    "RequestInfo": {
        "apiInfo": {
            "id": "string",
            "version": "string",
            "path": "string"
        },
        "deviceDetail": {
            "id": "string",
            "signature": "string"
        },
        "ts": 0,
        "action": "string",
        "key": "string",
        "msgId": "string",
        "requesterId": "string",
        "authToken": "a35b5ba7-2d5f-4272-8a67-0303cfab2c9f"
    },
    "vendor": {
        "tenantId": "pb.amritsar",
        "name": "DSO TATA1",
        "address": { 
            "tenantId": "pb.amritsar",
            "doorNo": "my door",
            "plotNo": "my plot",
            "landmark": "my landmark",
            "city": "amritsar",
            "district": "amritsar",
            "region": "amritsar",
            "state": "punjab",
            "country": "in",
            "pincode": "143001",
            "additionDetails": null,
            "buildingName": "my building",
            "street": "my streat",
            "locality": {
                "code": "SUN178",
                "name": "Mohalla Singh kia - Area2",
                "label": "Locality",
                "latitude": null,
                "longitude": null,
                "area": "Area2",
                "pincode": null,
                "boundaryNum": 1,
                "children": []
            },
            "geoLocation": {
                "latitude": 0,
                "longitude": 0,
                "additionalDetails": {}
            }
        },
        "owner": {

            "tenantId": "pb.amritsar",
            "name": "DSOc4",
            "fatherOrHusbandName": "Phani",
            "relationship": "FATHER",
            "gender": "MALE",
            "dob": 550261800000,
            "emailId": "test@dso.test",
            "correspondenceAddress": "KPHB",
            "mobileNumber": 8919146603
        },
        "vehicles": [{
        "tenantId": "pb.amritsar",
        "registrationNumber": "TS 09 PA 3586",
        "model":"1998",
        "type":"TATA.407",
        "tankCapacity":"2000",
        "suctionType":"SEWER_SUCTION_MACHINE",
        "pollutionCertiValidTill":1611584416772,
        "InsuranceCertValidTill":1611584416772,
        "fitnessValidTill":1611584416772,
        "roadTaxPaidTill":1611584416772,
        "gpsEnabled":true,
        "source":"Municipal records",
        "owner": {

            "tenantId": "pb.amritsar",
            "name": "DSOc4",
            "fatherOrHusbandName": "Phani",
            "relationship": "FATHER",
            "gender": "MALE",
            "dob": 550261800000,
            "emailId": "test@dso.test",
            "correspondenceAddress": "KPHB",
            "mobileNumber": 8919146617
        }
    },{
        "tenantId": "pb.amritsar",
        "registrationNumber": "TS 09 PA 2584",
        "model":"1998",
        "type":"MAHINDRA.BOLERO_PICKUP",
        "tankCapacity":"2000",
        "suctionType":"SEWER_SUCTION_MACHINE",
        "pollutionCertiValidTill":1611584416772,
        "InsuranceCertValidTill":1611584416772,
        "fitnessValidTill":1611584416772,
        "roadTaxPaidTill":1611584416772,
        "gpsEnabled":true,
        "source":"Municipal records",
        "owner": {

            "tenantId": "pb.amritsar",
            "name": "DSOc3",
            "fatherOrHusbandName": "Phani",
            "relationship": "FATHER",
            "gender": "MALE",
            "dob": 550261800000,
            "emailId": "test@dso.test",
            "correspondenceAddress": "KPHB",
            "mobileNumber": 8919146617
        }
    }],
        "drivers": [{

            "tenantId": "pb.amritsar",
            "name": "DriverDSO4",
            "fatherOrHusbandName": "Phani",
            "relationship": "FATHER",
            "gender": "MALE",
            "dob": 550261800000,
            "emailId": "test@dso.test",
            "correspondenceAddress": "KPHB",
            "mobileNumber": 8919146216
        },{

            "tenantId": "pb.amritsar",
            "name": "DriverDSO3",
            "fatherOrHusbandName": "Phani",
            "relationship": "FATHER",
            "gender": "MALE",
            "dob": 550261800000,
            "emailId": "test@dso.test",
            "correspondenceAddress": "KPHB",
            "mobileNumber": 8919146216
        }],
        "source": "WhatsApp"
    }
}'

```

## Integration Details

### Integration Scope

Any system or DIGIT module can integrated with Vendor Service, which helps to manage the Vendor with the vehicles, drivers and owner for the representative and login for the representative/owner to log into the system to carry our role-specific operations

### Integration Benefits

* Validation of DSO/Vendor availability
* Fetch the vehicle assigned to the DSO
* Fetch the Drivers assigned to the DSO

### Integration Steps

* FSM to call vendor/v1/\_search to fetch the DSOs
* FSM can call vendor/v1/\_search to fetch the DSOs and the respective vehicles and drivers

### Interaction Diagram

TBD

## Reference Docs

#### API List

<table data-header-hidden><thead><tr><th width="228"></th><th></th></tr></thead><tbody><tr><td><h4><strong>Title</strong> </h4></td><td><strong>Link</strong></td></tr><tr><td>/vendor/v1/_create</td><td><a href="https://www.getpostman.com/collections/c79e98843bcdcc873d09">https://www.getpostman.com/collections/c79e98843bcdcc873d09</a></td></tr><tr><td>/vendor/v1/_search</td><td><a href="https://www.getpostman.com/collections/c79e98843bcdcc873d09">https://www.getpostman.com/collections/c79e98843bcdcc873d09</a></td></tr><tr><td>/vendor/v1/_plainsearch</td><td><a href="https://www.getpostman.com/collections/c79e98843bcdcc873d09">https://www.getpostman.com/collections/c79e98843bcdcc873d09</a></td></tr></tbody></table>

&#x20;

&#x20;
