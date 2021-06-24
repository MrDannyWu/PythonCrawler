"""
create: 2019.11.11
company: Umiwe
auth:
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from random import sample, choice
from auto_setup_amz.db import *
from auto_setup_amz.db_utils import *
from requests import get
from auto_setup_amz.fateadm_api import TestFunc
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from string import Template
from zipfile import ZipFile
from pandas import read_excel


def create_proxy_auth_extension(scheme='http', plugin_path=None):
    # 代理服务器
    proxy_host = "http-pro.abuyun.com"
    proxy_port = "9010"

    # 代理隧道验证信息
    proxy_username = "H2893445CPWJT9UP"
    proxy_password = "A5847CF45C10919B"

    if plugin_path is None:
        plugin_path = r'D:/{}_{}@http-pro.abuyun.com_9010.zip'.format(proxy_username, proxy_password)

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Abuyun Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = Template(
        """
        var config = {
            mode: "fixed_servers",
            rules: {
                singleProxy: {
                    scheme: "${scheme}",
                    host: "${host}",
                    port: parseInt(${port})
                },
                bypassList: ["foobar.com"]
            }
          };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "${username}",
                    password: "${password}"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
        );
        """
    ).substitute(
        host=proxy_host,
        port=proxy_port,
        username=proxy_username,
        password=proxy_password,
        scheme=scheme,
    )

    with ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return plugin_path


def get_out_amzer(connect, asin, country_code, shop_name, type_text):
    try:
        if str(shop_name).strip() != 'nan' and str(shop_name).strip() != '':
            shop_name_list = str(shop_name).split('->')
        else:
            shop_name_list = ['']
        if country_code.lower() == 'us':
            domain_stuffix = 'com'
            STREET = '16701 Beach Blvd.,Huntington Beach,CA'
            CITY = 'Huntington Beach'
            PROVINCE = 'CA'
            POSTCODE = '92647'
        elif country_code.lower() == 'uk':
            domain_stuffix = 'co.uk'
            STREET = 'Lennon Studios, 109 Cambridge Court, Liverpool, L7 7AG, UK'
            CITY = 'Liverpool'
            COUNTRY = 'UK'
            POSTCODE = 'L7 7AG'
        elif country_code.lower() == 'ca':
            domain_stuffix = 'ca'
            STREET = '3499 Ashcroft Cres'
            CITY = 'Mississauga'
            PV = 'Ontario'
            COUNTRY = 'CA'
            POSTCODE = 'L5C 2E6'
        elif country_code.lower() == 'fr':
            domain_stuffix = 'fr'
            STREET = '96 Rue Saint Martin'
            CITY = 'L Etoile'
            PV = ''
            COUNTRY = 'FR'
            POSTCODE = '80830'
        elif country_code.lower() == 'de':
            domain_stuffix = 'de'
            STREET = 'Kors?rer Stra?e 21'
            CITY = 'Berlin'
            PV = ''
            COUNTRY = 'DE'
            POSTCODE = '10437'
        elif country_code.lower() == 'it':
            domain_stuffix = 'it'
            STREET = 'Via Penegal 14 A'
            CITY = 'Bolzano'
            PV = 'Bz'
            COUNTRY = 'IT'
            POSTCODE = '39100'
        elif country_code.lower() == 'ae':
            domain_stuffix = 'ae'
            STREET = '404 Al Saaha B Souk Al Bahar'
            CITY = 'Abu Dhabi'
            PV = 'Navy Gate'
            COUNTRY = 'AE'
            POSTCODE = ''
        elif country_code.lower() == 'es':
            domain_stuffix = 'es'
            STREET = 'Paseo Roncesvalles N°67'
            CITY = 'Cizur menor'
            PV = 'Navarra'
            COUNTRY = 'ES'
            POSTCODE = '31190'
        else:
            domain_stuffix = country_code.lower()
        PASSWORD = '12344321'
        group_url = 'https://www.amazon.{}/gp/offer-listing/{}'.format(domain_stuffix, asin)

        print('跟卖页面地址：', group_url)
        print('=========================================================================')
        print('')
        print('=================================信息输出=================================')
        print('正在启动浏览器...')
        chrome_options = Options()
        chrome_options.add_argument('blink-settings=imagesEnabled=false')
        # resp = requests.get('http://10.11.2.33:5010/get/')
        # json_data_1 = json.loads(resp.text)
        # proxy = json_data_1['proxy']
        # web_resp = requests.get('http://ged.ip3366.net/api/?key=20191122150329175&getnum=1&filter=1&proxytype=1')
        # print(web_resp.text)
        # proxy = web_resp.text
        # print(resp.text)
        # print(resp.text.split('\n')[-1])
        # proxy = resp.text.split('\n')[-1]

        executable_path = 'chromedriver.exe'
        # chrome_options.add_argument('--proxy-server=http://10.11.2.251:3128')
        # chrome_options.add_argument('--proxy-server=http://{}'.format(proxy))
        # chrome_options.add_argument('--proxy-server=http://171.223.207.30:8001')

        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_argument('log-level=3')
        # proxy_auth_plugin_path = create_proxy_auth_extension()
        chrome_options.binary_location = 'Chrome/Application/chrome.exe'
        # chrome_options.add_extension(proxy_auth_plugin_path)

        browser = webdriver.Chrome(executable_path=executable_path, options=chrome_options)

        browser.delete_all_cookies()
        print('浏览器启动完毕！')
        print('正在打开跟卖页面...')
        browser.get(group_url)
        browser.refresh()

        if country_code.lower() == 'us':
            browser.get(
                'https://www.amazon.com/gp/customer-preferences/select-language/ref=topnav_lang_c_ais?preferencesReturnUrl=%2Fgp%2Fproduct%2FB07XKZTM17%3Fpf_rd_p%3D2d1ab404-3b11-4c97-b3db-48081e145e35%26pf_rd_r%3DQPHNKRYSJQD1HT549CK2')
            sleep(3)
            browser.find_element_by_css_selector('.a-popover-trigger.a-declarative').click()
            sleep(2)
            browser.find_element_by_id('GLUXCountryListDropdown').click()
            a_list = browser.find_elements_by_css_selector(
                '.a-popover.a-dropdown.a-dropdown-common.a-declarative ul li a')
            for a in a_list:
                if 'united states' in a.text.lower():
                    a.click()
                    break
            browser.find_element_by_xpath('//button[@name="glowDoneButton"]').click()
            browser.find_element_by_id('icp-btn-save')
            browser.get(group_url)

        if country_code.lower() == 'fr':
            browser.find_element_by_id('nav-global-location-slot').click()
            sleep(3)
            browser.find_element_by_id('GLUXCountryListDropdown').click()
            a_list = browser.find_elements_by_css_selector(
                '.a-popover.a-dropdown.a-dropdown-common.a-declarative ul li a')
            for a in a_list:
                if 'guyane fran?aise' in a.text.lower():
                    a.click()
                    break
        sleep(3)

        results = browser.find_elements_by_xpath('//div[@class="a-row a-spacing-mini olpOffer"]')
        # print(results)
        print('成功打开跟卖页面！')

        shop_list = []
        temp_name_list = []
        for i in results:
            try:
                shop_name = i.find_element_by_xpath('./div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a').text
            except Exception as e:
                print(e)
                shop_name = 'other'
            id_num = i.find_element_by_xpath(
                './div[@class="a-column a-span2 olpBuyColumn a-span-last"]/div/form/span/span').get_attribute('id')
            if shop_name not in shop_name_list:
                shop_list.append([shop_name, id_num])
                temp_name_list.append(shop_name)

        if len(shop_list) > 0:
            print('')
            print('发现 {} 个跟卖卖家：{}'.format(len(shop_list),
                                          str(temp_name_list).replace('[', '').replace(']', '').replace("'",
                                                                                                        '').replace(',',
                                                                                                                    ' ')))
            print('')
            browser_1 = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
            browser_1.delete_all_cookies()

            query_sql = 'select id,username from email where status = 0 and error = ""'
            results = query_results(connect, query_sql)
            update_sql = 'update email set error="using" where id ={}'.format(results[1][0][0])
            insert_update_drop_data(connect, update_sql, '更新为using')

            results[1][0][0]
            email = results[1][0][1]
            if country_code.lower() == 'aea':
                pass
            else:
                query_virtual_people_sql = 'select phone,card,expires,cvv2 from virtual_people where country ="{}"'.format(
                    country_code.lower())
                virtual_peoples = query_results(connect, query_virtual_people_sql)[1]
                virtual_people_list = []
                for i in virtual_peoples:
                    virtual_people_list.append(i)
                virtual_people_data = choice(virtual_people_list)
                PHONE = virtual_people_data[0]
                CARD = virtual_people_data[1]
                EXPIRES = virtual_people_data[2]
                CVV = virtual_people_data[3]

            # 先登陆邮箱
            zz = 0
            while True:
                if zz == 15:
                    update_sql = 'update email set error="" where username ="{}"'.format(email)
                    insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
                    browser.quit()
                    browser_1.quit()
                    break
                try:
                    browser_1.get('https://mail.teekar.com/mail/')
                    break
                except Exception as e:
                    print(e)
                    try:
                        browser_1.get('https://mail.teekar.com/mail/')
                        break
                    except Exception as e:
                        print(e)
                        pass
                zz += 1
            browser_1.find_element_by_id('rcmloginuser').send_keys(email)
            browser_1.find_element_by_id('rcmloginpwd').send_keys(PASSWORD)
            browser_1.find_element_by_id('rcmloginsubmit').click()

            # 打开Amazon主页，并点击注册
            if country_code.lower() == 'uk':
                browser.get(
                    'https://www.amazon.co.uk/ap/register?_encoding=UTF8&openid.assoc_handle=gbflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.uk%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_newcust')
            else:
                browser.get('https://www.amazon.{}'.format(domain_stuffix))

                sleep(5)
                print(browser.find_element_by_id('nav-link-accountList').get_attribute('href'))
                nav_link_account_list = browser.find_element_by_id('nav-link-accountList').get_attribute('href')

                try:
                    browser.get(browser.find_element_by_id('nav-link-accountList').get_attribute('href'))
                except Exception as e:
                    print(e)
                    try:
                        # browser.refresh()
                        sleep(5)
                        browser.get(browser.find_element_by_id('nav-link-accountList').get_attribute('href'))
                    except Exception as e:
                        print(e)
                        browser.quit()
                        browser_1.quit()
                        update_sql = 'update email set error="" where username ="{}"'.format(email)
                        insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
                if 'homepage' in nav_link_account_list:
                    sleep(3)
                    try:
                        browser.get(browser.find_element_by_id('nav-link-accountList').get_attribute('href'))
                    except Exception as e:
                        print(e)
                        pass

                try:
                    browser.find_element_by_id('createAccountSubmit').click()
                except Exception as e:
                    print(e)
                    try:
                        # browser.refresh()
                        sleep(5)
                        browser.find_element_by_id('createAccountSubmit').click()
                    except Exception as e:
                        print(e)
                        browser.quit()
                        browser_1.quit()
                        update_sql = 'update email set error="" where username ="{}"'.format(email)
                        insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
            sleep(2)

            # 产生随机用户名
            cha_list = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h',
                        'g', 'f', 'e', 'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            username = ''.join(sample(cha_list, 9))
            print('随机生成用户名：', username)
            password = 'gsdyghFrefghsD.'
            print('账户密码为：', password)
            browser.find_element_by_id('ap_customer_name').send_keys(username)
            # 获取邮箱
            print('正在获取邮箱...')

            print('成功获取邮箱：', email)
            print('开始注册亚马逊账号...')

            try:
                browser.find_element_by_id('ap_use_email').click()
            except Exception as e:
                print(e)
                pass
            sleep(2)
            # 注册界面输入用户名邮箱密码 开始注册
            browser.find_element_by_id('ap_email').send_keys(email)
            browser.find_element_by_id('ap_password').send_keys(password)
            try:
                browser.find_element_by_id('ap_password_check').send_keys(password)
            except Exception as e:
                print(e)
                pass
            if country_code.lower() == 'ae':
                try:
                    browser.find_element_by_id('auth-create-account-button').click()
                except Exception as e:
                    print(e)
                    pass
            else:
                try:
                    browser.find_element_by_id('continue').click()
                except Exception as e:
                    print(e)
                    pass

            sleep(1)
            browser.find_elements_by_id('auth-captcha-image')
            print(len(browser.find_elements_by_id('auth-captcha-image')))
            if len(browser.find_elements_by_id('auth-captcha-image')) == 0:
                sleep(40)
                # 手动刷新接收邮箱
                browser_1.find_element_by_id('rcmbtn107').click()
                browser_1.get('https://mail.teekar.com/mail/?_task=mail&_mbox=INBOX')
                sleep(3)

                try:
                    mail_url = browser_1.find_element_by_css_selector('.message .subject .subject a').get_attribute(
                        'href')
                except Exception as e:
                    print(e)
                    try:
                        browser_1.get('https://mail.teekar.com/mail/?_task=mail&_mbox=INBOX')
                        sleep(3)
                        mail_url = browser_1.find_element_by_css_selector('.message .subject .subject a').get_attribute(
                            'href')
                    except Exception as e:
                        print(e)
                        update_sql = 'update email set error="" where username ="{}"'.format(email)
                        insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
                        browser.quit()
                        browser_1.quit()
                        pass

                try:
                    browser_1.get(mail_url)
                    sleep(3)
                    # 获取邮箱验证码
                    code = browser_1.find_element_by_css_selector('p.otp').text.strip()
                    print('成功获取邮箱验证码：', code)
                    # 将邮箱验证码填入，完成注册
                    browser.find_element_by_class_name('cvf-widget-input-code').send_keys(code)
                    browser.find_element_by_id('a-autoid-0').click()
                    print('亚马逊账号注册成功！')
                    browser_1.quit()
                    update_sql = 'update email set error="", status="1" where username ="{}"'.format(email)
                    insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')

                    # 打开跟卖页面
                    print('打开跟卖页面！')
                    browser.get(group_url)
                    browser.refresh()

                    results = browser.find_elements_by_xpath('//div[@class="a-row a-spacing-mini olpOffer"]')
                    print('成功打开跟卖页面！')

                    data_list = []
                    data_name_list = []
                    for i in results:

                        try:
                            shop_name = i.find_element_by_xpath(
                                './div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a').text
                        except Exception as e:
                            print(e)
                            shop_name = 'other'
                        id_num = i.find_element_by_xpath(
                            './div[@class="a-column a-span2 olpBuyColumn a-span-last"]/div/form/span/span').get_attribute(
                            'id')
                        if shop_name not in shop_name_list:
                            data_list.append([shop_name, id_num])
                            data_name_list.append(shop_name)
                    print('正在赶跟卖卖家：{}'.format(
                        str(data_name_list).replace('[', '').replace(']', '').replace("'", '').replace(',', ' ')))
                    if type_text == 'one':
                        for m in data_list[0: 1]:
                            browser.get(group_url)
                            browser.refresh()
                            browser.find_element_by_id(m[1]).click()
                    else:
                        for m in data_list:
                            browser.get(group_url)
                            browser.refresh()
                            browser.find_element_by_id(m[1]).click()

                    browser.get('https://www.amazon.{}/gp/cart/view.html/ref=lh_cart'.format(domain_stuffix))
                    link_list = browser.find_elements_by_xpath('//div[@class="a-row sc-action-links"]')

                    if country_code.lower() == 'ae':
                        link_list = browser.find_elements_by_css_selector('.sc-action-links.a-span-last')
                        for x, y in zip(link_list, range(len(link_list))):
                            x.find_element_by_css_selector('.quantity').click()
                            browser.find_element_by_id('dropdown{}_9'.format(y + 1)).click()
                            x.find_element_by_css_selector('.sc-quantity-textfield.sc-hidden').send_keys('999')
                            x.find_element_by_css_selector('.sc-update-link').click()
                            sleep(3)
                            try:
                                quantity_value = browser.find_elements_by_css_selector('.sc-action-quantity')[
                                    y].get_attribute('data-old-value')
                            except Exception as e:
                                print(e)
                            try:
                                alert_text = browser.find_element_by_css_selector(
                                    '.a-alert-content .a-size-base').text.strip()
                                print(alert_text)
                                if 'limit' in alert_text.lower() or 'lediglich' in alert_text.lower():
                                    print('有限购，每个用户每次只能购买：', quantity_value, '件，已加入购物车！')
                                else:
                                    print('无限购，跟卖卖家库存总量量为：', quantity_value, '件，已加入购物车！')
                            except Exception as e:
                                print(e)
                    else:

                        link_list = browser.find_elements_by_xpath('//div[@class="a-row sc-action-links"]')
                        for x, y in zip(link_list, range(len(link_list))):
                            x.find_element_by_xpath('./span[@class="sc-action-quantity"]').click()
                            browser.find_element_by_id('dropdown{}_10'.format(y + 1)).click()
                            x.find_element_by_xpath(
                                './span/span/input[@class="a-input-text a-width-small sc-quantity-textfield sc-hidden"]').send_keys(
                                '999')
                            x.find_element_by_xpath('./span/span/span[@class="a-spacing-top-small"]').click()
                            sleep(3)

                            try:
                                quantity_value = browser.find_elements_by_xpath('//span[@class="sc-action-quantity"]')[
                                    y].get_attribute('data-old-value')
                            except Exception as e:
                                print(e)
                            try:
                                alert_text = browser.find_element_by_css_selector(
                                    '.a-alert-content .a-size-base').text.strip()
                                print(alert_text)
                                if 'limit' in alert_text.lower() or 'lediglich' in alert_text.lower():
                                    print('有限购，每个用户每次只能购买：', quantity_value, '件，已加入购物车！')
                                else:
                                    print('无限购，跟卖卖家库存总量量为：', quantity_value, '件，已加入购物车！')
                            except Exception as e:
                                print(e)

                    browser.find_element_by_id('sc-buy-box-ptc-button').click()

                    # 填写新建地址信息
                    if country_code.lower() == 'us':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PROVINCE)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    elif country_code.lower() == 'uk':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        if browser.find_element_by_id('enterAddressCity').text == '':
                            browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(COUNTRY)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    elif country_code.lower() == 'ca':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)

                        select_ele = browser.find_element_by_xpath('//select[@id="enterAddressStateOrRegion"]')
                        s = Select(select_ele)
                        s.select_by_value(PV)  # 使用value方式选择值"微软 Powerpoint (.ppt)"
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    elif country_code.lower() == 'fr':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    elif country_code.lower() == 'de':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    elif country_code.lower() == 'it':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    elif country_code.lower() == 'ae':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        ccc = 3
                        while ccc > 1:
                            browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                            sleep(5)
                            try:
                                browser.find_element_by_css_selector('ul.autoCompleteResult').click()
                            except:
                                pass
                            try:
                                browser.find_element_by_id('enterAddressCity').send_keys(Keys.ENTER)
                            except:
                                pass
                            sleep(10)
                            browser.find_element_by_id('enterAddressDistrictOrCounty').send_keys(PV)
                            sleep(5)
                            try:
                                browser.find_element_by_css_selector('ul.autoCompleteResult').click()
                            except:
                                pass
                            try:
                                browser.find_element_by_id('enterAddressDistrictOrCounty').send_keys(Keys.ENTER)
                            except:
                                pass
                            ccc = ccc - 1

                        try:
                            browser.find_element_by_css_selector('.a-button.a-button-primary.a-padding-none ').click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()
                        except Exception as e:
                            print(e)
                            pass

                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        try:
                            browser.find_element_by_css_selector(
                                '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        except Exception as e:
                            print(e)
                            pass
                        print('地址填写完毕！')
                    elif country_code.lower() == 'es':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    else:
                        pass
                    sleep(5)
                    print('正在填写信用卡信息...')
                    if country_code.lower() in ['fr', 'es']:
                        try:
                            browser.find_element_by_css_selector(
                                '#wrapper-new-cc div .a-link-expander.a-declarative').click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-add-new-card').click()
                        except Exception as e:
                            print(e)
                            pass
                        sleep(5)

                        try:
                            browser.find_element_by_id('ccName').send_keys(username)
                        except Exception as e:
                            print(e)
                            pass

                    try:
                        browser.find_element_by_xpath('//input[@name="ppw-accountHolderName"]').send_keys(username)
                    except Exception as e:
                        print(e)
                        try:
                            browser.find_element_by_css_selector(
                                '#wrapper-new-cc div .a-link-expander.a-declarative').click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-add-new-card').click()
                        except Exception as e:
                            print(e)
                            pass
                        sleep(5)

                        try:
                            browser.find_element_by_id('ccName').send_keys(username)
                        except Exception as e:
                            print(e)
                            pass
                    sleep(2)
                    try:
                        browser.find_element_by_xpath('//input[@name="ppw-accountHolderName"]').send_keys(username)
                    except Exception as e:
                        print(e)

                    browser.find_element_by_xpath('//input[@name="addCreditCardNumber"]').send_keys(CARD)
                    if country_code.lower() == 'fr':
                        try:
                            browser.find_element_by_css_selector('.card-date .a-button.a-button-dropdown').click()
                        except Exception as e:
                            print(e)
                            pass

                    else:
                        try:
                            browser.find_element_by_css_selector('.a-nostyle.a-list-link').click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-expiry-month').click()
                        except Exception as e:
                            print(e)
                            pass
                    sleep(2)

                    try:
                        month_list = browser.find_elements_by_xpath('//ul[@id="1_dropdown_combobox"]/li/a')
                    except Exception as e:
                        print(e)
                        pass
                    sleep(1)
                    for x in month_list:
                        if int(x.get_attribute('data-value')) == int(EXPIRES.split('/')[0]):
                            x.click()
                    if country_code.lower() == 'fr':
                        try:
                            browser.find_elements_by_css_selector('.card-date .a-button-text.a-declarative')[1].click()
                        except Exception as e:
                            print(e)
                            pass
                    else:
                        try:
                            browser.find_elements_by_css_selector('.a-nostyle.a-list-link')[1].click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-expiry-year').click()
                        except Exception as e:
                            print(e)
                            pass
                    sleep(2)
                    year_list = browser.find_elements_by_xpath('//ul[@id="2_dropdown_combobox"]/li/a')
                    for y in year_list:
                        if int(y.get_attribute('data-value')) == int(EXPIRES.split('/')[1]):
                            y.click()
                    sleep(2)

                    print('信用卡信息填写完毕！')
                    if country_code.lower() == 'fr':
                        try:
                            browser.find_element_by_id('ccCVVNum').send_keys(CVV)
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_id('ccAddCard').click()
                        except Exception as e:
                            print(e)
                            pass
                        sleep(3)
                        try:
                            browser.find_element_by_xpath('//label/input[@type="radio"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        try:
                            browser.find_element_by_id('continue-top').click()
                        except Exception as e:
                            print(e)
                            pass
                        try:
                            browser.find_element_by_xpath('//label/input[@type="radio"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        try:
                            browser.find_element_by_id('prime-no-thanks').click()
                        except Exception as e:
                            print(e)
                            pass
                    if country_code.lower() == 'ae':
                        sleep(2)
                        try:
                            browser.find_element_by_xpath(
                                '//input[@name="addCreditCardVerificationNumber0"]').send_keys(CVV)
                        except Exception as e:
                            print(e)
                            pass
                        sleep(3)

                    try:
                        browser.find_element_by_xpath(
                            '//span[@class="a-button a-button-primary pmts-button-input"]').click()
                    except Exception as e:
                        print(e)
                        pass
                    try:
                        browser.find_element_by_css_selector('.continue-buttons .a-button.a-button-primary').click()
                    except Exception as e:
                        print(e)
                        pass

                    sleep(3)

                    try:
                        browser.find_element_by_xpath(
                            '//div[@class="a-column a-span8 pmts-cc-detail-row"]/div/div/div/label/input[@type="radio"]').click()
                        sleep(2)
                    except Exception as e:
                        print(e)
                        pass
                    sleep(3)

                    if country_code.lower() == 'ae':
                        sleep(2)
                        try:
                            browser.find_element_by_xpath(
                                '//input[@name="addCreditCardVerificationNumber0"]').send_keys(CVV)
                        except Exception as e:
                            print(e)
                            pass
                        sleep(3)

                    try:
                        browser.find_element_by_css_selector('.a-button-input').click()
                    except Exception as e:
                        print(e)
                        pass
                    sleep(5)
                    browser.find_element_by_id('placeYourOrder').click()
                    sleep(10)
                    browser.quit()
                    return 'success'
                except Exception as e:
                    print(e)
                    print('出错了！')
                    update_sql = 'update email set error="", status="1" where username ="{}"'.format(email)
                    insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
                    try:
                        browser.quit()
                    except Exception as e:
                        print(e)
                        pass
                    try:
                        browser_1.quit()
                    except Exception as e:
                        print(e)
                        pass

            else:
                print('等待处理验证码...')
                while True:
                    sleep(2)
                    try:
                        browser.find_element_by_id('ap_password').send_keys(password)

                        # print(1)
                        try:
                            browser.find_element_by_id('ap_password_check').send_keys(password)
                        except Exception as e:
                            print(e)
                            pass
                        img_url = \
                        browser.find_element_by_id('auth-captcha-image').get_attribute('src').split('?')[0].split('/')[
                            -1]
                        capture_text = ''
                        img = browser.find_element_by_id('auth-captcha-image').get_attribute('src')
                        header = {
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                            'Accept-Encoding': 'gzip, deflate, br',
                            'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6',
                            'Cache-Control': 'max-age=0',
                            'Connection': 'keep-alive',
                            'Sec-Fetch-Mode': 'navigate',
                            'Sec-Fetch-Site': 'none',
                            'Sec-Fetch-User': '?1',
                            'Upgrade-Insecure-Requests': '1',
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
                        }
                        try:
                            data = get(img, headers=header).content
                        except Exception as e:
                            print(e)
                            try:
                                data = get(img, headers=header).content
                            except Exception as e:
                                print(e)
                                pass
                        capture_text = TestFunc(data).pred_rsp.value
                        browser.find_element_by_id('auth-captcha-guess').send_keys(capture_text)
                        if country_code.lower() == 'ae':
                            try:
                                browser.find_element_by_id('auth-create-account-button').click()
                            except Exception as e:
                                print(e)
                                pass
                        else:
                            try:
                                browser.find_element_by_id('continue').click()
                            except Exception as e:
                                print(e)
                                pass
                        # print(img_url)
                    except Exception as e:
                        print(e)
                        break
                print('验证码处理成功！')
                sleep(40)
                # 手动刷新接收邮箱
                browser_1.find_element_by_id('rcmbtn107').click()
                browser_1.get('https://mail.teekar.com/mail/?_task=mail&_mbox=INBOX')
                sleep(3)
                try:
                    mail_url = browser_1.find_element_by_css_selector('.message .subject .subject a').get_attribute(
                        'href')
                except Exception as e:
                    print(e)
                    try:
                        browser_1.get('https://mail.teekar.com/mail/?_task=mail&_mbox=INBOX')
                        sleep(3)
                        mail_url = browser_1.find_element_by_css_selector('.message .subject .subject a').get_attribute(
                            'href')
                    except Exception as e:
                        print(e)
                        update_sql = 'update email set error="" where username ="{}"'.format(email)
                        insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
                        browser.quit()
                        browser_1.quit()
                        pass
                try:
                    browser_1.get(mail_url)
                    sleep(3)
                    code = browser_1.find_element_by_css_selector('p.otp').text.strip()
                    print('成功获取邮箱验证码：', code)
                    # 将邮箱验证码填入，完成注册
                    browser.find_element_by_class_name('cvf-widget-input-code').send_keys(code)
                    browser.find_element_by_id('a-autoid-0').click()
                    print('亚马逊账号注册成功！')
                    browser_1.quit()
                    update_sql = 'update email set error="", status="1" where username ="{}"'.format(email)
                    insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
                    print('打开跟卖页面！')
                    browser.get(group_url)
                    browser.refresh()
                    results = browser.find_elements_by_xpath('//div[@class="a-row a-spacing-mini olpOffer"]')
                    print('成功打开跟卖页面！')

                    data_list = []
                    data_name_list = []
                    for i in results:

                        try:
                            shop_name = i.find_element_by_xpath(
                                './div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a').text
                        except Exception as e:
                            print(e)
                            shop_name = 'other'
                        id_num = i.find_element_by_xpath(
                            './div[@class="a-column a-span2 olpBuyColumn a-span-last"]/div/form/span/span').get_attribute(
                            'id')
                        if shop_name not in shop_name_list:
                            data_list.append([shop_name, id_num])
                            data_name_list.append(shop_name)
                    print('正在赶跟卖卖家：{}'.format(
                        str(data_name_list).replace('[', '').replace(']', '').replace("'", '').replace(',', ' ')))
                    if type_text == 'one':
                        for m in data_list[0: 1]:
                            browser.get(group_url)
                            browser.refresh()
                            browser.find_element_by_id(m[1]).click()
                    else:
                        for m in data_list:
                            browser.get(group_url)
                            browser.refresh()
                            browser.find_element_by_id(m[1]).click()

                    browser.get('https://www.amazon.{}/gp/cart/view.html/ref=lh_cart'.format(domain_stuffix))
                    if country_code.lower() == 'ae':
                        link_list = browser.find_elements_by_css_selector('.sc-action-links.a-span-last')
                        for x, y in zip(link_list, range(len(link_list))):
                            x.find_element_by_css_selector('.quantity').click()
                            browser.find_element_by_id('dropdown{}_9'.format(y + 1)).click()
                            x.find_element_by_css_selector('.sc-quantity-textfield.sc-hidden').send_keys('999')
                            x.find_element_by_css_selector('.sc-update-link').click()
                            sleep(3)
                            try:
                                quantity_value = browser.find_elements_by_css_selector('.sc-action-quantity')[
                                    y].get_attribute('data-old-value')
                            except Exception as e:
                                print(e)
                            try:
                                alert_text = browser.find_element_by_css_selector(
                                    '.a-alert-content .a-size-base').text.strip()
                                print(alert_text)
                                if 'limit' in alert_text.lower() or 'lediglich' in alert_text.lower():
                                    print('有限购，每个用户每次只能购买：', quantity_value, '件，已加入购物车！')
                                else:
                                    print('无限购，跟卖卖家库存总量量为：', quantity_value, '件，已加入购物车！')
                            except Exception as e:
                                print(e)
                    else:

                        link_list = browser.find_elements_by_xpath('//div[@class="a-row sc-action-links"]')
                        for x, y in zip(link_list, range(len(link_list))):
                            x.find_element_by_xpath('./span[@class="sc-action-quantity"]').click()
                            browser.find_element_by_id('dropdown{}_10'.format(y + 1)).click()
                            x.find_element_by_xpath(
                                './span/span/input[@class="a-input-text a-width-small sc-quantity-textfield sc-hidden"]').send_keys(
                                '999')
                            x.find_element_by_xpath('./span/span/span[@class="a-spacing-top-small"]').click()
                            sleep(3)
                            try:
                                quantity_value = browser.find_elements_by_xpath('//span[@class="sc-action-quantity"]')[
                                    y].get_attribute('data-old-value')
                            except Exception as e:
                                print(e)
                            try:
                                alert_text = browser.find_element_by_css_selector(
                                    '.a-alert-content .a-size-base').text.strip()
                                print(alert_text)
                                if 'limit' in alert_text.lower() or 'lediglich' in alert_text.lower():
                                    print('有限购，每个用户每次只能购买：', quantity_value, '件，已加入购物车！')
                                else:
                                    print('无限购，跟卖卖家库存总量量为：', quantity_value, '件，已加入购物车！')
                            except Exception as e:
                                print(e)
                    try:
                        browser.find_element_by_id('sc-buy-box-ptc-button').click()
                    except Exception as e:
                        print(e)
                        browser.quit()
                        browser_1.quit()

                    if country_code.lower() == 'us':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PROVINCE)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()
                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    elif country_code.lower() == 'uk':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        if browser.find_element_by_id('enterAddressCity').text == '':
                            browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(COUNTRY)

                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()
                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    elif country_code.lower() == 'ca':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)

                        select_ele = browser.find_element_by_xpath('//select[@id="enterAddressStateOrRegion"]')
                        s = Select(select_ele)
                        s.select_by_value(PV)  # 使用value方式选择值"微软 Powerpoint (.ppt)"

                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()
                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    elif country_code.lower() == 'fr':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()
                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    elif country_code.lower() == 'de':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()
                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    elif country_code.lower() == 'it':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()
                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    elif country_code.lower() == 'ae':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        ccc = 3
                        while ccc > 1:
                            browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                            sleep(5)
                            try:
                                browser.find_element_by_css_selector('ul.autoCompleteResult').click()
                            except:
                                pass
                            try:
                                browser.find_element_by_id('enterAddressCity').send_keys(Keys.ENTER)
                            except:
                                pass
                            sleep(10)
                            browser.find_element_by_id('enterAddressDistrictOrCounty').send_keys(PV)
                            sleep(5)
                            try:
                                browser.find_element_by_css_selector('ul.autoCompleteResult').click()
                            except:
                                pass
                            try:
                                browser.find_element_by_id('enterAddressDistrictOrCounty').send_keys(Keys.ENTER)
                            except:
                                pass
                            ccc = ccc - 1
                        sleep(2)
                        try:
                            browser.find_element_by_css_selector('.a-button.a-button-primary.a-padding-none ').click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()
                        except Exception as e:
                            print(e)
                            pass

                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        try:
                            browser.find_element_by_css_selector(
                                '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        except Exception as e:
                            print(e)
                            pass
                        print('地址填写完毕！')
                    elif country_code.lower() == 'es':
                        print('正在填写地址信息...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()
                        sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('地址填写完毕！')
                    else:
                        pass

                    sleep(5)
                    if country_code.lower() in ['fr', 'es']:
                        try:
                            browser.find_element_by_css_selector(
                                '#wrapper-new-cc div .a-link-expander.a-declarative').click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-add-new-card').click()
                        except Exception as e:
                            print(e)
                            pass
                        sleep(5)

                        try:
                            browser.find_element_by_id('ccName').send_keys(username)
                        except Exception as e:
                            print(e)
                            pass

                    try:
                        browser.find_element_by_xpath('//input[@name="ppw-accountHolderName"]').send_keys(username)
                    except Exception as e:
                        print(e)
                        try:
                            browser.find_element_by_css_selector(
                                '#wrapper-new-cc div .a-link-expander.a-declarative').click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-add-new-card').click()
                        except Exception as e:
                            print(e)
                            pass
                        sleep(5)

                        try:
                            browser.find_element_by_id('ccName').send_keys(username)
                        except Exception as e:
                            print(e)
                            pass
                    sleep(2)
                    try:
                        browser.find_element_by_xpath('//input[@name="ppw-accountHolderName"]').send_keys(username)
                    except Exception as e:
                        print(e)

                    browser.find_element_by_xpath('//input[@name="addCreditCardNumber"]').send_keys(CARD)
                    if country_code.lower() == 'fr':
                        try:
                            browser.find_element_by_css_selector('.card-date .a-button.a-button-dropdown').click()
                        except Exception as e:
                            print(e)
                            pass

                    else:
                        try:
                            browser.find_element_by_css_selector('.a-nostyle.a-list-link').click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-expiry-month').click()
                        except Exception as e:
                            print(e)
                            pass
                    sleep(2)

                    month_list = browser.find_elements_by_xpath('//ul[@id="1_dropdown_combobox"]/li/a')
                    for x in month_list:
                        if int(x.get_attribute('data-value')) == int(EXPIRES.split('/')[0]):
                            x.click()
                    sleep(3)
                    if country_code.lower() == 'fr':
                        try:
                            browser.find_elements_by_css_selector('.card-date .a-button-text.a-declarative')[1].click()
                        except Exception as e:
                            print(e)
                            pass
                    else:
                        try:
                            browser.find_elements_by_css_selector('.a-nostyle.a-list-link')[1].click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-expiry-year').click()
                        except Exception as e:
                            print(e)
                            pass
                    sleep(2)
                    year_list = browser.find_elements_by_xpath('//ul[@id="2_dropdown_combobox"]/li/a')
                    for y in year_list:
                        if int(y.get_attribute('data-value')) == int(EXPIRES.split('/')[1]):
                            y.click()
                    sleep(2)
                    if country_code.lower() == 'fr':
                        try:
                            browser.find_element_by_id('ccCVVNum').send_keys(CVV)
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_id('ccAddCard').click()
                        except Exception as e:
                            print(e)
                            pass
                        sleep(3)
                        try:
                            browser.find_element_by_xpath('//label/input[@type="radio"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        try:
                            browser.find_element_by_id('continue-top').click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_xpath('//label/input[@type="radio"]').click()
                        except Exception as e:
                            print(e)
                            pass
                        try:
                            browser.find_element_by_id('prime-no-thanks').click()
                        except Exception as e:
                            print(e)
                            pass

                    if country_code.lower() == 'ae':
                        sleep(3)
                        try:
                            browser.find_element_by_xpath(
                                '//input[@name="addCreditCardVerificationNumber0"]').send_keys(CVV)
                        except Exception as e:
                            print(e)
                            pass
                        sleep(3)

                    try:
                        browser.find_element_by_xpath(
                            '//span[@class="a-button a-button-primary pmts-button-input"]').click()
                    except Exception as e:
                        print(e)
                        pass
                    try:
                        browser.find_element_by_css_selector('.continue-buttons .a-button.a-button-primary').click()
                    except Exception as e:
                        print(e)
                        pass

                    if country_code.lower() == 'ae':
                        sleep(3)
                        try:
                            browser.find_element_by_xpath(
                                '//input[@name="addCreditCardVerificationNumber0"]').send_keys(CVV)
                        except Exception as e:
                            print(e)
                            pass
                        sleep(3)

                    try:
                        browser.find_element_by_xpath(
                            '//span[@class="a-button a-button-primary pmts-button-input"]').click()
                    except Exception as e:
                        print(e)
                        pass

                    print('信用卡信息填写完毕！')
                    sleep(3)
                    try:
                        browser.find_element_by_xpath(
                            '//div[@class="a-column a-span8 pmts-cc-detail-row"]/div/div/div/label/input[@type="radio"]').click()
                        sleep(2)
                    except Exception as e:
                        print(e)
                        pass
                    sleep(3)
                    try:
                        browser.find_element_by_css_selector('.a-button-input').click()
                    except Exception as e:
                        print(e)
                        pass
                    sleep(5)
                    browser.find_element_by_id('placeYourOrder').click()
                    sleep(10)
                    browser.quit()
                    return 'success'
                except Exception as e:
                    print(e)
                    # except:
                    print('出错了！')
                    update_sql = 'update email set error="", status="1" where username ="{}"'.format(email)
                    insert_update_drop_data(connect, update_sql, '更改邮件状态成功！')
                    try:
                        browser.quit()
                    except Exception as e:
                        print(e)
                        pass
                    try:
                        browser_1.quit()
                    except Exception as e:
                        print(e)
                        pass

        else:
            browser.quit()
            pass
            return 'no'
    except Exception as e:
        print(e)
        print('出错了！')
        try:
            browser.quit()
        except Exception as e:
            print(e)
            pass
        try:
            browser_1.quit()
        except Exception as e:
            print(e)
            pass
        pass


def read_excel_self(f_path):
    res = read_excel(f_path)
    data_list = []
    for i in res:
        data_list.append(res[i].to_list())

    new_data_list = []

    for a, b, c in zip(data_list[0], data_list[1], data_list[2]):
        new_data_list.append([a, b, c])
    return new_data_list


def main(asin_text, country_code_text, shop_name_text, type_text, file_path_text):
    connect = connect_db(DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT)
    new_file_path = file_path_text.replace(file_path_text.split('\\')[-1], 'Result_' + file_path_text.split('\\')[-1])
    if country_code_text.lower() == 'us':
        country_name = '美国 com'
    elif country_code_text.lower() == 'uk':
        country_name = '英国 uk'
    elif country_code_text.lower() == 'ca':
        country_name = '加拿大 ca'
    elif country_code_text.lower() == 'fr':
        country_name = '法国 fr'
    elif country_code_text.lower() == 'de':
        country_name = '德国 de'
    elif country_code_text.lower() == 'it':
        country_name = '意大利 it'
    elif country_code_text.lower() == 'ae':
        country_name = '中东 ae'
    elif country_code_text.lower() == 'es':
        country_name = '西班牙 es'
    else:
        pass

    print('')
    print('=================================基本信息=================================')
    print('Asin：', asin_text)
    print('站点：', country_name)
    if str(shop_name_text).strip() == 'nan' or str(shop_name_text).strip() == '':
        our_shop_name = ''
    else:
        our_shop_name = str(str(shop_name_text).split('->')).replace('[', '').replace(']', '').replace("'", '').replace(
            ',', ' ')
    print('我们的店铺名：', our_shop_name)
    print('赶跟卖模式：', type_text)
    result = get_out_amzer(connect, asin_text, country_code_text, shop_name_text, type_text)

    try:
        connect.close()
    except Exception as e:
        print(e)
    if result == 'success':
        print('下单成功！')
        print('程序等待三分钟再运行...')
        sleep(180)
        print('=========================================================================')
    elif result == 'no':
        print('没有跟卖！！！')
        rea_results = ''
        try:
            with open(new_file_path.replace('.xlsx', '.csv'), 'r') as rea:
                rea_results = rea.read()
                rea.close()
        except Exception as e:
            print(e)
        if asin_text not in rea_results:
            with open(new_file_path.split('.')[0] + '.csv', 'a', encoding='utf-8-sig')as f:
                f.write(str(
                    asin_text + ',' + country_code_text + ',' + shop_name_text + ',' + type_text + ',已赶走！').strip() + '\n')
                f.close()
        print('程序等待三分钟再运行...')
        sleep(180)
    else:
        print('出现错误！！！')

    print('')
    print('')


if __name__ == '__main__':
    print('=================================信息输入=================================')

    file_path = input(r'请输入配置文件地址(例如；C:\Desktop\jack.xlsx)：')
    while True:
        if '"' in file_path:
            print('1')
            file_path = file_path.replace('"', '')
        datas_list = read_excel_self(file_path)
        for data in datas_list:
            print(data)
            asin = data[0]
            country_code = data[1]
            shop_name = data[2]
            type_te = 'all'

            main(asin, country_code, shop_name, type_te, file_path)

    # asin = input('请输入Asin：').strip()
    # if asin.isalnum() is True:
    #     pass
    # else:
    #     while True:
    #         asin = input('输入的asin不能包含特殊字符，请重新输入Asin：')
    #         if asin.isalnum() is True:
    #             break
    # # asin = 'B07V4R3J31'
    # # asin = 'B07YL2T543'
    # # asin = 'B079JL2FSY'
    # # country_code = 'uk'
    # # country_code = 'fr'
    # country_list = ['us', 'uk', 'ca', 'fr', 'de', 'it', 'ae', 'es']
    # country_code = input('请输入亚马逊站点的国别码（例如：英国:uk,美国:us,法国:fr,加拿大:ca）：')
    # if country_code.lower() in country_list:
    #     pass
    # else:
    #     while True:
    #         # print('国家代码输入错误，请重新输入：')
    #         country_code = input('国家代码输入错误，请重新输入：')
    #         if country_code.lower() in country_list:
    #             break
    # # country_code = 'ca'
    # # shop_name = 'Tianyu.HC'
    # shop_name = input('请输入我们公司自己的店铺名称（即：不需要赶走的，多个店铺名时使用“->”分开，例：shop_1->shop_2）：')
    # # print(shop_name)
    # shop_name = shop_name.strip()
    # # print(shop_name)
    # type_te = input('请输入一次赶走一个卖家还是全部（填one或者all, 优先填all）：')
    # if type_te.lower().strip() in ['one', 'all']:
    #     pass
    # else:
    #     while True:
    #         type_te = input('输入错误！请输入one或all：')
    #         if type_te.lower().strip() in ['one', 'all']:
    #             break
    # print('=========================================================================')
    # print('')
    # # print('--------------------------------------程序开始启动--------------------------------------')
    # while True:
    #     main(asin, country_code, shop_name, type_te)

