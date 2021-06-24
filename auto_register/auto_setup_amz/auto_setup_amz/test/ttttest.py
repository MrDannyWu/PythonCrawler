# # from selenium import webdriver
# # from selenium.webdriver.chrome.options import Options
# # import time
# # chrome_options = Options()
# #
# # # chrome_options.add_argument('blink-settings=imagesEnabled=False')
# # # chrome_options.add_argument('--user-data-dir=D:\\ud')
# # # # self.chrome_options.add_argument('--proxy-server=' +
# # # # proxy.replace('https', 'http'))
# # # chrome_options.add_argument('--proxy-server=http://10.11.2.251:3128')
# # # chrome_options.add_argument('--proxy-server=http://183.129.244.16:17210')
# # # chrome_options.add_argument('--disable-gpu')
# # # chrome_options.add_argument('--no-sandbox')
# # # chrome_options.add_argument('--disable-dev-shm-usage')
# # # chrome_options.add_argument('--headless')
# # #
# # chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# #
# # browser = webdriver.Chrome(chrome_options=chrome_options)
# #
# # browser.delete_all_cookies()
# #
# #
# # group_url = 'https://www.amazon.com/gp/offer-listing/B07VJRZ62R'
# # browser.get(group_url)
# # browser.refresh()
# # results = browser.find_elements_by_xpath('//div[@class="a-row a-spacing-mini olpOffer"]')
# # print('成功打开跟卖页面！')
# #
# # shop_name_list = ['busylittlebee']
# # shop_list = []
# # for i in results:
# #
# #     print(i)
# #     try:
# #         shop_name = i.find_element_by_xpath('./div[@class="a-column a-span2 olpSellerColumn"]/h3/span/a').text
# #     except:
# #         shop_name = 'other'
# #     id_num = i.find_element_by_xpath('./div[@class="a-column a-span2 olpBuyColumn a-span-last"]/div/form/span/span').get_attribute('id')
# #     print(shop_name)
# #     if shop_name not in shop_name_list:
# #         shop_list.append([shop_name, id_num])
# # print(shop_list)
# # for m in shop_list:
# #     browser.get(group_url)
# #     browser.refresh()
# #     browser.find_element_by_id(m[1]).click()
# #
# # browser.get('https://www.amazon.com/gp/cart/view.html/ref=lh_cart')
# # link_list = browser.find_elements_by_xpath('//div[@class="a-row sc-action-links"]')
# # for x, y in zip(link_list, range(len(link_list))):
# #
# #     x.find_element_by_xpath('./span[@class="sc-action-quantity"]').click()
# #     browser.find_element_by_id('dropdown{}_10'.format(y + 1)).click()
# #     x.find_element_by_xpath('./span/span/input[@class="a-input-text a-width-small sc-quantity-textfield sc-hidden"]').send_keys('999')
# #     x.find_element_by_xpath('./span/span/span[@class="a-spacing-top-small"]').click()
# #     time.sleep(2)
# #     # browser.find_element_by_id(id_num).click()
# #
# #     # if shop_name not in shop_name_list:
# #     #     print('正在赶走跟卖卖家：', shop_name)
# #     #     i.find_element_by_css_selector('div.a-button-stack form.a-spacing-none span.a-declarative').click()
# #     #
# #     #     break
# #
#
#
#
# # import requests
# # web = requests.get('https://opfcaptcha-prod.s3.amazonaws.com/6ffaa6ec3197420f8b0b7faad1af447e.jpg?AWSAccessKeyId=AKIA5WBBRBBBQV5HBEXR&Expires=1574305948&Signature=f8WB0iHQI4Yo6xUFrIc6riMq5dI%3D')
# # print(web)
# # print(web.content)
#
#
# # -*-*-
# # 感谢骚男 『magic (QQ: 2191943283)』 提供的源代码
# # 详细参考：https://www.jianshu.com/p/6b7f31a78f33
# # -*-*-
#
# from selenium import webdriver
# import string
# import zipfile
#
#
# def create_proxy_auth_extension(scheme='http', plugin_path=None):
#     # 代理服务器
#     proxy_host = "http-pro.abuyun.com"
#     proxy_port = "9010"
#
#     # 代理隧道验证信息
#     proxy_username = "H7F3KC58YHUD31VP"
#     proxy_password = "E5A42ED09181D9B5"
#
#     if plugin_path is None:
#         plugin_path = r'D:/{}_{}@http-pro.abuyun.com_9010.zip'.format(proxy_username, proxy_password)
#
#     manifest_json = """
#     {
#         "version": "1.0.0",
#         "manifest_version": 2,
#         "name": "Abuyun Proxy",
#         "permissions": [
#             "proxy",
#             "tabs",
#             "unlimitedStorage",
#             "storage",
#             "<all_urls>",
#             "webRequest",
#             "webRequestBlocking"
#         ],
#         "background": {
#             "scripts": ["background.js"]
#         },
#         "minimum_chrome_version":"22.0.0"
#     }
#     """
#
#     background_js = string.Template(
#         """
#         var config = {
#             mode: "fixed_servers",
#             rules: {
#                 singleProxy: {
#                     scheme: "${scheme}",
#                     host: "${host}",
#                     port: parseInt(${port})
#                 },
#                 bypassList: ["foobar.com"]
#             }
#           };
#
#         chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
#
#         function callbackFn(details) {
#             return {
#                 authCredentials: {
#                     username: "${username}",
#                     password: "${password}"
#                 }
#             };
#         }
#
#         chrome.webRequest.onAuthRequired.addListener(
#             callbackFn,
#             {urls: ["<all_urls>"]},
#             ['blocking']
#         );
#         """
#     ).substitute(
#         host=proxy_host,
#         port=proxy_port,
#         username=proxy_username,
#         password=proxy_password,
#         scheme=scheme,
#     )
#
#     with zipfile.ZipFile(plugin_path, 'w') as zp:
#         zp.writestr("manifest.json", manifest_json)
#         zp.writestr("background.js", background_js)
#
#     return plugin_path
#
#
# proxy_auth_plugin_path = create_proxy_auth_extension()
#
# option = webdriver.ChromeOptions()
#
# # option.add_argument("--start-maximized")
# option.add_extension(proxy_auth_plugin_path)
#
# driver = webdriver.Chrome(chrome_options=option)
# driver.get('https://www.amazon.com')
# driver.refresh()


# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# options = Options()                                         # 网上找到 你可以试试
# options.binary_location = "D:/Chrome/Application/chrome.exe"   # 这里是你指定浏览器的路径
# driver = webdriver.Chrome(chrome_options=options)
# driver.get('http://www.baidu.com')



# import requests
# from multiprocessing import Pool
#
#
# def get_html(url):
#     resp = requests.get(url)
#     print(resp)
#
#
# if __name__ == '__main__':
#     # 进程数
#     pool = Pool(10)
#     url_list = []
#     # 第一个参数为函数名字，参数要为一个
#     # 第二个参数要为一个列表
#     pool.map(get_html, url_list)



from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.amazon.ae/gp/buy/addressselect/handlers/display.html?hasWorkingJavascript=1')

cookie_list = [
{
    "domain": ".amazon.ae",
    "expirationDate": 2206248396.659209,
    "hostOnly": False,
    "httpOnly": True,
    "name": "at-acbae",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "Atza|IwEBIFMF6BM6q7dTqHeWCxl2_lc0cEBQZGe6dgAruc65-DsfLBvLLnHvfOk5eW4hP7o_ZX69Q-xXhfPyxR41b9fz42nJpTyrhfWG6F3KQA6qlmEHyuoIuWDgglh3iQkoV5ZZnfm_9svi6S0kg0Cj5yCSZLxeMkFyRP56-vxAQgR7RbOkm3TNX0qeeP6EdxjqC9tXg0X8r5dg0mGMXE9-UwDJDJMN34HNwROyMoOXNCFr6akF0iu2ICmTRb-gdeQ-Dcy-fJkE1WsQ-OPQpgdksbP4WTFcZgqCvOvLzS5n7trwf2RfSvdiEw09is9o3FMIQeZOF3kR4S1waHi8qC82KepGUqmu4m2pwvR0Tcocd-JtIlYaLUq3BGCe4-IwcDOSjgRXvfsWmKNRHp_xRlgYF-stW5tu",
    "id": 1
},
{
    "domain": ".amazon.ae",
    "expirationDate": 2082787200.86417,
    "hostOnly": False,
    "httpOnly": False,
    "name": "lc-acbae",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "en_AE",
    "id": 2
},
{
    "domain": ".amazon.ae",
    "expirationDate": 2206248396.659226,
    "hostOnly": False,
    "httpOnly": True,
    "name": "sess-at-acbae",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "\"F3Fkj6lN2McqFOJ6LMBaWMLUcITxz5bb45kibTFbccY=\"",
    "id": 3
},
{
    "domain": ".amazon.ae",
    "expirationDate": 2082758395.920731,
    "hostOnly": False,
    "httpOnly": False,
    "name": "session-id",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "260-9077892-9753960",
    "id": 4
},
{
    "domain": ".amazon.ae",
    "expirationDate": 2082758395.92069,
    "hostOnly": False,
    "httpOnly": False,
    "name": "session-id-time",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "2082758401l",
    "id": 5
},
{
    "domain": ".amazon.ae",
    "expirationDate": 2206252614.385151,
    "hostOnly": False,
    "httpOnly": False,
    "name": "session-token",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "8/4hUXpd8B5S/DDNNuNsO1/7sgINHCmI7DCtC1Gh7kKWGNge1kK8Br49jpfXQjuiVHSVOBqsyrbQwnp8ux1Y5b/xnWJmb3VhBU6Scx7D+1jiLZGkqNeEusviNr7Zx5BmXqP0Up4AYxEGAsl+l/6s5xZ0A3pF9mYvwKIE+Gj4w8csNii7O6R2HOMvo01xwWj2EFH0u43C1L303Xf+JbwowXMqvvIOK3tQ6IATejwPJ5zBOWXTu6AX8+l2xYrfLDqV2TXZhFsytoA=",
    "id": 6
},
{
    "domain": ".amazon.ae",
    "expirationDate": 2206248396.659238,
    "hostOnly": False,
    "httpOnly": True,
    "name": "sst-acbae",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "Sst1|PQG2HWrGpFv9VVzppdm4F9fIC5jnSXSQ-3Qh-x5LW93yGKRpsFMH4JVn4BlN9gs4ti0FdYcnJ7Q-qzKFWYmIuaJFm2MR4_g3As2Kt4uqdgHw880O_O-P_mslaCyf6xJoEtDTrLRTI4wdHSy7GMr89STmK-gZ0T-5WZVE_o7rr4-py3A8wBvw1Xu47o8AOr1kowc2EGggsW7Wo3hQ37pHZpJn-RTnfvIbgYluD5cFsmj5LQn2FuLSdpCJDzA89bXk_wC15nWaF3XXIuZOOPYogwJRKwWtn-aqprr0Tv4lwsYyBfjFL8e2_LCIjLA1cIttctSS0beGQ5ENo7gOeK3IFts46Q",
    "id": 7
},
{
    "domain": ".amazon.ae",
    "expirationDate": 2082758395.920747,
    "hostOnly": False,
    "httpOnly": False,
    "name": "ubid-acbae",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "257-3793703-8335648",
    "id": 8
},
{
    "domain": ".amazon.ae",
    "expirationDate": 2206248396.659198,
    "hostOnly": False,
    "httpOnly": False,
    "name": "x-acbae",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "\"DuMDO455wacpF27AELorbSpylO@kH?e04PrOKy61ZJgVPT@fU061AiwH@AAZO2VW\"",
    "id": 9
},
{
    "domain": ".amazon.ae",
    "expirationDate": 2082758395.134153,
    "hostOnly": False,
    "httpOnly": False,
    "name": "x-wl-uid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1pESNuMp0IEpdl7bwJEZc+3qDWc4OKdCYU9KD26G8qnSigPNvSlHuvk2B7T1usw/Vary7R+MMQKUIv2GtQr3KZDKIdbff4yBJE7PP/TaH1/WkQf44lDE7CPob76l6WaoENEVV3T1BHmXooOsYnxiyNg==",
    "id": 10
},
{
    "domain": "www.amazon.ae",
    "expirationDate": 1636012626,
    "hostOnly": True,
    "httpOnly": False,
    "name": "csm-hit",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "tb:s-ZHVJ4RQKKSNGVPW130ZB|1575532625896&t:1575532626216&adb:adblk_no",
    "id": 11
}
]

for i in cookie_list:
    browser.add_cookie(i)

browser.get('https://www.amazon.ae/gp/buy/addressselect/handlers/display.html?hasWorkingJavascript=1')
