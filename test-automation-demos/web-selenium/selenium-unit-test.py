import unittest
from selenium import webdriver
from selenium.webdriver import Keys
import HtmlTestRunner


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        options.add_argument('start-maximized')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument('no-sandbox')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_argument('disable-blink-features=AutomationControlled')
        cls.driver = webdriver.Chrome(options=options)

    def test_search_1(self):
        self.driver.get("http://google.com")
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(by="name", value='q')
        element.send_keys("OR HASSON")
        element.send_keys(Keys.ENTER)
        title = self.driver.title
        print(title)
        self.assertEqual(title, "OR HASSON - Google Search")

    def test_search_2(self):
        self.driver.get("http://google.com")
        self.driver.implicitly_wait(10)
        element = self.driver.find_element(by="name", value='q')
        element.send_keys("OR1 HASSON")
        element.send_keys(Keys.ENTER)
        title = self.driver.title
        print(title)
        self.assertEqual(title, "OR1 HASSON - Google Search")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='reports'),
        verbosity=2)
