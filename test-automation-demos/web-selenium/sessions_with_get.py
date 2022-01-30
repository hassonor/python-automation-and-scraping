from selenium import webdriver


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
    web_driver = get_driver("https://the-internet.herokuapp.com")

    els = web_driver.find_elements(by="tag name", value='a')
    print(f"There were {len(els)} anchor elements.")

    els = web_driver.find_elements(by="tag name", value='foo')
    print(f"There were {len(els)} foo elements.")

finally:
    web_driver.quit()

"""
Waiting Strategies
-------------------

1. Static Wait -> time.sleep(x) (LAST PRIORITY)

2. Implicit Wait -> Use the Webdriver server's built-in element finding retry, up to a timeout.
    -> When you have an implicit wait active, if you request an element from the server and it can't be
       found, the server will keep trying to find it up until the timeout you set
    -> Set the implicit wait timeout using driver.implicitly_wait(10).
    -> Implicit wait timeouts are global and apply to all elements you find.
    -> Implicit waits only work for finding elements, not for waiting for other kind of app state (like page titles,
    text values of elements, etc...)

3. Explicit Wait -> Use Expected Conditions to poll the app for appropriate state.
   -> Can check for any state which can be determined using Webdriver functionality.
   -> The polling functionality is built into the Python client on a class called WebDriverWait
      (selenium.webdriver.support.wait.WebDriverWait)
   -> WebDriverWaits have an until() method which takes an Expected Condition
      (selenium.webdriver.support.expected_conditions)
      
Some Expected Conditions Examples:
------------------------------------
expected_conditions.title_is('some title')
expected_conditions.url_to_be('https://some.url.com')
expected_conditions.presence_of_element_located((by="css selector", value='foo'))

"""
