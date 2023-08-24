import unittest

from tests_.common_.suites_.testSuites import TestSuites
from common_.htmlRunner_.htmlRunner import HtmlRunner

if __name__ == "__main__":
    testSuites = TestSuites()
    suite = testSuites.get_random_suite()

    htmlRunner = HtmlRunner()
    runner = htmlRunner.get_html_runner("Random Suite")
    runner.run(suite)

    # runner = unittest.TextTestRunner()
    # runner.run(suite)