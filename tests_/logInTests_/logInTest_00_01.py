import time
import unittest
from testData_ import testData
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages_.logIn_.logInPage import LogInPage
from pages_.navigationBar_.navigationBar import NavigationBar


class TestLogIn(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(testData.urlSignIn)

    def test_logIn(self):
        """
        test Amazon Log in with valid data
        :return:
        """
        self.logInPageObj = LogInPage(self.driver)
        self.logInPageObj.fill_login_field(testData.loginDataValidSona["username"])
        self.logInPageObj.click_to_continue_button()
        self.logInPageObj.fill_password_field(testData.loginDataValidSona["password"])
        time.sleep(5) # Added sleep time to avoid captcha from amazon
        self.logInPageObj.click_to_sign_in_button()

        self.navigationBarObj = NavigationBar(self.driver)
        self.assertNotEqual(self.navigationBarObj.get_welcome_username_from_accounts_and_lists(), "Hello, sign in")

    def test_logIn_with_invalid_password(self):
        self.logInPageObj = LogInPage(self.driver)
        self.logInPageObj.fill_login_field(testData.loginDataWithInvalidPassword["username"])
        self.logInPageObj.click_to_continue_button()
        self.logInPageObj.fill_password_field(testData.loginDataWithInvalidPassword["password"])
        time.sleep(3) # Added sleep time to avoid captcha from amazon
        self.logInPageObj.click_to_sign_in_button()

        self.logInPageObj.validate_incorrect_password_alert()


    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

