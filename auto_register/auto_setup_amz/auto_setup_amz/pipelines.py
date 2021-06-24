# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from auto_setup_amz.db import *
from auto_setup_amz.db_utils import *


class AutoSetupAmzPipeline(object):

    # 定义构造器，初始化要写入的文件
    def __init__(self):
        # 连接MySQL数据库
        self.connect = connect_db(DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT)
        # print('连接成功！')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.connect.ping(reconnect=True)
        self.cursor = self.connect.cursor()

        # 往数据库里面写入产品详情数据

        name = item['name']
        name_set = item['name_set']
        country = item['country']
        phone = item['phone']
        card = item['card']
        expires = item['expires']
        cvv2 = item['cvv2']
        username = item['username']
        password = item['password']
        error = item['error']
        spider = item['spider']
        report_date = item['report_date']
        update_time = item['update_time']
        is_used = item['is_used']

        query_product_id = 'select id from virtual_people where nameSet = "{}" and country = "{}" and phone = "{}" and card = "{}" and expires = "{}" and cvv2 = "{}"'.format(name_set, country, phone, card, expires, cvv2)
        query_product_id_result = self.cursor.execute(query_product_id)
        if query_product_id_result == 0:
            # crawl_times = 1
            insert_sql = 'insert into virtual_people(name, nameSet, country, phone, card, expires, cvv2, username, password, reportDate, updateTime, error, spider, isUsed)values ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}","{}", "{}","{}", {}, {})'.format(name, name_set, country, phone, card, expires, cvv2, username, password, report_date, update_time, error, spider, is_used)
            # print('sqqqqqqqqqqqqqqqqqqqqqqql: ', insert_sql)
            insert_update_drop_data(self.connect, insert_sql, '插入成功!')

        else:
            # print('为什么会到这')
            results = self.cursor.fetchall()
            id_num = results[0][0]
            # crawl_times = results[0][1] + 1
            update_sql = 'update virtual_people set name="{}", nameSet="{}", country="{}", phone="{}", card="{}", expires="{}", cvv2="{}", username="{}", password="{}", reportDate="{}", updateTime="{}", error="{}", spider="{}", isUsed="{}" where id={}'.format(name, name_set, country, phone, card, expires, cvv2, username, password, report_date, update_time, error, spider, is_used, id_num)
            # print(update_sql)
            insert_update_drop_data(self.connect, update_sql, '更新成功!')
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
