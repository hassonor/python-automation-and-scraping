from scrapy.selector import Selector
from selenium import webdriver


def get_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver


def get_covid19_cases_and_deaths_by_country(countries):
    driver = None
    list_of_cases_deaths = []
    for index, country in enumerate(countries):
        if index == 0:
            driver = get_driver(f'https://www.worldometers.info/coronavirus/country/{country}')
        else:
            driver.get(f'https://www.worldometers.info/coronavirus/country/{country}')
        sel = Selector(text=driver.page_source)
        details = sel.xpath("//*[@class='maincounter-number']/span/text()").extract()

        list_of_cases_deaths.append(f" {country} -> Covid-19 Cases:{details[0]} Covid-19 Deaths: {details[1]}")
    driver.close()

    return list_of_cases_deaths


list_of_countries = ['US', 'France', 'China', 'Greece', 'Cyprus', 'Israel']
print(get_covid19_cases_and_deaths_by_country(list_of_countries))

''' 
More Examples:
        # Get all text in all paragraph on the DOM
        # sel.css('p::text').getall()

        # select all 'img' than return  all src links all images attribute.
        # sel.css('img ::attr(src)').extract()
        
        # select 'img' than return  the first src link
        # sel.css('img ::attr(src)').extract()[1]
        
        # select id="like-149" and return the text on the span child.
        # sel.css('#like-149>span::text').get()
'''
