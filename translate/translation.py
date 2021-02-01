import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
def fanyi(url,input_text):
    try:
        browser = webdriver.PhantomJS()
        browser.get(url)
        #ad_close = browser.find_element_by_class_name('guide-close')
        #ad_close.click()
        input_dialog = browser.find_element_by_id('inputOriginal')
        #input_dialog.click()
        input_dialog.send_keys(input_text)
        submit = browser.find_element_by_id('transMachine')
        submit.click()
        #output_dialog = browser.find_element_by_id('transTarget')
        time.sleep(2)
    except:
        print('请求失败...')
    try:
        web_data = browser.page_source
        #print(web_data)
        soup = BeautifulSoup(web_data,'lxml')
        result = soup.select('#transTarget')[0].text
        return result
    except:
        print('None')
if __name__ == '__main__':
    url = 'http://fanyi.youdao.com/'
    print('          #############################################')
    print('          #      Welcome to DannyWu translation!      #')
    print('          #############################################')
    input_text = input('请输入要翻译的句子：')
    #print(input_text)
    result = fanyi(url,input_text)
    print('\n')
    print('\n')
    print('翻译内容：[',input_text,']')
    print('翻译结果：[',result,']')
