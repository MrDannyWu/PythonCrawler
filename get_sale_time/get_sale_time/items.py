# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetSaleTimeItem(scrapy.Item):
    product_asin = scrapy.Field()
    sale_time = scrapy.Field()
