# -*- coding: utf-8 -*-
import scrapy
from amazon.items import AmazonItem
import datetime


class GetCategoryProductSpider(scrapy.Spider):
    name = 'get_category_product'
    allowed_domains = ['amazon.com']
    host = 'https://www.amazon.com'
    start_urls = ['https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_unv_0_amazon-devices_1']
    custom_settings = {
        'ITEM_PIPELINES': {'amazon.pipelines.AmazonPipeline': 300}
    }

    def parse(self, response):
        """
        获取并检验第一层菜单下面还有没有子菜单
        :param response: response
        :return: null
        """
        up_category = 'Any Department:::https://www.amazon.com/Best-Sellers/zgbs/'
        a_text_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/li/a/text()').extract()
        a_link_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/li/a/@href').extract()
        if len(a_link_list) > 0:
            for a_text, a_link in zip(a_text_list, a_link_list):
                if 'Beauty & Personal Care' == a_text:
                    current_category = up_category + '-->' + a_text.strip() + ':::' + a_link.strip().split('ref=')[0]
                    url = a_link.strip().split('ref=')[0]
                    resp = scrapy.Request(url, meta={'meta_1': current_category}, callback=self.parse_one)
                    yield resp
        else:
            item = AmazonItem()
            product_link_list = response.xpath('//ol[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
            for link in product_link_list:
                item['product_url'] = self.host + link.split('?')[0]
                item['product_url_page_num'] = item['product_url'].split('/')[-1]
                item['product_category'] = up_category
                item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item['error'] = 'yes'
                yield item
            next_page_url = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
            resp = scrapy.Request(next_page_url, callback=self.get_next_page_data)
            yield resp

    def parse_one(self, response):
        """
        获取并检验第二层菜单下面还有没有子菜单
        :param response: response
        :return: null
        """
        up_category = response.meta['meta_1']
        print(up_category)
        a_text_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/li/a/text()').extract()
        a_link_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/li/a/@href').extract()
        if len(a_link_list) > 0:
            for a_text, a_link in zip(a_text_list, a_link_list):
                current_category = up_category + '-->' + a_text.strip() + ':::' + a_link.strip().split('ref=')[0]
                url = a_link.strip().split('ref=')[0]
                resp = scrapy.Request(url, meta={'meta_2': current_category}, callback=self.parse_two)
                yield resp
        else:
            item = AmazonItem()
            product_link_list = response.xpath('//ol[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
            for link in product_link_list:
                item['product_url'] = self.host + link.split('?')[0]
                item['product_url_page_num'] = item['product_url'].split('/')[-1]
                item['product_category'] = up_category
                item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item['error'] = 'yes'
                yield item
            next_page_url = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
            resp = scrapy.Request(next_page_url, meta={'product_category': up_category}, callback=self.get_next_page_data)
            yield resp

    def parse_two(self, response):
        """
        获取并检验第三层菜单下面还有没有子菜单
        :param response: response
        :return: null
        """
        up_category = response.meta['meta_2']
        print(up_category)
        a_text_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/li/a/text()').extract()
        a_link_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/li/a/@href').extract()
        if len(a_link_list) > 0:
            for a_text, a_link in zip(a_text_list, a_link_list):
                print(a_text, a_link)
                current_category = up_category + '-->' + a_text.strip() + ':::' + a_link.strip().split('ref=')[0]
                url = a_link.strip().split('ref=')[0]
                resp = scrapy.Request(url, meta={'meta_3': current_category}, callback=self.parse_three)
                yield resp
        else:
            item = AmazonItem()
            product_link_list = response.xpath('//ol[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
            for link in product_link_list:
                item['product_url'] = self.host + link.split('?')[0]
                item['product_url_page_num'] = item['product_url'].split('/')[-1]
                item['product_category'] = up_category
                item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item['error'] = 'yes'
                yield item
            next_page_url = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
            resp = scrapy.Request(next_page_url, meta={'product_category': up_category}, callback=self.get_next_page_data)
            yield resp

    def parse_three(self, response):
        """
        获取并检验第四层菜单下面还有没有子菜单
        :param response: response
        :return: null
        """
        up_category = response.meta['meta_3']
        a_text_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/li/a/text()').extract()
        a_link_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/li/a/@href').extract()
        if len(a_link_list) > 0:
            for a_text, a_link in zip(a_text_list, a_link_list):
                current_category = up_category + '-->' + a_text.strip() + ':::' + a_link.strip().split('ref=')[0]
                print(a_text, a_link)
                url = a_link.strip().split('ref=')[0]
                resp = scrapy.Request(url, meta={'meta_4': current_category}, callback=self.parse_four)
                yield resp
        else:
            item = AmazonItem()
            product_link_list = response.xpath('//ol[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
            for link in product_link_list:
                item['product_url'] = self.host + link.split('?')[0]
                item['product_url_page_num'] = item['product_url'].split('/')[-1]
                item['product_category'] = up_category
                item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item['error'] = 'yes'
                yield item
            next_page_url = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
            resp = scrapy.Request(next_page_url, meta={'product_category': up_category}, callback=self.get_next_page_data)
            yield resp

    def test(self, response):
        pass

    def parse_four(self, response):
        """
        获取并检验第五层菜单下面还有没有子菜单
        :param response: response
        :return: null
        """
        up_category = response.meta['meta_4']
        a_text_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/li/a/text()').extract()
        a_link_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/li/a/@href').extract()
        if len(a_link_list) > 0:
            for a_text, a_link in zip(a_text_list, a_link_list):
                current_category = up_category + '-->' + a_text.strip() + ':::' + a_link.strip().split('ref=')[0]
                print(a_text, a_link)
                url = a_link.strip().split('ref=')[0]
                resp = scrapy.Request(url, meta={'meta_5': current_category}, callback=self.parse_five)
                yield resp
        else:
            item = AmazonItem()
            product_link_list = response.xpath('//ol[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
            for link in product_link_list:
                item['product_url'] = self.host + link.split('?')[0]
                item['product_url_page_num'] = item['product_url'].split('/')[-1]
                item['product_category'] = up_category
                item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item['error'] = 'yes'
                yield item
            next_page_url = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
            resp = scrapy.Request(next_page_url, meta={'product_category': up_category}, callback=self.get_next_page_data)
            yield resp

    def parse_five(self, response):
        """
        获取并检验第六层菜单下面还有没有子菜单
        :param response: response
        :return: null
        """
        up_category = response.meta['meta_5']
        a_text_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/ul/li/a/text()').extract()
        a_link_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/ul/li/a/@href').extract()
        if len(a_link_list) > 0:
            for a_text, a_link in zip(a_text_list, a_link_list):
                current_category = up_category + '-->' + a_text.strip() + ':::' + a_link.strip().split('ref=')[0]
                print(a_text, a_link)
                url = a_link.strip().split('ref=')[0]
                resp = scrapy.Request(url, meta={'meta_6': current_category}, callback=self.parse_six)
                yield resp
        else:
            item = AmazonItem()
            product_link_list = response.xpath('//ol[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
            for link in product_link_list:
                item['product_url'] = self.host + link.split('?')[0]
                item['product_url_page_num'] = item['product_url'].split('/')[-1]
                item['product_category'] = up_category
                item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item['error'] = 'yes'
                yield item
            next_page_url = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
            resp = scrapy.Request(next_page_url, meta={'product_category': up_category}, callback=self.get_next_page_data)
            yield resp

    def parse_six(self, response):
        """
        获取并检验第七层菜单下面还有没有子菜单
        :param response: response
        :return: null
        """
        up_category = response.meta['meta_6']
        a_text_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/ul/ul/li/a/text()').extract()
        a_link_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/ul/ul/li/a/@href').extract()
        if len(a_link_list) > 0:
            for a_text, a_link in zip(a_text_list, a_link_list):
                current_category = up_category + '-->' + a_text.strip() + ':::' + a_link.strip().split('ref=')[0]
                print(a_text, a_link)
                url = a_link.strip().split('ref=')[0]
                resp = scrapy.Request(url, meta={'meta_7': current_category}, callback=self.parse_seven)
                yield resp
        else:
            item = AmazonItem()
            product_link_list = response.xpath('//ol[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
            for link in product_link_list:
                item['product_url'] = self.host + link.split('?')[0]
                item['product_url_page_num'] = item['product_url'].split('/')[-1]
                item['product_category'] = up_category
                item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item['error'] = 'yes'
                yield item
            next_page_url = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
            resp = scrapy.Request(next_page_url, meta={'product_category': up_category}, callback=self.get_next_page_data)
            yield resp

    def parse_seven(self, response):
        """
        获取并检验第八层菜单下面还有没有子菜单
        :param response: response
        :return: null
        """
        up_category = response.meta['meta_7']
        a_text_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/ul/ul/ul/li/a/text()').extract()
        a_link_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/ul/ul/ul/li/a/@href').extract()
        if len(a_link_list) > 0:
            for a_text, a_link in zip(a_text_list, a_link_list):
                current_category = up_category + '-->' + a_text.strip() + ':::' + a_link.strip().split('ref=')[0]
                print(a_text, a_link)
                url = a_link.strip().split('ref=')[0]
                resp = scrapy.Request(url, meta={'meta_8': current_category}, callback=self.parse_eight)
                yield resp
        else:
            item = AmazonItem()
            product_link_list = response.xpath('//ol[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
            for link in product_link_list:
                item['product_url'] = self.host + link.split('?')[0]
                item['product_url_page_num'] = item['product_url'].split('/')[-1]
                item['product_category'] = up_category
                item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item['error'] = 'yes'
                yield item
            next_page_url = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
            resp = scrapy.Request(next_page_url, meta={'product_category': up_category}, callback=self.get_next_page_data)
            yield resp

    def parse_eight(self, response):
        """
        获取并检验第九层菜单下面还有没有子菜单
        :param response: response
        :return: null
        """
        up_category = response.meta['meta_8']
        a_text_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/ul/ul/ul/ul/li/a/text()').extract()
        a_link_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/ul/ul/ul/ul/li/a/@href').extract()
        if len(a_link_list) > 0:
            for a_text, a_link in zip(a_text_list, a_link_list):
                current_category = up_category + '-->' + a_text.strip() + ':::' + a_link.strip().split('ref=')[0]
                print(a_text, a_link)
                url = a_link.strip().split('ref=')[0]
                resp = scrapy.Request(url, meta={'meta_9': current_category}, callback=self.parse_nine)
                yield resp
        else:
            item = AmazonItem()
            product_link_list = response.xpath('//ol[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
            for link in product_link_list:
                item['product_url'] = self.host + link.split('?')[0]
                item['product_url_page_num'] = item['product_url'].split('/')[-1]
                item['product_category'] = up_category
                item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item['error'] = 'yes'
                yield item
            next_page_url = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
            resp = scrapy.Request(next_page_url, meta={'product_category': up_category}, callback=self.get_next_page_data)
            yield resp

    def parse_nine(self, response):
        """
        获取并检验第十层菜单下面还有没有子菜单
        :param response: response
        :return: null
        """
        up_category = response.meta['meta_9']
        a_text_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/ul/ul/ul/ul/ul/li/a/text()').extract()
        a_link_list = response.xpath('//ul[@id="zg_browseRoot"]/ul/ul/ul/ul/ul/ul/ul/ul/ul/ul/li/a/@href').extract()
        if len(a_link_list) > 0:
            for a_text, a_link in zip(a_text_list, a_link_list):
                current_category = up_category + '-->' + a_text.strip() + ':::' + a_link.strip().split('ref=')[0]
                print(a_text, a_link)
                url = a_link.strip().split('ref=')[0]
                resp = scrapy.Request(url, meta={'meta_10': current_category}, callback=self.parse_ten)
                yield resp
        else:
            item = AmazonItem()
            product_link_list = response.xpath('//ol[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
            for link in product_link_list:
                item['product_url'] = self.host + link.split('?')[0]
                item['product_url_page_num'] = item['product_url'].split('/')[-1]
                item['product_category'] = up_category
                item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                item['error'] = 'yes'
                yield item
            next_page_url = response.xpath('//li[@class="a-last"]/a/@href').extract_first()
            resp = scrapy.Request(next_page_url, meta={'product_category': up_category}, callback=self.get_next_page_data)
            yield resp

    def parse_ten(self, response):
        print('会到这么？')
        pass

    def get_next_page_data(self, response):
        item = AmazonItem()
        product_category = response.meta['product_category']
        product_link_list = response.xpath('//ol[@id="zg-ordered-list"]/li/span/div/span/a/@href').extract()
        for link in product_link_list:
            item['product_url'] = self.host + link.split('?')[0]
            item['product_url_page_num'] = item['product_url'].split('/')[-1]
            item['product_category'] = product_category
            item['update_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            item['error'] = 'yes'
            yield item
