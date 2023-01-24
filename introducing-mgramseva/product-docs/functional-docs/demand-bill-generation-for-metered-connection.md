# Demand/Bill Generation For Metered Connection

The demand is generated for metered connections for the billing period (defined based on the meter reading date) selected by the user at the time of recording the meter reading.&#x20;

The 2 use cases to be handled are -

1. **First demand generated in the system**: The demand is generated for the selected billing period. The demand period would be from “Previous meter reading date” from the consumer master or the demand created as part of the master TO the date entered in the billing screen. The arrears are tagged to the previous billing period of the current demand, and the period is from the start of FY to the “Previous meter reading date” from the consumer master.
2. **Consecutive demand**: The demand is generated for the period defined based on
   * From Date: Meter reading date from last demand generated for the consumer
   * To Date: Is the selected meter reading date in the bill generation screen

**Charges/Heads & Calculation Logic**

As part of V1, only the water charges head is applicable. Rate Master is defined at the GPWSC level.

**Water Charges** - Charges are applicable as defined in the Rate Masters based on - Validity, Property Type, and Service Type where the calculation type is **“Unit Rate”** for the given number of units.

**Bill Period** - Is as per the date range selected for the bill generation.

**Exclusion**

* Reversion of demand is not allowed. This has to be taken up in the backend.

> [![Creative Commons License](https://i.creativecommons.org/l/by/4.0/80x15.png)_​_](http://creativecommons.org/licenses/by/4.0/)_All content on this page by_ [_eGov Foundation_](https://egov.org.in/) _is licensed under a_ [_Creative Commons Attribution 4.0 International License_](http://creativecommons.org/licenses/by/4.0/)_._
