import scrapy
from scrapy.loader.processors import MapCompose


def full_links(company_symbol_link):
    url = 'https://finance.yahoo.com/sector/ms_technology/'
    return url + company_symbol_link


class CompanyDetailsItem(scrapy.Item):
    company_name = scrapy.Field()
    company_symbol_link = scrapy.Field(input_processor=MapCompose(full_links))
    company_price_intraday = scrapy.Field()
