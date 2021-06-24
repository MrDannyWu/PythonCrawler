# -*- coding: utf-8 -*-
import scrapy
import requests
from bs4 import BeautifulSoup
from amz_sale_monitoring.items import AmzSaleMonitoringItem
from ..db import *
from ..db_utils import *
import datetime
from random import choice

class SaleMonitoringSpider(scrapy.Spider):
    # asin_text = 'B07D3C6NVL'
    # country_code_text = 'us'
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now_time)
    connect = connect_db(DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT)
    connect_proxy = connect_db(DB_HOST_P, DB_USER_P, DB_PASS_P, DATABASE_P, DB_PORT_P)

    header = {
        'cookie': 'session-id-time=2082787201l; session-id=130-9086340-7074154; ubid-main=130-0736566-9403533; sp-cdn="L5Z9:UM"; sst-main=Sst1|PQFV-XxZrs_RWWe4bZn8b204C2N6zWxJdPzz7g0-Itlmm2-8CF1iTI-cH_7Jpg24x-AIG_go_pXE_G1O931bKzICOdU3489YvhDwmc21DBhMGdDuIfmK_VsGQ0xIrw6IDpd5kJrhKO2jZkBCK0c77atxXhHcYlrAtFsteDjcyxOL-1FrjDKUsM0fvlArlfi8Wd-UodtqLPQD_20WIX4SROZ4s1Z2nTZ7f-Z6RwwvYtfY5_Gh4LDaS6LvepyJVlsDzkZxsJJLmCXlDheu2c5eAY7WnJpqbI8tEQ6pIUAD2rr6yXtWw6nP7v2THChZbv3IAWqkciGKz-lGznrU9VBZyiP2lA; i18n-prefs=USD; session-token=rqu+W6cvxuPC96AJVLGukWnGlrRI3t3uFrd25CFwYACLLJ6o00zc6hSPzyin7dTla0M+Pf6z+qOtrV4kqzLbvE4zkku5+JEtgUZ4RkTPfjvokxneQPxWRGDGKViDUSMrhkqpAe8u8UEr9wKZ5IWJRtHujUTkxuJCcHpFIAURPP8a/bj9cCFsH04W1IQUY9Ikg1w0GgEtzkgsR/tEuVz3bWE4BnlbsJxcNWK9g4/f1uOBwoOhQCxv3+gb57xleOhq; s_pers=%20s_fid%3D158CE4CD3FE83D21-0953BD0EFD2BA519%7C1735638258251%3B%20s_dl%3D1%7C1577787258252%3B%20gpv_page%3DProject%2520Zero%253A%2520Home%7C1577787258254%3B%20s_ev15%3D%255B%255B%2527NSBaidu%2527%252C%25271577785458256%2527%255D%255D%7C1735638258256%3B; x-wl-uid=1YGLlB4sarOeeU5OBsRmJcj2pP6xtF5Em5f2heGt4iCr9y1+b3Np3DIjHlqgEG1uzpVZCWfWszdTvq+mwx/98HQ==; cdn-session=AK-fb6183cac934fa0a008c411db2acb8f7; csm-hit=tb:2GQSS62PMRMEJS8QKJZE+s-YAP66R2WT531E1SZD43C|1578038379990&t:1578038379990&adb:adblk_no',
        'referer': 'https://www.amazon.com/',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
    }
    name = 'sale_monitoring'
    allowed_domains = ['amazon.com']

    def process_group_url(country_code, asin):
        domain_suffix = ''
        if country_code.lower() == 'us':
            domain_suffix = 'com'
        elif country_code.lower() == 'uk':
            domain_suffix = 'co.uk'
        elif country_code.lower() == 'ca':
            domain_suffix = 'ca'
        elif country_code.lower() == 'fr':
            domain_suffix = 'fr'
        elif country_code.lower() == 'de':
            domain_suffix = 'de'
        elif country_code.lower() == 'it':
            domain_suffix = 'it'
        elif country_code.lower() == 'ae':
            domain_suffix = 'ae'
        elif country_code.lower() == 'es':
            domain_suffix = 'es'
        elif country_code.lower() == 'in':
            domain_suffix = 'in'
        elif country_code.lower() == 'au':
            domain_suffix = 'com.au'
        elif country_code.lower() == 'mx':
            domain_suffix = 'com.mx'

        else:
            domain_suffix = country_code.lower()
        group_url = 'https://www.amazon.{}/gp/offer-listing/{}'.format(domain_suffix, asin)
        return group_url

    update_sql = 'update erp_amz_follow_sell_remind set put_status=3'

    # query_sql = 'select website, asin, exclude_stores from erp_amz_follow_sell_remind where put_status = 1 and endTime > "{}"'.format(now_time)
    query_sql = 'select website, asin, exclude_stores from erp_amz_follow_sell_remind'
    print(query_sql)
    query_re = query_results(connect, query_sql)
    print(query_re)

    start_urls = []
    asin_data_dic = {}
    for i in query_re[1]:
        group_url = process_group_url(i[0], i[1])
        start_urls.append(group_url)
        asin_data_dic[i[1]] = i[2]
    print(start_urls)
    print(asin_data_dic)

    # def start_requests(self):

    def parse(self, response):
        print(response.request.url)
        # asin = 'B07D3C6NVL'
        # country_code = 'com'
        country_code = response.request.url.split('.')[-1].split('/')[0]
        asin = response.request.url.split('/')[-1]
        shop_name_list = self.asin_data_dic[asin].split('-->')
        print('aaaaaaaaaaaaaaaaaaaaaaaa', shop_name_list)
        item = AmzSaleMonitoringItem()
        print(response)
        # 获取构造产品详情链接
        product_url = response.request.url.replace('gp/offer-listing', 'dp')
        print(product_url)

        try:
            results = response.xpath('//div[@class="a-row a-spacing-mini olpOffer"]')

            print('成功打开跟卖页面！')
            ip_list = []
            query_proxy_sql = 'select proxyIp from proxy where isActive = 1'
            query_result = query_results(self.connect_proxy, query_proxy_sql)
            if query_result[0] > 0:
                ip_tup = query_result[1]

                for i in ip_tup:
                    ip_list.append(i[0])

            if len(ip_list) == 0:
                pass
            else:
                proxy = choice(ip_list)
            proxies = {
                'https': proxy
            }
            print(proxies)
            # 获取sold seller
            try:
                respp = requests.get(product_url, headers=self.header, proxies=proxies)
                # print(respp.text)
                soup = BeautifulSoup(respp.text, 'lxml')
                try:
                    sold_seller = soup.select('#sellerProfileTriggerId')[0].text.strip()
                except Exception as e:
                    sold_seller = ''
                    buy_box = 0
                    print(e)
            except Exception as e:
                sold_seller = ''
                buy_box = 0
                print(e)
            print(sold_seller)
            # print(buy_box)
            # 获取跟卖页面的shop_name 和shop_id 
            shop_list = []
            for i in results:
                # Shop name, id
                try:
                    shop_name = i.xpath('./div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a/text()').extract_first()
                    if shop_name is None:
                        shop_name = 'amazon warehouse'
                    else:
                        shop_name = shop_name.strip()

                except Exception as e:
                    print(e)
                    shop_name = 'amazon warehouse'
                print(shop_name)

                # print('shop_name ', shop_name)
                # print('shop_id ', shop_id)
                # print('buy_box', buy_box)
                if shop_name not in shop_name_list:
                    shop_list.append(shop_name)
            if len(shop_list) == 0:
                print('没有跟卖！111')
                follow_seller_num = 0
                item['asin'] = asin
                item['country_code'] = country_code
                item['follow_seller_num'] = follow_seller_num
                item['error'] = '没有跟卖'
                yield item
            else:
                print('shop_list:', shop_list)
                if len(shop_list) > 0:
                    print('')
                    print('发现 {} 个跟卖卖家：{}'.format(len(shop_list), str(shop_list).replace('[', '').replace(']', '').replace("'", '').replace(',', ' ')))
                follow_seller_num = len(shop_list)
                for i in results:
                    # Shop name, id
                    try:
                        shop_name = i.xpath('./div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a/text()').extract_first()
                        shop_url = i.xpath('./div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a/@href').extract_first()
                        if shop_name is None:
                            shop_name = 'amazon warehouse'
                        else:
                            shop_name = shop_name.strip()
                            if sold_seller == shop_name:
                                buy_box = 1
                            else:
                                buy_box = 0

                        if shop_url is None:
                            shop_id = ''
                            delivery_is_fba = 1
                        else:
                            shop_id = shop_url.strip().split('&')[-1].split('=')[-1]
                            if 'isAmazonFulfilled=1' in shop_url:
                                delivery_is_fba = 1
                            elif 'isAmazonFulfilled=0' in shop_url:
                                delivery_is_fba = 0

                    except Exception as e:
                        print(e)
                        shop_name = 'amazon warehouse'
                        shop_id = ''
                        delivery_is_fba = 0
                    print(shop_name)
                    print(shop_id)
                    print(buy_box)

                    # Price and Currency
                    currency = ''
                    try:
                        price_text = i.xpath('./div/span[@class="a-size-large a-color-price olpOfferPrice a-text-bold"]/text()').extract_first()
                        print(price_text)
                        if price_text is None:
                            price = 0
                            currency = ''

                        elif 'EUR' in price_text and ',' in price_text and '.' in price_text:
                            price = float(price_text.replace('EUR', '').replace('.', '').replace(',', '.').strip())
                            currency = 'EUR'
                            print(currency)
                        elif 'EUR' in price_text and ',' in price_text:
                            price = float(price_text.replace('EUR', '').replace(',', '.').strip())
                            currency = 'EUR'
                            print(currency)
                        elif '$' in price_text and ',' in price_text:
                            price = float(price_text.replace('$', '').replace(',', '').strip())
                            currency = 'USD'
                        elif 'AED' in price_text:
                            price = float(price_text.replace('AED', '').replace(',', '').strip())
                            currency = 'AED'
                        elif '£' in price_text and ',' in price_text:
                            price = float(price_text.replace('£', '').replace(',', '').strip())
                            currency = 'GBP'
                        elif 'CDN$' in price_text and ',' in price_text:
                            price = float(price_text.replace('CDN$', '').replace(',', '').strip())
                            currency = 'CDN'
                        elif 'R$' in price_text and ',' in price_text and '.' in price_text:
                            price = float(price_text.replace('R$', '').replace('.', '').replace(',', '.').strip())
                            currency = 'BRL'
                        elif 'R$' in price_text and ',' in price_text:
                            price = float(price_text.replace('R$', '').replace(',', '.').strip())
                            currency = 'BRL'
                        else:
                            pass

                    except Exception as e:
                        price = 0
                        currency = ''
                        print(e)
                    print('price: ', price)
                    print('currency: ', currency)
                    print('delivery_is_fba: ', delivery_is_fba)

                    # Feedback count
                    try:
                        feedback_count_text = ''
                        feedback_count_temp = i.xpath('./div[@class="a-column a-span2 olpSellerColumn"]/p/text()')
                        for fc in feedback_count_temp:
                            # fc.extract_first()
                            feedback_count_text = feedback_count_text + fc.extract()
                        if feedback_count_text is None:
                            feedback_count = 0
                        elif feedback_count_text.strip() == '':
                            feedback_count = 0
                        else:
                            # print(feedback_count_text)
                            feedback_count = feedback_count_text.strip().split('(')[-1].split(' ')[0]

                    except Exception as e:
                        feedback_count = 0
                        print(e)
                    print('feedback_count', feedback_count)

                    # Feedback star
                    try:
                        feedback_star = i.xpath('./div[@class="a-column a-span2 olpSellerColumn"]/p/i/span/text()').extract_first()
                        if feedback_star is None:
                            feedback_star = 0
                        else:
                            feedback_star = feedback_star.strip().split(' ')[0]

                    except Exception as e:
                        feedback_star = 0
                        print(e)
                    print('feedback_star', feedback_star)
                    item['asin'] = asin
                    item['country_code'] = country_code
                    item['price'] = price
                    item['currency'] = currency
                    item['delivery_is_fba'] = delivery_is_fba
                    item['shop_id'] = shop_id
                    item['shop_name'] = shop_name
                    item['feedback_count'] = feedback_count
                    item['feedback_star'] = feedback_star
                    item['buy_box'] = buy_box
                    item['follow_seller_num'] = follow_seller_num
                    item['error'] = ''
                    item['follow_seller_list'] = shop_list
                    yield item

        except Exception as e:
            print(e)
            print('出错了！')
            # print('没有跟卖！222')
            follow_seller_num = 0
            item['asin'] = asin
            item['country_code'] = country_code
            item['follow_seller_num'] = follow_seller_num
            item['error'] = '出错了'
            yield item
