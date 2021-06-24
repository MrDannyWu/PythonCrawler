from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random
from auto_setup_amz.db import *
from auto_setup_amz.db_utils import *
import requests
from PIL import Image
from io import BytesIO
from auto_setup_amz.fateadm_api import TestFunc
from selenium.webdriver.support.ui import Select


def get_out_amzer(connect, asin, country_code, shop_name):
    shop_name_list = shop_name.split('->')
    if country_code == 'us':
        domain_stuffix = 'com'
        STREET = '16701 Beach Blvd.,Huntington Beach,CA'
        CITY = 'Huntington Beach'
        PROVINCE = 'CA'
        POSTCODE = '92647'
    elif country_code == 'uk':
        domain_stuffix = 'co.uk'
        STREET = 'Lennon Studios, 109 Cambridge Court, Liverpool, L7 7AG, UK'
        CITY = 'Liverpool'
        COUNTRY = 'UK'
        POSTCODE = 'L7 7AG'
    elif country_code == 'ca':
        domain_stuffix = 'ca'
        STREET = '3499 Ashcroft Cres'
        CITY = 'Mississauga'
        PV = 'Ontario'
        COUNTRY = 'UK'
        POSTCODE = 'L5C 2E6'
    elif country_code == 'fr':
        domain_stuffix = 'fr'
        STREET = 'Lennon Studios, 109 Cambridge Court, Liverpool, L7 7AG, UK'
        CITY = 'Liverpool'
        COUNTRY = 'UK'
        POSTCODE = 'L7 7AG'
    else:
        domain_stuffix = country_code
    PASSWORD = '12344321'

    group_url = 'https://www.amazon.{}/gp/offer-listing/{}'.format(domain_stuffix, asin)
    chrome_options = Options()
    # chrome_options.add_argument('blink-settings=imagesEnabled=false')
    # chrome_options.add_argument('--user-data-dir=D:\\ud')
    # # self.chrome_options.add_argument('--proxy-server=' +
    # # proxy.replace('https', 'http'))
    # chrome_options.add_argument('--proxy-server=http://10.11.2.251:3128')
    # chrome_options.add_argument('--proxy-server=http://183.129.244.16:15933')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--headless')
    #
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.set_window_size(1500, 960)
    browser.delete_all_cookies()

    # group_url = 'https://www.amazon.com/gp/offer-listing/B07VJRZ62R'
    browser.get(group_url)
    browser.refresh()
    results = browser.find_elements_by_xpath('//div[@class="a-row a-spacing-mini olpOffer"]')
    print(results)
    print('成功打开跟卖页面！')

    shop_list = []
    for i in results:

        print(i)
        try:
            shop_name = i.find_element_by_xpath('./div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a').text
        except:
            shop_name = 'other'
        id_num = i.find_element_by_xpath('./div[@class="a-column a-span2 olpBuyColumn a-span-last"]/div/form/span/span').get_attribute('id')
        print(shop_name)
        if shop_name not in shop_name_list:
            shop_list.append([shop_name, id_num])
    print(shop_list)
    print(len(shop_list))
    if len(shop_list) > 0:
        browser_1 = webdriver.Chrome(chrome_options=chrome_options)
        browser_1.delete_all_cookies()



        # STREET = '16701 Beach Blvd.,Huntington Beach,CA'
        # CITY = 'Huntington Beach'
        # PROVINCE = 'CA'
        # POSTCODE = '92647'
        # STREET = 'Lennon Studios, 109 Cambridge Court, Liverpool, L7 7AG, UK'
        # CITY = 'Liverpool'
        # PROVINCE = 'CA'
        # COUNTRY = 'UK'
        # POSTCODE = 'L7 7AG'

        query_sql = 'select id,username from email where status = 0 and error = ""'
        results = query_results(connect, query_sql)
        update_sql = 'update email set error="using" where id ={}'.format(results[1][0][0])
        insert_update_drop_data(connect, update_sql, '更新为using')

        results[1][0][0]
        print(results[1][0][0])
        print(results[1][0][1])
        email = results[1][0][1]
        # domain_stuffix =

        query_virtual_people_sql = 'select phone,card,expires from virtual_people where country ="{}"'.format(country_code)
        print(query_virtual_people_sql)
        virtual_peoples = query_results(connect, query_virtual_people_sql)[1]
        print(virtual_peoples)
        virtual_people_list = []
        for i in virtual_peoples:
            virtual_people_list.append(i)
        virtual_people_data = random.choice(virtual_people_list)
        print(virtual_people_data)
        # EMAIL = 'ghresdghesuh@volbaby.com'

        # PHONE = '641-660-0191'
        # CARD = '4916 5000 0531 8963'
        # EXPIRES = '1/2021'

        PHONE = virtual_people_data[0]
        CARD = virtual_people_data[1]
        EXPIRES = virtual_people_data[2]

        print(group_url)


        # 先登陆邮箱
        try:
            browser_1.get('https://mail.teekar.com/mail/')
        except:
            try:
                browser_1.get('https://mail.teekar.com/mail/')
            except:
                update_sql = 'update email set error="" where username ="{}"'.format(email)
                insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
                browser.quit()
                browser_1.quit()
                pass
        browser_1.find_element_by_id('rcmloginuser').send_keys(email)
        browser_1.find_element_by_id('rcmloginpwd').send_keys(PASSWORD)
        browser_1.find_element_by_id('rcmloginsubmit').click()

        # browser = webdriver.Chrome()
        # 打开Amazon主页，并点击注册
        browser.get('https://www.amazon.{}'.format(domain_stuffix))
        time.sleep(5)
        print(browser.find_element_by_id('nav-link-accountList').get_attribute('href'))
        try:
            # browser.find_element_by_id('nav-link-accountList').click()
            browser.get(browser.find_element_by_id('nav-link-accountList').get_attribute('href'))
        except:
            try:
                browser.refresh()
                time.sleep(10)
                browser.get(browser.find_element_by_id('nav-link-accountList').get_attribute('href'))
                # browser.find_element_by_id('nav-link-accountList').click()
            except:
                browser.quit()
                browser_1.quit()
                update_sql = 'update email set error="" where username ="{}"'.format(email)
                insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
        # time.sleep(10)
        try:
            browser.find_element_by_id('createAccountSubmit').click()
        except:
            try:
                browser.refresh()
                time.sleep(10)
                browser.find_element_by_id('createAccountSubmit').click()
            except:
                browser.quit()
                browser_1.quit()
                update_sql = 'update email set error="" where username ="{}"'.format(email)
                insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
        time.sleep(3)
        # browser.get('https://www.amazon.com/ap/register?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_newcust')

        # 产生随机用户名
        cha_list = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        username = ''.join(random.sample(cha_list, 9))
        print('随机生成用户名：', username)
        password = 'gsdyghFrefghsD.'
        print('账户密码为：', password)
        browser.find_element_by_id('ap_customer_name').send_keys(username)
        # 获取邮箱
        print('正在获取邮箱...')
        # browser_1.get('http://24mail.chacuo.net/enus')
        # browser_1.find_element_by_xpath('//select[@class="f16p"]').click()

        # email = browser_1.find_element_by_id('mail_copy').get_attribute('data-clipboard-text')

        print('成功获取邮箱：', email)
        print('开始注册亚马逊账号...')
        # 注册界面输入用户名邮箱密码 开始注册
        browser.find_element_by_id('ap_email').send_keys(email)
        # print(0)
        # time.sleep(3)
        browser.find_element_by_id('ap_password').send_keys(password)
        # time.sleep(3)
        # print(1)
        browser.find_element_by_id('ap_password_check').send_keys(password)
        # time.sleep(3)
        # print(2)
        browser.find_element_by_id('continue').click()
        time.sleep(1)
        # if 'cap'
        browser.find_elements_by_id('auth-captcha-image')
        print(len(browser.find_elements_by_id('auth-captcha-image')))
        if len(browser.find_elements_by_id('auth-captcha-image')) == 0:
            # print(3)
            time.sleep(50)
            # 手动刷新接收邮箱
            browser_1.find_element_by_id('rcmbtn107').click()
            # browser_1.find_element_by_id('rcmliSU5CT1g').click()
            browser_1.get('https://mail.teekar.com/mail/?_task=mail&_mbox=INBOX')
            time.sleep(3)
            mail_url = browser_1.find_element_by_css_selector('.message .subject .subject a').get_attribute('href')
            browser_1.get(mail_url)
            # print('1111111111111111111111111111')
            # print(2222222222222222222222222222222)
            time.sleep(3)
            # print(browser_1.page_source)
            # try:
            #     # 打开收到的邮箱
            #     browser_1.find_element_by_id('convertd').click()
            #     time.sleep(3)
            # except:
            #     browser.find_element_by_css_selector('div.a-section.a-spacing-none.a-spacing-top-large.a-text-center.cvf-widget-section-js a').click()
            #     time.sleep(30)
            #     # 手动刷新接收邮箱
            #     browser_1.find_element_by_class_name('red').click()
            #     # 打开收到的邮箱
            #     browser_1.find_element_by_id('convertd').click()
            #     time.sleep(3)
            # 获取邮箱验证码
            code = browser_1.find_element_by_css_selector('p.otp').text.strip()
            print('成功获取邮箱验证码：', code)
            # time.sleep(20)
            # 将邮箱验证码填入，完成注册
            browser.find_element_by_class_name('cvf-widget-input-code').send_keys(code)
            # time.sleep(100)
            browser.find_element_by_id('a-autoid-0').click()
            print('亚马逊账号注册成功！')
            browser_1.quit()
            update_sql = 'update email set error="", status="1" where username ="{}"'.format(email)
            insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')

            # 打开跟卖页面
            print('打开跟卖页面！')
            browser.get(group_url)
            browser.refresh()
            # results = browser.find_elements_by_css_selector('#olpOfferList div.a-section.a-padding-small div.a-section.a-spacing-double-large div.a-row.a-spacing-mini.olpOffer')
            # print('成功打开跟卖页面！')
            # for i in results:
            #     # print(i)
            #     try:
            #         shop_name = i.find_element_by_css_selector('div.a-column.a-span2.olpSellerColumn h3 span a').text
            #     except:
            #         shop_name = 'other'
            #
            #     if shop_name not in shop_name_list:
            #         print('正在赶走跟卖卖家：', shop_name)
            #         i.find_element_by_css_selector('div.a-button-stack form.a-spacing-none span.a-declarative').click()
            #
            #         break
            # browser.get('https://www.amazon.com/gp/cart/view.html/ref=lh_cart_dup')
            # browser.find_element_by_id('a-autoid-0').click()
            # browser.find_element_by_id('dropdown1_10').click()
            # browser.find_element_by_css_selector('.a-input-text.a-width-small.sc-quantity-textfield.sc-hidden').send_keys('999')
            # browser.find_element_by_id('a-autoid-1-announce').click()
            # time.sleep(1)

            results = browser.find_elements_by_xpath('//div[@class="a-row a-spacing-mini olpOffer"]')
            print('成功打开跟卖页面！')

            # shop_name_list = ['Zadii']
            data_list = []
            for i in results:

                print(i)
                try:
                    shop_name = i.find_element_by_xpath('./div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a').text
                except:
                    shop_name = 'other'
                id_num = i.find_element_by_xpath('./div[@class="a-column a-span2 olpBuyColumn a-span-last"]/div/form/span/span').get_attribute('id')
                print(shop_name)
                if shop_name not in shop_name_list:
                    data_list.append([shop_name, id_num])
            print(data_list)
            for m in data_list:
                browser.get(group_url)
                browser.refresh()
                browser.find_element_by_id(m[1]).click()

            browser.get('https://www.amazon.{}/gp/cart/view.html/ref=lh_cart'.format(domain_stuffix))
            link_list = browser.find_elements_by_xpath('//div[@class="a-row sc-action-links"]')
            for x, y in zip(link_list, range(len(link_list))):
                x.find_element_by_xpath('./span[@class="sc-action-quantity"]').click()
                browser.find_element_by_id('dropdown{}_10'.format(y + 1)).click()
                x.find_element_by_xpath('./span/span/input[@class="a-input-text a-width-small sc-quantity-textfield sc-hidden"]').send_keys('999')
                x.find_element_by_xpath('./span/span/span[@class="a-spacing-top-small"]').click()
                time.sleep(2)

            browser.find_element_by_id('sc-buy-box-ptc-button').click()

            # browser.get('https://www.amazon.com/a/addresses/add?ref=ya_address_book_add_button')
            # 填写新建地址信息
            if country_code == 'us':
                print('正在填写地址信息...')
                browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                # browser.find_element_by_id('enterAddressAddressLine2').send_keys()
                browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PROVINCE)
                browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                # browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                # print('地址填写完毕！')
                time.sleep(2)
                try:
                    browser.find_element_by_xpath('//input[@name="continue"]').click()
                except:
                    pass
                browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                print('地址填写完毕！')
            elif country_code == 'uk':
                print('正在填写地址信息...')
                browser.find_element_by_id('enterAddressFullName').send_keys(username)
                browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                # browser.find_element_by_id('enterAddressAddressLine2').send_keys()
                if browser.find_element_by_id('enterAddressCity').text == '':
                    browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                browser.find_element_by_id('enterAddressStateOrRegion').send_keys(COUNTRY)

                browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                # browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                # print('地址填写完毕！')
                time.sleep(2)
                try:
                    browser.find_element_by_xpath('//input[@name="continue"]').click()
                except:
                    pass
                browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                print('地址填写完毕！')
            elif country_code == 'ca':
                print('正在填写地址信息...')
                browser.find_element_by_id('enterAddressFullName').send_keys(username)
                browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                # if browser.find_element_by_id('enterAddressCity').text == '':
                browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                # browser.find_element_by_id('enterAddressStateOrRegion').click()
                # time.sleep(3)

                select_ele = browser.find_element_by_xpath('//select[@id="enterAddressStateOrRegion"]')
                # 2.初始化select类
                s = Select(select_ele)
                # 选择值
                # 1.下标
                # s.select_by_index(2)  # 使用下标选择"微软 Word (.doc)"
                # time.sleep(3)
                # 2.value值
                s.select_by_value(PV)  # 使用value方式选择值"微软 Powerpoint (.ppt)"
                # time.sleep(3)
                # # 3.通过文本方式
                # s.select_by_visible_text('RTF 文件 （.rtf)')


                browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)

                # browser.find_element_by_id('enterAddressAddressLine2').send_keys()

                # browser.find_element_by_id('enterAddressStateOrRegion').send_keys(COUNTRY)

                browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                # browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                # print('地址填写完毕！')
                time.sleep(2)
                try:
                    browser.find_element_by_xpath('//input[@name="continue"]').click()
                except:
                    pass
                browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                print('地址填写完毕！')
            else:
                pass
            time.sleep(5)
            # soup = BeautifulSoup(browser.page_source, 'lxml')
            # pre_text = soup.select('.a-section.a-spacing-none.pmts-widget-section')[0].get('data-pmts-component-id').split('-')[1]
            # print(pre_text)

            # 填写信用卡信息
            print('正在填写信用卡信息...')
            browser.find_element_by_xpath('//input[@name="ppw-accountHolderName"]').send_keys(username)
            browser.find_element_by_xpath('//input[@name="addCreditCardNumber"]').send_keys(CARD)
            # browser.find_element_by_xpath('//input[@name="ppw-expirationDate_month"]').click()
            # browser.find_element_by_id('pp-{}-52'.format(pre_text)).send_keys(CARD)
            # browser.find_element_by_id('pp-{}-59'.format(pre_text)).click()
            browser.find_element_by_css_selector('.pmts-expiry-month').click()
            time.sleep(2)

            month_list = browser.find_elements_by_xpath('//ul[@id="1_dropdown_combobox"]/li/a')
            # print(month_list)
            for x in month_list:
                # print(x)
                if int(x.get_attribute('data-value')) == int(EXPIRES.split('/')[0]):
                    x.click()
            #
            # browser.find_element_by_id('pp-{}-60'.format(pre_text)).click()
            browser.find_element_by_css_selector('.pmts-expiry-year').click()
            time.sleep(2)
            year_list = browser.find_elements_by_xpath('//ul[@id="2_dropdown_combobox"]/li/a')
            for y in year_list:
                # print(y)
                if int(y.get_attribute('data-value')) == int(EXPIRES.split('/')[1]):
                    y.click()
            print('信用卡信息填写完毕！')
            # browser.find_element_by_id('pp-{}-61'.format(pre_text)).click()
            # browser.find_element_by_css_selector('.a-button.a-button-primary.pmts-button-input').click()
            browser.find_element_by_xpath('//span[@class="a-button a-button-primary pmts-button-input"]').click()
            time.sleep(3)

            try:
                browser.find_element_by_xpath('//div[@class="a-column a-span8 pmts-cc-detail-row"]/div/div/div/label/input[@type="radio"]').click()
                time.sleep(2)
            except:
                pass
            time.sleep(3)
            browser.find_element_by_css_selector('.a-button-input').click()
            time.sleep(2)
            # try:
            #
            browser.find_element_by_id('placeYourOrder').click()
            print('下单成功！')

            time.sleep(10)
            print('成功赶走跟卖卖家：', shop_name)
            browser.quit()
        else:
            # print(3)
            # time.sleep(6000)
            # time.sleep(3)
            # browser.find_element_by_id('ap_password').send_keys(password)
            #
            # # print(1)
            # browser.find_element_by_id('ap_password_check').send_keys(password)
            # img_url = browser.find_element_by_id('auth-captcha-image').get_attribute('src').split('?')[0].split('/')[-1]
            # print(browser.find_element_by_id('auth-captcha-image').get_attribute('src'))
            # response = requests.get(browser.find_element_by_id('auth-captcha-image').get_attribute('src'))
            # response = response.content
            #
            # BytesIOObj = BytesIO()
            # BytesIOObj.write(response)
            # img = Image.open(BytesIOObj)
            # img.show()
            # capture_text = ''
            # capture_text = input('请输入验证码：')
            # img.close()
            # browser.find_element_by_id('auth-captcha-guess').send_keys(capture_text)
            # browser.find_element_by_id('continue').click()
            # print(img_url)
            # img.close()
            while True:
                time.sleep(2)
                try:
                    browser.find_element_by_id('ap_password').send_keys(password)

                    # print(1)
                    browser.find_element_by_id('ap_password_check').send_keys(password)
                    img_url = browser.find_element_by_id('auth-captcha-image').get_attribute('src').split('?')[0].split('/')[-1]
                    print(browser.find_element_by_id('auth-captcha-image').get_attribute('src'))
                    capture_text = ''
                    img = browser.find_element_by_id('auth-captcha-image').get_attribute('src')
                    data = requests.get(img).content
                    capture_text = TestFunc(data).pred_rsp.value
                    response = requests.get(browser.find_element_by_id('auth-captcha-image').get_attribute('src'))
                    response = response.content

                    BytesIOObj = BytesIO()
                    BytesIOObj.write(response)
                    img = Image.open(BytesIOObj)
                    # img.show()
                    # capture_text = ''
                    # capture_text = input('请输入验证码：')
                    # img.close()
                    browser.find_element_by_id('auth-captcha-guess').send_keys(capture_text)
                    browser.find_element_by_id('continue').click()
                    print(img_url)

                except:
                    break
            time.sleep(40)
            # 手动刷新接收邮箱
            browser_1.find_element_by_id('rcmbtn107').click()
            # browser_1.find_element_by_id('rcmliSU5CT1g').click()
            browser_1.get('https://mail.teekar.com/mail/?_task=mail&_mbox=INBOX')
            time.sleep(3)
            try:
                mail_url = browser_1.find_element_by_css_selector('.message .subject .subject a').get_attribute('href')
            except:
                try:
                    browser_1.get('https://mail.teekar.com/mail/?_task=mail&_mbox=INBOX')
                    time.sleep(3)
                    mail_url = browser_1.find_element_by_css_selector('.message .subject .subject a').get_attribute('href')
                except:
                    update_sql = 'update email set error="" where username ="{}"'.format(email)
                    insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
                    browser.quit()
                    browser_1.quit()
                    pass
            browser_1.get(mail_url)
            # print('1111111111111111111111111111')
            # print(2222222222222222222222222222222)
            time.sleep(3)
            # print(browser_1.page_source)
            # try:
            #     # 打开收到的邮箱
            #     browser_1.find_element_by_id('convertd').click()
            #     time.sleep(3)
            # except:
            #     browser.find_element_by_css_selector('div.a-section.a-spacing-none.a-spacing-top-large.a-text-center.cvf-widget-section-js a').click()
            #     time.sleep(30)
            #     # 手动刷新接收邮箱
            #     browser_1.find_element_by_class_name('red').click()
            #     # 打开收到的邮箱
            #     browser_1.find_element_by_id('convertd').click()
            #     time.sleep(3)
            # 获取邮箱验证码
            code = browser_1.find_element_by_css_selector('p.otp').text.strip()
            print('成功获取邮箱验证码：', code)
            # time.sleep(20)
            # 将邮箱验证码填入，完成注册
            browser.find_element_by_class_name('cvf-widget-input-code').send_keys(code)
            # time.sleep(100)
            browser.find_element_by_id('a-autoid-0').click()
            print('亚马逊账号注册成功！')
            browser_1.quit()
            update_sql = 'update email set error="", status="1" where username ="{}"'.format(email)
            print(update_sql)
            insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
            # 打开跟卖页面
            print('打开跟卖页面！')
            browser.get(group_url)
            browser.refresh()
            # results = browser.find_elements_by_css_selector('#olpOfferList div.a-section.a-padding-small div.a-section.a-spacing-double-large div.a-row.a-spacing-mini.olpOffer')
            # print('成功打开跟卖页面！')
            # for i in results:
            #     # print(i)
            #     try:
            #         shop_name = i.find_element_by_css_selector('div.a-column.a-span2.olpSellerColumn h3 span a').text
            #     except:
            #         shop_name = 'other'
            #
            #     if shop_name not in shop_name_list:
            #         print('正在赶走跟卖卖家：', shop_name)
            #         i.find_element_by_css_selector('div.a-button-stack form.a-spacing-none span.a-declarative').click()
            #
            #         break
            # browser.get('https://www.amazon.com/gp/cart/view.html/ref=lh_cart_dup')
            # browser.find_element_by_id('a-autoid-0').click()
            # browser.find_element_by_id('dropdown1_10').click()
            # browser.find_element_by_css_selector('.a-input-text.a-width-small.sc-quantity-textfield.sc-hidden').send_keys('999')
            # browser.find_element_by_id('a-autoid-1-announce').click()
            # time.sleep(1)

            results = browser.find_elements_by_xpath('//div[@class="a-row a-spacing-mini olpOffer"]')
            print('成功打开跟卖页面！')

            # shop_name_list = ['Zadii']
            data_list = []
            for i in results:

                print(i)
                try:
                    shop_name = i.find_element_by_xpath('./div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a').text
                except:
                    shop_name = 'other'
                id_num = i.find_element_by_xpath('./div[@class="a-column a-span2 olpBuyColumn a-span-last"]/div/form/span/span').get_attribute('id')
                print(shop_name)
                if shop_name not in shop_name_list:
                    data_list.append([shop_name, id_num])
            print(data_list)
            for m in data_list:
                browser.get(group_url)
                browser.refresh()
                browser.find_element_by_id(m[1]).click()

            browser.get('https://www.amazon.{}/gp/cart/view.html/ref=lh_cart'.format(domain_stuffix))
            link_list = browser.find_elements_by_xpath('//div[@class="a-row sc-action-links"]')
            for x, y in zip(link_list, range(len(link_list))):
                x.find_element_by_xpath('./span[@class="sc-action-quantity"]').click()
                browser.find_element_by_id('dropdown{}_10'.format(y + 1)).click()
                x.find_element_by_xpath('./span/span/input[@class="a-input-text a-width-small sc-quantity-textfield sc-hidden"]').send_keys('999')
                x.find_element_by_xpath('./span/span/span[@class="a-spacing-top-small"]').click()
                time.sleep(2)

            browser.find_element_by_id('sc-buy-box-ptc-button').click()

            # browser.get('https://www.amazon.com/a/addresses/add?ref=ya_address_book_add_button')
            # 填写新建地址信息
            # print('正在填写地址信息...')
            # browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
            # # browser.find_element_by_id('enterAddressAddressLine2').send_keys()
            # browser.find_element_by_id('enterAddressCity').send_keys(CITY)
            # browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PROVINCE)
            # browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
            # browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
            # browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()
            # time.sleep(2)
            # try:
            #     browser.find_element_by_xpath('//input[@name="continue"]').click()
            # except:
            #     pass
            # browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
            # print('地址填写完毕！')
            if country_code == 'us':
                print('正在填写地址信息...')
                browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                # browser.find_element_by_id('enterAddressAddressLine2').send_keys()
                browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PROVINCE)
                browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                # browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                # print('地址填写完毕！')
                time.sleep(2)
                try:
                    browser.find_element_by_xpath('//input[@name="continue"]').click()
                except:
                    pass
                browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                print('地址填写完毕！')
            elif country_code == 'uk':
                print('正在填写地址信息...')
                browser.find_element_by_id('enterAddressFullName').send_keys(username)
                browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                # browser.find_element_by_id('enterAddressAddressLine2').send_keys()
                if browser.find_element_by_id('enterAddressCity').text == '':
                    browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                browser.find_element_by_id('enterAddressStateOrRegion').send_keys(COUNTRY)

                browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                # browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                # print('地址填写完毕！')
                time.sleep(2)
                try:
                    browser.find_element_by_xpath('//input[@name="continue"]').click()
                except:
                    pass
                browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                print('地址填写完毕！')
            elif country_code == 'ca':
                print('正在填写地址信息...')
                browser.find_element_by_id('enterAddressFullName').send_keys(username)
                browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                # if browser.find_element_by_id('enterAddressCity').text == '':
                browser.find_element_by_id('enterAddressCity').send_keys(CITY)

                select_ele = browser.find_element_by_xpath('//select[@id="enterAddressStateOrRegion"]')
                # 2.初始化select类
                s = Select(select_ele)
                # 选择值
                # 1.下标
                # s.select_by_index(2)  # 使用下标选择"微软 Word (.doc)"
                # time.sleep(3)
                # 2.value值
                s.select_by_value(PV)  # 使用value方式选择值"微软 Powerpoint (.ppt)"

                browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)

                # browser.find_element_by_id('enterAddressAddressLine2').send_keys()

                # browser.find_element_by_id('enterAddressStateOrRegion').send_keys(COUNTRY)

                browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                # browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                # print('地址填写完毕！')
                time.sleep(2)
                try:
                    browser.find_element_by_xpath('//input[@name="continue"]').click()
                except:
                    pass
                browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                print('地址填写完毕！')
            else:
                pass

            time.sleep(5)
            # soup = BeautifulSoup(browser.page_source, 'lxml')
            # pre_text = soup.select('.a-section.a-spacing-none.pmts-widget-section')[0].get('data-pmts-component-id').split('-')[1]
            # print(pre_text)

            # 填写信用卡信息
            print('正在填写信用卡信息...')
            # browser.find_element_by_id('pp-{}-51'.format(pre_text)).send_keys(username)
            browser.find_element_by_xpath('//input[@name="ppw-accountHolderName"]').send_keys(username)
            browser.find_element_by_xpath('//input[@name="addCreditCardNumber"]').send_keys(CARD)
            # browser.find_element_by_xpath('//input[@name="ppw-expirationDate_month"]').click()
            # browser.find_element_by_id('pp-{}-52'.format(pre_text)).send_keys(CARD)
            # browser.find_element_by_id('pp-{}-59'.format(pre_text)).click()
            browser.find_element_by_css_selector('.pmts-expiry-month').click()
            time.sleep(2)

            month_list = browser.find_elements_by_xpath('//ul[@id="1_dropdown_combobox"]/li/a')
            # print(month_list)
            for x in month_list:
                # print(x)
                if int(x.get_attribute('data-value')) == int(EXPIRES.split('/')[0]):
                    x.click()
            #
            # browser.find_element_by_id('pp-{}-60'.format(pre_text)).click()
            browser.find_element_by_css_selector('.pmts-expiry-year').click()
            time.sleep(2)
            year_list = browser.find_elements_by_xpath('//ul[@id="2_dropdown_combobox"]/li/a')
            for y in year_list:
                # print(y)
                if int(y.get_attribute('data-value')) == int(EXPIRES.split('/')[1]):
                    y.click()
            print('信用卡信息填写完毕！')
            # browser.find_element_by_id('pp-{}-61'.format(pre_text)).click()
            # browser.find_element_by_css_selector('.a-button.a-button-primary.pmts-button-input').click()
            browser.find_element_by_xpath('//span[@class="a-button a-button-primary pmts-button-input"]').click()
            time.sleep(3)
            # browser.find_element_by_css_selector('.a-button-input').click()

            try:
                browser.find_element_by_xpath('//div[@class="a-column a-span8 pmts-cc-detail-row"]/div/div/div/label/input[@type="radio"]').click()
                time.sleep(2)
            except:
                pass
            time.sleep(3)
            browser.find_element_by_css_selector('.a-button-input').click()
            time.sleep(2)
            browser.find_element_by_id('placeYourOrder').click()
            print('下单成功！')

            time.sleep(10)
            print('成功赶走跟卖卖家：', shop_name)
            browser.quit()
            # time.sleep(1000)
            # browser.quit()
            # browser_1.quit()
            # print('IP被封了')
            # get_out_amzer()
    else:
        print('没有跟卖的卖家！')
        browser.quit()
        pass


def main(asin_text, country_code_text, shop_name_text):
    connect = connect_db(DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT)

    print(shop_name.split('->'))
    get_out_amzer(connect, asin_text, country_code_text, shop_name_text)
    # update_sql = 'update email set error="" where id ={}'.format(results[1][0][0])
    # insert_update_drop_data(connect, update_sql, '又改回来了')


if __name__ == '__main__':
    asin = input('请输入Asin：')
    # asin = 'B07V4R3J31'
    # asin = 'B07YL2T543'
    # asin = 'B079JL2FSY'
    # country_code = 'uk'
    # country_code = 'fr'
    country_code = input('请输入亚马逊站点的国别码：（例如：英国uk,美国us,法国fr,加拿大ca）')
    # country_code = 'ca'
    # shop_name = 'Tianyu.HC'
    shop_name = input('请输入我们公司自己的店铺名称（即：不需要赶走的）：')
    while True:
        main(asin, country_code, shop_name)
        time.sleep(120)