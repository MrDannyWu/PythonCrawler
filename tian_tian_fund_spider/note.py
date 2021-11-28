history_jing_zhi_url = 'http://api.fund.eastmoney.com/f10/lsjz?callback=jQuery18308971964548176494_1637509009788&fundCode=160218&pageIndex=1&pageSize=20&startDate=&endDate=&_=1637509063970'
request_type = 'get'
header = {
    'Connection': 'keep-alive',
    'Cookie': 'qgqp_b_id=6b65ace5a17527f9335bd2606a5a9646; _qddaz=QD.e7jevh.mjk435.kqns8wd5; AUTH_FUND.EASTMONEY.COM_GSJZ=AUTH*TTJJ*TOKEN; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; st_si=96549850135914; st_asi=delete; EMFUND0=null; EMFUND5=11-21%2023%3A22%3A30@%23%24%u62DB%u5546%u6CAA%u6DF1300%u5730%u4EA7%u7B49%u6743%u91CD%u6307%u6570A@%23%24161721; EMFUND6=11-20%2023%3A22%3A49@%23%24%u534E%u590F%u6210%u957F%u6DF7%u5408@%23%24000001; EMFUND7=11-20%2023%3A31%3A57@%23%24%u65B9%u6B63%u5BCC%u90A6%u8D8B%u52BF%u9886%u822A%u6DF7%u5408C@%23%24012914; EMFUND9=11-21%2023%3A23%3A29@%23%24%u56FD%u6CF0%u56FD%u8BC1%u623F%u5730%u4EA7%u884C%u4E1A%u6307%u6570@%23%24160218; EMFUND8=11-21 23:32:32@#$%u4E07%u5BB6%u65B0%u5229%u7075%u6D3B%u914D%u7F6E%u6DF7%u5408@%23%24519191; st_pvi=40773206748191; st_sp=2021-07-03%2018%3A02%3A17; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=112; st_psi=20211121233649781-112200305283-0118586823',
    'DNT': '1',
    'Host': 'api.fund.eastmoney.com',
    'Referer': 'http://fundf10.eastmoney.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

import requests

resp = requests.get(history_jing_zhi_url, headers=header)
print(resp)
print(resp.text)

# 查看历史净值页面
h_url = 'http://fundf10.eastmoney.com/jjjz_160218.html'