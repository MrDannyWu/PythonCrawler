import scrapy
import json
from tian_tian_fund_spider.items import FundGuZhiSpiderItem


class FundGuZhiSpiderSpider(scrapy.Spider):
    """
    抓取天天基金估值
    """
    custom_settings = {
        'ITEM_PIPELINES': {
            'tian_tian_fund_spider.pipelines.FundGuZhiSpiderPipeline': 300,
        }
    }
    name = 'fund_gu_zhi_spider'
    allowed_domains = ['fund.eastmoney.com']
    start_urls = [
        'http://api.fund.eastmoney.com/FundGuZhi/GetFundGZList?type=1&sort=3&orderType=desc&canbuy=0&pageIndex={}&pageSize=200&callback=jQuery183019877059102314365_1596370479764&_=1596370517255'.format(
            i) for i in range(1, 47)]

    def parse(self, response):
        # print(response.text)
        # tr_list = response.xpath('//tbody[@id="tableContent"]/tr')
        # for i in tr_list:
        #     print(i)
        item = FundGuZhiSpiderItem()
        # print(response.text.replace('({', '{').replace('})', '}'))
        json_data = json.loads('{' + response.text.split('({')[1].replace('})', '}'), encoding='utf-8')['Data']['list']
        # for i in json_data:
        #     item = TianTianFundSpiderItem()
        #     item = i
        item['gu_zhi'] = json_data
        yield item
