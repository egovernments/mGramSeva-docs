# Setting up a new tenant

This documentation outlines the process of setting up a new tenant in MDMS (Master Data Management System). To achieve this, it involves cloning the MDMS repository locally and utilizing a Python script that interacts with an Excel file containing essential information for the new tenant setup.

### Prerequisites

1. Clone the [MDMS](https://github.com/misdwss/mdms-mgramseva) repository to your local machine.
2. Have the Excel file ready for reference. The structure of the Excel file is critical, and any changes must align with the specified columns. The reference to the Excel file is given below.

### Python Script Configuration

1. Locate the Python script for adding a new tenant. The script can either be placed in the "tenants" folder locally or specify the full path where your "tenants.json" folder is present within the script.
2.  Open the script and edit the following lines to match your requirements:

    ```python
    dataframe = openpyxl.load_workbook("Book2.xlsx")
    ```



    Replace "Book2.xlsx" with the name of your Excel file containing tenant information.
3.  Specify the sheet name in your Excel file where the required data is stored.

    ```python
    dataframe1 = dataframe["Sheet1"]
    ```

### Excel File Preparation

1. Ensure your Excel file adheres to the specified format. The columns must match the template provided, and any deviation may result in script failure.
2. Do not modify the column structure in the Excel sheet, as the script relies on a consistent format.

### Running the Script

Execute the Python script after configuring it according to your needs. The script will process the Excel file, and upon completion, a new file named "tenants\_new.json" will be generated.

**Deploying to MDMS:**

* Copy the generated `tenants_new.json` file to the MDMS repository or select and apply the updated data within MDMS as needed.\


{% file src="../../../.gitbook/assets/Book2.xlsx" %}

{% file src="../../../.gitbook/assets/create_tenants_json_Book2.py" %}

After creating a tenant in the tenants.json file we need to make a separate folder in mdms for each tenant&#x20;

