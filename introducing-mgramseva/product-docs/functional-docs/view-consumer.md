# View Consumer

## Overview

1. Users are redirected to the View Consumer screen from the home screen via
   * Collect payments → Search Screen → Consumer Details Screen
   * Download bills & receipts → Search screen → Consumer Details Screen
   * Dashboard → Collections → Click on Consumer ID
   * Household Register → Click on Consumer ID
2. This screen contains all information related to HH

Static HH card displays the following details

1. New Connection ID (also displayed as a heading)
2. Consumer name
3. Father's name
4. Phone number
5. Old connection ID
6. Address - Door Number, Street number, Ward (attached)
7. Property type
8. Service type
   * for metered connections - the meter number is displayed

## **For Non-Metered Connection**

1. If the bill is not generated (Post rollout until the first month)
   * Only the data Card is shown - No action is required  &#x20;
2. Once the first demand is generated - A new consumer bill/card gets generated and displays the following data points and actions -
   * &#x20;Billing cycle – the latest billing cycle
     * Amount -&#x20;
       * Current Amount - fixed charges applicable to the billing cycle
       * Arrears - Arrears from the first month (From next month onwards this field displays any unpaid dues)
       * Total Amount - Sum of current amount and arrears
     * Action Items
       * Download or Share Bill
         * Clicking on download bill prompts users to download the bill (Bill details are given in a separate user story)
         * Share bill (WhatsApp icon) opens sharing options to the phone OS and the user is able to share bills via WhatsApp
         * Message to go in WhatsApp “Please find Bill for water charges with Connection ID WS-83121-8312 generated on dd/mm/yyyy” along with bill PDF
         * Name of the PDF - “Bill ID”
       * Collect Payment
         * The Collect payment button takes the revenue collector to the payment collection screen
3. After the First payment collection is done
   * A receipt history block is visible only after the first payment transaction is completed through mGramSeva
     * A list of all the receipts is shown under this section as cards, with different data points as actions. Order of receipts is newest → oldest from top to bottom
     * Each receipt card contains
       * Receipt ID
       * Amount Paid
       * Paid Date
     * Actions
       * Download Receipt - downloads the receipt in the Revenue collectors phone as a PDF
         * Name of PDF - “Receipt ID”
       *   Share (WhatsApp)

           * Message to go in WhatsApp “Please find the receipt for water charges with Connection ID WS-83121-8312 paid on dd/mm/yyyy” along with receipt PDF



![](<../../../.gitbook/assets/image (19).png>)

New Connection Before First Bill Generation

![](<../../../.gitbook/assets/image (137).png>)

First bill is generated - Payment Collection is pending

![](<../../../.gitbook/assets/image (145).png>)

2 payments made

## For Metered Connection

1. If a bill is not generated (Post rollout until the first month)
   * A data card is displayed on the screen
   * Below the data card - the Card to generate a new bill is also displayed
   * This card contains
     * Last bill generation date - For the first time this is picked up from data entry. Next time onwards the system captures the last bill generation date
     * Days from last bill generation date - indicates to the revenue collector the number of days passed since the last time a bill is generated
     * Previous Meter reading - Displays the last read meter units&#x20;
     * Pending Amount
       * Before the first bill is generated, the arrears are captured during data entry
       * After the first bill is generated, the pending amount includes the entire amount due for the specific user
     * Generate a new bill
       * Clicking on Generate a New Bill initiates bill generation flow for metered connection
     * <mark style="background-color:blue;">Note - Users have to generate a bill to start collecting payments. Arrear amount collection also is not possible till the first bill is generated.</mark>&#x20;
2. After the first bill is generated
   * A new consumer bill/card gets generated with the following data points and actions
     * Last bill generation date - date of bill generation
       * Amount -
         * Current Amount - Volumetric charges between 2 latest meter readings according to rate master
         * Arrears - All previously unpaid dues
       * Total Amount - Sum of current amount and arrears
     * Action Items
       * Download, Share Bill
         * Clicking on the download bill prompts users to download the bill for the respective amount (Bill details are given in a separate user story)
         * Share bill (WhatsApp icon) opens the sharing options of the phone OS and the users can share bill via WhatsApp
         * Message to go in WhatsApp “ Please find Bill for water charges with Connection ID WS-83121-8312 generated on dd/mm/yyyy” along with bill PDF
         * Name of the PDF - “Bill ID”
       * Collect Payment
         * Collect payment takes the revenue collector to the payment collection screen
3. After the first payment collection is done
   * A receipt history block is visible only after the first payment happens through mGramSeva
   * A list of all the receipts is shown under this section as cards, with different data points as actions. Order of receipts is newest → oldest from top to bottom
   * Each receipt card contains
     * Receipt ID
     * Amount Paid
     * Paid Date
   * Actions
     * Download Receipt - downloads the receipt to the revenue collectors phone as a PDF
       * Name of PDF - “Receipt ID”
     * Share(WhatsApp)
       * Message to go in WhatsApp “ Please find receipt for water charges with Connection ID WS-83121-8312 paid on dd/mm/yyyy” along with receipt PDF
4. If a new bill is generated again by clicking on ‘Generate a new bill’ - the revenue collector goes through the bill generation flow and a single new card appears between ‘Generate bill’ and ‘Consumer receipts block’

<img src="../../../.gitbook/assets/image (2).png" alt="" data-size="original">![](<../../../.gitbook/assets/image (111).png>)

![](<../../../.gitbook/assets/image (119).png>)



[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/80x15.png)_​_](http://creativecommons.org/licenses/by/4.0/)_All content on this page by_ [_eGov Foundation_](https://egov.org.in/) _is licensed under a_ [_Creative Commons Attribution 4.0 International License_](http://creativecommons.org/licenses/by/4.0/)_._
