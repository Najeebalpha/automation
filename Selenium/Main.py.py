from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAutomationPractice:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def open_website(self):
        self.driver.get("http://automationpractice.pl/index.php")

    def sign_in(self, username, password):
        signin_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        signin_button.click()

        username_field = self.wait.until(EC.visibility_of_element_located((By.ID, "email")))
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "passwd")
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

    def go_to_home(self):
        home_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header_logo"]/a')))
        home_link.click()

    def go_to_best_seller(self):
        best_seller_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="home-page-tabs"]/li[2]/a')))
        best_seller_tab.click()

    def test_sign_in_and_navigation(self):
        try:
            self.open_website()

            username = "Najib@yopmail.com"
            password = "EOi8bdHZ"
            self.sign_in(username, password)

            # Assert the title after logging in
            assert "My Shop" in self.driver.title, "Title after logging in is not 'My Shop'."
            print("Title after logging in is 'My Shop'. Assertion passed.")

            self.go_to_home()
            assert "My Shop" in self.driver.title, "Home page title mismatch."
            print("Home page title is 'My Shop'. Assertion passed.")

            self.go_to_best_seller()
            assert "My Shop" in self.driver.title, "Best Sellers page title mismatch."
            print("Best Sellers page title is 'My Shop'. Assertion passed.")

            # Add more test steps and assertions as needed for other scenarios.

            print("All assertions completed successfully.")
        except AssertionError as e:
            print(f"Assertion failed: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    test = TestAutomationPractice()
    test.test_sign_in_and_navigation()
