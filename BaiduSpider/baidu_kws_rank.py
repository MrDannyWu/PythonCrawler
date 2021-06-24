import requests
from bs4 import BeautifulSoup
# from lxml import etree


def get_html(url, header):
    try:
        resp = requests.get(url, headers=header)
        resp.encoding = 'utf-8'
        return resp.text, resp.url
    except:
        try:
            resp = requests.get(url, headers=header)
            resp.encoding = 'utf-8'
            return resp.text, resp.url
        except:
            print('Connection Error!')
            return '', ''


def parse(kw, response):
    # html = etree.HTML(response)
    soup = BeautifulSoup(response, 'lxml')
    items = soup.select('#content_left .c-container h3 a')
    for item in items:
        title = item.text
        baidu_url = item.get('href')
        print(title, baidu_url)
        # resp = requests.get()
        response = get_html(baidu_url, '')
        # resp = requests.get(baidu_url)
        # article_url = resp.url
        print(kw, title, baidu_url, response[1])
        with open('baidu_search_results.csv', 'a')as f:
            f.write(kw.replace(',' ,'') + ',' + title.strip().replace(',' ,'') + ',' + baidu_url.strip() + ',' + response[1].strip() + '\n')


def main():
    # page为0 10 20
    with open('baidu_search_results.csv', 'w', encoding='utf-8')as f:
        f.write('kw,title,baidu_url,article_url' + '\n')
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'BAIDUID=EE7458AACB63D267A8F7ADCF3E2A5649:FG=1; BIDUPSID=EE7458AACB63D267A8F7ADCF3E2A5649; PSTM=1559977330; BD_UPN=12314753; BDUSS=kl1WE9uUnFqR3JqcUdEckNvRUwxdlZhTWtlYnBmQWUxaC1DWHd3SVZFREJreTFkSVFBQUFBJCQAAAAAAAAAAAEAAAB-vqpjztLP687Ssru5u7rDYW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMEGBl3BBgZdT; MCITY=-2912%3A; cflag=13%3A3; BD_HOME=1; H_PS_PSSID=1438_21091_29522_29519_29098_29568_29221_29639; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; BD_CK_SAM=1; PSINO=6; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; sug=3; sugstore=0; ORIGIN=0; bdime=0; H_PS_645EC=cc4bEaBSNexg2WboXuxArRXq20yMgTEWOUwIK8Ata5ZGgnryXVS8539Srew; BDSVRTM=132; COOKIE_SESSION=185_0_8_7_4_11_0_1_7_4_6_3_0_0_0_0_1565701497_0_1566395589%7C9%231435211_117_1565496413%7C9',
        'Host': 'www.baidu.com',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    base_url = 'https://www.baidu.com/s?wd={}&pn={}'
    with open('kws.txt', 'r', encoding='utf-8')as rea:
        results = rea.readlines()
        rea.close()
    for kw in results:
        for i in range(3):
            url = base_url.format(kw.strip(), i*10)
            print(url)
            response = get_html(url, header)
            # print(response)
            parse(kw.strip(), response[0])


if __name__ == '__main__':
    main()
