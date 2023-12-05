# Setup Git Repository

## Overview

This page provides step-by-step details on setting up a git repo for code, configs, V1 MDMS, and Infra As Code.

## Steps

Fork the following repos that contain the master data and default configurations. Customize the data (master data, ULB, Tenant details, Users, etc) as per specific implementation requirements in the respective GitHub organization accounts.

Follow the steps given below to setup the git repository,

* ​[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) both the [MDMS](https://github.com/egovernments/egov-mdms-data/tree/UAT), and [config](https://github.com/egovernments/configs/tree/UAT) repos into your GitHub organization account.
* Create a [GitHub user account](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account), and generate an ssh authentication key ([generate a new SSH key ](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)and [add it to the above user account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
* Enable new GitHub users to access the forked repos.
* Add the ssh private key generated in the previous step to the [egov-demo-secrets.yaml](https://github.com/egovernments/DIGIT-DevOps/blob/release/config-as-code/environments/egov-demo-secrets.yaml#L36) within the git-sync section.
* Update the services in the git-sync repository by specifying the forked repository and branch in the [egov-demo.yaml](https://github.com/egovernments/DIGIT-DevOps/blob/release/config-as-code/environments/egov-demo.yaml#L263-L339) file.

```
/DIGIT-DevOps/config-as-code/environments/egov-demo-secrets.yaml
```

* Update the deployment configuration details for the below as per your specifications:
  1. Number of replicas/scale of each service (depending on whether dev or prod load)
  2. You must update the SMS gateway, email gateway, and payment gateway details for the notification and payment gateway services, etc.
  3. Update the config and MDMS GitHub repos wherever marked.
  4. Update GMap key (In case you are using Google Map services in your PGR, PT, TL, etc)
  5. Create one private S3 bucket for Filestore and one public bucket for logos. Add the bucket details respectively and create an IAM user with the s3 bucket access. Add IAM user details to [\<env-secrets.yaml>](https://github.com/egovernments/DIGIT-DevOps/blob/release/config-as-code/environments/egov-demo-secrets.yaml).
  6. URL/DNS on which DIGIT will be exposed.
  7. SSL certificate for the above URL.
  8. Any specific endpoint configurations (Internal/external).

```
/DIGIT-DevOps/config-as-code/environments/egov-demo.yaml
```
