# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class Above100PriceCheck(object):
	def process_item(self, item, spider):

		try:
			price = float(item['company_price_intraday'])
			if price > 100:
				item['company_price_intraday'] = '>100'
		except:
			pass


		return item


class Below50PriceCheck(object):
	def process_item(self, item, spider):
		try:
			price = float(item['company_price_intraday'])
			if price < 50:
				item['company_price_intraday'] = '<50'
		except:
			pass	

		return item
