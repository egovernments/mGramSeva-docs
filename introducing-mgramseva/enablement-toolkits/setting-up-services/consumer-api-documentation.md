# Consumer API Documentation

## Introduction

This page provides step-by-step instructions for creating a consumer in the mGramSeva system using two API calls. The first API call is for creating a property, and the second API call is for making a connection for the consumer.

## Pre-requisites

Before proceeding with the given tasks, ensure the following prerequisites are met:

1. **Authentication Token (authToken):** Obtain a valid authentication token for the desired environment. This token is necessary to authenticate and authorize your requests.
2. **API Endpoints:** Ensure you have access to both APIs required for creating a property and a consumer. Make sure you have the correct API documentation or information about the endpoints, request payloads, and any required headers.
3. **Postman:** If you don't have Postman installed, download and install it. Import [this](https://web.postman.co/workspace/My-Workspace\~9f040a08-ea42-45f5-8e7b-4e79ceae42c7/collection/24183907-ecbf5436-a14f-4345-92fe-28d5e24569a5?action=share\&source=copy-link\&creator=24183907) collection in Postman. Make sure you change the URL as per your requirements.

## Steps

Follow the steps given below to create consumers using either Property Create API or Consumer Create API.

### 1. Property Creation API

Here's a step-by-step guide:

1. **Locate the Property Creation API:**
   * Open the Postman collection you imported.
   * Find the request corresponding to the Property Creation API. It might be named something like "Create Property" or similar.
2. **Set Request Parameters:**
   * Review the request parameters for creating a property.
   * For metered connections, provide values for `initialMeterReading`, `meterReading`, `meterId`, and `previousReading`. Set them to null if not applicable.
   * Set `ConnectionType` to "Metered" for metered connections and "Non\_Metered" for non-metered connections.
   * Ensure that `oldConnectionNo` is unique every time you create a property.
3. **Execute the Request:**
   * Click on the "Send" button to execute the request.
   * Review the response to confirm that the property has been created successfully.
4. **Copy Property ID:**
   * In the response, you should find the `propertyId` field. Copy the value of `propertyId` as this will be needed for subsequent steps.

Now, you have successfully created a property, and you have the `propertyId` copied for future use. Ensure to follow any additional instructions provided in the Postman collection or the API documentation.

### 2. Consumer Creation API

Follow the steps below to create a consumer using the Consumer Creation API from the Postman collection:

1. **Locate the Consumer Creation API:**
   * Open the Postman collection.
   * Find the request corresponding to the Consumer Creation API. It may be named "Create Consumer - Metered" for metered connections or "Create Consumer - Non-Metered" for non-metered connections.
2. **Set Request Parameters:**
   * Review the request parameters for creating a consumer.
   * For metered connections, provide values for `initialMeterReading`, `meterReading`, `meterId`, and `previousReading`. Set them to null if not applicable.
   * Set `ConnectionType` to "Metered" for metered connections and "Non\_Metered" for non-metered connections.
   * Ensure that `oldConnectionNo` is unique every time you create a consumer.
   * Use the `propertyId` obtained from creating the property as instructed in the previous step.
3. **Execute the Request:**
   * Click on the "Send" button to execute the request.
   * Review the response to ensure that the consumer has been created successfully.

By following these instructions and providing the necessary details, you should be able to successfully create a consumer with a property and connection in the mGramSeva system. Ensure that you follow any additional guidelines or instructions provided in the Postman collection or API documentation.

