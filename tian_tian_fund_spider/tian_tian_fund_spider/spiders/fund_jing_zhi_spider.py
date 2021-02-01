import scrapy
import json
from tian_tian_fund_spider.items import FundJingZhiSpiderItem


class FundJingZhiSpiderSpider(scrapy.Spider):
    """
    抓取天天基金净值
    """
    custom_settings = {

        'DEFAULT_REQUEST_HEADERS': {
            'Connection': 'keep-alive',
            # 'Cookie': 'st_si=40529082525104; st_asi=delete; st_pvi=51871271130091; st_sp=2020-08-02%2018%3A55%3A50; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=10; st_psi=20200802201439758-0-7839806187',
            'DNT': '1',
            'Host': 'fund.eastmoney.com',
            'Referer': 'http://fund.eastmoney.com',
        },
        'ITEM_PIPELINES': {
            'tian_tian_fund_spider.pipelines.FundJingZhiSpiderPipeline': 300,
        }
    }
    name = 'fund_jing_zhi_spider'
    allowed_domains = ['fund.eastmoney.com']
    start_urls = ['http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page={},200&dt=1596373971516&atfc=&onlySale=0'.format(i) for i in range(1, 47)]

    def parse(self, response):
        item = FundJingZhiSpiderItem()
        # print(response.text)
        # tr_list = response.xpath('//tbody[@id="tableContent"]/tr')
        # for i in tr_list:
        #     print(i)
        # print(response.text.split('datas:')[1].split(',count:')[0])
        json_data = json.loads(response.text.split('datas:')[1].split(',count:')[0], encoding='utf-8')
        show_day = json.loads(response.text.split('showday:')[1].replace(']}', ']'), encoding='utf-8')
        # print(json_data)
        # for i in json_data:
        #     item = FundJingZhiSpiderItem()
        #     data = {}
        #     for j, k in zip(i, range(50)):
        #         data['field{}'.format(k)] = j
        #     item = data
        item['jing_zhi'] = json_data
        item['show_day'] = show_day
        yield item
