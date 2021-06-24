# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from get_sale_time.db import *


class GetSaleTimePipeline(object):
    # 定义构造器，初始化要写入的文件
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
        print('连接成功！')
        self.cursor = self.connect.cursor()
        self.cursor_one = self.connect.cursor()

    def process_item(self, item, spider):
        # 往数据库里面写入数据
        # self.cursor.execute('insert into product(product_url)VALUES ("{}")'.format(item['the_last_link']))
        self.connect.ping(reconnect=True)
        self.cursor = self.connect.cursor()
        # 保存产品url
        product_asin = item['product_asin']
        sale_time = item['sale_time']
        update_sql = 'update amz_product set sale_time="{}" where asin ="{}"'.format(sale_time, product_asin)
        self.cursor.execute(update_sql)
        self.connect.commit()

        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
