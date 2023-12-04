---
description: Setting up git repo for code, configs,V1 mdms, Infra As Code
---

# Setting up Git Repository

Fork the following repos that contain the master data and default configs which you would customize as per your specific implementation later. Like (Master Data, ULB, Tenant details, Users, etc) to your respective GitHub organization account.

* ​[fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) both the [mdms](https://github.com/egovernments/egov-mdms-data/tree/UAT), and [config](https://github.com/egovernments/configs/tree/UAT) repos into your GitHub organization account
* Once you fork the repos into your GitHub organization account, Create a [github user account](https://docs.github.com/en/get-started/signing-up-for-github/signing-up-for-a-new-github-account), and generate an ssh authentication key( [generate new SSH key ](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)and [add it to above user account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
* New GitHub users should be enabled to access the earlier forked repos
* Add the ssh private key that you generated in the previous step to [egov-demo-secrets.yaml](https://github.com/egovernments/DIGIT-DevOps/blob/release/config-as-code/environments/egov-demo-secrets.yaml#L36) under the git-sync section.
* Modify the services git-Sync repo and branch with your fork repo and branch in [egov-demo.yaml](https://github.com/egovernments/DIGIT-DevOps/blob/release/config-as-code/environments/egov-demo.yaml#L263-L339)

```
/DIGIT-DevOps/config-as-code/environments/egov-demo-secrets.yaml
```

Update the deployment configs for the below as per your specifications:

1. Number of replicas/scale of each individual service (Depending on whether dev or prod load)
2. You must update SMS gateway, email gateway, and payment gateway details for the notification and payment gateway services, etc.
3. Update the config, MDMS github repos wherever marked
4. Update GMap key (In case you are using Google Map services in your PGR, PT, TL, etc)
5. Create one private S3 bucket for Filestore and one public bucket for logos. Add the bucket details respectively and create an IAM user with the s3 bucket access. Add IAM user details to [\<env-secrets.yaml>](https://github.com/egovernments/DIGIT-DevOps/blob/release/config-as-code/environments/egov-demo-secrets.yaml).
6. URL/DNS on which the DIGIT will be exposed.
7. SSL certificate for the above URL.
8. Any specific endpoint configs (Internal/external)

```
/DIGIT-DevOps/config-as-code/environments/egov-demo.yaml
```
