---
description: Sample of SMS present in mGramSeva application
---

# SMS Template

## Overview

This page provides details on how to register the SMS templates with the specified TEMPLATE ID for each Localization key and append the TEMPLATE ID at the end of the message in the Localization system.

## Steps

To register the provided SMS templates with a specific TEMPLATE ID for each Localization key and append the TEMPLATE ID at the end of the message

The sample SMS messages in the table below have to be registered with a specific TEMPLATE ID (Eg.'100700746377980') for each **Localization key.**

Append the TEMPLATE ID at the end of the message.&#x20;

Push the SMS templates in Localisation.

<table><thead><tr><th width="193">Action</th><th width="225">Localization key</th><th>Localization message</th></tr></thead><tbody><tr><td> First time login OTP</td><td>RESET_PASSWORD_FIRST_TIME_OTP</td><td>OTP to reset password on NalJal is {otp}</td></tr><tr><td>Forgot Password OTP</td><td>RESET_PASSWORD_OTP</td><td>OTP to reset password on NalJal is {otp}</td></tr><tr><td>Creation login details</td><td>MGram.User.Invitation</td><td>Dear {USER}, You've been invited to NalJal Application. Please login using {LINK}. Username: {PHNO} Password: {PASSWORD}</td></tr><tr><td>Demand (Bulk)</td><td>mGram.GP.MonthlyDemandGenerated</td><td>Dear {ownername}, Demand for Billing Cycle {billingcycle} has been generated for {tenant -name}. Kindly plan for collection of Water Charges for this period. {LINK} DWSS</td></tr><tr><td>Pending Collection Reminder</td><td>mGram.GPUser.CollectionReminder</td><td>Dear {ownername}, Rs.{amount} is pending collections against Water Charges at {WIMC} as of {Date}. Click {PENDING_COL_LINK} to see more details. DWSS</td></tr><tr><td>New Calendar Month</td><td>mGram.GPUser.PreviousMonthSummary</td><td>Dear {user}, Rs.{PREVIOUS_MONTH_COLLECTION} has been collected in {PREVIOUS_MONTH} against water charges &#x26; Rs.{PREVIOUS_MONTH_EXPENSE} has been spent as expenditure for {WIMC}. Click {LINK} to see more details. DWSS</td></tr><tr><td>Fortnight</td><td>NEW_ENPENDITURE_SMS_EN_REMINDER</td><td>Please enter new expenditure bills online for {WIMC}. Click {NEW_EXP_LINK} to make an expense entry now. DWSS</td></tr><tr><td>Alternate Fortnight</td><td>MARK_PAID_BILL_SMS_EN_REMINDER</td><td>Expenditure bills for {WIMC} are awaiting payment confirmation. Please click {EXP_MRK_LINK} and mark them as paid, if paid already. DWSS</td></tr><tr><td>Demand (Bulk) - (NM &#x26; M)</td><td>mGram.Consumer.NewBill</td><td>Dear {ownername}, New water bill for Billing Cycle {Period} has been generated for Consumer Id {consumerno} for Rs.{billamount}. Click {BILL_LINK} to download latest bill. DWSS</td></tr><tr><td>Demand (Bulk) - (NM &#x26; M)-1</td><td>mGram.consumer.payment.message</td><td>Dear {ownername}, Pending Amount for water charges for Consumer Id {connectionno} is Rs.{billamount}. Click {PAY_LINK} to pay online. DWSS</td></tr><tr><td>Bill Paid</td><td>Gram.Consumer.DownloadReceipt</td><td>Dear {ownername}, Rs.{amountpaid} has been paid for Water Charges for Consumer Id {consumercode}. Pending Amount is Rs.{pendingamount}. Click {RECEIPT_LINK} to Download Receipt. DWSS</td></tr><tr><td>Feedback Collection</td><td>mGram.Consumer.TakeSurvey</td><td>Dear {ownername}, Thank you for paying water charges. Please take this short survey {SURVEY_LINK} and help us know more about water supply at {WIMC}. DWSS</td></tr></tbody></table>
