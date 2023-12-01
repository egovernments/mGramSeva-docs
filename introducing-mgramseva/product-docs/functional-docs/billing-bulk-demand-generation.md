# Billing - Bulk Demand Generation

All Gram Panchayats have a monthly billing cycle for water charges.  The Scheduler automatically triggers on the “X” date of every month to generate demand and raise bills for non-metered connections.

* Metered connections do not fall under bulk demand generation

1. For the first month of go-live, it is only the arrears and no demand that is generated hence there is no bill to collect payments.
2. From the second month (X date of Month 2) onwards, demand is generated.
3. Once the demand is generated, a notification is triggered to all mGramSeva users.
   * Details of Notification
     * “Demand for water charges has been raised for \<GP>. New Bill Amount is Rs. Xyz. Overall pending amount is Rs.AbcD”
4. Each non-metered household also gets notifications
   * SMS Notification with Bill PDF
     * Dear “username”, A new water bill has been generated against \<connection ID>. Please download the bill using \<link>
   * &#x20;SMS notification with a payment link
     * Dear “username”, A new water bill has been generated against \<connection ID>. Please pay the bill online to avoid late payment charges\<link>
5. Revenue collectors can see a new card (Updated card from month 2 onwards) with information related to demand and payment collection on the HH Details screen.
6. There is also a demand collection tile/card on the home screen.
   * This is used in cases when the scheduler is not run (due to technical errors) and the Gram Panchayat wants to run it manually.
7. The system does nothing if the manual demand generation is done in the middle of the billing cycle for which demand has already been generated.
   * Manual demand generation helps only when the scheduler has not generated a demand for a billing cycle.

For Demand Generation Logic refer to [Bulk Demand Generation for Non-Metered](broken-reference)

In the Bulk Demand screen -

**Service Category:** Defaulted to Water Charges (Module)

**Service Type:** Defaulted to “Non-Metered”

**Billing Year:** Dropdown with the list of the financial years from the master

**Billing Cycle:** Dropdown with the list of billing cycles for the selected financial year

Clicking on Generate Demand triggers the demand for the given billing cycle based on the logic defined above.

![](<../../../.gitbook/assets/image (125).png>)

> [![Creative Commons License](https://i.creativecommons.org/l/by/4.0/80x15.png)_​_](http://creativecommons.org/licenses/by/4.0/)_All content on this page by_ [_eGov Foundation_](https://egov.org.in/) _is licensed under a_ [_Creative Commons Attribution 4.0 International License_](http://creativecommons.org/licenses/by/4.0/)_._
