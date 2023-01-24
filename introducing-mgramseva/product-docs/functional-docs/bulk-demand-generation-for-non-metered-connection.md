# Bulk Demand Generation For Non-Metered Connection

There are 2 methods to generate Bulk Demand -

1. Auto (scheduler based)
2. Manual

**Auto**: The demand is generated at end of the month or the first day of next month or as scheduled for the recently completed billing cycle. Use cases are as below -

1. **First demand generated in the system**: The demand is generated for the recently completed billing cycle considering the arrears in the master data. The arrears are tagged to the previous billing cycle of the current demand.
2. **Consecutive demands**: The demand is generated for all the months pending from the most recent to the last billing cycle completed.
3. The demand is generated for the recently completed billing cycle.

**Manual**: The demand is generated for the billing cycle selected by the user. The demand is generated only for those consumers for whom demand does not exist for the selected month.

1. **First demand generated in the system**: The demand is generated for the selected billing cycle considering the arrears in the master data. The arrears are tagged to the previous billing cycle of the current demand.
2. **Consecutive demand**: The demand for the selected month is generated only if the previous billing cycle demand exists. If the demand for the previous cycle does not exist, it gives an error message “Demand generation is pending from billing cycle - \<Name of cycle>. please generate demand from this cycle in sequence”. The validation considers the most recent billing cycle that exists in the system.

**Charges/Heads & Calculation Logic**

As part of V1, only the water charges head is applicable. Rate Master is defined at the GPWSC level.

**Water Charges** - Charges are applicable as defined in the Rate Masters based on - Validity, Property Type, and Service Type where the calculation type is **“Per Bill Cycle”** for the given billing period.

**Bill Period** - The billing periods are monthly as per the standards followed across GPWSCs. In future, GPWSC may switch to bi-monthly to reduce the processing effort. The sample billing period data is given in the MDMS data.

**Exclusion**

* Reversion of demand is not allowed. This has to be done in the backend.
* Exception reporting for every batch processing can be accessed from the backend only.

> [![Creative Commons License](https://i.creativecommons.org/l/by/4.0/80x15.png)_​_](http://creativecommons.org/licenses/by/4.0/)_All content on this page by_ [_eGov Foundation_](https://egov.org.in/) _is licensed under a_ [_Creative Commons Attribution 4.0 International License_](http://creativecommons.org/licenses/by/4.0/)_._
