from common_.utilities_.customLogger import *
import unittest

class TestCase(unittest.TestCase):
    @logg
    def test_1(self):
        print("Called Test N1")

    # @log
    # def test_2(self):
    #     print("Called Test N@")
