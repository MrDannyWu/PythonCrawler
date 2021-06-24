# -*- coding: utf-8 -*-
import scrapy
from get_sale_time.db import DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT
import pymysql
from get_sale_time.items import GetSaleTimeItem
import datetime


class GetProductSaleTimeSpider(scrapy.Spider):
    name = 'get_product_sale_time'
    allowed_domains = ['keeps.com']
    start_urls = []
    # custom_settings = {
    #     'ROBOTSTXT_OBEY': False,
    #     'COOKIES_ENABLED': False,
    #     'DOWNLOADER_MIDDLEWARES': {
    #         'amazon.middlewares.SeleniumMiddleware': 700
    #     },
    #     'ITEM_PIPELINES': {
    #         'amazon.pipelines.GetProductSaleTime': 600
    #     }
    # }

    # def query_product(self):
    base_url_1 = 'https://keepa.com/iframe_addon.html#1-0-{}'
    connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
    cursor = connect.cursor()
    query_all_sql = 'select asin from amz_product where error != "404" and sale_time is null'
    # query_all_sql = 'select asin from amz_product where error != "404"'
    cursor.execute(query_all_sql)
    results = cursor.fetchall()
    for i in results[0: 1000]:
        url = base_url_1.format(i[0])
        print(url)
        start_urls.append(url)
        # return results

    def parse(self, response):
        item = GetSaleTimeItem()
        rank_days = ''
        request_url = response.request.url
        print('GGGGGGGGGGGGGGGGGGGGG', request_url)
        # print(str(response.xpath('//div[@id="productTableDescriptionIFrame"]/text()').extract_first()))
        if len(response.xpath('//td[@class="legendRange"]/text()')) > 0:
            rank_days = response.xpath('//td[@class="legendRange"]/text()').extract()[-1]
            print(rank_days)
            days = rank_days.split('(')[1].split('days')[0].strip()
            print(days)
            item['product_asin'] = request_url.split('-')[-1]
            # sale_time = (datetime.datetime.now() - datetime.timedelta(days=int(days))).strftime("%Y-%m-%d %H:%M:%S")
            sale_time = (datetime.datetime.now() - datetime.timedelta(days=int(days))).strftime("%Y-%m-%d")
            item['sale_time'] = sale_time
            yield item

        elif len(response.xpath('//div[@id="productTableDescriptionIFrame"]')) and ('does not provide any data' in str(response.xpath('//div[@id="productTableDescriptionIFrame"]/text()').extract_first()) or 'none' in str(response.xpath('//div[@id="productTableDescriptionIFrame"]/text()').extract_first()).lower() or 'product not' in str(response.xpath('//div[@id="productTableDescriptionIFrame"]/text()').extract_first()).lower()):
            rank_days = ''
            print('没有此Asin值')
            item = GetSaleTimeItem()
            item['product_asin'] = request_url.split('-')[-1]
            item['sale_time'] = ''
            yield item
        else:
            print('请求失败！')