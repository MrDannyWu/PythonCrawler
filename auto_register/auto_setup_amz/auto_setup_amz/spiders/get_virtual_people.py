# -*- coding: utf-8 -*-
import scrapy
import datetime
from auto_setup_amz.items import AutoSetupAmzItem


class GetVirtualPeopleSpider(scrapy.Spider):
    name = 'get_virtual_people'
    allowed_domains = ['fakenamegenerator.com']
    start_urls = []
    for i in range(1000):
        start_urls.append('https://www.fakenamegenerator.com/gen-random-us-us.php')
        start_urls.append('https://www.fakenamegenerator.com/gen-random-en-uk.php')
        start_urls.append('https://www.fakenamegenerator.com/gen-random-fr-fr.php')
        start_urls.append('https://www.fakenamegenerator.com/gen-random-en-ca.php')
        start_urls.append('https://www.fakenamegenerator.com/gen-random-gr-gr.php')
        start_urls.append('https://www.fakenamegenerator.com/gen-random-it-it.php')
        start_urls.append('https://www.fakenamegenerator.com/gen-random-sp-sp.php')
        start_urls.append('https://www.fakenamegenerator.com/gen-random-ar-us.php')

    def parse(self, response):
        # response.encoding = 'utf-8'
        # print(response.text)
        request_url = response.request.url
        item = AutoSetupAmzItem()
        name = ''
        name_set = request_url.split('random-')[1].split('.')[0].split('-')[0]

        country = request_url.split('random-')[1].split('.')[0].split('-')[1]

        if name_set == 'ar':
            name_set == 'ae'
            country = 'ae'
        # address = scrapy.Field()
        phone = ''
        card = ''
        expires = ''
        cvv2 = ''
        username = ''
        password = ''
        error = ''
        spider = ''
        report_date = datetime.datetime.now().strftime('%Y-%m-%d')
        update_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # if len(response.xpath('//h3/text()')) > 0:
        #     name = response.xpath('//h3/text()').extract_first()
        if len(response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="info"]/div[@class="content"]/div[@class="extra"]/dl')) > 0:
            dl_list = response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="info"]/div[@class="content"]/div[@class="extra"]/dl')
            # print('sssssssssssssssssssss', len(response.xpath('//div[@id="details"]/div[@class="content"]/div[@class="info"]/div[@class="content"]/div[@class="extra"]/dl')))
            for x in dl_list:
                if len(x.xpath('./dt')) > 0 and 'phone' in x.xpath('./dt/text()').extract_first().lower() and len(x.xpath('./dd')) > 0:
                    # print(x.xpath('./dt/text()').extract_first())
                    phone = x.xpath('./dd/text()').extract_first().strip()
                    # print(phone)
                if len(x.xpath('./dt')) > 0 and ('visa' in x.xpath('./dt/text()').extract_first().lower() or 'mastercard' in x.xpath('./dt/text()').extract_first().lower()) and len(x.xpath('./dd')) > 0:
                    # print(x.xpath('./dt/text()').extract_first())
                    card = x.xpath('./dd/text()').extract_first().strip()
                    # print(card)
                if len(x.xpath('./dt')) > 0 and 'expires' in x.xpath('./dt/text()').extract_first().lower() and len(x.xpath('./dd')) > 0:
                    # print(x.xpath('./dt/text()').extract_first())
                    expires = x.xpath('./dd/text()').extract_first().strip()
                    # print(expires)
                if len(x.xpath('./dt')) > 0 and ('cvv2' in x.xpath('./dt/text()').extract_first().lower() or 'cvc2' in x.xpath('./dt/text()').extract_first().lower()) and len(x.xpath('./dd')) > 0:
                    # print(x.xpath('./dt/text()').extract_first())
                    cvv2 = x.xpath('./dd/text()').extract_first().strip()
                    # print(cvv2)
            item['name'] = name
            item['name_set'] = name_set
            item['country'] = country
            item['phone'] = phone
            item['card'] = card
            item['expires'] = expires
            item['cvv2'] = cvv2
            item['username'] = username
            item['password'] = password
            item['error'] = error
            item['spider'] = 1
            item['report_date'] = report_date
            item['update_time'] = update_time
            item['is_used'] = 0
            yield item
        # else:
        #     item['name'] = name
        #     item['name_set'] = name_set
        #     item['country'] = country
        #     item['phone'] = phone
        #     item['card'] = card
        #     item['expires'] = expires
        #     item['cvc2'] = cvc2
        #     item['username'] = username
        #     item['password'] = password
        #     item['error'] = error
        #     item['spider'] = spider
        #     item['status'] = status
        #     item['report_date'] = report_date
        #     item['update_time'] = update_time
        #     item['is_used'] = 0
        #     yield item