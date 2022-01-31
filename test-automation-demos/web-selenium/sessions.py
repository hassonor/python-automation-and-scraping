from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys


def get_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver


try:
    web_driver = get_driver("https://google.com")
    element = web_driver.find_element(by="name", value='q').send_keys("Automation step by step")
    element.send_keys("Automation step by step")
    element.send_keys(Keys.ENTER)


finally:
    sleep(2)
    web_driver.quit()
    print("Completed")
