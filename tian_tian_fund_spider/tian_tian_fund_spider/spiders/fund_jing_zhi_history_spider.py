import scrapy
import json
from tian_tian_fund_spider.items import FundJingZhiHistorySpiderItem
from hahaha_utils.mysql_client import MySQLClient
from tian_tian_fund_spider.settings import ES_HOST, ES_PORT, DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME
from urllib import parse as url_parse


class FundJingZhiSpiderSpider(scrapy.Spider):
    """
    抓取天天基金净值
    """
    custom_settings = {

        'DEFAULT_REQUEST_HEADERS': {
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'fund.eastmoney.com',
            'Referer': 'http://fund.eastmoney.com',
        },
        'ITEM_PIPELINES': {
            'tian_tian_fund_spider.pipelines.FundJingZhiHistroySpiderPipeline': 300,
        }
    }
    msc = MySQLClient(DB_HOST, DB_USER, DB_PASS, DB_NAME, DB_PORT)
    query_sql = 'SELECT DISTINCT fund_code, fund_name, fund_name_pin_yin FROM fund_jing_zhi'

    name = 'fund_jing_zhi_history_spider'
    allowed_domains = ['fund.eastmoney.com']

    data_list = msc.fetch_all(query_sql)
    start_urls = []
    for data in data_list:
        fund_code = data[0]
        fund_name = data[1]
        fund_name_pin_yin = data[2]
        start_urls.append('https://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18301333693608415918_1639063874620&fundCode={}&pageIndex=1&pageSize=20000&startDate=&endDate=&_=1639063905699&aaa={}&bbb={}'.format(fund_code, fund_name, fund_name_pin_yin))

    def parse(self, response):

        item = FundJingZhiHistorySpiderItem()

        json_data = json.loads('{"Data": ' +response.text.split('{"Data":')[1][:-1], encoding='utf-8')

        # 获取请求的url，根据url获取fund_code，fund_name，fund_name_pin_yin
        request_url = url_parse.unquote(response.url)
        fund_code = request_url.split('fundCode=')[-1].split('&')[0].strip()
        fund_name = request_url.split('aaa=')[-1].split('&')[0].strip()
        fund_name_pin_yin = request_url.split('bbb=')[-1].split('&')[0].strip()

        # 历史数据接口没有这些字段，所以给个默认值
        dwjz_day_before = -999.0000
        ljjz_day_before = -999.0000
        daily_growth_value = -999.0000
        handling_fee = -999.0000
        jz_date_day_before = '1970-01-01'

        # 遍历所有的历史记录
        data_list = []
        for data in json_data['Data']['LSJZList']:
            try:
                jz_date = data['FSRQ']
            except:
                jz_date = '1970-01-01'

            try:
                dwjz = data['DWJZ']
                if dwjz == '' or dwjz == '---':
                    dwjz = -999.0000
            except:
                dwjz = -999.0000

            try:
                ljjz = data['LJJZ']
                if ljjz == '' or ljjz == '---':
                    ljjz = -999.0000
            except:
                ljjz = -999.0000

            try:
                daily_growth_rate = data['JZZZL']
                if daily_growth_rate == '' or daily_growth_rate == '---':
                    daily_growth_rate = -999.0000
            except:
                daily_growth_rate = -999.0000

            try:
                buy_status = data['SGZT']
            except:
                buy_status = ''

            try:
                sale_status = data['SHZT']
            except:
                sale_status = ''

            # SDATE = data['SDATE']
            # ACTUALSYI = data['ACTUALSYI']
            # NAVTYPE = data['NAVTYPE']
            # FHFCZ = data['FHFCZ']
            # FHFCBZ = data['FHFCBZ']
            # DTYPE = data['DTYPE']
            # FHSP = data['FHSP']

            table_key = '{}_{}'.format(fund_code, jz_date)

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

        item['jing_zhi'] = data_list
        yield item
