# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutoSetupAmzItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    name_set = scrapy.Field()
    country = scrapy.Field()
    # address = scrapy.Field()
    expires = scrapy.Field()
    phone = scrapy.Field()
    card = scrapy.Field()
    cvv2 = scrapy.Field()
    username = scrapy.Field()
    password = scrapy.Field()
    error = scrapy.Field()
    spider = scrapy.Field()
    # status = scrapy.Field()
    report_date = scrapy.Field()
    update_time = scrapy.Field()
    is_used = scrapy.Field()

