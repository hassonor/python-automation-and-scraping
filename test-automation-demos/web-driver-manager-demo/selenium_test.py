from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

# Run with Chrome
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://google.com")
# time.sleep(2)
# driver.quit()

# Run with FireFox
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://google.com")
time.sleep(2)
driver.quit()
