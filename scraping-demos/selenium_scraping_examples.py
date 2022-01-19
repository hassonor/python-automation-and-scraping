import yagmail
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt


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


def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(" ")[0])
    return output


def get_ynet_title():
    # Scraping H1 Title of Ynet
    driver = get_driver('http://www.ynet.co.il/home/0,7340,L-8,00.html')
    element = driver.find_element(by='css selector',
                                  value='h1.slotTitle')
    print(element.text)
    driver.close()


def get_dax_current_point():
    driver = get_driver('http://il.investing.com/indices/major-indices')
    time.sleep(2)
    element = driver.find_element(by='xpath',
                                  value="/html/body/div/div/div/div[2]/main/div[4]/table/tbody/tr[11]/td[3]")
    print("DAX: " + element.text)
    driver.close()


def login_demo():
    driver = get_driver("http://automated.pythonanywhere.com/login/")
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)
    text = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
    return clean_text(text)


def write_value_to_file(text):
    """Write input text into a text file"""
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)


def send_email(price):
    sender = config('EMAIL_SENDER')
    receiver = config('EMAIL_RECEIVER')

    subject = "The stock price is lower than -1.10%"

    contents = f"""
    The stock price is now {price}%
    """

    yag = yagmail.SMTP(user=sender, password=config('PASSWORD'))
    yag.send(to=receiver, subject=subject, contents=contents)
    print("Email Sent!")


def main():
    # get_ynet_title()

    # get_dax_current_point()

    # print(login_demo())
    # driver = get_driver("http://automated.pythonanywhere.com/")
    # while True:
    #     time.sleep(2)
    #     element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    #     text = str(clean_text(element.text))
    #     write_value_to_file(text)

    # driver = get_driver("https://titan22.com/account/login?return_url=%2Faccount")
    # driver.find_element(by="id", value="CustomerEmail").send_keys("hassonor@gmail.com")
    # time.sleep(2)
    # driver.find_element(by="id", value="CustomerPassword").send_keys("hdzyfjt252.Aa252" + Keys.RETURN)
    # time.sleep(2)
    # driver.find_element(by="xpath",
    #                     value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    # print(driver.current_url)

    driver = get_driver("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    time.sleep(2)
    element = driver.find_element(by="xpath",
                                  value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]')
    text = str(clean_text(element.text))
    print(text)

    if float(text) < -0.10:
        send_email(str(text))


main()
