# User Events Service

### Overview

eGov-User-Events service provide a common point to manage all the events generated for the user in the system. Events include updates from multiple applications like PT, PGR, TL etc, events created by the employee addressing the citizen etc. This service provides APIs to create , update and search such events for the user.

### Pre-requisites

Before you proceed with the documentation, make sure the following pre-requisites are met -

* _Java 8_
* Kafka server is up and running
* egov-persister service is running and has egov-user-events persister config path added in it
* PSQL server is running  and database is created

### Key Functionalities

* Provide common platform to create, manage and notify events.
* Events can be created either by an API call or through pushing records to the Kafka Queue.

### Interaction Diagram

### Deployment Details

1. Add mdms configs required for egov-user-events.
2. Add Role-Action mapping for API’s.
3. Deploy the latest version of egov-user-events
4. Add egov-user-events file in config folder in git and add that path in persister . _(The file path is to be added in environment yaml file in param called_ persist-yml-path _)_

### Configuration Details

Add master data in MDMS service with module name as **mseva**. Following is some sample master data for the service:\
\
**Event Categories**

```
{
  "tenantId": "pb",
  "moduleName": "mseva",
  "EventCategories": [
    {
      "code": "PUBLICHEALTH",
      "eventType":"EVENTSONGROUND",
      "active": true
    },
    {
      "code": "CULTURAL",
      "eventType":"EVENTSONGROUND",
      "active": true
    },
    {
      "code": "WARDCOMMITTEEMEETING",
      "eventType":"EVENTSONGROUND",
      "active": true
    }
  ]
}
```

**Event Types**:

```
{
  "tenantId": "pb",
  "moduleName": "mseva",
  "EventTypes": [
    {
      "code": "BROADCAST",
      "active": true
    },
    {
      "code": "EVENTSONGROUND",
      "active": true
    },
    {
      "code": "SYSTEMGENERATED",
      "active": true
    },
    {
      "code": "OTHERS",
      "active": true
    }
  ]
}
```

Using /localization/messages/v1/\_upsert , add localisation (templates) for notification messages to be sent. Following are the product notification templates:

```
{
  "messages": [
    {
      "code": "egovuserevents.notification.counterevent.ondelete",
      "message": "<event_name> has been deleted. Please remove from your calendar.",
      "module": "egov-user-events",
      "locale": "en_IN"
    },
    {
      "code": "egovuserevents.notification.counterevent.onupdate",
      "message": "Details of <event_name> have been updated.",
      "module": "egov-user-events",
      "locale": "en_IN"
    }
  ]
}
```

**Configurable Properties:**

&#x20;Following are the properties in application.properties file in egov-user-events service which are configurable.

| **Property**                                        | **Value**                 | **Remarks**                                                                                                                                            |
| --------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| <p>kafka.topics.persister.save.events</p><p> </p>   | save-user-events          | This is the persister topic onto which user-events pushes records for persistence. This is for creating events.                                        |
| <p>kafka.topics.persister.update.events</p><p> </p> | update-user-events        | This is the persister topic onto which user-events pushes records for persistence. This is for updating events.                                        |
| <p>kafka.topics.lat.details</p><p> </p>             | user-events-lat           | This is the persister topic onto which user-events pushes records for persistence. This is for storing last-access-time / last-login-time of the user. |
| <p>kafka.topics.save.events</p><p> </p>             | persist-user-events-async | Topic to which the user-events consumer is subscribed. Producers willing to create events must push records to this topic.                             |
| kafka.topics.update.events                          | update-user-events-async  | Topic to which the user-events consumer is subscribed. Producers willing to update events must push records to this topic                              |
| <p>mseva.notif.search.offset</p><p> </p>            | 0                         | Default pagination offset.                                                                                                                             |
| <p>mseva.notif.search.limit</p><p> </p>             | 200                       | Default pagination limit.                                                                                                                              |

**Entities:**

Events: Model to capture the events information. This object captures all the details of an event which is either being created or updated.

EventDetails: Captures details of the event such as organiser, location, time etc are captured here. This is the child object to Events object. This has significance only the type of the event is ‘EVENTSONGROUND’.

Action: This captures the user-actions involved in the event. Say pay now option, reopen option, download certificate option etc.

Recipient: Every event is addressed to a crowd to which a notification of the same is sent. This model captures information about the recipients of the notification of this event or can also be framed as details of the adresse of the event.

Event Type: Events are divided into multiple types as follows:

1. BROADCAST - These are messages broadcasted addressing a group of people. For instance, “There’s road blockage near the bus stand, please use a different route”
2. EVENTSONGROUND - These are events organised by a group of people addressing another group of people usually it is the ULB organising events for the citizens. It can be any activity like a 10K Marathon, Polio Drive, Property Tax collection drive etc.&#x20;
3. SYSTEMGENERATED - These events generated by different systems on the egov platform like PT, TL, PGR etc addressing a group of people. For instance, “Dear Citizen, Your TL has been approved please proceed to Pay here \<PAY\_NOW>”
4. OTHERS - Events that don’t belong to the types mentioned above.

These are configured in MDMS.

Event Category: Events are categorised into following:

1. PUBLICHEALTH - Events related to public health.
2. CULTURAL - Cultural events
3. WARDCOMMITEEMEETING - Events for recurring meetings of ward committee.

