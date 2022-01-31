from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
# Implicit Waits
# driver.implicitly_wait(10)

driver.get("https://google.com")
driver.find_element(by="name", value="q").send_keys("Automation")
driver.find_element(by="name", value="q").send_keys(Keys.ENTER)
wait = WebDriverWait(driver, 10)

try:
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-q='What is automation used for?']")))
    print("element is clickable")
    element.click()
except TimeoutException:
    print("element is not clickable")
    exit(1)

print("Test Completed")
driver.quit()
