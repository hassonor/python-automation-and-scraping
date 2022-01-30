from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
try:
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com')
    form_auth_link = wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Form Authentication')
    ))
    form_auth_link.click()

    username = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#username')
    ))
    username.send_keys('tomsmith')

    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('SuperSecretPassword!')

    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()

    wait.until(EC.presence_of_element_located(
        (By.LINK_TEXT, 'Logout')
    )).click()

    flash = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '#flash')
    ))

    assert 'logged out' in flash.text
finally:
    driver.quit()

"""
WebElements Objects
-------------------
Calls to driver.find_elements(s) return one or more WebElement objects
-> WeElements are represented by an ID shared between client and server to refer to the same HTML element
-> In Python, WebElements are instances of a class and have number of useful methods for interacting with elements
-> Certain other Webdriver commands take elements as parameters, and for those, WebElement
objects can be used
"""

"""
Basic Element Interation
------------------------
element.click() -> Click or tap the element
element.send_keys('text') -> Send 'text' as a eries of keystrokes into an input field element
element.clear() -> Remove any text or value from an input field element
text = element.text -> Retrieve the text displayed within the element, and assign it to Python variable text

"""

"""
More Interation Examples
------------------------
driver.back(); driver.forward() -> Go back or forward in browser history
driver.refresh() -> Refresh the page
source = driver.page_source -> Get the current HTML source as a string
res = driver.execute_script('return 2+2;') -> Execute Javascript in the context of the page and get the result
driver.save_screenshot('foo.png') -> Save a screenshot of the current state of the page to a file

"""

"""
Window Interaction
------------------
name_list = driver.windows_handles -> Get a list of IDs for all available windows
driver.switch_to.window(handle) -> Switch to a given window by its handle
handle = driver.current_window_handle -> Get the handle of the currently active window

"""

"""
Window Size/ Position
---------------------
driver.maximize_window() -> Maximize the window
driver.minimize_window() -> Minimize the window
driver.get_window_rect() -> Get the width, height, and x & y position of the window
driver.set_window_rect(x=50, y=50, height=100, width=200) -> Set the width, height and position of the window

"""

"""
Frame Interation
------------------
Frames are webpages embedded in other webpages
* Frames come in two varieties: <frame> and <iframe>
* Selenium / WebDriver allow you to work with <frame> and <iframe> in exactly the same way

driver.switch_to.frame(frame) -> Switch to a given frame, either by its index, its name, or as a found WebElement
driver.switch_to.parent_frame() -> Switch focus to the parent of the current frame (has no effect if already the top
level)
driver.switch_to.default_content() -> Switch focus back to the default frame/window

"""

"""
Alert Interation
-----------------
alert = driver.switch_to.alert -> Switch context to the alert and get a reference to it as an alert object
alert.accept() -> Accept the alert
alert.dismiss() -> Dismiss the alert
text = alert.text -> Get the text displayed in the alert
alert.send_keys('foo') -> Send keystrokes into a prompt-type alert

"""
