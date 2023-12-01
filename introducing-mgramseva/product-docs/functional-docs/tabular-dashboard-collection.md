# Tabular Dashboard - Collection

## Overview

Clicking on the Dashboard on the home screen navigates the user to the revenue dashboard view for the current month. This provides a tabular view of the list of consumer records.

## Data Points

The following data points/actions are needed on the screen -

<table data-header-hidden><thead><tr><th width="331">Item</th><th>Explanation</th></tr></thead><tbody><tr><td>Search Consumer records</td><td><ul><li>Search by name or connection ID</li><li>Name should be a partial match. As the user starts typing a consumer name, respective consumers get filtered in the table displayed below</li><li>Connection ID should be a partial match. This is the new connection ID. As the user starts typing a New connection ID, respective consumers get filtered in the table displayed below</li></ul></td></tr><tr><td>Filters</td><td><ul><li>Default is “All” View. Switching to Residential or commercial filters table accordingly. Alongside the filter, how many consumers fall into that filter is shown in numbers</li><li>The table also has sort options for each column (ascending, descending)</li></ul></td></tr><tr><td>Columns</td><td><ul><li><p>Connection ID</p><ul><li>New Connection ID of the consumer- this should be clickable, and take users to the HH details page</li><li>A metered connection should have “M” in a ⭕️ that is followed across as standard for metered connection</li></ul></li><li><p>Name</p><ul><li>name of the consumer. Show until 20 Characters and truncate by showing 3 dots if the name is longer</li></ul></li><li>Collections - Amount paid by the user in that month</li></ul></td></tr></tbody></table>

![](<../../../.gitbook/assets/image (68).png>)

> [![Creative Commons License](https://i.creativecommons.org/l/by/4.0/80x15.png)_​_](http://creativecommons.org/licenses/by/4.0/)_All content on this page by_ [_eGov Foundation_](https://egov.org.in/) _is licensed under a_ [_Creative Commons Attribution 4.0 International License_](http://creativecommons.org/licenses/by/4.0/)_._
