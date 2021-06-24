# -*- coding: utf-8 -*-

import pymysql
from amazon.db import DATABASE, DB_HOST, DB_PASS, DB_USER, DB_PORT
import datetime
# import os


class AmazonPipeline(object):

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
        self.cursor_one = self.connect.cursor()

        # 保存目录到MySQL
        # print(item['product_category'].split('-->'))
        for j in range(len(item['product_category'].split('-->'))):
            # 将一个长的目录结构分为两两相邻的列表，例如：a-->b-->c--> ==> [a,b] [b,c]
            if len(item['product_category'].split('-->')[0 + j: j + 2]) == 2:
                class_one_two = item['product_category'].split('-->')[0 + j: j + 2]
                # 查询父目录有没有父目录的sql，query_pid
                query_pid = 'SELECT pid from amz_product_category where category = "{}" and category_url="{}"'.format(class_one_two[0].split(':::')[0], class_one_two[0].split(':::')[1])
                # 查询结果的个数，query_pid_result
                query_pid_result = self.cursor_one.execute(query_pid)
                # 若查询结果为零，代表数据库中没有父目录
                if query_pid_result == 0:
                    # 插入父节点，设置父节点的pid为0
                    insert_parent_category = 'insert into amz_product_category(category, pid, category_url, update_time)VALUES ("{}", "{}", "{}", "{}")'.format(class_one_two[0].split(':::')[0], 0, class_one_two[0].split(':::')[1], item['update_time'])
                    self.cursor_one.execute(insert_parent_category)
                    self.connect.commit()
                    # 查询父目录的id，留着下面当作子目录的pid
                    query_parent_id = 'SELECT id from amz_product_category where category = "{}" and category_url="{}"'.format(class_one_two[0].split(':::')[0], class_one_two[0].split(':::')[1])
                    self.cursor_one.execute(query_parent_id)
                    parent_id = self.cursor_one.fetchall()[0][0]
                    # 如果父目录没有，子目录肯定没有，直接插入子目录
                    insert_child_category = 'insert into amz_product_category(category, pid, category_url, update_time)VALUES ("{}", "{}", "{}", "{}")'.format(class_one_two[1].split(':::')[0], parent_id, class_one_two[1].split(':::')[1], item['update_time'])
                    self.cursor_one.execute(insert_child_category)
                    self.connect.commit()
                # 查询结果不为零，即数据库中已存在了父目录
                else:
                    # 查询父目录的id，下面通过父目录的id来更新父目录
                    query_parent_id = 'SELECT id from amz_product_category where category = "{}" and category_url="{}"'.format(class_one_two[0].split(':::')[0], class_one_two[0].split(':::')[1])
                    self.cursor_one.execute(query_parent_id)
                    parent_id = self.cursor_one.fetchall()[0][0]
                    # 数据库中已经存在父目录了，就更新父目录
                    update_parent = 'update amz_product_category set update_time = "{}" where id = "{}"'.format(item['update_time'], parent_id)
                    self.cursor_one.execute(update_parent)
                    self.connect.commit()
                    # 通过子目录的名称以及子目录的url来判断数据库中有没有子目录
                    query_child = 'SELECT pid from amz_product_category where category = "{}" and category_url="{}"'.format(class_one_two[1].split(':::')[0], class_one_two[1].split(':::')[1])
                    query_child_result = self.cursor_one.execute(query_child)
                    # 若查询结果为零，代表没有子目录
                    if query_child_result == 0:
                        # 直接插入子目录
                        insert_child_category = 'insert into amz_product_category(category, pid, category_url, update_time)VALUES ("{}", "{}", "{}", "{}")'.format(class_one_two[1].split(':::')[0], parent_id, class_one_two[1].split(':::')[1], item['update_time'])
                        self.cursor_one.execute(insert_child_category)
                        self.connect.commit()
                    # 若查询结果不为零，代表已经存在子目录
                    else:
                        # 查询已存在的子目录的id，下面通过子目录的id来更新子目录
                        query_child_id = 'SELECT id from amz_product_category where category = "{}" and category_url="{}"'.format(class_one_two[1].split(':::')[0], class_one_two[1].split(':::')[1])
                        self.cursor_one.execute(query_child_id)
                        child_id = self.cursor_one.fetchall()[0][0]
                        # 通过子目录的id更新子目录
                        update_child = 'update amz_product_category set update_time = "{}" where id = "{}"'.format(item['update_time'], child_id)
                        self.cursor_one.execute(update_child)
                        self.connect.commit()
        # 保存产品url
        product_category_text = item['product_category'].split('-->')[-1].split(':::')[0]
        product_category_link = item['product_category'].split('-->')[-1].split(':::')[1]
        asin = item['product_url'].split('/')[-2]
        product_url = item['product_url'].split('ref=')[0]
        query_class_id = 'SELECT id from amz_product_category where category = "{}" and category_url="{}"'.format(product_category_text, product_category_link)
        self.cursor.execute(query_class_id)
        class_id = self.cursor.fetchall()[0][0]
        query_sql = 'SELECT id from amz_product where asin = "{}"'.format(asin)
        # insert_sql = 'insert into amz_product(class_id, asin, product_url, update_time, error)VALUES ( "{}", "{}", "{}", "{}", "{}")'.format(class_id, asin, product_url, item['update_time'], item['error'])
        insert_sql = 'insert into amz_product(class_id, asin, product_url, update_time, error, is_new)VALUES ( "{}", "{}", "{}", "{}", "{}", {})'.format(class_id, asin, product_url, item['update_time'], item['error'], 1)
        query_result = self.cursor.execute(query_sql)
        if query_result == 0:
            self.cursor.execute(insert_sql)
            self.connect.commit()
        elif query_result == 1:
            results = self.cursor.fetchall()
            id_num = results[0][0]
            # update_sql = 'update amz_product set class_id="{}", product_url="{}", update_time="{}", error="{}" where id ={}'.format(class_id, product_url, item['update_time'], item['error'], id_num)
            update_sql = 'update amz_product set class_id="{}", product_url="{}", update_time="{}", error="{}", is_new={} where id ={}'.format(class_id, product_url, item['update_time'], item['error'], 0, id_num)
            self.cursor.execute(update_sql)
            self.connect.commit()

        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


