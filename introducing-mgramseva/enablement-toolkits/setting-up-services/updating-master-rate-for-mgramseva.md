# Updating Master Rate for Mgramseva

This documentation outlines the step-by-step process for using a Python script to change master rates for Mgramseva in bulk. The script reads data from an Excel file, updates the master rates, and generates a new CSV file containing the modified information. Once the script is successfully executed, changes can be pushed to the local MDMS repository on GitHub.

**Prerequisites:**

* Python script
* MDMS repository cloned on the local system
* Excel file with tenant names, old master rates, and new master rates

**Steps:**

**1. Prepare Excel File:**

* Ensure the Excel file contains three columns: Tenant Name (in lowercase), Old Master Rate, and New Master Rate.
* If the columns are not present, add them to the Excel file.

**2. Clone and Create Branch:**

* Clone the MDMS repository to your local system.
* Create a new branch from the branch where you intend to make changes.

**3. Update Python Script:**

* Open the Python script and locate the variables:
  * `updatedfile`: Provide the path to your Excel sheet.
  * `localFilePath`: Specify the path where your MDMS repository is cloned.
  * Identify the columns in the Excel file where Tenant Name, Old Master Rate, and New Master Rate are stored. Update the script accordingly:

```
uniqueVillageName = row[2].value
oldMasterRate = row[7].value
newMasterRate = row[8].value
```

* Run the script.

**4. Script Execution:**

* Do not open the Excel file during script execution.
* The script will generate a new file named `new_updated_file4.csv` containing information about whether rates were updated or not.

**5. Verification:**

* Check `new_updated_file4.csv` to verify if all rates were updated successfully.

**6. Push Changes to Git:**

* If all rates are updated, the local changes will affect the MDMS repository.
* Raise a pull request and merge changes from the Git repository.

**Note:**

* It is crucial not to open the Excel file while the script is running to avoid data inconsistencies.
* Ensure that the Python environment and dependencies are properly set up.

Following these steps should enable you to efficiently update master rates for Mgramseva in bulk, ensuring accurate and streamlined changes to the MDMS repository.



{% file src="../../../.gitbook/assets/Master Rate Tracking (1).xlsx" %}

{% file src="../../../.gitbook/assets/ChangeTariffOfVillage.py" %}
