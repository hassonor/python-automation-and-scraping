import HtmlTestRunner
from selenium import webdriver
import unittest


class GoogleSsearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.driver.find_element(by="name", value="q").send_keys("Automation")
        self.driver.find_element(by="name", value="btnK").click()
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='reports'),
        verbosity=2)
