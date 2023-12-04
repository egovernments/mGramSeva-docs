# Loading Consumers For mGramSeva

## Overview

This page provides step-by-step instructions for using a Python script to create consumers for mGramSeva. Follow these guidelines to load consumer data into the system using the Python script provided.

## Steps

#### Step 1: Prepare Excel Sheet

Before running the script, ensure you have a properly formatted Excel sheet. The sheet should include the following columns:

* Consumer Name (Mandatory, use "NA" if not available)
* Gender (Male/Female)
* Father Name (Mandatory, use "NA" if not available)
* Mobile Number (Mandatory)
* Old Connection Number
* Property Type
* Service Type (till now in we have Non-metered only for data loading)
* Ward (Always set to "Ward 1")
* Meter Reading (If available, use provided date; otherwise, default to "12/01/2022")
* GPWSC Name
* Arrears
* Previous Reading ((if arrears and previous reading are not given, write '0')

Ensure the format of the meter reading matches the provided sample format given in excel file below, as incorrect formatting may lead to loading failures.

### 2. Python Script Configuration

Edit the Python script with the following details:

* Set the host URL based on whether it's for production, QA, or UAT.
* Provide the username and password corresponding to your host URL.
* Specify the path where your Excel file is stored. It is recommended to store the Excel file in the same location as your Python script.

### 3. Running the Script

Execute the Python script after configuring the host URL, username, password, and file path. The script will load data into mGramSeva based on the information provided in the Excel sheet.

### 4. Post-Execution Steps

Do not open the Excel file until the script completes its task. After completion, open the Excel file to check the status. The status will indicate whether the operation was successful or if there was a failure. If there's a failure, refer to the provided reason for further investigation and resolution.

{% file src="../../../.gitbook/assets/Consumers.xlsx" %}

{% file src="../../../.gitbook/assets/loadConsumer-uat (1).py" %}
