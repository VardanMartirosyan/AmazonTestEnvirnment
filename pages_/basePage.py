from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from common_.utilities_.customLogger import *


class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver


    def _find_element(self, locator):
        if self._is_element_visible(locator):
            element = self.driver.find_element(*locator)
            return element
        else:
            print("ELEMENT NOT FOUND")
            exit(5)

    def _is_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def _elementy_should_be_visible(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except:
            print("ERROR: Element not visible but should be")
            exit(3)

    def _get_title(self):
        return self.driver.title

    def _fill_field(self, element, text):
        element.clear()
        element.send_keys(text)
        # loger.log("Info", "successful;lly added text to element")

    def _mouse_move(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def _click_to_element(self, webElement):
        webElement.click()

    def _drag_and_drop(self):
        #Action Chain
        pass

    def _press_and_hold(self):
        pass

    def _get_element_text(self, webElement):
        return webElement.text

    def _get_element_text_by_locator(self, locator):
        element = self._find_element(locator)
        return element.text

    def _double_click(self):
        pass
