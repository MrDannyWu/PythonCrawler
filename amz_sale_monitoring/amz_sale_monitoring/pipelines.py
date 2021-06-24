"""
@Author: your name
@Date: 2019-12-31 11:36:17
@LastEditTime : 2020-01-06 08:41:31
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \amz_sale_monitoring\amz_sale_monitoring\pipelines.py
"""
# -*- coding: utf-8 -*-
from amz_sale_monitoring.db import *
from amz_sale_monitoring.db_utils import *
import datetime
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class AmzSaleMonitoringPipeline(object):

    def __init__(self):
        self.connect = connect_db(DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT)

    def process_item(self, item, spider):
        self.connect.ping(reconnect=True)
        now_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        asin = item['asin']
        country_code = item['country_code']
        follow_seller_num = int(item['follow_seller_num'])
        error = item['error']
        # 将数据更新至erp_amz_follow_sell_remind
        # 查询满足当前country_code以及asin的id
        query_sql_1 = 'select id from erp_amz_follow_sell_remind where website="{}" and asin="{}"'.format(country_code, asin)
        query_result = query_results(self.connect, query_sql_1)
        print(query_result)
        product_id = query_result[1][0][0]
        print(product_id)

        # 更新follow_seller_num至erp_amz_follow_sell_remind表
        update_sql_1 = 'update erp_amz_follow_sell_remind set followSellerNum={} where id ={}'.format(follow_seller_num, product_id)
        print(update_sql_1)
        insert_update_drop_data(self.connect, update_sql_1)

        if error in ['出错了', '没有跟卖']:
            pass
        else:

            price = item['price']
            currency = item['currency']
            delivery_is_fba = int(item['delivery_is_fba'])
            shop_id = item['shop_id']
            shop_name = item['shop_name']
            try:
                feedback_count = int(item['feedback_count'].replace(',', '').replace('\xa0', ''))
            except:
                feedback_count = 0
            try:
                feedback_star = float(item['feedback_star'].replace(',', '.').replace('\xa0', ''))
            except:
                feedback_star = 0
            buy_box = int(item['buy_box'])
            follow_seller_list = item['follow_seller_list']
            # 将详细数据插入到erp_amz_follow_sell_details表里面
            query_sql_2 = 'select id from erp_amz_follow_sell_details where website="{}" and asin="{}" and shopId="{}"'.format(country_code, asin, shop_id)
            print(query_sql_2)
            query_result_details = query_results(self.connect, query_sql_2)
            print(query_result_details)
            result_number = query_result_details[0]
            if result_number == 0:
                insert_details_sql = 'INSERT INTO erp_amz_follow_sell_details(asin, website, price, currency, deliveryIsFba, shopId, shopName, feedbackCount, ' \
                                     'feedbackStar, buyBox, error, spider, createTime, updateTime, status) VALUES ("{}", "{}", {}, "{}", {}, "{}", "{}", {}, {}, {}, "{}", "{}", "{}", "{}", "{}")' \
                                     ''.format(asin, country_code, price, currency, delivery_is_fba, shop_id, shop_name, feedback_count, feedback_star, buy_box, error, "1", now_datetime, now_datetime, 'following')
                print(insert_details_sql)
                insert_update_drop_data(self.connect, insert_details_sql)
            else:

                update_details_sql = 'UPDATE erp_amz_follow_sell_details set price={}, currency="{}", deliveryIsFba={}, shopId="{}", shopName="{}", feedbackCount={}, feedbackStar={}, buyBox={}, error="{}", spider="{}", ' \
                                     'updateTime="{}", status="{}" where website="{}" and asin="{}" and shopId="{}"'.format(price, currency, delivery_is_fba, shop_id, shop_name, feedback_count, feedback_star, buy_box, error, '1', now_datetime, 'following', country_code, asin, shop_id)
                print(update_details_sql)
                insert_update_drop_data(self.connect, update_details_sql)

                update_details_sql_1 = 'UPDATE erp_amz_follow_sell_details set status="{}", updateTime="{}" where website="{}" and asin="{}" and shopName not in {}'.format('unfollowed', now_datetime, country_code, asin, tuple(follow_seller_list))
                print(update_details_sql_1)
                insert_update_drop_data(self.connect, update_details_sql_1)

    def close_spider(self, spider):
        self.connect.close()
