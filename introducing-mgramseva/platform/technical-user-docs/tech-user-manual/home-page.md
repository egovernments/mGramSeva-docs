# Home Page

## Overview

Users are redirected to the home page screen after successful login. ​ This screen consists of multiple sections and user interactions. If the user is mapped to multiple tenants then a dropdown appears. The user can select the desired tenant to proceed further. Once the user selects the tenant, the feature cards are displayed on the screen based on the roles mapped for the selected tenant.

## **First Time Login**

YES → WalkThrough/User Guidance Enabled

NO → Home Screen

![](<../../../../.gitbook/assets/image (38).png>)

If the user logs in for the first time a system walkthrough begins automatically.

Else, users can view walkthroughs at any time by clicking on the help icon.

### **Logic Implemented For Walkthrough**

****![](<../../../../.gitbook/assets/image (114).png>)****

Create a global key for each card.

Create placeholder cards, pointers and description widgets.

On click, the position of the card is determined and the placeholder card appears on the overlay exactly.

### **Files Path**

Primary Files

[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/HomeWalkThroughContainer.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/Home/HomeWalkThrough/HomeWalkThroughContainer.dart),

[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/Home/HomeWalkThrough/HomeWalkThroughList.dart)[punjab-mgramseva/HomeWalkThroughList.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/Home/HomeWalkThrough/HomeWalkThroughList.dart)

Next → Changes the active index of the global key and repeat the same process outlined in the implementation logic

skip, End → closes the overlay

Home Screen - consists of multiple feature cards

Cards are displayed based on Role Access

## Notifications

The home screen also consists of notifications. The notifications are customized for each user ID and user role.

### **Logic Implemented For Notifications**

Individual API calls are made with the user ID and with the user role that merges both and notifications are displayed accordingly.

****![](<../../../../.gitbook/assets/image (140).png>)****

### **Files Path**

Primary Files[ <img src="https://github.com/fluidicon.png" alt="" data-size="line">punjab-mgramseva/Home.dart at develop · egovernments/punjab-mgramseva](https://github.com/egovernments/punjab-mgramseva/blob/develop/frontend/mgramseva/lib/screeens/Home/Home.dart)

