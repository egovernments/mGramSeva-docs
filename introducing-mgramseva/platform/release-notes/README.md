---
description: mGramseva 1.2 Release Notes
---

# Release Notes

## Release Summary <a href="#release-summary" id="release-summary"></a>

mGramSeva 1.2 release features enhancements with a few functional changes and non-functional changes.

* Create and update consumers with the option to pay penalty and advance
* Allow users to collect advance payment
* Penalty amount addition if the due amount is not paid before the due date
* Addition of father/husband column in household register
* Receipt and bill PDF changes based on advance and penalty amount and localization fixes
* Dashboard data and trend graph data mismatch fixes
* **Non-functional:** After flutter upgradation, APK was not working in Android > 12 fixes

## New ‌Feature Additions/Enhancements <a href="#new-feature-additions-enhancements" id="new-feature-additions-enhancements"></a>

<table><thead><tr><th width="242">Feature</th><th>Description</th></tr></thead><tbody><tr><td>Penalty and advance</td><td><ul><li>Penalty and advance features added for consumers (Note: penalty/advance can be disabled from MDMS for a particular tenant)</li></ul></td></tr><tr><td>Collect advance amount</td><td><ul><li>Advance amount collection enabled (Note: Can be disabled from MDMS)</li></ul></td></tr><tr><td>Father/husband column in the household register</td><td><ul><li>Additional column added in Household Register screen and PDF.</li></ul></td></tr><tr><td>Receipt and bill enhancements and fixes</td><td><ul><li>Advance and penalty fields added</li><li>Localisation issue fixed</li></ul></td></tr><tr><td>Dashboard data and graph data mismatch fixes</td><td><ul><li>Due to the data mismatch, from two APIs, for both the graph and table, the data is taken from a single API</li></ul></td></tr><tr><td>APK fixes</td><td><ul><li>APK was showing a white screen in Android > 12, Fixes</li></ul></td></tr></tbody></table>

### Road Map

**The below enhancements in reports and dashboard are addressed for tracking/viewing Advance and Penalty details**

* P[FM-1729](https://digit-discuss.atlassian.net/browse/PFM-1729) [Enhancements in Household Register to display Active/Inactive status, Advance, last demand and to enable sorting](https://digit-discuss.atlassian.net/browse/PFM-1729)
* PFM-1739 Ch[anges in the Monthly collection dashboard to display the Advance adjustment, Advance/Penalty collection and pending penalty](https://digit-discuss.atlassian.net/browse/PFM-1739)
* PFM-[1740](https://digit-discuss.atlassian.net/browse/PFM-1740) Cha[nges in the Main dashboard to display the Advance adjustment, Advance/Penalty collection and pending penalty](https://digit-discuss.atlassian.net/browse/PFM-1740)
* PFM-1[741](https://digit-discuss.atlassian.net/browse/PFM-1741) Roll[out dashboard changes for including Advance penalty details](https://digit-discuss.atlassian.net/browse/PFM-1741)

### Other Enhancements

* [PFM-1728 The old connection ID is to be made mandatory and unique in create/update consumer screen](https://digit-discuss.atlassian.net/browse/PFM-1728)
* PF[M-1730](https://digit-discuss.atlassian.net/browse/PFM-1730) C[reate a new card in the login to display the GPWSC details and the rate info.](https://digit-discuss.atlassian.net/browse/PFM-1730)

### Success Metrics

Primary KPI for overall mGramSeva - [mGramseva Adoption KPI](https://docs.google.com/presentation/d/1Unpd0r\_kds6uM9swdCU4jdfACHkEy-oi/edit#slide=id.g17f4a59bf94\_0\_6)

**Additional:**\
% of consumers paying and GPWSC collecting advance \
% of the advance amount of revenue collected month on month\
\
**Outcomes:**\
\* Increased revenue\
\* Timely payments

## Known Issues

[PFM-1699](https://digit-discuss.atlassian.net/browse/PFM-1699) - [Reactivating the consumer and checking if it is allowing to generate the demand for previous month](https://digit-discuss.atlassian.net/browse/PFM-1699)\
[PFM-1761](https://digit-discuss.atlassian.net/browse/PFM-1761) - [HH Register PDF | Consumer name in Hindi should be fetched in Hindi even if language selected is English.](https://digit-discuss.atlassian.net/browse/PFM-1761)\
[PFM-1671](https://digit-discuss.atlassian.net/browse/PFM-1671) - [Bill and Receipt localization issue not displayed properly for tenant and month name](https://digit-discuss.atlassian.net/browse/PFM-1671)

## Document Resources and Links

<table><thead><tr><th width="304">UI Technical Documents</th><th>Backend Service Documents</th></tr></thead><tbody><tr><td><p></p><ul><li><a data-mention href="../technical-user-docs/mgramseva-ui/">mgramseva-ui</a></li><li><a data-mention href="../technical-user-docs/tech-user-manual/household-register.md">household-register.md</a></li><li><a data-mention href="../technical-user-docs/tech-user-manual/consumer-details/">consumer-details</a></li><li><a data-mention href="../technical-user-docs/tech-user-manual/consumer-details/update-consumer.md">update-consumer.md</a></li><li><a data-mention href="../technical-user-docs/tech-user-manual/dashboards/monthly-dashboard.md">monthly-dashboard.md</a></li><li><a data-mention href="../technical-user-docs/tech-user-manual/collect-payment.md">collect-payment.md</a></li></ul></td><td><p></p><ul><li><a data-mention href="../technical-user-docs/mgramseva-ui/mgramseva-ui/mgramseva-penalty-changes.md">mgramseva-penalty-changes.md</a></li><li><a data-mention href="../technical-user-docs/mgramseva-ui/mgramseva-ui/mgramseva-advance-changes.md">mgramseva-advance-changes.md</a></li></ul></td></tr></tbody></table>

