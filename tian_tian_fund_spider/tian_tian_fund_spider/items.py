# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FundGuZhiSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    gu_zhi = scrapy.Field()


class FundJingZhiSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    jing_zhi = scrapy.Field()
    show_day = scrapy.Field()
