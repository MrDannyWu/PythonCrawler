# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmzSaleMonitoringItem(scrapy.Item):
    # define the fields for your item here like:
    asin = scrapy.Field()
    country_code = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    delivery_is_fba = scrapy.Field()
    shop_id = scrapy.Field()
    shop_name = scrapy.Field()
    feedback_count = scrapy.Field()
    feedback_star = scrapy.Field()
    buy_box = scrapy.Field()
    follow_seller_num = scrapy.Field()
    error = scrapy.Field()
    aaa = scrapy.Field()
    follow_seller_list = scrapy.Field()

