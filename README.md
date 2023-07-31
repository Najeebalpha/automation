Automated Test for Automation Practice Website
Description
This repository contains an automated test script written in Python using Selenium WebDriver to test a website (http://automationpractice.pl/index.php). The script performs several test scenarios, including user login, navigation to the home page, and navigating to the best sellers page. The test assertions verify that the expected page titles are displayed after each action.

Prerequisites
To run the automated test, you need the following software installed on your system:

Python (3.6 or later)
Chrome Web Browser
ChromeDriver (automatically installed using webdriver_manager)


Installation
Clone the repository to your local machine:
git clone https://github.com/yourusername/automation_practice_test.git

Navigate to the project directory:
cd automation_practice_test

Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate


Install the required Python packages:
pip install -r requirements.txt
Running the Test


To execute the automated test, run the following command from the project directory:
python test_automation_practice.py

The script will open a Chrome browser window and perform the test scenarios step by step. It will then print the results of each assertion, indicating whether the tests passed or failed.

Test Results
The test results will be displayed in the console output. Each assertion will be marked as "Assertion passed" if it succeeded or "Assertion failed" if it did not meet the expected condition. If any errors occur during the test execution, relevant error messages will be displayed, helping you identify potential issues.

