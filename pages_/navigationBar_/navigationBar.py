from selenium.webdriver.common.by import By
from pages_.basePage import BasePage

class NavigationBar(BasePage):
    def __init__(self, driver):
        super(NavigationBar, self).__init__(driver)
        self.__usernameFromAccountsAndListsLocator = (By.ID, 'nav-link-accountList-nav-line-1')
        self.__searchFieldLocator = (By.ID, 'twotabsearchtextbox')
        self.__searchButtonLocator = (By.ID, 'nav-search-submit-button')
        self.__cartProductsQuantityLocator = (By.ID, 'nav-cart-count')

    def get_welcome_username_from_accounts_and_lists(self):
        self._elementy_should_be_visible(self.__usernameFromAccountsAndListsLocator)
        element = self._find_element(self.__usernameFromAccountsAndListsLocator)
        text = self._get_element_text(element)
        return text

    def fill_search_field(self, text="AGV K3 Helmet"):
        searchFieldElement = self._find_element(self.__searchFieldLocator)
        self._fill_field(searchFieldElement, text)

    def click_to_search_button(self):
        searchButtonElement = self._find_element(self.__searchButtonLocator)
        self._click_to_element(searchButtonElement)

    def get_cart_product_quantity(self):
        return int(self._get_element_text_by_locator(self.__cartProductsQuantityLocator))


