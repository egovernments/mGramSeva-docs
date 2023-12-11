# Workflow

***

## Overview

This page provides the steps to follow to create a workflow in mGramSeva.

## Steps

#### Workflow Creation in mGramSeva

Follow these steps to create a workflow in mGramSeva:

1. **Check Existing Workflow:**
   * Utilize the provided Postman collection that includes workflow create and search APIs.
   * Use the search API to check if the workflow for the specified state already exists.
2. **Workflow Creation:**
   * If the workflow is not present, proceed to create it using the create API.
   * Ensure to provide the necessary details in the userInfo section, give superuser information.
   * Adjust parameters like tenantId and roles according to your specific requirements.
3. **Port Forwarding:**
   *   Execute port forwarding to the workflow service using the following kubectl command:

       ```
       kubectl port-forward <pod-name> -n mgramseva
       ```

       Replace `<pod-name>` with the appropriate pod name.
4. **Create Workflow:**
   * After port forwarding, initiate the workflow creation process.
5. **Search Through API:**
   * Use the search API to verify that the workflow has been successfully created.
   * Adjust the search parameters as needed.

These steps ensure a smooth workflow creation process in mGramSeva. Make sure to follow each step in sequence for a seamless experience.

***
