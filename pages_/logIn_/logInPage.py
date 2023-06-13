import time

from selenium import webdriver
from pages_.basePage import BasePage
from selenium.webdriver.common.by import By

class LogInPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super(LogInPage, self).__init__(driver)
        self.__usernameFieldLocator = (By.ID, 'ap_email')
        self.__continueButtonLocator = (By.ID, 'continue')
        self.__passwordFieldLocator = (By.ID, 'ap_password')
        self.__signInButtonLocator = (By.ID, 'signInSubmit')
        self.__errorMessageThereWasAProblemLocator = (By.XPATH, "//h4[@class='a-alert-heading' and text()='There was a problem']")
        self.__errorMessageYourPasswordIsIncorrectLocator = (By.CLASS_NAME, 'a-list-item')

    def fill_login_field(self, username):
        usernameFieldElement = self._find_element(self.__usernameFieldLocator)
        self._fill_field(usernameFieldElement, username)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        self._click_to_element(continueButtonElement)

    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        self._fill_field(passwordFieldElement, password)

    def click_to_sign_in_button(self):
        signInButtonElement = self._find_element(self.__signInButtonLocator)
        self._click_to_element(signInButtonElement)

    def validate_incorrect_password_alert(self):
        assert self._get_element_text_by_locator(self.__errorMessageThereWasAProblemLocator) == "There was a problem"
        assert self._get_element_text_by_locator(self.__errorMessageYourPasswordIsIncorrectLocator) == "Your password is incorrect"

    def quick_log_in(self):
        from testData_ import testData
        self.fill_login_field(testData.loginDataValidSona["username"])
        self.click_to_continue_button()
        self.fill_password_field(testData.loginDataValidSona["password"])
        time.sleep(3)
        self.click_to_sign_in_button()
