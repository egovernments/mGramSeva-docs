---
description: 'Sample of SMS present in mgramseva product :'
---

# SMS Template

The below SMS needs to be registered with a specific TEMPLATE ID(Eg.'100700746377980') for each **Localization key**

Append the TEMPLATE ID at the end of the message.&#x20;

Push the SMS templates in Localisation.

| Action                      | Localization key                    | Localization message                                                                                                                                                                                                         |
| --------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  First time login OTP       | RESET\_PASSWORD\_FIRST\_TIME\_OTP   | OTP to reset password on NalJal is {otp}                                                                                                                                                                                     |
| Forgot Password OTP         | RESET\_PASSWORD\_OTP                | OTP to reset password on NalJal is {otp}                                                                                                                                                                                     |
| Creation login details      | MGram.User.Invitation               | Dear {USER}, You've been invited to NalJal Application. Please login using {LINK}. Username: {PHNO} Password: {PASSWORD}                                                                                                     |
| Demand (Bulk)               | mGram.GP.MonthlyDemandGenerated     | Dear {ownername}, Demand for Billing Cycle {billingcycle} has been generated for {tenant -name}. Kindly plan for collection of Water Charges for this period. {LINK} DWSS                                                    |
| Pending Collection Reminder | mGram.GPUser.CollectionReminder     | Dear {ownername}, Rs.{amount} is pending collections against Water Charges at {WIMC} as of {Date}. Click {PENDING\_COL\_LINK} to see more details. DWSS                                                                      |
| New Calendar Month          | mGram.GPUser.PreviousMonthSummary   | Dear {user}, Rs.{PREVIOUS\_MONTH\_COLLECTION} has been collected in {PREVIOUS\_MONTH} against water charges & Rs.{PREVIOUS\_MONTH\_EXPENSE} has been spent as expenditure for {WIMC}. Click {LINK} to see more details. DWSS |
| Fortnight                   | NEW\_ENPENDITURE\_SMS\_EN\_REMINDER | Please enter new expenditure bills online for {WIMC}. Click {NEW\_EXP\_LINK} to make an expense entry now. DWSS                                                                                                              |
| Alternate Fortnight         | MARK\_PAID\_BILL\_SMS\_EN\_REMINDER | Expenditure bills for {WIMC} are awaiting payment confirmation. Please click {EXP\_MRK\_LINK} and mark them as paid, if paid already. DWSS                                                                                   |
| Demand (Bulk) - (NM & M)    | mGram.Consumer.NewBill              | Dear {ownername}, New water bill for Billing Cycle {Period} has been generated for Consumer Id {consumerno} for Rs.{billamount}. Click {BILL\_LINK} to download latest bill. DWSS                                            |
| Demand (Bulk) - (NM & M)-1  | mGram.consumer.payment.message      | Dear {ownername}, Pending Amount for water charges for Consumer Id {connectionno} is Rs.{billamount}. Click {PAY\_LINK} to pay online. DWSS                                                                                  |
| Bill Paid                   | Gram.Consumer.DownloadReceipt       | Dear {ownername}, Rs.{amountpaid} has been paid for Water Charges for Consumer Id {consumercode}. Pending Amount is Rs.{pendingamount}. Click {RECEIPT\_LINK} to Download Receipt. DWSS                                      |
| Feedback Collection         | mGram.Consumer.TakeSurvey           | Dear {ownername}, Thank you for paying water charges. Please take this short survey {SURVEY\_LINK} and help us know more about water supply at {WIMC}. DWSS                                                                  |
