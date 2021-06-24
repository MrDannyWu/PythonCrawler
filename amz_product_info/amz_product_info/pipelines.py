# -*- coding: utf-8 -*-

import pymysql
from amz_product_info.db import *
import datetime
# import os


class GetProductDetailsPipeline(object):

    # 定义构造器，初始化要写入的文件
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host=DB_HOST_1, user=DB_USER_1, password=DB_PASS_1, db=DATABASE_1, port=DB_PORT_1)
        print('连接成功！')
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        self.connect.ping(reconnect=True)
        self.cursor = self.connect.cursor()
        if item['product_name'] != '':
            # 往数据库里面写入产品详情数据
            product_id = item['product_id']
            site = item['site']
            sku = item['sku']
            account = item['account']
            product_url = item['product_url'].replace('"', '').replace('\\', '').strip()
            product_name = item['product_name'].replace('"', '').replace('\\', '').strip()
            product_picture_url = item['product_picture_url'].replace('"', '').replace('\\', '').strip()
            product_price_temp = item['product_price'].replace('"', '').replace('\\', '').strip()
            if product_price_temp != '':
                if ('$' in product_price_temp or '£' in product_price_temp or '￥' in product_price_temp) and 'CDN$' not in product_price_temp:
                    product_base_price = product_price_temp.replace('$', '').replace('£', '').replace('￥', '').replace(',', '').strip()
                    print('pppppppppppp', product_base_price)
                    if '-' in product_price_temp:
                        product_price = float(product_base_price.split('-')[-1].strip())
                        product_min_price = float(product_base_price.split('-')[0].strip())
                        currency_symbol = product_price_temp.strip()[0]
                    else:
                        product_price = float(product_base_price)
                        product_min_price = 'null'
                        currency_symbol = product_price_temp.strip()[0]
                elif '€' in product_price_temp:
                    product_base_price = product_price_temp.replace('€', '').replace('.', '').replace(',', '.').strip()
                    print('pppppppppppp', product_base_price)
                    if '-' in product_price_temp:
                        product_price = float(product_base_price.split('-')[-1].strip())
                        product_min_price = float(product_base_price.split('-')[0].strip())
                        currency_symbol = product_price_temp.strip()[-1]
                    else:
                        product_price = float(product_base_price)
                        product_min_price = 'null'
                        currency_symbol = product_price_temp.strip()[-1]
                elif 'EUR' in product_price_temp:
                    product_base_price = product_price_temp.replace('EUR', '').replace('.', '').replace(',', '.').strip()
                    print('pppppppppppp', product_base_price)
                    if '-' in product_price_temp:
                        product_price = float(product_base_price.split('-')[-1].strip())
                        product_min_price = float(product_base_price.split('-')[0].strip())
                        currency_symbol = '€'
                    else:
                        product_price = float(product_base_price)
                        product_min_price = 'null'
                        currency_symbol = '€'
                elif 'CDN$' in product_price_temp:
                    product_base_price = product_price_temp.replace('CDN$', '').replace(',', '').strip()
                    print('pppppppppppp', product_base_price)
                    if '-' in product_price_temp:
                        product_price = float(product_base_price.split('-')[-1].strip())
                        product_min_price = float(product_base_price.split('-')[0].strip())
                        currency_symbol = 'CDN$'
                    else:
                        product_price = float(product_base_price)
                        product_min_price = 'null'
                        currency_symbol = 'CDN$'
                elif '₹' in product_price_temp:
                    product_base_price = product_price_temp.replace('₹', '').replace(',', '').strip()
                    print('pppppppppppp', product_base_price)
                    if '-' in product_price_temp:
                        product_price = float(product_base_price.split('-')[-1].strip())
                        product_min_price = float(product_base_price.split('-')[0].strip())
                        currency_symbol = '₹'
                    else:
                        product_price = float(product_base_price)
                        product_min_price = 'null'
                        currency_symbol = '₹'
                elif 'AED' in product_price_temp:
                    product_base_price = product_price_temp.replace('AED', '').replace(',', '').strip()
                    print('pppppppppppp', product_base_price)
                    if '-' in product_price_temp:
                        product_price = float(product_base_price.split('-')[-1].strip())
                        product_min_price = float(product_base_price.split('-')[0].strip())
                        currency_symbol = 'AED'
                    else:
                        product_price = float(product_base_price)
                        product_min_price = 'null'
                        currency_symbol = 'AED'
                else:
                    print('pppppppppppp', product_price_temp)
                # if ''
                # if '$' in product_price_temp and '-' not in product_price_temp:
                #     product_price = float(product_price_temp.replace('$', '').replace(',', '').strip())
                #     product_min_price = 'null'
                #     currency_symbol = '$'
                # elif '$' in product_price_temp and '-' in product_price_temp:
                #     product_price = float(product_price_temp.replace('$', '').split('-')[-1].strip().replace(',', ''))
                #     product_min_price = float(product_price_temp.replace('$', '').split('-')[0].strip().replace(',', ''))
                #     currency_symbol = '$'
                # elif '£' in product_price_temp and '-' not in product_price_temp:
                #     product_price = float(product_price_temp.replace('£', '').replace(',', '').strip())
                #     product_min_price = 'null'
                #     currency_symbol = '£'
                # elif '$' in product_price_temp and '-' in product_price_temp:
                #     product_price = float(product_price_temp.replace('$', '').split('-')[-1].strip().replace(',', ''))
                #     product_min_price = float(product_price_temp.replace('$', '').split('-')[0].strip().replace(',', ''))
                #     currency_symbol = '$'
                # else:
                #     product_price = 'null'
                #     product_min_price = 'null'
                #     currency_symbol = ''
            else:
                product_price = 'null'
                product_min_price = 'null'
                currency_symbol = ''

            try:
                if item['product_stars'].replace('"', '').replace('\\', '').strip() != '':
                    if 'von' in item['product_stars'].replace('"', '').replace('\\', '').strip():
                        product_stars = float(item['product_stars'].replace('"', '').replace('\\', '').strip().split('von')[0].replace(',', '.').strip())
                    elif 'sur' in item['product_stars'].replace('"', '').replace('\\', '').strip():
                        product_stars = float(item['product_stars'].replace('"', '').replace('\\', '').strip().split('sur')[0].replace(',', '.').strip())
                    elif 'su' in item['product_stars'].replace('"', '').replace('\\', '').strip():
                        product_stars = float(item['product_stars'].replace('"', '').replace('\\', '').strip().split('su')[0].replace(',', '.').strip())
                    elif 'de' in item['product_stars'].replace('"', '').replace('\\', '').strip():
                        product_stars = float(item['product_stars'].replace('"', '').replace('\\', '').strip().split('de')[0].replace(',', '.').strip())
                    elif 'ち' in item['product_stars'].replace('"', '').replace('\\', '').strip():
                        product_stars = float(item['product_stars'].replace('"', '').replace('\\', '').strip().split('ち')[-1].replace(',', '.').strip())
                    else:
                        product_stars = float(item['product_stars'].replace('"', '').replace('\\', '').strip())
                else:
                    product_stars = 'null'
            except:
                product_stars = 'null'

            try:
                if item['product_reviews'].replace('"', '').replace('\\', '').strip() != '':
                    product_reviews = int(item['product_reviews'].replace('"', '').replace('\\', '').replace('voti', '').replace('Sternebewertungen', '').replace('ratings', '').replace('Sternebewertung', '').replace('calificaciones', '').replace('calificación', '').replace('rating', '').replace('個の評価', '').replace('valoraciones', '').replace('valoración', '').replace('évaluations', '').replace('évaluation', '').strip())
                else:
                    product_reviews = 'null'
            except:
                product_reviews = 'null'

            product_asin = item['product_asin'].replace('"', '').replace('\\', '').strip()

            try:
                if item['product_big_class'].replace('"', '').replace('\\', '').strip() != 0:
                    product_big_class = int(item['product_big_class'].replace('"', '').replace('\\', '').replace('Nr.', '').replace('n.º', '').replace('n.°', '').replace('n.', '').replace('.', '').replace('nº', '').replace('n°', '').replace('位', '').strip())
                else:
                    product_big_class = 'null'
            except:
                product_big_class = 'null'

            try:
                if item['product_small_class'].replace('"', '').replace('\\', '').strip() != '':
                    product_small_class = int(item['product_small_class'].replace('"', '').replace('\\', '').replace('Nr.', '').replace('n.º', '').replace('n.°', '').replace('n.', '').replace('.', '').replace('nº', '').replace('n°', '').replace('位', '').strip())
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

            query_product_id = 'select id from amz_product_info where product_id = {} and product_url="{}" and report_time ="{}"'.format(product_id, product_url, report_time)
            query_product_id_result = self.cursor.execute(query_product_id)
            if query_product_id_result == 0:
                insert_sql = 'insert into amz_product_info(product_id, site, sku, account, product_url, product_name, product_picture_url, product_price, product_min_price, currency_symbol, product_stars, product_reviews, product_asin, product_big_class, product_small_class, report_time, update_time)values ({}, "{}", "{}", "{}", "{}", "{}", "{}", {}, {}, "{}", {}, {}, "{}", {}, {}, "{}", "{}")'.format(product_id, site, sku, account, product_url, product_name, product_picture_url, product_price, product_min_price, currency_symbol, product_stars, product_reviews, product_asin, product_big_class, product_small_class, report_time, update_time)
                # print(insert_sql)
                self.cursor.execute(insert_sql)
                self.connect.commit()
            else:
                results = self.cursor.fetchall()
                id_num = results[0][0]
                update_sql = 'update amz_product_info set product_id={}, site="{}", sku="{}", account="{}", product_url="{}", product_name="{}", product_picture_url="{}", product_price={}, product_min_price={}, currency_symbol="{}", product_stars={}, product_reviews={}, product_asin="{}", product_big_class={}, product_small_class={}, report_time="{}", update_time="{}" where id ={}'.format(product_id, site, sku, account, product_url, product_name, product_picture_url, product_price, product_min_price, currency_symbol, product_stars, product_reviews, product_asin, product_big_class, product_small_class, report_time, update_time, id_num)
                # print(update_sql)
                self.cursor.execute(update_sql)
                self.connect.commit()

            error = 'no'
            update_sql = 'update amz_product_url set update_time="{}", error="{}" where id={}'.format(item['update_time'], error, product_id)
            self.cursor.execute(update_sql)
            self.connect.commit()
            return item
        else:
            if item['http_status_code'] == 404:
                # delete_404_product_sql = 'delete from amz_product where id = {}'.format(item['product_id'])
                error = '404'
                update_sql = 'update amz_product_url set update_time="{}", error="{}" where id={}'.format(item['update_time'], error, item['product_id'])
                # print(item['product_id'], item['http_status_code'])
                # print(delete_404_product_sql)
                self.cursor.execute(update_sql)
                self.connect.commit()
            else:
                product_id = item['product_id']
                error = 'yes'
                update_sql = 'update amz_product_url set update_time="{}", error="{}" where id={}'.format(item['update_time'], error, product_id)
                self.cursor.execute(update_sql)
                self.connect.commit()

            return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


