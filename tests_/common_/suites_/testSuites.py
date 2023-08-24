import unittest
from tests_.logInTests_.logInTest_00_01 import TestLogIn
from tests_.productRelatedTests_.productRelatedTest_00_01 import ProductRelatedTest


class TestSuites():
    def get_smoke_suite(self):
        pass

    def get_regression_suite(self):
        pass

    def get_performance_suite(self):
        pass

    def get_random_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(ProductRelatedTest('test_search_product_and_add_to_cart'))
        suite.addTest(TestLogIn('test_logIn'))
        suite.addTest(TestLogIn('test_logIn_with_invalid_password'))
        return suite