class GetProductDetailsPipeline(object):

    # 定义构造器，初始化要写入的文件
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
        print('连接成功！')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.connect.ping(reconnect=True)
        self.cursor = self.connect.cursor()
        if item['product_name'] != '':
            # 往数据库里面写入产品详情数据
            product_id = item['product_id']
            product_class_id = item['product_class_id']
            product_url = item['product_url'].replace('"', '').replace('\\', '').strip()
            product_name = item['product_name'].replace('"', '').replace('\\', '').strip()
            product_picture_url = item['product_picture_url'].replace('"', '').replace('\\', '').strip()
            product_price_temp = item['product_price'].replace('"', '').replace('\\', '').strip()
            is_new = item['is_new']
            try:
                if product_price_temp != '':
                    if '$' in product_price_temp and '-' not in product_price_temp:
                        product_price = float(product_price_temp.replace('$', ''))
                        product_min_price = 'null'
                        currency_symbol = '$'
                    elif '$' in product_price_temp and '-' in product_price_temp:
                        product_price = float(product_price_temp.replace('$', '').split('-')[-1].strip())
                        product_min_price = float(product_price_temp.replace('$', '').split('-')[0].strip())
                        currency_symbol = '$'
                    else:
                        product_price = 'null'
                        product_min_price = 'null'
                        currency_symbol = '$'
                else:
                    product_price = 'null'
                    product_min_price = 'null'
                    currency_symbol = '$'
            except:
                product_price = 'null'
                product_min_price = 'null'
                currency_symbol = '$'

            try:
                if item['product_stars'].replace('"', '').replace('\\', '').strip() != '':
                    product_stars = float(item['product_stars'].replace('"', '').replace('\\', '').strip())
                else:
                    product_stars = 'null'
            except:
                product_stars = 'null'

            try:
                if item['product_reviews'].replace('"', '').replace('\\', '').strip() != '':
                    product_reviews = int(item['product_reviews'].replace('"', '').replace('\\', '').strip())
                else:
                    product_reviews = 'null'
            except:
                product_reviews = 'null'

            product_asin = item['product_asin'].replace('"', '').replace('\\', '').strip()

            try:
                if item['product_big_class'].replace('"', '').replace('\\', '').strip() != 0:
                    product_big_class = int(item['product_big_class'].replace('"', '').replace('\\', '').strip())
                else:
                    product_big_class = 'null'
            except:
                product_big_class = 'null'

            try:
                if item['product_small_class'].replace('"', '').replace('\\', '').strip() != '':
                    product_small_class = int(item['product_small_class'].replace('"', '').replace('\\', '').strip())
                else:
                    product_small_class = 'null'
            except:
                product_small_class = 'null'

            try:
                if item['shelf_time'] != '':
                    time_original = item['shelf_time']
                    time_format = datetime.datetime.strptime(time_original, '%B %d, %Y')
                    shelf_time = '"' + time_format.strftime('%Y-%m-%d') + '"'
                else:
                    shelf_time = 'null'
            except:
                shelf_time = 'null'

            try:
                if item['sale_time'] != '':
                    sale_time = '"' + item['sale_time'] + '"'
                else:
                    sale_time = 'null'
            except:
                sale_time = 'null'
            update_time = item['update_time']
            report_time = datetime.datetime.now().strftime("%Y-%m-%d")

            query_product_id = 'select id from amz_product_details where product_id = {} and product_asin="{}" and report_time ="{}"'.format(product_id, product_asin, report_time)
            query_product_id_result = self.cursor.execute(query_product_id)
            if query_product_id_result == 0:
                insert_sql = 'insert into amz_product_details(product_id, product_class_id, product_url, product_name, product_picture_url, product_price, product_min_price, currency_symbol, product_stars, product_reviews, product_asin, product_big_class, product_small_class, report_time, update_time, is_new)values ({}, {}, "{}", "{}", "{}", {}, {}, "{}", {}, {}, "{}", {}, {}, "{}", "{}", {})'.format(product_id, product_class_id, product_url, product_name, product_picture_url, product_price, product_min_price, currency_symbol, product_stars, product_reviews, product_asin, product_big_class, product_small_class, report_time, update_time, is_new)
                # print(insert_sql)
                self.cursor.execute(insert_sql)
                self.connect.commit()
            else:
                results = self.cursor.fetchall()
                id_num = results[0][0]
                update_sql = 'update amz_product_details set product_id={}, product_class_id={}, product_url="{}", product_name="{}", product_picture_url="{}", product_price={}, product_min_price={}, currency_symbol="{}", product_stars={}, product_reviews={}, product_asin="{}", product_big_class={}, product_small_class={}, report_time="{}", update_time="{}", is_new={} where id ={}'.format(product_id, product_class_id, product_url, product_name, product_picture_url, product_price, product_min_price, currency_symbol, product_stars, product_reviews, product_asin, product_big_class, product_small_class, report_time, update_time, is_new, id_num)
                # print(update_sql)
                self.cursor.execute(update_sql)
                self.connect.commit()

            error = 'no'
            update_sql = 'update amz_product set update_time="{}", error="{}" where id={} and class_id={}'.format(item['update_time'], error, product_id, product_class_id)
            self.cursor.execute(update_sql)
            self.connect.commit()
            return item
        else:
            if item['http_status_code'] == 404:
                # delete_404_product_sql = 'delete from amz_product where id = {}'.format(item['product_id'])
                error = '404'
                update_sql = 'update amz_product set update_time="{}", error="{}" where id={} and class_id={}'.format(item['update_time'], error, item['product_id'], item['product_class_id'])
                # print(item['product_id'], item['http_status_code'])
                # print(delete_404_product_sql)
                self.cursor.execute(update_sql)
                self.connect.commit()
            else:
                product_id = item['product_id']
                product_class_id = item['product_class_id']
                error = 'yes'
                update_sql = 'update amz_product set update_time="{}", error="{}" where id={} and class_id={}'.format(item['update_time'], error, product_id, product_class_id)
                self.cursor.execute(update_sql)
                self.connect.commit()

            return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


