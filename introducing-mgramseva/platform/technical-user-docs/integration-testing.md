# Integration Testing

## About Integration Testing

Integration testing (also called end-to-end testing or GUI testing) is used to simulate a user interacting with your app by doing things like clicking buttons, selecting items, scrolling items, etc.\
Integration testing is used to test how individual pieces work together as a whole or capture the performance of an application running on a real device.

![](<../../../.gitbook/assets/image (110).png>)

## **Plugins Used**

integration\_test

## **Integration Test Setup**

![](<../../../.gitbook/assets/image (95).png>)

We declared the integration\_test package in pubspec.yaml as shown in the img above.

![](<../../../.gitbook/assets/image (46).png>)

* The test\_driver directory contains the integration\_test\_driver.dart file. (The folder structure is shown in image above). The integration driver is called from this file.
* The integration\_test directory contains the test script files of different screens. &#x20;
* The Test Inputs directory contains the test\_inputs.dart file. This file has the user actions inputs in json format. We can change user actions in this file.&#x20;

## **Integration Test Run**

There are two ways to start the integration testing**:**

* To run the integration test on virtual emulator / mobile, run the command on your terminal :\
  `cd ./frontend/mgramseva && flutter drive --driver=test_driver/integration_test_driver.dart`\
  `--target=integration_test/login_test.dart` ****&#x20;

(...or...)

* Go to `./frontend/mgramseva/utils/execute_integration.sh` and run the `execute_integration.sh` file on the virtual emulator / mobile. The integration test will start.

## **File Path**

User actions Inputs - `.frontend/mgramseva/integration_test/Test Inputs/test_inputs.dart`

Integration Test Driver - `.frontend/mgramseva/test_driver/integration_test_driver.dart`

Execute Integration Test - `.frontend/mgramseva/utils/execute_integration.sh`

## **Reference Links**

{% embed url="https://docs.flutter.dev/cookbook/testing/integration/introduction" %}



[![Creative Commons License](https://i.creativecommons.org/l/by/4.0/80x15.png)_​_](http://creativecommons.org/licenses/by/4.0/)_All content on this page by_ [_eGov Foundation_](https://egov.org.in/) _is licensed under a_ [_Creative Commons Attribution 4.0 International License_](http://creativecommons.org/licenses/by/4.0/)_._
