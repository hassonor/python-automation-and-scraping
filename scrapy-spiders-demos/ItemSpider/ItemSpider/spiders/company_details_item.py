import scrapy
from ItemSpider.items import CompanyDetailsItem


class CompanyDetailsItemSpider(scrapy.Spider):
    name = "company_details_item"
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['https://finance.yahoo.com/sector/ms_technology/']

    def parse(self, response):
        url = 'https://finance.yahoo.com/sector/ms_technology'

        company_name_list = response.xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[2]/text()').extract()
        company_price_intraday_list = response.xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[3]/fin-streamer/@value').extract()
        company_symbol_list = response.xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[1]/a/text()').extract()
        company_symbol_link_list = response.xpath(
            '//*[@id="scr-res-table"]/div[1]/table/tbody/tr/td[1]/a/@href').extract()

        count = len(company_name_list)

        for i in range(0, count):
            details = CompanyDetailsItem()
            details['company_name'] = company_name_list[i]
            details['company_price_intraday'] = company_price_intraday_list[i]
            details['company_symbol'] = company_symbol_list[i]
            details['company_symbol_link'] = url + company_symbol_link_list[i]

            yield details
