import scrapy
import json


class WebSpiderSpider(scrapy.Spider):
    name = 'web_spider'
    allowed_domains = ['douyin.com']
    start_urls = ['https://www.douyin.com/aweme/v1/web/channel/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&tag_id=&count=10&version_code=160100&version_name=16.1.0&_signature=_02B4Z6wo00d01Q-jdpgAAIDCMCXAvtzor30Po3IAACM.8f']

    def parse(self, response):
        print(response.text)
        json_data = json.loads(response.text)
        print(json_data)
        for i in json_data['aweme_list']:
            print('aaaaaaaaaaaaaaaaaaaaa:', i)