These event categories are mapped to event types internally. The categories mentioned here are for EVENTSONGROUND type. These are configured in MDMS.

&#x20;

**How does it work?:**

This service manages user events on the egov-platform, which means all the events about which the user (essentially citizen) has to be notified are stored and retrieved through this service. Events can be created either by an API call or through pushing records to the Kafka Queue.&#x20;

Every event should contain information about the event type, event category, event name, description, recipient, actions, event details etc. Based on the type of the event, the list of mandatory fields varies. MDMS configurations required for this service to work can be found here: [https://github.com/egovernments/egov-mdms-data/tree/master/data/pb/mseva](https://github.com/egovernments/egov-mdms-data/tree/master/data/pb/mseva)

Once the event is sent for creation, the service validates all the required fields and assigns a recipient list to that event. An event can be addressed to a particular person, group of people, a user type and also roles. Events like updates on the TL application are addressed to the owner of the TL only, Events like Polio drive are addressed to the entire ULB, Events like mass Bill generation are addressed only to those who are required to pay those bills. Like this an recipient list is generated based on the request and stored in the system.&#x20;

When an event is updated a counter event is generated, Counter events are of 2 types: Counter event on Delete and Counter event on Update. When an event in ACTIVE status is made INACTIVE or CANCELLED, counter event on delete is generated. When details of an event are updated irrespective of the status a counter event on update is generated. These counter-events are stored along with the actual event in the system. However, when a counter-event on delete is generated, its corresponding actual event is marked INACTIVE. &#x20;

One of the important aspects of this service is the search API. Searching for the events stored in the user-events system is different for different roles. When a CITIZEN searches, all the events addressed to that citizen are retrieved, the events that contain corresponding counter-events are deduplicated and only the latest ACTIVE events are returned.&#x20;

We’ve a use-case where past-events have to be marked INACTIVE, this applies to all the BROADCAST and EVENTSONGROUND type of events which are time-capped. If a BROADCAST event is active from 1/Jan to 10/Jan, it’ll be marked inactive post 10/Jan, after which the CITIZEN stops receiving any updates to that event. This changing of status of the events is achieved by a lazy-update technique instead of a cron-job. Due to this, the search API not only returns the events but also updates the status of events before returning it to the user based on whether it has expired.&#x20;

When an EMPLOYEE searches, all the EVENTSONGROUND posted in his particular ULB are returned by default irrespective of the status. He/She can perform actions on those events, which if active, are notified to the CITIZEN.

An EMPLOYEE can search event based on the date the range, whatever the event created or last modified in that range, will appear in the search response. So, to get the details about event in a particular date range pass the value in **fromDate** and **toDate** field of search criteria.

_**fromDate**_ and _**toDate**_ fields accept epoch value only.&#x20;

And to get details about Delete event, pass Status as **CANCELLED** and to get details about Broadcast event pass eventType as **BROADCAST.**\


Please go through the code and descriptions over every method to understand the use-cases and flow-of-logic in a better way.

### Integration

#### Integration Scope

eGov-user-events can be integrated with any organisation or system which wants to send the events generated for the user in the system

#### Integration Benefits

* Easy manages user events on the system, which means all the events about which the user (essentially citizen) has to be notified are stored and retrieved through this service.

#### Steps to Integration

1. Employee can create events in the system using /egov-user-event/v1/events/\_create endpoint
2. Employee can update events in the system using /egov-user-event/v1/events/\_update endpoint
3. Events are searched in the system using /egov-user-event/v1/events/\_search endpoint
4. /egov-user-event/v1/events/notifications/\_count API is use to fetch the count of total, unread, read notifications.
5. /egov-user-event/v1/events/lat/\_update API is use to update the last-login-time of the user. We store last-login-time of the user through this API thereby deciding which notifications have been read.

### Reference Docs

#### Doc Links

| **Title**                 | **Link**                                                                                                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| API Swagger Documentation | [Swagger Documentation](https://editor.swagger.io/?url=https://raw.githubusercontent.com/egovernments/DIGIT-OSS/master/municipal-services/docs/user-events.yml#!/) |

#### API List

| <h4><strong>Title</strong> </h4>                 | **Link**                                                                                                                   |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
|  _/egov-user-event/v1/events/\_create_           | [https://www.getpostman.com/collections/14812d58dff5565bd3d9](https://www.getpostman.com/collections/14812d58dff5565bd3d9) |
| _/egov-user-event/v1/events/\_update_            | [https://www.getpostman.com/collections/14812d58dff5565bd3d9](https://www.getpostman.com/collections/14812d58dff5565bd3d9) |
| _/egov-user-event/v1/events/\_search_            | [https://www.getpostman.com/collections/14812d58dff5565bd3d9](https://www.getpostman.com/collections/14812d58dff5565bd3d9) |
| /egov-user-event/v1/events/notifications/\_count | [https://www.getpostman.com/collections/14812d58dff5565bd3d9](https://www.getpostman.com/collections/14812d58dff5565bd3d9) |
| /egov-user-event/v1/events/lat/\_update          | [https://www.getpostman.com/collections/14812d58dff5565bd3d9](https://www.getpostman.com/collections/14812d58dff5565bd3d9) |

_(Note: All the API’s are in the same postman collection therefore same link is added in each row)_\
