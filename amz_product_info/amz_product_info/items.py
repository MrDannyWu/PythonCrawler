# -*- coding: utf-8 -*-
import scrapy


class AmazonItem(scrapy.Item):
    product_category = scrapy.Field()
    category = scrapy.Field()
    product_url = scrapy.Field()
    product_url_page_num = scrapy.Field()
    update_time = scrapy.Field()
    error = scrapy.Field()


class GetProductDetailsItem(scrapy.Item):
    product_id = scrapy.Field()
    site = scrapy.Field()
    sku = scrapy.Field()
    account = scrapy.Field()
    product_url = scrapy.Field()
    product_name = scrapy.Field()
    product_picture_url = scrapy.Field()
    product_price = scrapy.Field()
    product_stars = scrapy.Field()
    product_reviews = scrapy.Field()
    product_asin = scrapy.Field()
    product_big_class = scrapy.Field()
    product_small_class = scrapy.Field()
    shelf_time = scrapy.Field()
    sale_time = scrapy.Field()
    update_time = scrapy.Field()
    http_status_code = scrapy.Field()
