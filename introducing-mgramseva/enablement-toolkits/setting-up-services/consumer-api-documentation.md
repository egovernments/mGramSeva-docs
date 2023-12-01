# Consumer API Documentation

### Introduction

This document provides step-by-step instructions for creating a consumer in the mgramseva system using two API calls. The first API call is for creating a property, and the second API call is for making a connection for the consumer.

#### Prerequisites

1. Obtain a valid authentication token (`authToken`) for the desired environment.
2. Both API (i.e. for creating property and consumer) should be with you.
3. Import [this](https://web.postman.co/workspace/My-Workspace\~9f040a08-ea42-45f5-8e7b-4e79ceae42c7/collection/24183907-ecbf5436-a14f-4345-92fe-28d5e24569a5?action=share\&source=copy-link\&creator=24183907) collection in Postman. (change the URL as per your req)

### 1. Property Creation API

First, make property by using the Property creation API given in Postman collection

**Important Notes:**

* For metered connections, provide initialMeterReading, meterReading, meterId, and previousReading; otherwise, set them to null.
* ConnectionType should be "Metered" for metered connections and "Non\_Metered" for non-metered connections.
* Ensure the oldConnectionNo is unique every time.
* Use the propertyId obtained from creating the property.

After making the property you will get the property ID in response copy that.

### 2. Consumer Creation API

In the Postman collection, you can see two API's **Metered connection for consumer creation** API and a **Non-metered connection for consumer** **creation** API

* For metered connections, provide initialMeterReading, meterReading, meterId, and previousReading; otherwise, set them to null.
* ConnectionType should be "Metered" for metered connections and "Non\_Metered" for non-metered connections.
* Ensure the oldConnectionNo is unique every time.
* Use the propertyId obtained from creating the property.

By following these instructions and providing the necessary details, you can successfully create a consumer with a property and connection in the Mgramseva system.
