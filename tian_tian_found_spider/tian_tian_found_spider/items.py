# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FoundGuZhiSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    gu_zhi = scrapy.Field()


class FoundJingZhiSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # gu_zhi = scrapy.Field()
    pass