class GetProductDetailsPipelineTwo(object):

    # 定义构造器，初始化要写入的文件
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
        print('连接成功！')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.connect.ping(reconnect=True)
        self.cursor = self.connect.cursor()
        if item['product_name'] != '':
            # 往数据库里面写入产品详情数据
            product_id = item['product_id']
            product_class_id = item['product_class_id']
            product_url = item['product_url'].replace('"', '').replace('\\', '').strip()
            product_name = item['product_name'].replace('"', '').replace('\\', '').strip()
            product_picture_url = item['product_picture_url'].replace('"', '').replace('\\', '').strip()
            product_price_temp = item['product_price'].replace('"', '').replace('\\', '').strip()
            is_new = item['is_new']
            try:
                if product_price_temp != '':
                    if '$' in product_price_temp and '-' not in product_price_temp:
                        product_price = float(product_price_temp.replace('$', ''))
                        product_min_price = 'null'
                        currency_symbol = '$'
                    elif '$' in product_price_temp and '-' in product_price_temp:
                        product_price = float(product_price_temp.replace('$', '').split('-')[-1].strip())
                        product_min_price = float(product_price_temp.replace('$', '').split('-')[0].strip())
                        currency_symbol = '$'
                    else:
                        product_price = 'null'
                        product_min_price = 'null'
                        currency_symbol = '$'
                else:
                    product_price = 'null'
                    product_min_price = 'null'
                    currency_symbol = '$'
            except:
                product_price = 'null'
                product_min_price = 'null'
                currency_symbol = '$'

            try:
                if item['product_stars'].replace('"', '').replace('\\', '').strip() != '':
                    product_stars = float(item['product_stars'].replace('"', '').replace('\\', '').strip())
                else:
                    product_stars = 'null'
            except:
                product_stars = 'null'

            try:
                if item['product_reviews'].replace('"', '').replace('\\', '').strip() != '':
                    product_reviews = int(item['product_reviews'].replace('"', '').replace('\\', '').strip())
                else:
                    product_reviews = 'null'
            except:
                product_reviews = 'null'

            product_asin = item['product_asin'].replace('"', '').replace('\\', '').strip()

            try:
                if item['product_big_class'].replace('"', '').replace('\\', '').strip() != 0:
                    product_big_class = int(item['product_big_class'].replace('"', '').replace('\\', '').strip())
                else:
                    product_big_class = 'null'
            except:
                product_big_class = 'null'

            try:
                if item['product_small_class'].replace('"', '').replace('\\', '').strip() != '':
                    product_small_class = int(item['product_small_class'].replace('"', '').replace('\\', '').strip())
                else:
                    product_small_class = 'null'
            except:
                product_small_class = 'null'

            try:
                if item['shelf_time'] != '':
                    time_original = item['shelf_time']
                    time_format = datetime.datetime.strptime(time_original, '%B %d, %Y')
                    shelf_time = '"' + time_format.strftime('%Y-%m-%d') + '"'
                else:
                    shelf_time = 'null'
            except:
                shelf_time = 'null'

            try:
                if item['sale_time'] != '':
                    sale_time = '"' + item['sale_time'] + '"'
                else:
                    sale_time = 'null'
            except:
                sale_time = 'null'
            update_time = item['update_time']
            report_time = datetime.datetime.now().strftime("%Y-%m-%d")

            query_product_id = 'select id from amz_product_details where product_id = {} and product_asin="{}" and report_time ="{}"'.format(product_id, product_asin, report_time)
            query_product_id_result = self.cursor.execute(query_product_id)
            if query_product_id_result == 0:
                # is_new = 1
                insert_sql = 'insert into amz_product_details(product_id, product_class_id, product_url, product_name, product_picture_url, product_price, product_min_price, currency_symbol, product_stars, product_reviews, product_asin, product_big_class, product_small_class, report_time, update_time, is_new)values ({}, {}, "{}", "{}", "{}", {}, {}, "{}", {}, {}, "{}", {}, {}, "{}", "{}", {})'.format(product_id, product_class_id, product_url, product_name, product_picture_url, product_price, product_min_price, currency_symbol, product_stars, product_reviews, product_asin, product_big_class, product_small_class, report_time, update_time, is_new)
                # insert_sql = 'insert into amz_product_details(product_id, product_class_id, product_url, product_name, product_picture_url, product_price, product_min_price, currency_symbol, product_stars, product_reviews, product_asin, product_big_class, product_small_class, shelf_time, sale_time, report_time, update_time)values ({}, {}, "{}", "{}", "{}", {}, {}, "{}", {}, {}, "{}", {}, {}, {}, {}, "{}", "{}")'.format(product_id, product_class_id, product_url, product_name, product_picture_url, product_price, product_min_price, currency_symbol, product_stars, product_reviews, product_asin, product_big_class, product_small_class, shelf_time, sale_time, report_time, update_time)
                # print(insert_sql)
                self.cursor.execute(insert_sql)
                self.connect.commit()

            else:
                results = self.cursor.fetchall()
                id_num = results[0][0]
                # is_new = 0
                update_sql = 'update amz_product_details set product_id={}, product_class_id={}, product_url="{}", product_name="{}", product_picture_url="{}", product_price={}, product_min_price={}, currency_symbol="{}", product_stars={}, product_reviews={}, product_asin="{}", product_big_class={}, product_small_class={}, report_time="{}", update_time="{}", is_new={} where id ={}'.format(product_id, product_class_id, product_url, product_name, product_picture_url, product_price, product_min_price, currency_symbol, product_stars, product_reviews, product_asin, product_big_class, product_small_class, report_time, update_time, is_new, id_num)
                # update_sql = 'update amz_product_details set product_id={}, product_class_id={}, product_url="{}", product_name="{}", product_picture_url="{}", product_price={}, product_min_price={}, currency_symbol="{}", product_stars={}, product_reviews={}, product_asin="{}", product_big_class={}, product_small_class={}, shelf_time={}, sale_time={}, report_time="{}", update_time="{}" where id ={}'.format(product_id, product_class_id, product_url, product_name, product_picture_url, product_price, product_min_price, currency_symbol, product_stars, product_reviews, product_asin, product_big_class, product_small_class, shelf_time, sale_time, report_time, update_time, id_num)
                # print(update_sql)
                self.cursor.execute(update_sql)
                self.connect.commit()
            error = 'no'
            update_sql = 'update amz_product set update_time="{}", error="{}" where id={} and class_id={}'.format(item['update_time'], error, product_id, product_class_id)
            self.cursor.execute(update_sql)
            self.connect.commit()

            return item
        else:
            # print(item['product_id'], item['http_status_code'])
            if item['http_status_code'] == 404:
                error = '404'
                update_sql = 'update amz_product set update_time="{}", error="{}" where id={} and class_id={}'.format(item['update_time'], error, item['product_id'], item['product_class_id'])
                # delete_404_product_sql = 'delete from amz_product where id = {}'.format(item['product_id'])
                # print(item['product_id'], item['http_status_code'])
                # print(delete_404_product_sql)
                self.cursor.execute(update_sql)
                self.connect.commit()
            else:
                product_id = item['product_id']
                product_class_id = item['product_class_id']
                error = 'yes'
                update_sql = 'update amz_product set update_time="{}", error="{}" where id={} and class_id={}'.format(item['update_time'], error, product_id, product_class_id)
                self.cursor.execute(update_sql)
                self.connect.commit()

            return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
