Automated Sign-Up Process Using Selenium

This Python script demonstrates an automated sign-up process for a website using the Selenium framework. Selenium is a popular tool for automating web browser interactions, and this script specifically uses the Chrome WebDriver. The script interacts with web elements, navigates pages, and fills out a registration form on a given website.

Requirements

1. Python: Make sure you have Python installed on your system. The script is written in Python and requires Python 3.x to run.
2. Chrome WebDriver: The script uses the Chrome WebDriver for browser automation. The WebDriver will be automatically managed and installed using the `webdriver_manager.chrome` package.
3. Selenium: Install the Selenium library using the following command:
   ```
   pip install selenium
   ```

Usage

1. Clone or download this repository to your local machine.

2. Navigate to the project directory using the command line.

3. Run the script:
   ```
   python script_name.py
   ```
   Replace `script_name.py` with the actual name of the script file.

4. The script will open a Chrome browser window, navigate to the sign-up page, fill out the registration form, and submit it. You'll see output indicating whether the registration was successful or if an error occurred during the process.

Script Overview

The script defines a class `SignUpPage`, which encapsulates the interactions with the sign-up page's elements. The main actions performed by the script include:

1. Initializing the Chrome WebDriver and maximizing the browser window.
2. Creating an instance of the `SignUpPage` class to manage interactions with the sign-up page.
3. Navigating to the specified sign-up page URL.
4. Clicking the "Sign Up" button.
5. Filling out the registration form fields with test data.
6. Selecting a country and providing a phone number.
7. Agreeing to terms and conditions.
8. Submitting the registration form.
9. Handling exceptions and printing appropriate messages.



