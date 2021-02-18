# This is a sample Python script.
import unittest
from appium import webdriver
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class calculator_test(unittest.TestCase):
    calcsession = None;
    calcresult = None;


    def setUp(self):
        print("Setup done")
        desired_caps = {}
        desired_caps["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        self.calcsession = webdriver.Remote(
            command_executor='http://127.0.0.1:4723',
            desired_capabilities=desired_caps
        )


    def tearDown(self):
        print("tear down")
        self.calcsession.quit()

    def test_additon(self):
        print("inside addition")

    def test_sub(self):
        print("inside sub")