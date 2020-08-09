# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from elasticsearch import Elasticsearch
from elasticsearch import helpers


class FundGuZhiSpiderPipeline:

    def __init__(self):
        self.es_hosts = {
            "192.168.31.116": 9200
        }
        self.es = Elasticsearch(hosts=self.es_hosts)
        # self.body = {
        #     "query": {
        #         "match": {
        #             "name": "Danny"
        #         }
        #     }
        # }
        # result = self.es.search(body=self.body, index='users')

    def process_item(self, item, spider):
        gu_zhi = item['gu_zhi']
        data_list = []
        for data in gu_zhi:
            # print(i)
            data['_index'] = 'tian_tian_fund_gu_zhi'

            if data['bzdm'] != '' and data['bzdm'] != '---':
                data['bzdm'] = int(data['bzdm'])
            else:
                data['bzdm'] = -200
            #
            if data['FScaleType'] != '' and data['FScaleType'] != '---':
                data['FScaleType'] = int(data['FScaleType'])
            else:
                data['FScaleType'] = -200
            #
            if data['JJGSID'] != '' and data['JJGSID'] != '---':
                data['JJGSID'] = int(data['JJGSID'])
            else:
                data['JJGSID'] = -200
            #
            if data['IsExchg'] != '' and data['IsExchg'] != '---':
                data['IsExchg'] = int(data['IsExchg'])
            else:
                data['IsExchg'] = -200
            #
            if data['Rate'] != '' and data['Rate'] != '---':
                data['Rate'] = float(data['Rate'].replace('%', ''))
            else:
                data['Rate'] = -200.0
            #
            if data['fundtype'] != '' and data['fundtype'] != '---':
                data['fundtype'] = int(data['fundtype'])
            else:
                data['fundtype'] = -200

            if data['IsListTrade'] != '' and data['IsListTrade'] != '---':
                data['IsListTrade'] = int(data['IsListTrade'])
            else:
                data['IsListTrade'] = -200

            if data['isbuy'] != '' and data['isbuy'] != '---':
                data['isbuy'] = int(data['isbuy'])
            else:
                data['isbuy'] = -200

            if data['gspc'] != '' and data['gspc'] != '---':
                data['gspc'] = float(data['gspc'].replace('%', ''))
            else:
                data['gspc'] = -200.0

            if data['gsz'] != '' and data['gsz'] != '---':
                data['gsz'] = float(data['gsz'])
            else:
                data['gsz'] = -200.0

            if data['gszzl'] != '' and data['gszzl'] != '---':
                data['gszzl'] = float(data['gszzl'].replace('%', ''))
            else:
                data['gszzl'] = -200.0

            if data['jzzzl'] != '' and data['jzzzl'] != '---':
                data['jzzzl'] = float(data['jzzzl'].replace('%', ''))
            else:
                data['jzzzl'] = -200.0

            if data['dwjz'] != '' and data['dwjz'] != '---':
                data['dwjz'] = float(data['dwjz'].replace('%', ''))
            else:
                data['dwjz'] = -200.0

            if data['gbdwjz'] != '' and data['gbdwjz'] != '---':
                data['gbdwjz'] = float(data['gbdwjz'])
            else:
                data['gbdwjz'] = -200.0

            data_list.append(data)

        helpers.bulk(self.es, actions=data_list)

        # return item


class FundJingZhiSpiderPipeline:
    def __init__(self):
        self.es_hosts = {
            "192.168.31.116": 9200
        }
        self.es = Elasticsearch(hosts=self.es_hosts)

    def process_item(self, item, spider):
        # print(item['gu_zhi'])
        gu_zhi = item['jing_zhi']
        show_day = item['show_day']
        data_list = []
        key_list = ['fund_code', 'fund_name', 'fund_name_en', 'dwjz1', 'ljjz1', 'dwjz2', 'ljjz2', 'day_value', 'day_rate', 'buy_status', 'sale_status',
                    'field1', 'field2', 'field3', 'field4', 'field5', 'field6', 'field7', 'field8', 'field9', 'handling_fee', ]

        for i in gu_zhi:
            data = {}
            for m, n in zip(key_list, i):
                # if m == 'fund_code':
                #     n = int(n)
                # if m == 'dwjz1':
                #     n = float(n)
                # if m == 'ljjz1':
                #     n = float(n)
                # if m == 'dwjz2':
                #     n = float(n)
                # if m == 'ljjz2':
                #     n = float(n)

                data[m] = n

            if data['fund_code'] != '':
                data['fund_code'] = int(data['fund_code'])
            else:
                data['fund_code'] = -200

            if data['dwjz1'] != '':
                data['dwjz1'] = float(data['dwjz1'])
            else:
                data['dwjz1'] = -200.0

            if data['ljjz1'] != '':
                data['ljjz1'] = float(data['ljjz1'])
            else:
                data['ljjz1'] = -200.0

            if data['dwjz2'] != '':
                data['dwjz2'] = float(data['dwjz2'])
            else:
                data['dwjz2'] = -200.0

            if data['ljjz2'] != '':
                data['ljjz2'] = float(data['ljjz2'])
            else:
                data['ljjz2'] = -200.0

            if data['day_value'] != '':
                data['day_value'] = float(data['day_value'])
            else:
                data['day_value'] = -200.0

            if data['day_rate'] != '':
                data['day_rate'] = float(data['day_rate'])
            else:
                data['day_rate'] = -200.0

            if data['handling_fee'] != '':
                data['handling_fee'] = float(data['handling_fee'].replace('%', ''))
            else:
                data['handling_fee'] = -200.0

                # print(i)
                # print(len(i))
            data['_index'] = 'tian_tian_fund_jing_zhi'
            data['show_day'] = show_day
            data['date1'] = show_day[0]
            data['date2'] = show_day[1]
            print(data)
            data_list.append(data)
        helpers.bulk(self.es, actions=data_list)

        # return item
