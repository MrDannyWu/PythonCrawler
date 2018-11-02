import selenium
from selenium import webdriver
import time

url = 'http://www.sunac.com.cn/news.aspx?tags=1'
browser = webdriver.Chrome()
browser.get(url)
#source = browser.page_source

for i in range(30):
    try:
        more = browser.find_element_by_id('more').click()
        time.sleep(2)
    except:
        pass
links = browser.find_elements_by_tag_name('a')
links = browser.find_elements_by_xpath('/html/body/form/div[3]/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/ul/div/li/a')
for link in links:
    url = link.get_attribute('href')
    #if 'tags=1&Newsid' in str(url):
    print(link.text)
    print(url)
    print('')
