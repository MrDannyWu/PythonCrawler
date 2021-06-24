from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random


def get_out_amzer():
    asin = 'B074JFY4JF'
    # asin = 'B079JL2FSY'
    country_code = 'com'
    shop_name_list = ['Zadii']
    group_url = 'https://www.amazon.{}/gp/offer-listing/{}'.format(country_code, asin)
    STREET = '16701 Beach Blvd.,Huntington Beach,CA'
    CITY = 'Huntington Beach'
    PROVINCE = 'CA'
    POSTCODE = '92647'
    PHONE = '641-660-0191'
    CARD = '4916 5000 0531 8963'
    EXPIRES = '1/2021'
    print(group_url)
    chrome_options = Options()
    # chrome_options.add_argument('blink-settings=imagesEnabled=false')
    # chrome_options.add_argument('--user-data-dir=D:\\ud')
    # # self.chrome_options.add_argument('--proxy-server=' +
    # # proxy.replace('https', 'http'))
    # chrome_options.add_argument('--proxy-server=http://10.11.2.251:3128')
    # chrome_options.add_argument('--proxy-server=http://183.129.244.16:17210')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')
    # chrome_options.add_argument('--headless')
    #
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser_1 = webdriver.Chrome(chrome_options=chrome_options)

    # browser = webdriver.Chrome()
    # 打开Amazon主页，并点击注册
    browser.get(
        'https://www.amazon.com/ap/register?_encoding=UTF8&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26ref_%3Dnav_newcust')
    # browser.get('https://www.amazon.com/')
    # browser.find_element_by_css_selector('#nav-signin-tooltip .nav-signin-tooltip-footer a.nav-a').click()
    # soup = BeautifulSoup(browser.page_source, 'lxml')
    # soup.select('#nav-signin-tooltip ')

    # 产生随机用户名
    cha_list = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f',
                'e', 'd', 'c', 'b', 'a', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    username = ''.join(random.sample(cha_list, 9))
    print('随机生成用户名：', username)
    password = 'gsdyghFrefghsD.'
    print('账户密码为：', password)
    browser.find_element_by_id('ap_customer_name').send_keys(username)
    # 获取邮箱
    print('正在获取邮箱...')
    browser_1.get('http://24mail.chacuo.net/enus')
    browser_1.find_element_by_xpath('//select[@class="f16p"]').click()

    email = browser_1.find_element_by_id('mail_copy').get_attribute('data-clipboard-text')

    print('成功获取邮箱：', email)
    print('开始注册亚马逊账号...')
    # 注册界面输入用户名邮箱密码 开始注册
    browser.find_element_by_id('ap_email').send_keys(email)
    # print(0)
    time.sleep(3)
    browser.find_element_by_id('ap_password').send_keys(password)
    time.sleep(3)
    # print(1)
    browser.find_element_by_id('ap_password_check').send_keys(password)
    time.sleep(3)
    # print(2)
    browser.find_element_by_id('continue').click()
    time.sleep(1)
    # if 'cap'
    browser.find_elements_by_id('auth-captcha-image')
    print(len(browser.find_elements_by_id('auth-captcha-image')))
    if len(browser.find_elements_by_id('auth-captcha-image')) == 0:
        # print(3)
        time.sleep(30)
        # 手动刷新接收邮箱
        browser_1.find_element_by_class_name('red').click()
        # print('1111111111111111111111111111')

        # browser_1.refresh()
        # print(2222222222222222222222222222222)
        time.sleep(3)
        try:
            # 打开收到的邮箱
            browser_1.find_element_by_id('convertd').click()
            time.sleep(3)
        except:
            browser.find_element_by_css_selector(
                'div.a-section.a-spacing-none.a-spacing-top-large.a-text-center.cvf-widget-section-js a').click()
            time.sleep(30)
            # 手动刷新接收邮箱
            browser_1.find_element_by_class_name('red').click()
            # 打开收到的邮箱
            browser_1.find_element_by_id('convertd').click()
            time.sleep(3)
        # 获取邮箱验证码
        code = browser_1.find_element_by_class_name('otp').text.strip()
        print('成功获取邮箱验证码：', code)
        # time.sleep(20)
        # 将邮箱验证码填入，完成注册
        browser.find_element_by_class_name('cvf-widget-input-code').send_keys(code)
        # time.sleep(100)
        browser.find_element_by_id('a-autoid-0').click()
        print('亚马逊账号注册成功！')
        browser_1.quit()

        # 打开跟卖页面
        print('打开跟卖页面！')
        browser.get(group_url)
        results = browser.find_elements_by_css_selector(
            '#olpOfferList div.a-section.a-padding-small div.a-section.a-spacing-double-large div.a-row.a-spacing-mini.olpOffer')
        print('成功打开跟卖页面！')
        for i in results:
            # print(i)
            try:
                shop_name = i.find_element_by_css_selector('div.a-column.a-span2.olpSellerColumn h3 span a').text
            except:
                shop_name = 'other'

            if shop_name not in shop_name_list:
                print('正在赶走跟卖卖家：', shop_name)
                i.find_element_by_css_selector('div.a-button-stack form.a-spacing-none span.a-declarative').click()

                break
        browser.get('https://www.amazon.com/gp/cart/view.html/ref=lh_cart_dup')
        browser.find_element_by_id('a-autoid-0').click()
        browser.find_element_by_id('dropdown1_10').click()
        browser.find_element_by_css_selector('.a-input-text.a-width-small.sc-quantity-textfield.sc-hidden').send_keys(
            '999')
        browser.find_element_by_id('a-autoid-1-announce').click()
        time.sleep(1)
        browser.find_element_by_id('sc-buy-box-ptc-button').click()

        # browser.get('https://www.amazon.com/a/addresses/add?ref=ya_address_book_add_button')
        # 填写新建地址信息
        print('正在填写地址信息...')
        browser.find_element_by_id('enterAddressAddressLine1').send_keys(STREET)
        # browser.find_element_by_id('enterAddressAddressLine2').send_keys()
        browser.find_element_by_id('enterAddressCity').send_keys(CITY)
        browser.find_element_by_id('enterAddressStateOrRegion').send_keys(PROVINCE)
        browser.find_element_by_id('enterAddressPostalCode').send_keys(POSTCODE)
        browser.find_element_by_id('enterAddressPhoneNumber').send_keys(PHONE)
        browser.find_element_by_css_selector('.a-button-text.submit-button-with-name').click()

        browser.find_element_by_css_selector(
            '.sosp-continue-button.a-button.a-button-primary.a-button-span12.a-padding-none.continue-button span input').click()
        print('地址填写完毕！')

        time.sleep(5)
        soup = BeautifulSoup(browser.page_source, 'lxml')
        pre_text = \
        soup.select('.a-section.a-spacing-none.pmts-widget-section')[0].get('data-pmts-component-id').split('-')[1]
        # print(pre_text)

        # 填写信用卡信息
        print('正在填写信用卡信息...')
        browser.find_element_by_id('pp-{}-51'.format(pre_text)).send_keys(username)
        browser.find_element_by_id('pp-{}-52'.format(pre_text)).send_keys(CARD)
        browser.find_element_by_id('pp-{}-57'.format(pre_text)).click()
        time.sleep(2)

        month_list = browser.find_elements_by_xpath('//ul[@id="1_dropdown_combobox"]/li/a')
        # print(month_list)
        for x in month_list:
            # print(x)
            if int(x.get_attribute('data-value')) == int(EXPIRES.split('/')[0]):
                x.click()
        #
        browser.find_element_by_id('pp-{}-58'.format(pre_text)).click()
        time.sleep(2)
        year_list = browser.find_elements_by_xpath('//ul[@id="2_dropdown_combobox"]/li/a')
        for y in year_list:
            # print(y)
            if int(y.get_attribute('data-value')) == int(EXPIRES.split('/')[1]):
                y.click()
        print('信用卡信息填写完毕！')
        browser.find_element_by_id('pp-{}-59'.format(pre_text)).click()
        time.sleep(3)
        browser.find_element_by_css_selector('.a-button-input').click()
        time.sleep(2)
        browser.find_element_by_id('placeYourOrder').click()
        print('下单成功！')

        time.sleep(10)
        print('成功赶走跟卖卖家：', shop_name)
        browser.quit()
    else:
        time.sleep(1000)
        browser.quit()
        browser_1.quit()
        print('IP被封了')
        get_out_amzer()


def main():
    get_out_amzer()


if __name__ == '__main__':
    main()