import scrapy

class CompanyDetailsItem(scrapy.Item):
    company_name = scrapy.Field()
    company_price_intraday = scrapy.Field()
    company_symbol = scrapy.Field()
    company_symbol_link = scrapy.Field()
