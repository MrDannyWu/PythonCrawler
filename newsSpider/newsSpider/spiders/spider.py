# -*- coding: utf-8 -*-
import scrapy 
from newsSpider.items import NewsspiderItem
class newsSpider(scrapy.Spider): 
    name = 'news' 
    allowed_domains = ['sina.com.cn'] 
    start_urls = ['http://news.sina.com.cn/guide/'] 
    def parse(self, response):
        # 　以一级目录的“地方站”作为根来循环遍历所有的一级目录url和title
        for each in response.xpath("//div[@id='tab01']/div[@data-sudaclick!='citynav']"): 
            # 获取一级目录的url
            first_url = each.xpath('./h3/a/@href').extract()[0]
            #　循环遍历二级目录url
            for other in each.xpath("./ul/li/a"): 
                #　获取二级目录的url
                if other.xpath('./@href').extract()[0].startswith(first_url):
                    item = NewsspiderItem()
                    second_url = other.xpath('./@href').extract()[0]
                    item['first_url'] = first_url
                    item['second_url'] = second_url
                    # 获取二级目录请求
                    yield scrapy.Request(url=item['second_url'],meta={'meta_1':item},callback=self.second_parse)
    def second_parse(self,response):
        meta_1 = response.meta['meta_1'] 
        items = [] 
        # 循环遍历获取文章url
        for each in response.xpath('//a/@href'):
            if each.extract().encode('utf-8').startswith(meta_1['first_url'].encode('utf-8')) and each.extract().encode('utf-8').endswith('.shtml'.encode('utf-8')):
                item = NewsspiderItem()
                item['first_url'] = meta_1['first_url']
                item['second_url'] = meta_1['second_url']
                item['article_url'] = each.extract()
                items.append(item) 
                # 获取文章请求
                for each in items: 
                    yield scrapy.Request(each['article_url'],meta={'meta_2':each},callback=self.detail_parse)
    def detail_parse(self,response): 
        item = response.meta['meta_2'] 
        # 获取文章的标题，时间，文章内容
        item['head'] = ''.join(response.css("h1::text").extract())
        item['time'] = ''.join(response.css(".date-source .date::text").extract())
        item['article'] = ''.join(response.xpath("//div[@id='artibody']/p/text()").extract())
        # 由于item里面还包含了一级目录和二级目录的url我将剔除它们
        item1 = {
            'head':item['head'],
            'time':item['time'],
            'article':item['article']
        }
        if '2018年11月15日' in str(item1['time']):
            yield item1


