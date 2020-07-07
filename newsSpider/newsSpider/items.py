# -*- coding: utf-8 -*-

import scrapy
class NewsspiderItem(scrapy.Item):
    # 一级目录url
    first_url = scrapy.Field()
    # 一级目录标题
    #first_title = scrapy.Field()
    # 二级目录url
    second_url = scrapy.Field()
    # 二级目录标题
    #second_title = scrapy.Field()
    # 文章url
    article_url = scrapy.Field()
    # 文章标题
    head = scrapy.Field()
    # 文章内容
    article = scrapy.Field()
    # 文章时间
    time = scrapy.Field()

