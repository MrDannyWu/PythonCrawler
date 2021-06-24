# -*- coding: utf-8 -*-
import scrapy
from amazon.db import DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT
import pymysql
import json
import datetime
from amazon.items import GetProductDetailsItem


class GetProductDetailsSpider(scrapy.Spider):
    handle_httpstatus_list = [404, 500]
    name = 'get_product_details'
    allowed_domains = ['amazon.com']
    start_urls = ['']
    custom_settings = {
        'ITEM_PIPELINES': {'amazon.pipelines.GetProductDetailsPipeline': 300}
    }

    def query_product(self):
        """
        查询数据库所有error不为404的产品
        :return: 返回查询结果
        """
        connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
        cursor = connect.cursor()
        # query_all_sql = 'select * from product where class_id = 6768 and asin = "B004O290TW"'
        query_all_sql = 'select * from amz_product where error != "404"'
        cursor.execute(query_all_sql)
        results = cursor.fetchall()
        return results

    def start_requests(self):
        results = self.query_product()
        for product in results:
            product_id = product[0]
            product_class_id = product[1]
            product_url = product[3]
            is_new = product[8]
            meat = {'product_id': product_id, 'product_class_id': product_class_id, 'product_url': product_url, 'is_new': is_new}
            resp = scrapy.Request(product_url, meta=meat, callback=self.parse)
            yield resp

    def parse(self, response):
        item = GetProductDetailsItem()
        product_id = response.meta['product_id']
        product_class_id = response.meta['product_class_id']
        product_url = response.meta['product_url']
        is_new = response.meta['is_new']
        product_name = ''
        product_picture_url = ''
        product_price = ''
        product_stars = ''
        product_reviews = ''
        product_asin = ''
        product_big_class = ''
        product_small_class = ''
        shelf_time = ''
        sale_time = ''

        update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 目前分三种页面排版类型，根据不同的页面的排版来制定相应的方法解析数据
        if len(response.xpath('//div[@id="detail-bullets"]')) > 0:
            # 获取商品名称
            if len(response.xpath('//span[@id="productTitle"]/text()')) > 0:
                product_name = response.xpath('//span[@id="productTitle"]/text()').extract_first().strip()
            else:
                pass

            # 获取商品图片
            if len(response.xpath('//img[@id="landingImage"]')) > 0:
                product_picture_url_list = json.loads(response.xpath('//img[@id="landingImage"]/@data-a-dynamic-image').extract_first().strip())
                keys = []
                for key in product_picture_url_list:
                    keys.append(key)
                product_picture_url = keys[0]
            else:
                pass

            # 获取商品价格
            if len(response.xpath('//span[@id="priceblock_ourprice"]/text()')) > 0:
                product_price = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract_first().strip()
                # print('到这了11111', response.xpath('//span[@id="priceblock_ourprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_snsprice_Based"]/span')) > 0:
                product_price = response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract_first().strip()
                # print('到这了22222', response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract(), aaasin)

            if len(response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]')):
                product_price = response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract_first()
                # print('到这了33333', response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_pospromoprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract_first().strip()
                # print('到这了44444', response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="price_inside_buybox"]')) > 0:
                product_price = response.xpath('//span[@id="price_inside_buybox"]/text()').extract_first().strip()
                # print('到这了55555', response.xpath('//span[@id="price_inside_buybox"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_dealprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_dealprice"]/text()').extract_first().strip()

            if len(response.xpath('//div[@id="csxswImgcsd_0"]/div/span')) > 0:
                product_price = response.xpath('//div[@id="csxswImgcsd_0"]/div/span/text()').extract_first().strip()

            if len(response.xpath('//div[@id="olp-upd-new"]/span/a/text()')) > 0:
                product_price = response.xpath('//div[@id="olp-upd-new"]/span/a/text()').extract_first().split('from')[-1].strip()

            if len(response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span')) > 0:
                product_price = response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span/text()').extract_first().strip()

            # 获取商品star
            if len(response.xpath('//span[@id="acrPopover"]/@title')) > 0:
                product_stars = response.xpath('//span[@id="acrPopover"]/@title').extract_first().split('out of')[0].strip()
            else:
                pass

            # 获取商品reviews
            if len(response.xpath('//span[@id="acrCustomerReviewText"]/text()')) > 0:
                product_reviews = response.xpath('//span[@id="acrCustomerReviewText"]/text()').extract_first().split('customer')[0].strip().replace(',', '')
            else:
                pass

            # 获取商品大类
            if len(response.xpath('//li[@id="SalesRank"]/text()')) > 0:
                xpath_list = response.xpath('//li[@id="SalesRank"]/text()').extract()
                for j in xpath_list:
                    if '#' in j:
                        product_big_class = j.strip().replace(',', '').replace('#', '').split(' ')[0]
                    else:
                        pass
            else:
                pass

            # 获取商品小类
            if len(response.xpath('//li[@id="SalesRank"]/ul/li')) > 0:
                product_small_class = response.xpath('//li[@id="SalesRank"]/ul/li/span/text()').extract_first().strip().replace('#', '')
            else:
                pass

            # 上架时间
            shelf_time = ''
            # 售卖时间
            # sale_time = ''

            item['product_id'] = product_id
            item['product_class_id'] = product_class_id
            item['product_url'] = product_url
            item['product_name'] = product_name
            item['product_picture_url'] = product_picture_url
            item['product_price'] = product_price
            item['product_stars'] = product_stars
            item['product_reviews'] = product_reviews
            item['product_asin'] = product_url.split('/')[-2]
            item['product_big_class'] = product_big_class
            item['product_small_class'] = product_small_class
            item['shelf_time'] = shelf_time
            item['sale_time'] = sale_time
            item['update_time'] = update_time
            item['is_new'] = is_new
            print('detail-bullets形式', product_url, '\n')

        elif len(response.xpath('//table[@id="productDetails_detailBullets_sections1"]')) > 0:
            # 获取商品名称
            if len(response.xpath('//span[@id="productTitle"]/text()')) > 0:
                product_name = response.xpath('//span[@id="productTitle"]/text()').extract_first().strip()
            else:
                pass

            # 获取商品图片
            if len(response.xpath('//img[@id="landingImage"]')) > 0:
                product_picture_url_list = json.loads(response.xpath('//img[@id="landingImage"]/@data-a-dynamic-image').extract_first().strip())
                keys = []
                for key in product_picture_url_list:
                    keys.append(key)
                product_picture_url = keys[0]
            else:
                pass

            # 获取商品价格
            if len(response.xpath('//span[@id="priceblock_ourprice"]/text()')) > 0:
                product_price = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract_first().strip()
                # print('到这了11111', response.xpath('//span[@id="priceblock_ourprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_snsprice_Based"]/span')) > 0:
                product_price = response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract_first().strip()
                # print('到这了22222', response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract(), aaasin)

            if len(response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]')):
                product_price = response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract_first()
                # print('到这了33333', response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract(),aaasin)

            if len(response.xpath('//span[@id="priceblock_pospromoprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract_first().strip()
                # print('到这了44444', response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="price_inside_buybox"]')) > 0:
                product_price = response.xpath('//span[@id="price_inside_buybox"]/text()').extract_first().strip()
                # print('到这了55555', response.xpath('//span[@id="price_inside_buybox"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_dealprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_dealprice"]/text()').extract_first().strip()

            if len(response.xpath('//div[@id="csxswImgcsd_0"]/div/span')) > 0:
                product_price = response.xpath('//div[@id="csxswImgcsd_0"]/div/span/text()').extract_first().strip()

            if len(response.xpath('//div[@id="olp-upd-new"]/span/a/text()')) > 0:
                product_price = response.xpath('//div[@id="olp-upd-new"]/span/a/text()').extract_first().split('from')[-1].strip()

            if len(response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span')) > 0:
                product_price = response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span/text()').extract_first().strip()

            # 获取商品star
            if len(response.xpath('//span[@id="acrPopover"]/@title')) > 0:
                product_stars = response.xpath('//span[@id="acrPopover"]/@title').extract_first().split('out of')[0].strip()
            else:
                pass

            # 获取商品reviews
            if len(response.xpath('//span[@id="acrCustomerReviewText"]/text()')) > 0:
                product_reviews = response.xpath('//span[@id="acrCustomerReviewText"]/text()').extract_first().split('customer')[0].strip().replace(',', '')
            else:
                pass

            # 获取商品大小类
            if len(response.xpath('//table[@id="productDetails_detailBullets_sections1"]/tr')) > 0:
                for tr in response.xpath('//table[@id="productDetails_detailBullets_sections1"]/tr'):
                    if 'Best Sellers Rank' in tr.xpath('./th/text()').extract_first().strip():
                        if len(tr.xpath('./td/span/span[1]')) > 0:
                            product_big_class = tr.xpath('./td/span/span[1]/text()').extract_first().strip().replace('#', '').replace(',', '').split(' ')[0]
                        if len(tr.xpath('./td/span/span[2]')) > 0:
                            product_small_class = tr.xpath('./td/span/span[2]/text()').extract_first().strip().replace('#', '').replace(',', '').split(' ')[0]

            # 上架时间
            if len(response.xpath('//table[@id="productDetails_detailBullets_sections1"]/tr')) > 0:
                for tr in response.xpath('//table[@id="productDetails_detailBullets_sections1"]/tr'):
                    if 'first' in tr.xpath('./th/text()').extract_first().strip().lower():
                        if len(tr.xpath('./td')) > 0:
                            shelf_time = tr.xpath('./td/text()').extract_first().strip()

            # 售卖时间
            # sale_time = ''
            item['product_id'] = product_id
            item['product_class_id'] = product_class_id
            item['product_url'] = product_url
            item['product_name'] = product_name
            item['product_picture_url'] = product_picture_url
            item['product_price'] = product_price
            item['product_stars'] = product_stars
            item['product_reviews'] = product_reviews
            item['product_asin'] = product_url.split('/')[-2]
            item['product_big_class'] = product_big_class
            item['product_small_class'] = product_small_class
            item['shelf_time'] = shelf_time
            item['sale_time'] = sale_time
            item['update_time'] = update_time
            item['is_new'] = is_new
            print('表格形式的产品信息陈列！', product_url, '\n')

        elif len(response.xpath('//div[@id="detailBulletsWrapper_feature_div"]')) > 0:

            # 获取商品名称
            if len(response.xpath('//span[@id="productTitle"]/text()')) > 0:
                product_name = response.xpath('//span[@id="productTitle"]/text()').extract_first().strip()
            else:
                pass

            # 获取商品图片
            if len(response.xpath('//img[@id="landingImage"]')) > 0:
                product_picture_url_list = json.loads(response.xpath('//img[@id="landingImage"]/@data-a-dynamic-image').extract_first().strip())
                keys = []
                for key in product_picture_url_list:
                    keys.append(key)
                product_picture_url = keys[0]
            else:
                pass

            # 获取商品价格
            if len(response.xpath('//span[@id="priceblock_ourprice"]/text()')) > 0:
                product_price = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract_first().strip()
                # print('到这了11111', response.xpath('//span[@id="priceblock_ourprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_snsprice_Based"]/span')) > 0:
                product_price = response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract_first().strip()
                # print('到这了22222', response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract(), aaasin)

            if len(response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]')):
                product_price = response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract_first()
                # print('到这了33333', response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract(),aaasin)

            if len(response.xpath('//span[@id="priceblock_pospromoprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract_first().strip()
                # print('到这了44444', response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="price_inside_buybox"]')) > 0:
                product_price = response.xpath('//span[@id="price_inside_buybox"]/text()').extract_first().strip()
                # print('到这了55555', response.xpath('//span[@id="price_inside_buybox"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_dealprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_dealprice"]/text()').extract_first().strip()

            if len(response.xpath('//div[@id="csxswImgcsd_0"]/div/span')) > 0:
                product_price = response.xpath('//div[@id="csxswImgcsd_0"]/div/span/text()').extract_first().strip()

            if len(response.xpath('//div[@id="olp-upd-new"]/span/a/text()')) > 0:
                product_price = response.xpath('//div[@id="olp-upd-new"]/span/a/text()').extract_first().split('from')[-1].strip()

            if len(response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span')) > 0:
                product_price = response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span/text()').extract_first().strip()

            # 获取商品star
            if len(response.xpath('//span[@id="acrPopover"]/@title')) > 0:
                product_stars = response.xpath('//span[@id="acrPopover"]/@title').extract_first().split('out of')[0].strip()
            else:
                pass

            # 获取商品reviews
            if len(response.xpath('//span[@id="acrCustomerReviewText"]/text()')) > 0:
                product_reviews = response.xpath('//span[@id="acrCustomerReviewText"]/text()').extract_first().split('customer')[0].strip().replace(',', '')
            else:
                pass

            # 获取商品大小类
            if len(response.xpath('//li[@id="SalesRank"]')) > 0:
                for ite in response.xpath('//li[@id="SalesRank"]/text()').extract():
                    if '#' in ite:
                        product_big_class = ite.strip().replace('#', '').replace(',', '').split(' ')[0]
                if len(response.xpath('//li[@id="SalesRank"]/ul/li[1]/span[1]')) > 0:
                    product_small_class = response.xpath('//li[@id="SalesRank"]/ul/li[1]/span[1]/text()').extract_first().strip().replace('#', '').replace(',', '').split(' ')[0]

            # 上架时间
            if len(response.xpath('//div[@id="detailBullets_feature_div"]/ul/li')) > 0:
                for li_tag in response.xpath('//div[@id="detailBullets_feature_div"]/ul/li'):
                    if len(li_tag.xpath('./span/span[1]')) > 0 and 'first listed on' in li_tag.xpath('./span/span[1]/text()').extract_first() and len(li_tag.xpath('./span/span[2]')) > 0:
                        shelf_time = li_tag.xpath('./span/span[2]/text()').extract_first().strip()

            # 售卖时间
            # sale_time = ''
            item['product_id'] = product_id
            item['product_class_id'] = product_class_id
            item['product_url'] = product_url
            item['product_name'] = product_name
            item['product_picture_url'] = product_picture_url
            item['product_price'] = product_price
            item['product_stars'] = product_stars
            item['product_reviews'] = product_reviews
            item['product_asin'] = product_url.split('/')[-2]
            item['product_big_class'] = product_big_class
            item['product_small_class'] = product_small_class
            item['shelf_time'] = shelf_time
            item['sale_time'] = sale_time
            item['update_time'] = update_time
            item['is_new'] = is_new
            print('detailBulletsWrapper_feature_div形式', product_url, '\n')

        elif len(response.xpath('//div[@id="prodDetails"]')) > 0 and len(response.xpath('//table[@id="productDetails_detailBullets_sections1"]')) == 0:
            # 获取商品名称
            if len(response.xpath('//span[@id="productTitle"]/text()')) > 0:
                product_name = response.xpath('//span[@id="productTitle"]/text()').extract_first().strip()
            else:
                pass

            # 获取商品图片
            if len(response.xpath('//img[@id="landingImage"]')) > 0:
                product_picture_url_list = json.loads(response.xpath('//img[@id="landingImage"]/@data-a-dynamic-image').extract_first().strip())
                keys = []
                for key in product_picture_url_list:
                    keys.append(key)
                product_picture_url = keys[0]
            else:
                pass

            # 获取商品价格
            if len(response.xpath('//span[@id="priceblock_ourprice"]/text()')) > 0:
                product_price = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract_first().strip()
                # print('到这了11111', response.xpath('//span[@id="priceblock_ourprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_snsprice_Based"]/span')) > 0:
                product_price = response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract_first().strip()
                # print('到这了22222', response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract(), aaasin)

            if len(response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]')):
                product_price = response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract_first()
                # print('到这了33333', response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()'),aaasin)

            if len(response.xpath('//span[@id="priceblock_pospromoprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract_first().strip()
                # print('到这了44444', response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="price_inside_buybox"]')) > 0:
                product_price = response.xpath('//span[@id="price_inside_buybox"]/text()').extract_first().strip()
                # print('到这了55555', response.xpath('//span[@id="price_inside_buybox"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_dealprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_dealprice"]/text()').extract_first().strip()

            if len(response.xpath('//div[@id="csxswImgcsd_0"]/div/span')) > 0:
                product_price = response.xpath('//div[@id="csxswImgcsd_0"]/div/span/text()').extract_first().strip()

            if len(response.xpath('//div[@id="olp-upd-new"]/span/a/text()')) > 0:
                product_price = response.xpath('//div[@id="olp-upd-new"]/span/a/text()').extract_first().split('from')[-1].strip()

            if len(response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span')) > 0:
                product_price = response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span/text()').extract_first().strip()

            # 获取商品star
            if len(response.xpath('//span[@id="acrPopover"]/@title')) > 0:
                product_stars = response.xpath('//span[@id="acrPopover"]/@title').extract_first().split('out of')[0].strip()
            else:
                pass

            # 获取商品reviews
            if len(response.xpath('//span[@id="acrCustomerReviewText"]/text()')) > 0:
                product_reviews = response.xpath('//span[@id="acrCustomerReviewText"]/text()').extract_first().split('customer')[0].strip().replace(',', '')
            else:
                pass

            # 获取商品大小类
            if len(response.xpath('//li[@id="SalesRank"]/td[2]')) > 0:
                for td_value in response.xpath('//li[@id="SalesRank"]/td[2]/text()').extract():
                    if '#' in td_value:
                        product_big_class = td_value.strip().replace('#', '').replace(',', '').split(' ')[0]
                if len(response.xpath('//li[@id="SalesRank"]/td[2]/ul/li[1]')) > 0:
                    product_small_class = response.xpath('//li[@id="SalesRank"]/td[2]/ul/li[1]/span[1]/text()').extract_first().strip().replace('#', '').replace(',', '').split(' ')[0]

            if len(response.xpath('//tr[@id="SalesRank"]/td[2]')) > 0:
                for td_value in response.xpath('//tr[@id="SalesRank"]/td[2]/text()').extract():
                    if '#' in td_value:
                        product_big_class = td_value.strip().replace('#', '').replace(',', '').split(' ')[0]
                if len(response.xpath('//tr[@id="SalesRank"]/td[2]/ul/li[1]')) > 0:
                    product_small_class = response.xpath('//tr[@id="SalesRank"]/td[2]/ul/li[1]/span[1]/text()').extract_first().strip().replace('#', '').replace(',', '').split(' ')[0]

            # 上架时间
            shelf_time = ''
            # 售卖时间
            # sale_time = ''
            item['product_id'] = product_id
            item['product_class_id'] = product_class_id
            item['product_url'] = product_url
            item['product_name'] = product_name
            item['product_picture_url'] = product_picture_url
            item['product_price'] = product_price
            item['product_stars'] = product_stars
            item['product_reviews'] = product_reviews
            item['product_asin'] = product_url.split('/')[-2]
            item['product_big_class'] = product_big_class
            item['product_small_class'] = product_small_class
            item['shelf_time'] = shelf_time
            item['sale_time'] = sale_time
            item['update_time'] = update_time
            item['is_new'] = is_new
            print('detailBullets_feature_div形式', product_url, '\n')

        else:
            print('还有其他的！', product_url)
            item['product_id'] = product_id
            item['product_class_id'] = product_class_id
            item['product_url'] = product_url
            item['product_name'] = product_name
            item['product_picture_url'] = product_picture_url
            item['product_price'] = product_price
            item['product_stars'] = product_stars
            item['product_reviews'] = product_reviews
            item['product_asin'] = product_url.split('/')[-2]
            item['product_big_class'] = product_big_class
            item['product_small_class'] = product_small_class
            item['shelf_time'] = shelf_time
            item['sale_time'] = sale_time
            item['update_time'] = update_time
            item['is_new'] = is_new
            item['http_status_code'] = response.status

        yield item


