# Revenue Collection - Offline

Once the demand is generated for metered and non-metered connections, revenue collectors come to this screen to collect payments.

1. Users can see the consumer billing information on the screen
2. Clicking on View Details expands the card and shows more details. Clicking on the Hide Details collapses the card to show only connection ID, Consumer Name & Total Due Amount.
3. Payment amount - can either pay
   * The full amount, or
   * Custom amount - Users can enter the custom amount in the input field - this cannot be zero or greater than the total due amount.
4. Payment methods
   * Cash - select cash and proceed to payment takes the user to the successful collection screen
   * Online - The online payment option displays a Q/R code on the user screen that can be scanned by another phone to pay the due.
   * Post payment via any mode - payment success screen is shown
   * Receipt ID format - RB-dd/mm/yyyy-yy/running\_sequence\_number
5. User Actions
   * Download receipt - download PDF version of receipt with receipt ID as the name of PDF while downloading
   * Share receipt via WhatsApp - opens the Phone OS sharing options
   * back to home - takes the user back to the home screen
6. SMS to HH
   * As soon as the amount is paid and the Revenue collector reaches the Payment success screen SMS is sent to HH.
     * SMS 1 - Dear ‘Username’, Paid Rs.X for water charges for bill period \<Cycle>. Download receipt \<link>
     * SMS 2 - Dear ‘Username’, Please leave a review on water supply at \<GP> at \<Link>
     * HH is able to leave a review for water charges. Refer [Feedback - Post Payments](https://ifix.digit.org/exemplar/mgramseva/features/feedback-post-payment)

![](<../../../.gitbook/assets/image (136).png>)

**Details on the card**&#x20;

| Detail           | Comments                                                                                                                                                                                                                                                        |                                                                                                                                      |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Connection ID    | New Connection ID will be displayed here                                                                                                                                                                                                                        |                                                                                                                                      |
| Consumer Name    | Consumer Name (Should take updated consumer name)                                                                                                                                                                                                               |                                                                                                                                      |
| Bill ID number   | ID of the Bill                                                                                                                                                                                                                                                  |                                                                                                                                      |
| Bill period      | <p>For non-metered connections</p><ol><li>This is the latest billing cycle for which demand is generated</li></ol><p>For metered connections</p><ol><li>This is the new bill generated from the meter reading between the 2 most recent billing dates</li></ol> | <p></p><p>Format</p><ol><li>Month &#x3C;space> Financial Year</li><li>Previous meter reading date - New meter reading date</li></ol> |
| Water charges    | Amount for the latest billing cycle                                                                                                                                                                                                                             | For metered, calculate charges as per rate master between the latest 2 billing dates                                                 |
| Arrears          | All old arrears accumulated for HH                                                                                                                                                                                                                              | Expansion should breakup of arrears by individual billing cycles/bill generation dates                                               |
| Total Due amount | Net amount consumer has to pay                                                                                                                                                                                                                                  |                                                                                                                                      |

​![](<../../../.gitbook/assets/image (124).png>)![](<../../../.gitbook/assets/image (35).png>)

* When an online payment method is selected, the “Collect Payment” option is disabled. Since HH scans the QR, the Revenue collector does not have control over the online process.
* The partial amount cannot be greater than the full amount.

_All content on this page by_ [_eGov Foundation_](https://egov.org.in/) _is licensed under a_ [_Creative Commons Attribution 4.0 International License_](http://creativecommons.org/licenses/by/4.0/)_._
