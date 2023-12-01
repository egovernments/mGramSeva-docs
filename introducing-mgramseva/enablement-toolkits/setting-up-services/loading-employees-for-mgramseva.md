# Loading Employees For mGramSeva

## **Overview**

This page provides a clear and concise guide for automating user creation in mGramSeva. It allows you to efficiently create users and manage their roles in the system.

Follow the steps provided on this page to create users for mGramSeva using a Python script. The process involves preparing an Excel sheet with user information, configuring the Python script, and executing it.

## **Pre-requisites**

1. Python script for creating users for mGramSeva.The sample format of the Python script is attached below.
2. Excel sheet containing user data. The sample format of the Excel sheet is attached below. Make sure to populate the data in the same format.
   * Columns: tenant name, mobile no, father name, gender, date of birth (dd/mm/yyyy), type, and ward (fixed to "ward 1").
   * Types: Sarpanch, Secretory, Revenue Collector, Division User or State User
   * Roles for Sarpanch: COLLECTION\_OPERATOR, EXPENSE\_PROCESSING, BULK\_DEMAND\_PROCESSING, DASHBOARD\_VIEWER, GP\_ADMIN.
   * Roles for Secretory: EXPENSE\_PROCESSING, BULK\_DEMAND\_PROCESSING, DASHBOARD\_VIEWER, GP\_ADMIN, COLLECTION\_OPERATOR.
   * Roles for Revenue Collector: COLLECTION\_OPERATOR, DASHBOARD\_VIEWER.
   * Roles for Division User: HRMS\_ADMIN, DIVISION\_ADMIN
   * Roles for State User: HRMS\_ADMIN, STATE\_ADMIN

## Steps

1.  **Prepare the Excel Sheet:**

    Create an Excel sheet with the following columns and data in the given format:

    * Tenant Name (in lowercase)

    **For State User tenant name will be pb**

    * Mobile Number
    * Father's Name (Mandatory, use "NA" if not available)
    * &#x20;Gender (M/F - this data is mandatory)
    * Date of Birth (in the format dd/mm/yyyy)
    * &#x20;Type (Sarpanch, Secretory, Revenue Collector, Division User or State User)
    *   Roles

        Based on the User Type, set corresponding roles:

        * Sarpanch: COLLECTION\_OPERATOR, EXPENSE\_PROCESSING, BULK\_DEMAND\_PROCESSING, DASHBOARD\_VIEWER, GP\_ADMIN
        * Secretary: EXPENSE\_PROCESSING, BULK\_DEMAND\_PROCESSING, DASHBOARD\_VIEWER, GP\_ADMIN, COLLECTION\_OPERATOR
        * Revenue Collector: COLLECTION\_OPERATOR, DASHBOARD\_VIEWER
        * Division User: HRMS\_ADMIN, DIVISION\_ADMIN
        * State User: HRMS\_ADMIN, STATE\_ADMIN
    * The 'Boundary' should be set to "Ward 1" as per mGramSeva standards.
2. **Run the Python Script:**
   * Open the Python script.
   * Provide the following information within the script:
     * Host URL: Specify the target environment (prod, qa, or uat).
     * Username and Password: As per your host URL.
     * Path to the Excel file: Ensure the Excel file is in the same location as the script.
   * Execute the script.
3. **Post-Execution:**
   * **Do not open the Excel file until the script has completed its task.**
   * After the script finishes, open the Excel file to review the results.
   * The Excel file will contain two columns:
     * User ID: If successful, the ID will be present.
     * Status: Will indicate either "Success" or "Failure." If failed, the reason for failure will be provided.

{% file src="../../../.gitbook/assets/updated-user.xlsx" %}

{% file src="../../../.gitbook/assets/onBoarding (1).py" %}
