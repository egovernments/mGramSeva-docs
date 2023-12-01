---
description: Domain or subdomain registry and mapping cname
---

# Domain Name Configuration

Add AWS load balancer or gateway url as cname entry in domain DNS

External IP will come from the AWS load balancer or gateway

**Introduction**

The domain name is the address through which the internet users can access the website rather than entering the whole IP address in the search bar of the browser.

This domain name is ideally chosen by the state/client since it is a product that has to be used for/by them.

**Data Table**

Following is the table through which the information can be shared.

| Sr. No. | Domain Name                                                                                           | EXTERNAL-IP              |
| ------- | ----------------------------------------------------------------------------------------------------- | ------------------------ |
| 1.      | [mgramseva-dwss.punjab.gov.in/](http://127.0.0.1:5000/o/-MEQmzNGXk5ajuZujG7E/s/zX7FRGf1qVY4f9GG5VhS/) | <p><br>3.108.166.195</p> |

Note: The data given in the table is sample data.

## Procedure <a href="#procedure" id="procedure"></a>

Since all state governments/clients prefer to host the websites on their servers, this activity is ideally done by them.

### Data Definition <a href="#data-definition" id="data-definition"></a>

| Sr. No.                       | Column Name | Data Type    | Data Size | Is Mandatory? | Description                                                              |
| ----------------------------- | ----------- | ------------ | --------- | ------------- | ------------------------------------------------------------------------ |
| <ol start="1"><li> </li></ol> | Domain Name | Alphanumeric | 253       | Yes           | The name/address of the website being used to access the website/ module |
| <ol start="1"><li> </li></ol> | EXTERNAL-IP | Alphanumeric | 32        | Yes           | It is the IP address that has to be mapped to the domain name            |

### Steps to Fill Data <a href="#steps-to-fill-data" id="steps-to-fill-data"></a>

Following are the steps which are to be followed:

1. Download the data template attached to this page.
2. Get a good understanding of all the headers in the template sheet, their data type, size, and definitions by referring to the ‘Data Definition’ section of this document.
3. In case of any doubt, please reach out to the person who has shared this template with you to discuss and clear your doubts.
4. If the state agrees to host the website on their server, provide them with the 2 columns mentioned in the attached template.
5. If the state disagrees to host on their server, then a domain name has to be purchased by any of the external vendors and the EXTERNAL-IP address has to be mapped with them.
6. Verify the data once again by going through the checklist and making sure that each and every point mentioned in the checklist is covered.

## Checklist <a href="#checklist" id="checklist"></a>

This checklist covers all the activities that are common across the entities.

| Sr. No. | Checklist Parameter                                                                | Example                                                                         |
| ------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| 1       | Make sure that each and every point in this reference list has been taken care of. | [Checklist](https://digit-discuss.atlassian.net/wiki/spaces/DO/pages/502203140) |

## Attachments <a href="#attachments" id="attachments"></a>

Following is the attached configurable data template in case the state is doing the required activities.

1. Configurable Data Template - Domain Name Configuration

{% file src="../../../.gitbook/assets/Configurable Data Template Domain Name_V1.xlsx" %}

2. Sample Configurable Data - Domain Name Configuration

{% file src="../../../.gitbook/assets/Configurable Sample Data Domain Name_V1.xlsx" %}
