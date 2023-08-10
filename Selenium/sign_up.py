from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def navigate_to_sign_up_page(self, url):
        self.driver.get(url)
    
    def click_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()
    
    def type_in_element(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

def main():
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    # Initialize the page object
    sign_up_page = SignUpPage(driver)
    
    try:
        # Navigate to the sign-up page
        sign_up_page.navigate_to_sign_up_page(" https://qa.d1ainun5cjrnni.amplifyapp.com")
        
        # Click the Sign Up button
        sign_up_page.click_element((By.ID, "Sign up"))

        # Fill out the registration form
        sign_up_page.type_in_element((By.ID, "register_firstName"), "Najib")
        sign_up_page.type_in_element((By.ID, "register_lastName"), "Shehu")
        sign_up_page.type_in_element((By.ID, "register_email"), "Najeebshehu6550@gmail.com")
        sign_up_page.type_in_element((By.ID, "register_businessName"), "Naj pal ltd")
        
        # Select country and phone number
        sign_up_page.click_element((By.ID, "rc_select_0"))
        country_option_locator = (By.XPATH, "//div[@data-value='Kenya']")
        sign_up_page.click_element(country_option_locator)
        
        sign_up_page.type_in_element((By.NAME, "phoneNumber"), "8036143565")
        sign_up_page.type_in_element((By.ID, "register_password"), "secure_password")
        sign_up_page.type_in_element((By.ID, "register_confirmPassword"), "secure_password")
        
        # Select subscription plan
        subscription_locator = (By.XPATH, "//label[contains(text(), 'Starter')]/input")
        sign_up_page.click_element(subscription_locator)
        
        # Agree to terms and conditions
        agreement_locator = (By.NAME, "agreement")
        sign_up_page.click_element(agreement_locator)
        
        # Submit the form
        submit_button_locator = (By.XPATH, "//button[@type='submit']")
        sign_up_page.click_element(submit_button_locator)

        print("Registration successful waiting for validation!")

    except Exception as e:
        print("An error occurred:", str(e))

    finally:
        # Close the browser window
        driver.quit()

if __name__ == "__main__":
    main()
