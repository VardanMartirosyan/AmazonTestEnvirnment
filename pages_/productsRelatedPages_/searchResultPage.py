from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class SearchResultPage(BasePage):
    def __init__(self, driver):
        super(SearchResultPage, self).__init__(driver)
        self.__firstProductLocator = (By.XPATH, "(//span[@class='a-size-base-plus a-color-base a-text-normal'])[1]")

    def click_to_first_product(self):
        firstProductElement = self._find_element(self.__firstProductLocator)
        self._click_to_element(firstProductElement)
