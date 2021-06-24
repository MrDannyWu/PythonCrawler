"""
create: 2019.11.11
company: Umiwe
auth:
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random
from auto_setup_amz.db import *
from auto_setup_amz.db_utils import *
import requests
from auto_setup_amz.fateadm_api import TestFunc
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import string
import zipfile
import pandas as pd


def create_proxy_auth_extension(scheme='http', plugin_path=None):
    # ���������
    proxy_host = "http-pro.abuyun.com"
    proxy_port = "9010"

    # ���������֤��Ϣ
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

    background_js = string.Template(
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

    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)

    return plugin_path


def get_out_amzer(connect, asin, country_code, shop_name, type_text):
    try:
        shop_name_list = shop_name.split('->')
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
            STREET = 'Paseo Roncesvalles N��67'
            CITY = 'Cizur menor'
            PV = 'Navarra'
            COUNTRY = 'ES'
            POSTCODE = '31190'
        else:
            domain_stuffix = country_code.lower()
        PASSWORD = '12344321'
        group_url = 'https://www.amazon.{}/gp/offer-listing/{}'.format(domain_stuffix, asin)

        print('����ҳ���ַ��', group_url)
        print('=========================================================================')
        print('')
        print('=================================��Ϣ���=================================')
        print('�������������...')
        chrome_options = Options()
        chrome_options.add_argument('blink-settings=imagesEnabled=false')
        # chrome_options.add_argument('--user-data-dir=D:\\ud')
        # # self.chrome_options.add_argument('--proxy-server=' +
        # # proxy.replace('https', 'http'))
        # resp = requests.get('http://10.11.2.33:5010/get/')
        # json_data_1 = json.loads(resp.text)
        # proxy = json_data_1['proxy']
        # web_resp = requests.get('http://ged.ip3366.net/api/?key=20191122150329175&getnum=1&filter=1&proxytype=1')
        # print(web_resp.text)
        # proxy = web_resp.text
        # resp = requests.get('http://183.129.244.16:88/open?user_name=sahbnesrhbnwtp1&timestamp=1575366632&md5=C03318739F51AEB2303E80D0EAC110DD&pattern=txt&number=1')
        # print(resp.text)
        # print(resp.text.split('\n')[-1])
        # proxy = resp.text.split('\n')[-1]

        executable_path = 'chromedriver.exe'
        # chrome_options.add_argument('--proxy-server=http://{}'.format(proxy))
        # chrome_options.add_argument('--proxy-server=http://10.11.2.251:3128')
        # chrome_options.add_argument('--proxy-server=http://{}'.format(proxy))
        # chrome_options.add_argument('--proxy-server=http://{}'.format(proxy))
        # chrome_options.add_argument('--proxy-server=http://171.223.207.30:8001')

        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--headless')
        # Ongan [OC13]->TD-Twelve
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_argument('log-level=3')
        # proxy_auth_plugin_path = create_proxy_auth_extension()
        # chrome_options.binary_location = 'Chrome/Application/Chrome.exe'
        # chrome_options.add_extension(proxy_auth_plugin_path)

        browser = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
        # browser.get('https://www.baidu.com/s?wd=ip')
        # time.sleep(10)
        # browser.set_window_size(1500, 960)
        # browser.set_window_size(1,1)
        browser.delete_all_cookies()
        print('�����������ϣ�')

        # group_url = 'https://www.amazon.com/gp/offer-listing/B07VJRZ62R' B07S636X9B
        print('���ڴ򿪸���ҳ��...')
        browser.get(group_url)
        browser.refresh()

        if country_code.lower() == 'us':
            browser.get(
                'https://www.amazon.com/gp/customer-preferences/select-language/ref=topnav_lang_c_ais?preferencesReturnUrl=%2Fgp%2Fproduct%2FB07XKZTM17%3Fpf_rd_p%3D2d1ab404-3b11-4c97-b3db-48081e145e35%26pf_rd_r%3DQPHNKRYSJQD1HT549CK2')
            time.sleep(3)
            browser.find_element_by_css_selector('.a-popover-trigger.a-declarative').click()
            time.sleep(2)
            browser.find_element_by_id('GLUXCountryListDropdown').click()
            a_list = browser.find_elements_by_css_selector(
                '.a-popover.a-dropdown.a-dropdown-common.a-declarative ul li a')
            for a in a_list:
                # print(a)
                if 'united states' in a.text.lower():
                    a.click()
                    break
            browser.find_element_by_xpath('//button[@name="glowDoneButton"]').click()
            browser.find_element_by_id('icp-btn-save')
            browser.get(group_url)

        if country_code.lower() == 'fr':
            browser.find_element_by_id('nav-global-location-slot').click()
            time.sleep(3)
            browser.find_element_by_id('GLUXCountryListDropdown').click()
            a_list = browser.find_elements_by_css_selector(
                '.a-popover.a-dropdown.a-dropdown-common.a-declarative ul li a')
            for a in a_list:
                # print(a)
                if 'guyane fran?aise' in a.text.lower():
                    a.click()
                    break
                # browser.find_element_by_xpath('//button[@name="glowDoneButton"]').click()
                # browser.find_element_by_id('icp-btn-save')
                # browser.get(group_url)
        time.sleep(5)

        results = browser.find_elements_by_xpath('//div[@class="a-row a-spacing-mini olpOffer"]')
        # print(results)
        print('�ɹ��򿪸���ҳ�棡')

        shop_list = []
        temp_name_list = []
        for i in results:

            # print(i)
            try:
                shop_name = i.find_element_by_xpath('./div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a').text
            except Exception as e:
                print(e)
                shop_name = 'other'
            id_num = i.find_element_by_xpath(
                './div[@class="a-column a-span2 olpBuyColumn a-span-last"]/div/form/span/span').get_attribute('id')
            # print(shop_name)
            if shop_name not in shop_name_list:
                shop_list.append([shop_name, id_num])
                temp_name_list.append(shop_name)

        if len(shop_list) > 0:
            print('')
            print('���� {} ���������ң�{}'.format(len(shop_list),
                                          str(temp_name_list).replace('[', '').replace(']', '').replace("'",
                                                                                                        '').replace(',',
                                                                                                                    ' ')))
            print('')
            browser_1 = webdriver.Chrome(executable_path=executable_path, options=chrome_options)
            # browser_1.minimize_window()
            # browser_1.set_window_size(1,1)
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
            insert_update_drop_data(connect, update_sql, '����Ϊusing')

            results[1][0][0]
            # print(results[1][0][0])
            # print(results[1][0][1])
            email = results[1][0][1]
            # domain_stuffix =
            if country_code.lower() == 'aea':
                pass
            else:
                query_virtual_people_sql = 'select phone,card,expires,cvv2 from virtual_people where country ="{}"'.format(
                    country_code.lower())
                # print(query_virtual_people_sql)
                virtual_peoples = query_results(connect, query_virtual_people_sql)[1]
                # print(virtual_peoples)
                virtual_people_list = []
                for i in virtual_peoples:
                    virtual_people_list.append(i)
                virtual_people_data = random.choice(virtual_people_list)
                # print(virtual_people_data)
                # EMAIL = 'ghresdghesuh@volbaby.com'

                # PHONE = '641-660-0191'
                # CARD = '4916 5000 0531 8963'
                # EXPIRES = '1/2021'

                PHONE = virtual_people_data[0]
                CARD = virtual_people_data[1]
                EXPIRES = virtual_people_data[2]
                CVV = virtual_people_data[3]

            # print(group_url)

            # �ȵ�½����
            zz = 0
            while True:
                if zz == 15:
                    update_sql = 'update email set error="" where username ="{}"'.format(email)
                    insert_update_drop_data(connect, update_sql, '�����ʼ�״̬�ɹ���')
                    browser.quit()
                    browser_1.quit()
                    break
                try:
                    browser_1.get('https://mail.teekar.com/mail/')
                    break
                # except:
                except Exception as e:
                    print(e)
                    try:
                        browser_1.get('https://mail.teekar.com/mail/')
                        break
                    # except:
                    except Exception as e:
                        print(e)
                        # update_sql = 'update email set error="" where username ="{}"'.format(email)
                        # insert_update_drop_data(connect, update_sql, '�����ʼ�״̬�ɹ���')
                        # browser.quit()
                        # browser_1.quit()
                        pass
                zz += 1
            browser_1.find_element_by_id('rcmloginuser').send_keys(email)
            browser_1.find_element_by_id('rcmloginpwd').send_keys(PASSWORD)
            browser_1.find_element_by_id('rcmloginsubmit').click()

            # browser = webdriver.Chrome()
            # ��Amazon��ҳ�������ע��
            if country_code.lower() == 'uk':
                browser.get(
                    'https://www.amazon.co.uk/ap/register?_encoding=UTF8&openid.assoc_handle=gbflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.co.uk%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_newcust')
            else:
                browser.get('https://www.amazon.{}'.format(domain_stuffix))

                time.sleep(5)
                print(browser.find_element_by_id('nav-link-accountList').get_attribute('href'))
                nav_link_account_list = browser.find_element_by_id('nav-link-accountList').get_attribute('href')

                try:
                    # browser.find_element_by_id('nav-link-accountList').click()
                    browser.get(browser.find_element_by_id('nav-link-accountList').get_attribute('href'))
                # except:
                except Exception as e:
                    print(e)
                    try:
                        browser.refresh()
                        time.sleep(10)
                        browser.get(browser.find_element_by_id('nav-link-accountList').get_attribute('href'))
                        # browser.find_element_by_id('nav-link-accountList').click()
                    # except:
                    except Exception as e:
                        print(e)
                        browser.quit()
                        browser_1.quit()
                        update_sql = 'update email set error="" where username ="{}"'.format(email)
                        insert_update_drop_data(connect, update_sql, '�����ʼ�״̬�ɹ���')
                # time.sleep(10)
                if 'homepage' in nav_link_account_list:
                    time.sleep(3)
                    try:
                        browser.get(browser.find_element_by_id('nav-link-accountList').get_attribute('href'))
                    except Exception as e:
                        print(e)
                        pass

                try:
                    browser.find_element_by_id('createAccountSubmit').click()
                except Exception as e:
                    print(e)
                    # except:
                    try:
                        browser.refresh()
                        time.sleep(10)
                        browser.find_element_by_id('createAccountSubmit').click()
                    except Exception as e:
                        print(e)
                        # except:
                        browser.quit()
                        browser_1.quit()
                        update_sql = 'update email set error="" where username ="{}"'.format(email)
                        insert_update_drop_data(connect, update_sql, '�����ʼ�״̬�ɹ���')
            time.sleep(2)
            # browser.get('https://www.amazon.com/ap/register?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_newcust')

            # ��������û���
            cha_list = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h',
                        'g', 'f', 'e', 'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            username = ''.join(random.sample(cha_list, 9))
            print('��������û�����', username)
            password = 'gsdyghFrefghsD.'
            print('�˻�����Ϊ��', password)
            browser.find_element_by_id('ap_customer_name').send_keys(username)
            # ��ȡ����
            print('���ڻ�ȡ����...')
            # browser_1.get('http://24mail.chacuo.net/enus')
            # browser_1.find_element_by_xpath('//select[@class="f16p"]').click()

            # email = browser_1.find_element_by_id('mail_copy').get_attribute('data-clipboard-text')

            print('�ɹ���ȡ���䣺', email)
            print('��ʼע������ѷ�˺�...')

            # print(browser.page_source)
            # print(str(browser.find_element_by_id('ap_use_email')))
            # print(browser.find_element_by_id('ap_use_email').get_attribute('id'))
            try:
                browser.find_element_by_id('ap_use_email').click()
            except Exception as e:
                print(e)
                pass
            time.sleep(2)
            # ע����������û����������� ��ʼע��
            browser.find_element_by_id('ap_email').send_keys(email)
            # print(0)
            # time.sleep(3)
            browser.find_element_by_id('ap_password').send_keys(password)
            # time.sleep(3)
            # print(1)
            try:
                browser.find_element_by_id('ap_password_check').send_keys(password)
            except Exception as e:
                print(e)
                pass
            # time.sleep(100000)
            # print(2)
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

            # time.sleep(10000)
            time.sleep(1)
            # if 'cap'
            browser.find_elements_by_id('auth-captcha-image')
            print(len(browser.find_elements_by_id('auth-captcha-image')))
            if len(browser.find_elements_by_id('auth-captcha-image')) == 0:
                # print(3)
                time.sleep(50)
                # �ֶ�ˢ�½�������Ting.Store
                browser_1.find_element_by_id('rcmbtn107').click()
                # browser_1.find_element_by_id('rcmliSU5CT1g').click()
                browser_1.get('https://mail.teekar.com/mail/?_task=mail&_mbox=INBOX')
                time.sleep(3)

                try:
                    mail_url = browser_1.find_element_by_css_selector('.message .subject .subject a').get_attribute(
                        'href')
                except Exception as e:
                    print(e)
                    # except:
                    try:
                        browser_1.get('https://mail.teekar.com/mail/?_task=mail&_mbox=INBOX')
                        time.sleep(3)
                        mail_url = browser_1.find_element_by_css_selector('.message .subject .subject a').get_attribute(
                            'href')
                    except Exception as e:
                        print(e)
                        # except:
                        update_sql = 'update email set error="" where username ="{}"'.format(email)
                        insert_update_drop_data(connect, update_sql, '�����ʼ�״̬�ɹ���')
                        browser.quit()
                        browser_1.quit()
                        pass

                # mail_url = browser_1.find_element_by_css_selector('.message .subject .subject a').get_attribute('href')
                try:
                    browser_1.get(mail_url)
                    # print('1111111111111111111111111111')
                    # print(2222222222222222222222222222222)
                    time.sleep(3)
                    # print(browser_1.page_source)
                    # try:
                    #     # ���յ�������
                    #     browser_1.find_element_by_id('convertd').click()
                    #     time.sleep(3)
                    # except:
                    #     browser.find_element_by_css_selector('div.a-section.a-spacing-none.a-spacing-top-large.a-text-center.cvf-widget-section-js a').click()
                    #     time.sleep(30)
                    #     # �ֶ�ˢ�½�������
                    #     browser_1.find_element_by_class_name('red').click()
                    #     # ���յ�������
                    #     browser_1.find_element_by_id('convertd').click()
                    #     time.sleep(3)
                    # ��ȡ������֤��
                    code = browser_1.find_element_by_css_selector('p.otp').text.strip()
                    print('�ɹ���ȡ������֤�룺', code)
                    # time.sleep(20)
                    # ��������֤�����룬���ע��
                    browser.find_element_by_class_name('cvf-widget-input-code').send_keys(code)
                    # time.sleep(100)
                    browser.find_element_by_id('a-autoid-0').click()
                    print('����ѷ�˺�ע��ɹ���')
                    browser_1.quit()
                    update_sql = 'update email set error="", status="1" where username ="{}"'.format(email)
                    insert_update_drop_data(connect, update_sql, '�����ʼ�״̬�ɹ���')

                    # �򿪸���ҳ��
                    print('�򿪸���ҳ�棡')
                    browser.get(group_url)
                    browser.refresh()
                    # results = browser.find_elements_by_css_selector('#olpOfferList div.a-section.a-padding-small div.a-section.a-spacing-double-large div.a-row.a-spacing-mini.olpOffer')
                    # print('�ɹ��򿪸���ҳ�棡')
                    # for i in results:
                    #     # print(i)
                    #     try:
                    #         shop_name = i.find_element_by_css_selector('div.a-column.a-span2.olpSellerColumn h3 span a').text
                    #     except:
                    #         shop_name = 'other'
                    #
                    #     if shop_name not in shop_name_list:
                    #         print('���ڸ��߸������ң�', shop_name)
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
                    print('�ɹ��򿪸���ҳ�棡')

                    # shop_name_list = ['Zadii']
                    data_list = []
                    data_name_list = []
                    for i in results:

                        # print(i)
                        try:
                            shop_name = i.find_element_by_xpath(
                                './div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a').text
                        except Exception as e:
                            print(e)
                            # except:
                            shop_name = 'other'
                        id_num = i.find_element_by_xpath(
                            './div[@class="a-column a-span2 olpBuyColumn a-span-last"]/div/form/span/span').get_attribute(
                            'id')
                        # print(shop_name)
                        if shop_name not in shop_name_list:
                            data_list.append([shop_name, id_num])
                            data_name_list.append(shop_name)
                    # print(data_list)
                    print('���ڸϸ������ң�{}'.format(
                        str(data_name_list).replace('[', '').replace(']', '').replace("'", '').replace(',', ' ')))
                    # for m in data_list:
                    #     browser.get(group_url)
                    #     browser.refresh()
                    #     browser.find_element_by_id(m[1]).click()
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
                    # time.sleep(10000)

                    if country_code.lower() == 'ae':
                        link_list = browser.find_elements_by_css_selector('.sc-action-links.a-span-last')
                        for x, y in zip(link_list, range(len(link_list))):
                            x.find_element_by_css_selector('.quantity').click()
                            browser.find_element_by_id('dropdown{}_9'.format(y + 1)).click()
                            x.find_element_by_css_selector('.sc-quantity-textfield.sc-hidden').send_keys('999')
                            x.find_element_by_css_selector('.sc-update-link').click()
                            time.sleep(5)
                    else:

                        link_list = browser.find_elements_by_xpath('//div[@class="a-row sc-action-links"]')
                        # time.sleep(100000)
                        for x, y in zip(link_list, range(len(link_list))):
                            x.find_element_by_xpath('./span[@class="sc-action-quantity"]').click()
                            browser.find_element_by_id('dropdown{}_10'.format(y + 1)).click()
                            x.find_element_by_xpath(
                                './span/span/input[@class="a-input-text a-width-small sc-quantity-textfield sc-hidden"]').send_keys(
                                '999')
                            x.find_element_by_xpath('./span/span/span[@class="a-spacing-top-small"]').click()
                            time.sleep(5)

                            try:
                                quantity_value = browser.find_elements_by_xpath('//span[@class="sc-action-quantity"]')[
                                    y].get_attribute('data-old-value')
                                print('����: ', quantity_value)
                            except Exception as e:
                                print(e)
                            try:
                                alert_text = browser.find_element_by_css_selector(
                                    '.a-alert-content .a-size-base').text.strip()
                                print(alert_text)
                                if 'limit' in alert_text:
                                    print('���޹����޹�����Ϊ��', quantity_value)
                            except Exception as e:
                                print(e)

                    # for x, y in zip(link_list, range(len(link_list))):
                    #     x.find_element_by_xpath('./span[@class="sc-action-quantity"]').click()
                    #     browser.find_element_by_id('dropdown{}_10'.format(y + 1)).click()
                    #     x.find_element_by_xpath('./span/span/input[@class="a-input-text a-width-small sc-quantity-textfield sc-hidden"]').send_keys('999')
                    #     x.find_element_by_xpath('./span/span/span[@class="a-spacing-top-small"]').click()
                    #     time.sleep(5)

                    browser.find_element_by_id('sc-buy-box-ptc-button').click()

                    # browser.get('https://www.amazon.com/a/addresses/add?ref=ya_address_book_add_button')
                    # ��д�½���ַ��Ϣ
                    if country_code.lower() == 'us':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # browser.find_element_by_id('enterAddressAddressLine2').send_keys()
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PROVINCE)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        # browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        # print('��ַ��д��ϣ�')
                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'uk':
                        print('������д��ַ��Ϣ...')
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
                        # print('��ַ��д��ϣ�')
                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'ca':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # if browser.find_element_by_id('enterAddressCity').text == '':
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        # browser.find_element_by_id('enterAddressStateOrRegion').click()
                        # time.sleep(3)

                        select_ele = browser.find_element_by_xpath('//select[@id="enterAddressStateOrRegion"]')
                        # 2.��ʼ��select��
                        s = Select(select_ele)
                        # ѡ��ֵ
                        # 1.�±�
                        # s.select_by_index(2)  # ʹ���±�ѡ��"΢�� Word (.doc)"
                        # time.sleep(3)
                        # 2.valueֵ
                        s.select_by_value(PV)  # ʹ��value��ʽѡ��ֵ"΢�� Powerpoint (.ppt)"
                        # time.sleep(3)
                        # # 3.ͨ���ı���ʽ
                        # s.select_by_visible_text('RTF �ļ� ��.rtf)')

                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)

                        # browser.find_element_by_id('enterAddressAddressLine2').send_keys()

                        # browser.find_element_by_id('enterAddressStateOrRegion').send_keys(COUNTRY)

                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        # browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        # print('��ַ��д��ϣ�')
                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'fr':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # if browser.find_element_by_id('enterAddressCity').text == '':
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)

                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)

                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)

                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'de':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # if browser.find_element_by_id('enterAddressCity').text == '':
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)

                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)

                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)

                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'it':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # if browser.find_element_by_id('enterAddressCity').text == '':
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)

                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)

                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)

                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'ae':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # if browser.find_element_by_id('enterAddressCity').text == '':
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        time.sleep(2)
                        browser.find_element_by_id('enterAddressCity').send_keys(Keys.ENTER)

                        browser.find_element_by_id('enterAddressDistrictOrCounty').send_keys(PV)
                        time.sleep(2)
                        browser.find_element_by_id('enterAddressDistrictOrCounty').send_keys(Keys.ENTER)

                        # browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        # time.sleep(100000)

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

                        time.sleep(2)
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
                            # except:
                            pass
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'es':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # if browser.find_element_by_id('enterAddressCity').text == '':
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)

                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)

                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)

                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    else:
                        pass
                    time.sleep(5)
                    # soup = BeautifulSoup(browser.page_source, 'lxml')
                    # pre_text = soup.select('.a-section.a-spacing-none.pmts-widget-section')[0].get('data-pmts-component-id').split('-')[1]
                    # print(pre_text)
                    # time.sleep(10000)
                    # ��д���ÿ���Ϣ
                    print('������д���ÿ���Ϣ...')
                    if country_code.lower() in ['fr', 'es']:
                        try:
                            browser.find_element_by_css_selector(
                                '#wrapper-new-cc div .a-link-expander.a-declarative').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-add-new-card').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        time.sleep(5)

                        try:
                            browser.find_element_by_id('ccName').send_keys(username)
                        except Exception as e:
                            print(e)
                            # except:
                            pass

                    try:
                        browser.find_element_by_xpath('//input[@name="ppw-accountHolderName"]').send_keys(username)
                    except Exception as e:
                        print(e)
                        # except:
                        pass

                    browser.find_element_by_xpath('//input[@name="addCreditCardNumber"]').send_keys(CARD)

                    # browser.find_element_by_xpath('//input[@name="ppw-expirationDate_month"]').click()
                    # browser.find_element_by_id('pp-{}-52'.format(pre_text)).send_keys(CARD)
                    # browser.find_element_by_id('pp-{}-59'.format(pre_text)).click()
                    # time.sleep(300)
                    if country_code.lower() == 'fr':
                        try:
                            browser.find_element_by_css_selector('.card-date .a-button.a-button-dropdown').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass

                    else:
                        try:
                            # browser.find_element_by_css_selector('.pmts-expiry-month').click()
                            browser.find_element_by_css_selector('.a-nostyle.a-list-link').click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-expiry-month').click()
                            # browser.find_element_by_css_selector('.a-nostyle.a-list-link').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                    time.sleep(2)

                    try:
                        month_list = browser.find_elements_by_xpath('//ul[@id="1_dropdown_combobox"]/li/a')
                    except Exception as e:
                        print(e)
                        # except:
                        pass
                    time.sleep(1)
                    # print(month_list)
                    for x in month_list:
                        # print(x)
                        if int(x.get_attribute('data-value')) == int(EXPIRES.split('/')[0]):
                            x.click()
                    #
                    # browser.find_element_by_id('pp-{}-60'.format(pre_text)).click()
                    if country_code.lower() == 'fr':
                        try:
                            browser.find_elements_by_css_selector('.card-date .a-button-text.a-declarative')[1].click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                    else:
                        try:
                            # browser.find_element_by_css_selector('.pmts-expiry-year').click()
                            browser.find_elements_by_css_selector('.a-nostyle.a-list-link')[1].click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-expiry-year').click()
                            # browser.find_elements_by_css_selector('.a-nostyle.a-list-link')[1].click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                    time.sleep(2)
                    year_list = browser.find_elements_by_xpath('//ul[@id="2_dropdown_combobox"]/li/a')
                    for y in year_list:
                        # print(y)
                        if int(y.get_attribute('data-value')) == int(EXPIRES.split('/')[1]):
                            y.click()
                    time.sleep(2)

                    # try:
                    #     browser.find_element_by_xpath('//input[@name="addCreditCardVerificationNumber"]').send_keys(CVV)
                    # except:
                    #     pass
                    print('���ÿ���Ϣ��д��ϣ�')
                    # browser.find_element_by_id('pp-{}-61'.format(pre_text)).click()
                    # browser.find_element_by_css_selector('.a-button.a-button-primary.pmts-button-input').click()
                    if country_code.lower() == 'fr':
                        try:
                            browser.find_element_by_id('ccCVVNum').send_keys(CVV)
                        except Exception as e:
                            print(e)
                            # except:
                            pass

                        try:
                            browser.find_element_by_id('ccAddCard').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        time.sleep(3)
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

                    try:
                        browser.find_element_by_xpath(
                            '//span[@class="a-button a-button-primary pmts-button-input"]').click()
                    except Exception as e:
                        print(e)
                        # except:
                        pass
                    try:
                        browser.find_element_by_css_selector('.continue-buttons .a-button.a-button-primary').click()
                    except Exception as e:
                        print(e)
                        # except:
                        pass

                    time.sleep(3)

                    if country_code.lower() == 'ae':
                        time.sleep(3)
                        try:
                            browser.find_element_by_xpath(
                                '//input[@name="addCreditCardVerificationNumber0"]').send_keys(CVV)
                        except Exception as e:
                            print(e)
                            pass
                        time.sleep(3)

                    try:
                        browser.find_element_by_xpath(
                            '//div[@class="a-column a-span8 pmts-cc-detail-row"]/div/div/div/label/input[@type="radio"]').click()
                        time.sleep(2)
                    except Exception as e:
                        print(e)
                        # except:
                        pass
                    time.sleep(3)
                    try:
                        browser.find_element_by_css_selector('.a-button-input').click()
                    except Exception as e:
                        print(e)
                        pass
                    time.sleep(5)
                    # try:
                    #
                    browser.find_element_by_id('placeYourOrder').click()
                    # print('�µ��ɹ���')

                    time.sleep(10)
                    # print('�ɹ����߸������ң�', data_list)
                    browser.quit()
                    return 'success'
                except Exception as e:
                    print(e)
                    # except:a-column a-span8 pmts-cc-detail-row
                    print('�����ˣ�')
                    update_sql = 'update email set error="", status="1" where username ="{}"'.format(email)
                    insert_update_drop_data(connect, update_sql, '�����ʼ�״̬�ɹ���')
                    try:
                        browser.quit()
                    except Exception as e:
                        print(e)
                        # except:
                        pass
                    try:
                        browser_1.quit()
                    except Exception as e:
                        print(e)
                        # except:
                        pass

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
                # capture_text = input('��������֤�룺')
                # img.close()
                # browser.find_element_by_id('auth-captcha-guess').send_keys(capture_text)
                # browser.find_element_by_id('continue').click()
                # print(img_url)
                # img.close()
                print('�ȴ�������֤��...')
                while True:
                    time.sleep(2)
                    try:
                        browser.find_element_by_id('ap_password').send_keys(password)

                        # print(1)
                        try:
                            browser.find_element_by_id('ap_password_check').send_keys(password)
                        except Exception as e:
                            print(e)
                            pass
                        img_url = \
                            browser.find_element_by_id('auth-captcha-image').get_attribute('src').split('?')[0].split(
                                '/')[
                                -1]
                        # print(browser.find_element_by_id('auth-captcha-image').get_attribute('src'))
                        capture_text = ''
                        img = browser.find_element_by_id('auth-captcha-image').get_attribute('src')
                        # print('pppppppp', img)
                        # print(requests.get(img))
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
                            data = requests.get(img, headers=header).content
                        except Exception as e:
                            print(e)
                            # except:
                            try:
                                data = requests.get(img, headers=header).content
                            except Exception as e:
                                print(e)
                                # except:
                                pass
                        # print(data)
                        capture_text = TestFunc(data).pred_rsp.value
                        # response = requests.get(browser.find_element_by_id('auth-captcha-image').get_attribute('src'))
                        # response = response.content

                        # BytesIOObj = BytesIO()
                        # BytesIOObj.write(response)
                        # img = Image.open(BytesIOObj)
                        # img.show()
                        # capture_text = ''
                        # capture_text = input('��������֤�룺')
                        # img.close()
                        browser.find_element_by_id('auth-captcha-guess').send_keys(capture_text)
                        # time.sleep(100000)

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
                        print(img_url)
                    except Exception as e:
                        print(e)
                        # except:
                        break
                print('��֤�봦��ɹ���')
                time.sleep(40)
                # �ֶ�ˢ�½�������
                browser_1.find_element_by_id('rcmbtn107').click()
                # browser_1.find_element_by_id('rcmliSU5CT1g').click()
                browser_1.get('https://mail.teekar.com/mail/?_task=mail&_mbox=INBOX')
                time.sleep(3)
                try:
                    mail_url = browser_1.find_element_by_css_selector('.message .subject .subject a').get_attribute(
                        'href')
                except Exception as e:
                    print(e)
                    # except:
                    try:
                        browser_1.get('https://mail.teekar.com/mail/?_task=mail&_mbox=INBOX')
                        time.sleep(3)
                        mail_url = browser_1.find_element_by_css_selector('.message .subject .subject a').get_attribute(
                            'href')
                    except Exception as e:
                        print(e)
                        # except:
                        update_sql = 'update email set error="" where username ="{}"'.format(email)
                        insert_update_drop_data(connect, update_sql, '�����ʼ�״̬�ɹ���')
                        browser.quit()
                        browser_1.quit()
                        pass
                try:
                    browser_1.get(mail_url)
                    # print('1111111111111111111111111111')
                    # print(2222222222222222222222222222222)
                    time.sleep(3)
                    # print(browser_1.page_source)
                    # try:
                    #     # ���յ�������
                    #     browser_1.find_element_by_id('convertd').click()
                    #     time.sleep(3)
                    # except:
                    #     browser.find_element_by_css_selector('div.a-section.a-spacing-none.a-spacing-top-large.a-text-center.cvf-widget-section-js a').click()
                    #     time.sleep(30)
                    #     # �ֶ�ˢ�½�������
                    #     browser_1.find_element_by_class_name('red').click()
                    #     # ���յ�������
                    #     browser_1.find_element_by_id('convertd').click()
                    #     time.sleep(3)
                    # ��ȡ������֤��
                    code = browser_1.find_element_by_css_selector('p.otp').text.strip()
                    print('�ɹ���ȡ������֤�룺', code)
                    # time.sleep(20)
                    # ��������֤�����룬���ע��
                    browser.find_element_by_class_name('cvf-widget-input-code').send_keys(code)
                    # time.sleep(100)
                    browser.find_element_by_id('a-autoid-0').click()
                    print('����ѷ�˺�ע��ɹ���')
                    browser_1.quit()
                    update_sql = 'update email set error="", status="1" where username ="{}"'.format(email)
                    # print(update_sql)
                    insert_update_drop_data(connect, update_sql, '�����ʼ�״̬�ɹ���')
                    # �򿪸���ҳ��
                    print('�򿪸���ҳ�棡')
                    browser.get(group_url)
                    browser.refresh()
                    # results = browser.find_elements_by_css_selector('#olpOfferList div.a-section.a-padding-small div.a-section.a-spacing-double-large div.a-row.a-spacing-mini.olpOffer')
                    # print('�ɹ��򿪸���ҳ�棡')
                    # for i in results:
                    #     # print(i)
                    #     try:
                    #         shop_name = i.find_element_by_css_selector('div.a-column.a-span2.olpSellerColumn h3 span a').text
                    #     except:
                    #         shop_name = 'other'
                    #
                    #     if shop_name not in shop_name_list:
                    #         print('���ڸ��߸������ң�', shop_name)
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
                    print('�ɹ��򿪸���ҳ�棡')

                    # shop_name_list = ['Zadii']
                    data_list = []
                    data_name_list = []
                    for i in results:

                        # print(i)
                        try:
                            shop_name = i.find_element_by_xpath(
                                './div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a').text
                        except Exception as e:
                            print(e)
                            # except:
                            shop_name = 'other'
                        id_num = i.find_element_by_xpath(
                            './div[@class="a-column a-span2 olpBuyColumn a-span-last"]/div/form/span/span').get_attribute(
                            'id')
                        # print(shop_name)
                        if shop_name not in shop_name_list:
                            data_list.append([shop_name, id_num])
                            data_name_list.append(shop_name)
                    print('���ڸϸ������ң�{}'.format(
                        str(data_name_list).replace('[', '').replace(']', '').replace("'", '').replace(',', ' ')))
                    # print(data_list)
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
                            time.sleep(5)
                    else:

                        link_list = browser.find_elements_by_xpath('//div[@class="a-row sc-action-links"]')
                        # time.sleep(100000)
                        for x, y in zip(link_list, range(len(link_list))):
                            x.find_element_by_xpath('./span[@class="sc-action-quantity"]').click()
                            browser.find_element_by_id('dropdown{}_10'.format(y + 1)).click()
                            x.find_element_by_xpath(
                                './span/span/input[@class="a-input-text a-width-small sc-quantity-textfield sc-hidden"]').send_keys(
                                '999')
                            x.find_element_by_xpath('./span/span/span[@class="a-spacing-top-small"]').click()
                            time.sleep(5)
                            try:
                                quantity_value = browser.find_elements_by_xpath('//span[@class="sc-action-quantity"]')[
                                    y].get_attribute('data-old-value')
                                print('����: ', quantity_value)
                            except Exception as e:
                                print(e)
                            try:
                                alert_text = browser.find_element_by_css_selector(
                                    '.a-alert-content .a-size-base').text.strip()
                                print(alert_text)
                                if 'limit' in alert_text:
                                    print('���޹����޹�����Ϊ��', quantity_value)
                            except Exception as e:
                                print(e)
                    try:
                        browser.find_element_by_id('sc-buy-box-ptc-button').click()
                    except Exception as e:
                        print(e)
                        # except:
                        browser.quit()
                        browser_1.quit()

                    # browser.get('https://www.amazon.com/a/addresses/add?ref=ya_address_book_add_button')
                    # ��д�½���ַ��Ϣ
                    # print('������д��ַ��Ϣ...')
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
                    # print('��ַ��д��ϣ�')
                    if country_code.lower() == 'us':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # browser.find_element_by_id('enterAddressAddressLine2').send_keys()
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PROVINCE)
                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        # browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        # print('��ַ��д��ϣ�')
                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'uk':
                        print('������д��ַ��Ϣ...')
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
                        # print('��ַ��д��ϣ�')
                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'ca':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # if browser.find_element_by_id('enterAddressCity').text == '':
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)

                        select_ele = browser.find_element_by_xpath('//select[@id="enterAddressStateOrRegion"]')
                        # 2.��ʼ��select��
                        s = Select(select_ele)
                        # ѡ��ֵ
                        # 1.�±�
                        # s.select_by_index(2)  # ʹ���±�ѡ��"΢�� Word (.doc)"
                        # time.sleep(3)
                        # 2.valueֵ
                        s.select_by_value(PV)  # ʹ��value��ʽѡ��ֵ"΢�� Powerpoint (.ppt)"

                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)

                        # browser.find_element_by_id('enterAddressAddressLine2').send_keys()

                        # browser.find_element_by_id('enterAddressStateOrRegion').send_keys(COUNTRY)

                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        # browser.find_element_by_css_selector('.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        # print('��ַ��д��ϣ�')
                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'fr':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # if browser.find_element_by_id('enterAddressCity').text == '':
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)

                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)

                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)

                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'de':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # if browser.find_element_by_id('enterAddressCity').text == '':
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)

                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)

                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)

                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'it':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # if browser.find_element_by_id('enterAddressCity').text == '':
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)

                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)

                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)

                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'ae':
                        print('������д��ַ��Ϣ...')
                        # time.sleep(10000)
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # if browser.find_element_by_id('enterAddressCity').text == '':
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
                        time.sleep(2)
                        browser.find_element_by_id('enterAddressCity').send_keys(Keys.ENTER)

                        browser.find_element_by_id('enterAddressDistrictOrCounty').send_keys(PV)
                        time.sleep(2)
                        browser.find_element_by_id('enterAddressDistrictOrCounty').send_keys(Keys.ENTER)

                        # browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        time.sleep(2)
                        # time.sleep(100000)
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

                        time.sleep(2)
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
                            # except:
                            pass
                        print('��ַ��д��ϣ�')
                    elif country_code.lower() == 'es':
                        print('������д��ַ��Ϣ...')
                        browser.find_element_by_id('enterAddressFullName').send_keys(username)
                        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
                        # if browser.find_element_by_id('enterAddressCity').text == '':
                        browser.find_element_by_id('enterAddressCity').send_keys(CITY)

                        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PV)

                        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
                        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)

                        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

                        time.sleep(2)
                        try:
                            browser.find_element_by_xpath('//input[@name="continue"]').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        browser.find_element_by_css_selector(
                            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
                        print('��ַ��д��ϣ�')
                    else:
                        pass

                    time.sleep(5)
                    # time.sleep(10000)
                    # soup = BeautifulSoup(browser.page_source, 'lxml') ('01.50.51.98.15', '4532 1674 5133 6479', '10/2023', '813')
                    # pre_text = soup.select('.a-section.a-spacing-none.pmts-widget-section')[0].get('data-pmts-component-id').split('-')[1]
                    # print(pre_text)

                    # ��д���ÿ���Ϣ
                    # try:
                    #     browser.find_element_by_css_selector('a-link-expander a-declarative')
                    # except:
                    #     pass
                    # print('������д���ÿ���Ϣ...')
                    # browser.find_element_by_id('pp-{}-51'.format(pre_text)).send_keys(username)
                    if country_code.lower() in ['fr', 'es']:
                        try:
                            browser.find_element_by_css_selector(
                                '#wrapper-new-cc div .a-link-expander.a-declarative').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-add-new-card').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        time.sleep(5)

                        try:
                            browser.find_element_by_id('ccName').send_keys(username)
                        except Exception as e:
                            print(e)
                            # except:
                            pass

                    try:
                        browser.find_element_by_xpath('//input[@name="ppw-accountHolderName"]').send_keys(username)
                    except Exception as e:
                        print(e)
                        # except:
                        pass
                    browser.find_element_by_xpath('//input[@name="addCreditCardNumber"]').send_keys(CARD)
                    # browser.find_element_by_xpath('//input[@name="ppw-expirationDate_month"]').click()
                    # browser.find_element_by_id('pp-{}-52'.format(pre_text)).send_keys(CARD)
                    # browser.find_element_by_id('pp-{}-59'.format(pre_text)).click()
                    # time.sleep(300)
                    if country_code.lower() == 'fr':
                        try:
                            browser.find_element_by_css_selector('.card-date .a-button.a-button-dropdown').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass

                    else:
                        try:
                            # browser.find_element_by_css_selector('.pmts-expiry-month').click()
                            browser.find_element_by_css_selector('.a-nostyle.a-list-link').click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-expiry-month').click()
                            # browser.find_element_by_css_selector('.a-nostyle.a-list-link').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                    time.sleep(2)

                    month_list = browser.find_elements_by_xpath('//ul[@id="1_dropdown_combobox"]/li/a')
                    # print(month_list)
                    for x in month_list:
                        # print(x)
                        # print(x.get_attribute('data-value'))
                        if int(x.get_attribute('data-value')) == int(EXPIRES.split('/')[0]):
                            x.click()
                    #
                    # browser.find_element_by_id('pp-{}-60'.format(pre_text)).click()
                    time.sleep(3)
                    if country_code.lower() == 'fr':
                        try:
                            browser.find_elements_by_css_selector('.card-date .a-button-text.a-declarative')[1].click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                    else:
                        try:
                            # browser.find_element_by_css_selector('.pmts-expiry-year').click()
                            browser.find_elements_by_css_selector('.a-nostyle.a-list-link')[1].click()
                        except Exception as e:
                            print(e)
                            pass

                        try:
                            browser.find_element_by_css_selector('.pmts-expiry-year').click()
                            # browser.find_elements_by_css_selector('.a-nostyle.a-list-link')[1].click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                    time.sleep(2)
                    year_list = browser.find_elements_by_xpath('//ul[@id="2_dropdown_combobox"]/li/a')
                    # print(year_list)
                    for y in year_list:
                        # print(y)
                        if int(y.get_attribute('data-value')) == int(EXPIRES.split('/')[1]):
                            y.click()
                    time.sleep(2)
                    # try:
                    #     browser.find_element_by_xpath('//input[@name="addCreditCardVerificationNumber"]').send_keys(CVV)
                    # except:
                    #     pass
                    if country_code.lower() == 'fr':
                        try:
                            browser.find_element_by_id('ccCVVNum').send_keys(CVV)
                        except Exception as e:
                            print(e)
                            # except:
                            pass

                        try:
                            browser.find_element_by_id('ccAddCard').click()
                        except Exception as e:
                            print(e)
                            # except:
                            pass
                        time.sleep(3)
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

                    # browser.find_element_by_id('pp-{}-61'.format(pre_text)).click()
                    # browser.find_element_by_css_selector('.a-button.a-button-primary.pmts-button-input').click()

                    try:
                        browser.find_element_by_xpath(
                            '//span[@class="a-button a-button-primary pmts-button-input"]').click()
                    except Exception as e:
                        print(e)
                        # except:
                        pass
                    try:
                        browser.find_element_by_css_selector('.continue-buttons .a-button.a-button-primary').click()
                    except Exception as e:
                        print(e)
                        # except:
                        pass

                    if country_code.lower() == 'ae':
                        time.sleep(3)
                        try:
                            browser.find_element_by_xpath(
                                '//input[@name="addCreditCardVerificationNumber0"]').send_keys(CVV)
                        except Exception as e:
                            print(e)
                            pass
                        time.sleep(3)
                    print('���ÿ���Ϣ��д��ϣ�')
                    time.sleep(3)
                    # browser.find_element_by_css_selector('.a-button-input').click()

                    try:
                        browser.find_element_by_xpath(
                            '//div[@class="a-column a-span8 pmts-cc-detail-row"]/div/div/div/label/input[@type="radio"]').click()
                        time.sleep(2)
                    except Exception as e:
                        print(e)
                        # except:
                        pass
                    time.sleep(3)
                    try:
                        browser.find_element_by_css_selector('.a-button-input').click()
                    except Exception as e:
                        print(e)
                        pass
                    time.sleep(5)
                    browser.find_element_by_id('placeYourOrder').click()
                    # print('�µ��ɹ���')

                    time.sleep(10)
                    # print('�ɹ����߸������ң�', data_list)
                    browser.quit()
                    return 'success'
                    # browser.quit()
                    # browser_1.quit()
                    # print('IP������')
                    # get_out_amzer()
                except Exception as e:
                    print(e)
                    # except:
                    print('�����ˣ�')
                    update_sql = 'update email set error="", status="1" where username ="{}"'.format(email)
                    insert_update_drop_data(connect, update_sql, '�����ʼ�״̬�ɹ���')
                    try:
                        browser.quit()
                    except Exception as e:
                        print(e)
                        # except:
                        pass
                    try:
                        browser_1.quit()
                    except Exception as e:
                        print(e)
                        # except:
                        pass

        else:
            # print('û�и��������ң�')
            browser.quit()
            # print('����ȴ�������������...')
            # time.sleep(180)
            pass
            return 'no'
    except Exception as e:
        print(e)
        # except:
        print('�����ˣ�')
        try:
            browser.quit()
        except Exception as e:
            print(e)
            # except:
            pass
        try:
            browser_1.quit()
        except Exception as e:
            print(e)
            # except:
            pass
        pass


def read_excel(f_path):
    # print(f_path)
    res = pd.read_excel(f_path)

    data_list = []
    for i in res:
        data_list.append(res[i].to_list())

    new_data_list = []

    for a, b, c in zip(data_list[0], data_list[1], data_list[2]):
        # print(a, b, c)
        new_data_list.append([a, b, c])
    return new_data_list


def main(asin_text, country_code_text, shop_name_text, type_text, file_path_text):
    connect = connect_db(DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT)
    new_file_path = file_path_text.replace(file_path_text.split('\\')[-1], 'Result_' + file_path_text.split('\\')[-1])
    # print(new_file_path)
    if country_code_text.lower() == 'us':
        country_name = '���� com'
    elif country_code_text.lower() == 'uk':
        country_name = 'Ӣ�� uk'
    elif country_code_text.lower() == 'ca':
        country_name = '���ô� ca'
    elif country_code_text.lower() == 'fr':
        country_name = '���� fr'
    elif country_code_text.lower() == 'de':
        country_name = '�¹� de'
    elif country_code_text.lower() == 'it':
        country_name = '����� it'
    elif country_code_text.lower() == 'ae':
        country_name = '�ж� ae'
    elif country_code_text.lower() == 'es':
        country_name = '������ es'
    else:
        pass

    print('')
    print('=================================������Ϣ=================================')
    print('Asin��', asin_text)
    print('վ�㣺', country_name)
    our_shop_name = str(shop_name_text.split('->')).replace('[', '').replace(']', '').replace("'", '').replace(',', ' ')
    print('���ǵĵ�������', our_shop_name)
    print('�ϸ���ģʽ��', type_text)
    result = get_out_amzer(connect, asin_text, country_code_text, shop_name_text, type_text)

    try:
        connect.close()
    except Exception as e:
        print(e)
    if result == 'success':
        print('�µ��ɹ���')
        print('����ȴ�������������...')
        time.sleep(180)
        print('=========================================================================')
    elif result == 'no':
        print('û�и���������')
        rea_results = ''
        try:
            with open(new_file_path.replace('.xlsx', '.csv'), 'r') as rea:
                rea_results = rea.read()
                rea.close()
        except Exception as e:
            print(e)
        if asin_text not in rea_results:
            with open(new_file_path.split('.')[0] + '.csv', 'a', encoding='utf-8-sig')as f:
                f.write(str(asin_text + ',' + country_code_text + ',' + shop_name_text + ',' + type_text + ',�Ѹ��ߣ�').strip() + '\n')
                f.close()
        print('����ȴ�������������...')
        time.sleep(180)
    else:
        print('���ִ��󣡣���')

        # time.sleep(60)
    #
    print('')
    print('')
    # update_sql = 'update email set error="" where id ={}'.format(results[1][0][0])
    # insert_update_drop_data(connect, update_sql, '�ָĻ�����')


if __name__ == '__main__':
    print('=================================��Ϣ����=================================')

    file_path = input('�����������ļ���ַ(���磻C:\Desktop\jack.xlsx)��')
    while True:
        if '"' in file_path:
            print('1')
            file_path = file_path.replace('"', '')
        datas_list = read_excel(file_path)
        for data in datas_list:
            print(data)
            asin = data[0]
            country_code = data[1]
            shop_name = data[2]
            type_te = 'all'

            main(asin, country_code, shop_name, type_te, file_path)

    # asin = input('������Asin��').strip()
    # if asin.isalnum() is True:
    #     pass
    # else:
    #     while True:
    #         asin = input('�����asin���ܰ��������ַ�������������Asin��')
    #         if asin.isalnum() is True:
    #             break
    # # asin = 'B07V4R3J31'
    # # asin = 'B07YL2T543'
    # # asin = 'B079JL2FSY'
    # # country_code = 'uk'
    # # country_code = 'fr'
    # country_list = ['us', 'uk', 'ca', 'fr', 'de', 'it', 'ae', 'es']
    # country_code = input('����������ѷվ��Ĺ����루���磺Ӣ��:uk,����:us,����:fr,���ô�:ca����')
    # if country_code.lower() in country_list:
    #     pass
    # else:
    #     while True:
    #         # print('���Ҵ�������������������룺')
    #         country_code = input('���Ҵ�������������������룺')
    #         if country_code.lower() in country_list:
    #             break
    # # country_code = 'ca'
    # # shop_name = 'Tianyu.HC'
    # shop_name = input('���������ǹ�˾�Լ��ĵ������ƣ���������Ҫ���ߵģ����������ʱʹ�á�->���ֿ�������shop_1->shop_2����')
    # # print(shop_name)
    # shop_name = shop_name.strip()
    # # print(shop_name)
    # type_te = input('������һ�θ���һ�����һ���ȫ������one����all, ������all����')
    # if type_te.lower().strip() in ['one', 'all']:
    #     pass
    # else:
    #     while True:
    #         type_te = input('�������������one��all��')
    #         if type_te.lower().strip() in ['one', 'all']:
    #             break
    # print('=========================================================================')
    # print('')
    # # print('--------------------------------------����ʼ����--------------------------------------')
    # while True:
    #     main(asin, country_code, shop_name, type_te)



