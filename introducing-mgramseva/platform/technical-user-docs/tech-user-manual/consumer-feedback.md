# Consumer Feedback

## Overview

Users can provide their feedback by giving a rating. It's an Open URL. It doesn’t require any Authentication user.

**Link** → {baseURL}mgramseva/feedBack?paymentId={}\&connectionno={}\&tenantId={}

![](<../../../../.gitbook/assets/image (101).png>)

Users can switch to multiple languages.

After submitting the feedback, users are navigated to the feedback submitted successfully acknowledgement screen.

## **API Details**

| API                              | Params                                                                                                                                                                                                                                                                                                                                          | Description                 |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `ws-services/wc/_submitfeedback` | <p><code>connectionno</code>,<code>paymentId</code>,</p><p><code>tenantId</code></p><p><code>additionaldetails":{"CheckList":[{"code":"HAPPY_WATER_SUPPLY","type":"SINGLE_SELECT","value":"3"},{"code":"WATER_QUALITY_GOOD","type":"SINGLE_SELECT","value":"5"},{"code":"WATER_SUPPLY_REGULAR","type":"SINGLE_SELECT","value":"5"}]}</code></p> | API to submit user feedback |

