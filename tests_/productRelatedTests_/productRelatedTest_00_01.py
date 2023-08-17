import unittest

from testData_ import testData
from common_.utilities_.customLogger import *

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages_.logIn_.logInPage import LogInPage
from pages_.navigationBar_.navigationBar import NavigationBar
from pages_.productsRelatedPages_.searchResultPage import SearchResultPage
from pages_.productsRelatedPages_.productDetailsPage import ProductDetailsPage


from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from common_.utilities_.customListener import MyListener

class ProductRelatedTest(unittest.TestCase):
    def setUp(self) -> None:
        self.simpleDriver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver = EventFiringWebDriver(self.simpleDriver, MyListener())
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(testData.urlSignIn)
        loginPageObj = LogInPage(self.driver)
        loginPageObj.quick_log_in()


    def test_search_product_and_add_to_cart(self):
        """
        test Amazon search product then add product to cart
        :return:
        """
        navigationBarObj = NavigationBar(self.driver)
        navigationBarObj.fill_search_field("AGV K1 helmet")
        navigationBarObj.click_to_search_button()

        searchResultPageObj = SearchResultPage(self.driver)
        searchResultPageObj.click_to_first_product()

        # Get card products quanitity for validation
        cartPreviewsQuantity = navigationBarObj.get_cart_product_quantity()
        productDetailsPageObj = ProductDetailsPage(self.driver)
        productDetailsPageObj.click_to_add_to_cart_button()
        cartCurrentQuantity = navigationBarObj.get_cart_product_quantity()

        # Validate then after adding product to card then cart products count should be encrised by 1
        self.assertEqual(cartPreviewsQuantity + 1, cartCurrentQuantity)


    def tearDown(self) -> None:
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

