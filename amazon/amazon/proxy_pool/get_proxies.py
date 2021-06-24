import requests
import json
from lxml import etree


def get_html(url, header):
    try:
        resp = requests.get(url, headers=header)
        # print(resp.text)
        return resp.text
    except:
        try:
            resp = requests.get(url, headers=header)
            # print(resp.text)
            return resp.text
        except:
            print('Connection Error...')
            pass


def parse(web_data):
    json_data = json.loads(web_data, encoding='utf-8')
    for item in json_data:
        proxy = {'http': 'http://' + item['proxy']}
        value = test_proxy(proxy)
        if value == 1:
            print("'" + 'http://' + item['proxy'] + "',")


def test_proxy(proxy):
    header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'cache-control': 'max-age=0',
        'cookie': 'session-id=147-6265937-3499123; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=130-7397069-1989509; x-wl-uid=1sdxloWXlGOagPWAypZFkwKly88j+N1GATonP1x4CwRInPn8uSqj/BhfPdxOd66kkq5TXknfFTvc=; s_vn=1596528480075%26vn%3D1; regStatus=pre-register; s_pers=%20s_fid%3D4DEF01D5C3C75630-0ACCC3C002E5B82B%7C1722933512990%3B%20s_dl%3D1%7C1565082512992%3B%20gpv_page%3DUS%253AAZ%253ASOA-overview-sell%7C1565082512997%3B%20s_ev15%3D%255B%255B%2527AZUSSOA-sell%2527%252C%25271565080713001%2527%255D%255D%7C1722933513001%3B; s_nr=1565574950332-Repeat; s_vnum=1997574950333%26vn%3D1; s_dslv=1565574950335; lc-main=en_US; sp-cdn="L5Z9:CN"; x-amz-captcha-1=1566544835835156; x-amz-captcha-2=/Tg8bm4YvdMzrXGBBlTa5A==; session-token=Yod6w2BJQB7JZqZ2f120XtsSR3n1Mb5hdLbFKKbtJv+nbDxKELOlDFP5i48oGUZkZD7or7q/boxhaV+UUNplwegz8x/cOWvTuLFjUHCsYCumX+fjMvgFBnnBx4VmMWRoNu0N1tzLHAywX5oBxKKRI4fLKorCIfsegtTvbMluaXY4Wiqg3u6QFEBAUXtmdSnr; csm-hit=tb:8FWXJQYV3TJA996RVEME+s-8FWXJQYV3TJA996RVEME|1566879612098&t:1566879612098&adb:adblk_no',
        'referer': 'https://www.amazon.com',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    url = 'https://www.amazon.com/Disney-Aurora-Toilette-Spray-Ounce/dp/B003C0WQRU/'
    value = 0
    try:
        resp = requests.get(url, headers=header, proxies=proxy)
        web_data = resp.text
        response = etree.HTML(web_data)
        if len(response.xpath('//div[@id="detail-bullets"]')) > 0:
            value = 1
    except:
        try:
            resp = requests.get(url, headers=header, proxies=proxy)
            web_data = resp.text
            response = etree.HTML(web_data)
            if len(response.xpath('//div[@id="detail-bullets"]')) > 0:
                value = 1
        except:
            try:
                resp = requests.get(url, headers=header, proxies=proxy)
                web_data = resp.text
                response = etree.HTML(web_data)
                if len(response.xpath('//div[@id="detail-bullets"]')) > 0:
                    value = 1
            except:
                pass
    return value


def main():
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': '118.24.52.95',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

    url = 'http://118.24.52.95/get_all/'
    web_data = get_html(url, header)
    parse(web_data)


if __name__ == '__main__':
    main()