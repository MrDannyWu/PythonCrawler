# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from hahaha_utils.mysql_client import MySQLClient
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import datetime
from tian_tian_fund_spider.settings import ES_HOST, ES_PORT, DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME


class FundGuZhiSpiderPipeline:

    def __init__(self):

        self.mc = MySQLClient(DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT)
        self.guzhi_insert_sql = 'INSERT INTO `fund_gu_zhi`{} VALUES{} ON DUPLICATE KEY UPDATE {}'
        # self.es_hosts = {
        #     ES_HOST: ES_PORT
        # }
        # self.es = Elasticsearch(hosts=self.es_hosts)
        self.date_today = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
        # self.body = {
        #     "query": {
        #         "match": {
        #             "name": "Danny"
        #         }
        #     }
        # }
        # result = self.es.search(body=self.body, index='users')

    def get_lower_case_name(self, text):
        lst = []
        if text.isupper():
            return text.lower()
        else:
            for index, char in enumerate(text):
                if char.isupper() and index != 0:
                    lst.append("_")
                lst.append(char)

            return "".join(lst).lower()

    def process_item(self, item, spider):
        gu_zhi = item['gu_zhi']
        # save to ES
        data_list = []
        # save to mysql
        data_list_1 = []
        for data in gu_zhi:
            key_list = []
            value_list = []
            sql_text = ''
            for i in data:
                new_key = self.get_lower_case_name(i)
                key_list.append(new_key)
                value = data[i]
                try:
                    if value[-1] == '%':
                        value = value[:-1]
                except:
                    pass
                value_list.append(value)
                sql_text = sql_text + new_key + ' = VALUES(' + new_key + '),'
            key_list.append('key')
            value_list.append(data['bzdm'] + '_' + data['gxrq'])
            data['_index'] = 'tian_tian_fund_gu_zhi'
            insert_mysql_sql = self.guzhi_insert_sql.format(str(tuple(key_list)).replace("'", '`'), tuple(value_list), sql_text[:-1])
            self.mc.insert_one(insert_mysql_sql.replace('None', 'NULL'))



class FundJingZhiSpiderPipeline:

    def __init__(self):
        self.mc = MySQLClient(DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT)
        self.jing_zhi_insert_sql = 'INSERT INTO `fund_jing_zhi`(`fund_code`, `fund_name`, `fund_name_pin_yin`, `dwjz`, `ljjz`, `dwjz_day_before`, `ljjz_day_before`, `daily_growth_value`, `daily_growth_rate`, `buy_status`, `sale_status`, `handling_fee`, `jz_date`, `jz_date_day_before`, `table_key`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE fund_code=VALUES(fund_code), fund_name=VALUES(fund_name), fund_name_pin_yin=VALUES(fund_name_pin_yin), dwjz=VALUES(dwjz), ljjz=VALUES(ljjz), dwjz_day_before=VALUES(dwjz_day_before), ljjz_day_before=VALUES(ljjz_day_before), daily_growth_value=VALUES(daily_growth_value), daily_growth_rate=VALUES(daily_growth_rate), buy_status=VALUES(buy_status), sale_status=VALUES(sale_status), handling_fee=VALUES(handling_fee), jz_date=VALUES(jz_date), jz_date_day_before=VALUES(jz_date_day_before), table_key=VALUES(table_key)'
        self.date_today = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")

    def process_item(self, item, spider):
        gu_zhi = item['jing_zhi']
        show_day = item['show_day']
        data_list = []
        jz_date = show_day[0]
        jz_date_day_before = show_day[1]

        for data in gu_zhi:

            try:
                fund_code = data[0]
                if fund_code == '' or fund_code == '---':
                    fund_code = ''
            except:
                fund_code = ''

            try:
                fund_name = data[1]
                if fund_name == '' or fund_name == '---':
                    fund_name = ''
            except:
                fund_name = ''

            try:
                fund_name_pin_yin = data[2]
                if fund_name_pin_yin == '' or fund_name_pin_yin == '---':
                    fund_name_pin_yin = ''
            except:
                fund_name_pin_yin = ''

            try:
                dwjz = float(data[3])
                if dwjz == '' or dwjz == '---':
                    dwjz = -999.0000
            except:
                dwjz = -999.0000

            try:
                ljjz = float(data[4])
                if ljjz == '' or ljjz == '---':
                    ljjz = -999.0000
            except:
                ljjz = -999.0000

            try:
                dwjz_day_before = float(data[5])
                if dwjz_day_before == '' or dwjz_day_before == '---':
                    dwjz_day_before = -999.0000
            except:
                dwjz_day_before = -999.0000

            try:
                ljjz_day_before = float(data[6])
                if ljjz_day_before == '' or ljjz_day_before == '---':
                    ljjz_day_before = -999.0000
            except:
                ljjz_day_before = -999.0000

            try:
                daily_growth_value = float(data[7])
                if daily_growth_value == '' or daily_growth_value == '---':
                    daily_growth_value = -999.0000
            except:
                daily_growth_value = -999.0000

            try:
                daily_growth_rate = float(data[8])
                if daily_growth_rate == '' or daily_growth_rate == '---':
                    daily_growth_rate = -999.0000
            except:
                daily_growth_rate = -999.0000

            try:
                buy_status = data[9]
                if buy_status == '' or buy_status == '---':
                    buy_status = ''
            except:
                buy_status = ''

            try:
                sale_status = data[10]
                if sale_status == '' or sale_status == '---':
                    sale_status = ''
            except:
                sale_status = ''

            try:
                handling_fee = float(data[20].replace('%', ''))
                if handling_fee == '' or handling_fee == '---':
                    handling_fee = -999.0000
            except:
                handling_fee = -999.0000

            table_key = '{}_{}'.format(data[0], jz_date)

            data_list.append((
                fund_code,
                fund_name,
                fund_name_pin_yin,
                dwjz,
                ljjz,
                dwjz_day_before,
                ljjz_day_before,
                daily_growth_value,
                daily_growth_rate,
                buy_status,
                sale_status,
                handling_fee,
                jz_date,
                jz_date_day_before,
                table_key))
        self.mc.insert_many(self.jing_zhi_insert_sql, tuple(data_list))



class FundJingZhiHistroySpiderPipeline:

    def __init__(self):
        self.mc = MySQLClient(DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT)
        self.jing_zhi_insert_sql = 'INSERT INTO `fund_jing_zhi_history`(`fund_code`, `fund_name`, `fund_name_pin_yin`, `dwjz`, `ljjz`, `dwjz_day_before`, `ljjz_day_before`, `daily_growth_value`, `daily_growth_rate`, `buy_status`, `sale_status`, `handling_fee`, `jz_date`, `jz_date_day_before`, `table_key`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE fund_code=VALUES(fund_code), fund_name=VALUES(fund_name), fund_name_pin_yin=VALUES(fund_name_pin_yin), dwjz=VALUES(dwjz), ljjz=VALUES(ljjz), dwjz_day_before=VALUES(dwjz_day_before), ljjz_day_before=VALUES(ljjz_day_before), daily_growth_value=VALUES(daily_growth_value), daily_growth_rate=VALUES(daily_growth_rate), buy_status=VALUES(buy_status), sale_status=VALUES(sale_status), handling_fee=VALUES(handling_fee), jz_date=VALUES(jz_date), jz_date_day_before=VALUES(jz_date_day_before), table_key=VALUES(table_key)'

    def process_item(self, item, spider):
        data_list = item['jing_zhi']
        self.mc.insert_many(self.jing_zhi_insert_sql, tuple(data_list))