# -*- coding: utf-8 -*-
import scrapy
from amazon.db import DB_HOST, DB_USER, DB_PASS, DATABASE, DB_PORT
import pymysql
import json
import datetime
from amazon.items import GetProductDetailsItem
# import os
# import requests
# from bs4 import BeautifulSoup
# from amazon.AmazonCaptcha.py.AmazonCaptcha import process


class GetProductDetailsSpider(scrapy.Spider):
    handle_httpstatus_list = [404, 500]
    name = 'get_product_details_four_1'
    allowed_domains = ['amazon.com']
    start_urls = ['']
    custom_settings = {
        'ITEM_PIPELINES': {'amazon.pipelines.GetProductDetailsPipelineTwo': 300},
        'DOWNLOADER_MIDDLEWARES': {'amazon.middlewares.AbuyunProxy': 300}
    }
    # PATH = 'D:/Workspace/python.system.com/Amz/amazon/amazon/AmazonCaptcha'
    # base_url = 'https://www.amazon.com/errors/validateCaptcha?amzn={}&amzn-r={}&field-keywords={}'
    # header = {
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    #     'accept-encoding': 'gzip, deflate, br',
    #     'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh-TW;q=0.7,zh;q=0.6',
    #     'cookie': 'session-id-time=2082787201l; i18n-prefs=USD; sp-cdn="L5Z9:CN"; session-id=136-5144459-7065013; ubid-main=132-5228167-2046518; x-wl-uid=10TwTcH7Zh+tDFXt9ni3fw+lwlyTng4Joqp9edQ/eC7OW0qOOzLc/SIw5AZkJY5Y7FSyMx6ld4wU=; session-token=u5y4XKIZyDmY3eIS5WzWddoxt6jRxQocm6suKeP6vf3LC+W9kIzgNW06kOZteZOT0i27DG8JTf6Yn+6oqVskMkn9GH2LMfdWrQnpI9wClz6zv3sH7g7yJeqh0liA+aTW06vrEaTjHnuwmmnO7EolV6h5pXqn+eeZS61YJPSaDgY6Mg5m3uYY50Zqve9cdbOb; x-amz-captcha-1=1571102337024506; x-amz-captcha-2=aaUuD+/t7jv2+Eyd2OtvfQ==; csm-hit=tb:SZ088R9F9ZEX58W0N8WA+s-P4RYFN7M00W34JNH1WPP|1571102721204&t:1571102721204&adb:adblk_no',
    #     'referer': 'https://www.amazon.com',
    #     'sec-fetch-mode': 'navigate',
    #     'sec-fetch-site': 'same-origin',
    #     'sec-fetch-user': '?1',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    # }

    def query_product(self):
        """
        查询数据库所有error为yes的产品
        :return: 返回查询结果
        """
        connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASS, db=DATABASE, port=DB_PORT)
        cursor = connect.cursor()
        # query_all_sql = 'select * from product where class_id = 6768 and asin = "B004O290TW"'
        query_all_sql = 'select * from amz_product where error = "yes"'
        # query_all_sql = 'select * from amz_product where id = "52051"'
        # query_all_sql = "select * from amz_product where asin in ('B000C1Z3LS', 'B07GDL95WL', 'B00T2VV6O2', 'B00C9358NU', 'B00A6FAXOM', 'B000C1ZB3I', 'B004YRCPCQ', 'B07PF697CX', 'B01D3P59KO', 'B00DSCXUNQ', 'B002JWEP1W', 'B01DOFOKFS', 'B0014XELHK', 'B00BWQ1D48', 'B00CK0B26E', 'B004D1Z4XA', 'B076ZY87ZK', 'B000VOLLW6', 'B001LBH1T0', 'B0092PVSP0', 'B00I21MLEC', 'B01D8A7254', 'B005IQ4368', 'B00BOJFQYQ', 'B00K5F816K', 'B07SS5WCM8', 'B002HWS7RM', 'B07C5PRBPZ', 'B00066N8Z2', 'B00KFR73NU', 'B00MY6EI1K', 'B00K34IYCY', 'B00EJD6WQ0', 'B001H64OTE', 'B07NSJZMHS', 'B079NC27GK', 'B00KI0X0I6', 'B07D6GM758', 'B00H9T5Z7S', 'B004Y6AFB0', 'B07QWBL3FK', 'B01N7PMIIC', 'B01CRNF6FG', 'B01DJYNPOG', 'B071CYZ92V', 'B00BBD508C', 'B00NHAYK0Q', 'B07P8ZL6GG', 'B00HMSU4ZE', 'B00H6SQY3Q', 'B003WR5I96', 'B00EYIAR52', 'B005VRA66K', 'B07RL6LPLL', 'B01BM67TO0', 'B071P3D7SH', 'B00FU78S8E', 'B0719S2Y9L', 'B01FQBX6KI', 'B00IJMAFI8', 'B0080IIGB4', 'B079P3RGS6', 'B01BNTP2BS', 'B078QV8BV8', 'B07NP95V3W', 'B0093ZQ1WE', 'B07QSY7XK6', 'B01E8LS404', 'B0755RG3HC', 'B0118QC1BA', 'B010647EJO', 'B000ZJW6TY', 'B07RQC9Y9Z', 'B07T2QXP4C', 'B0006ZYPVE', 'B01MR4Y0CZ', 'B078LFGC48', 'B0776L662W', 'B072FFZ61K', 'B01ANA4T7G', 'B002Z7FSVM', 'B07N78DK15', 'B01DZQPW44', 'B07DWW41FH', 'B001BAG38G', 'B00ZY65RUI', 'B001S46QIM', 'B018CLNEOM', 'B07F1LDVX1', 'B01HUUT08U', 'B017D5N9W0', 'B011QHFB4A', 'B07H2Z8LVY', 'B00EP3N4IS', 'B00CF2DHWE', 'B010BUYGU8', 'B0105ZMQ24', 'B00J2ZLSBY', 'B001G9068U', 'B01LTIAU7Y', 'B0000532A2', 'B07SL4WKDZ', 'B000C1Z7P0', 'B0037XA22S', 'B00BCPL7B8', 'B06XHH38FB', 'B000142OD6', 'B00EFR0JQY', 'B00XTTFI6K', 'B07DP5JQH2', 'B016V5H6MM', 'B075CMZ294', 'B000EMDK38', 'B07178P973', 'B00CQ7LGJY', 'B019FZ6SY2', 'B000KEIPC6', 'B00GSODYSW', 'B000FCR7MM', 'B00G4UBQDK', 'B07NNNYDRP', 'B01LTIAUHE', 'B002ABQJIE', 'B07KJ2LDCN', 'B07PDVZG7M', 'B01ADREVQS', 'B0046ZFLD6', 'B07DN5WFG3', 'B076Q9JV91', 'B07D247PFM', 'B00CHVX10Q', 'B000OFD8AK', 'B0033RA5CU', 'B06W56KP5R', 'B01APTZDJS', 'B005I4WBDM', 'B00V3RRPF2', 'B06XXPLT2T', 'B00J9UR64U', 'B000XTG912', 'B00OR1NSTS', 'B000SIOVVS', 'B002CMLS0A', 'B00Q23KER8', 'B01CLQSHVO', 'B07765ZBQT', 'B00IMHN0B4', 'B00O0OEEJU', 'B0058E3XJI', 'B002CMLS50', 'B000WI02HG', 'B01N17EUBE', 'B0009OMNQQ', 'B00OJSQITG', 'B00FMRVWB2', 'B06WLH86FF', 'B00JF2J4GK', 'B00BNAQK4Q', 'B018YN7HDW', 'B0751L3KP9', 'B0014568CO', 'B000GG16QA', 'B07BMG16C8', 'B075WVB9YV', 'B01NBH66QV', 'B004TMOVFU', 'B075MV4F58', 'B004DBC15E', 'B07H38WX77', 'B00639DKCC', 'B075TVVCT9', 'B0788WS84D', 'B07SNB8SVT', 'B0777R27B7', 'B00JH1CTBG', 'B016E1HM0O', 'B01FBTOPC8', 'B0028Q4OQ0', 'B01MZ0PHYE', 'B00EX6BVO6', 'B00F9H0IKQ', 'B01HCU4P3S', 'B001E722V8', 'B07NJGJ8CV', 'B001ET776Q', 'B00OJ7U96A', 'B01N5HGZ1J', 'B00639DXSI', 'B003I5XHHM', 'B005WLZVBU', 'B071ZTLF1N', 'B00GYRAQAM', 'B009Z4KEOY', 'B0001YNVW4', 'B07JJVQ64R', 'B0069US0DO', 'B075L86GX4', 'B0089SFJJM', 'B007EHSBZ8', 'B071X3XQSN', 'B000XEATY0', 'B07DJCBGB6', 'B07HHHZ8FT', 'B008NA4MGW', 'B01FHC57NK', 'B07BY8NKM2', 'B079LGZ6W6', 'B07S2RD6YT', 'B07BKC85BK', 'B005BEF5EQ', 'B004ECHLUM', 'B000C1ZDTU', 'B000VOJHBS', 'B004ZLZR8A', 'B079XZDYHL', 'B0089SFJLU', 'B01DWG10MA', 'B003E0VMWI', 'B00MKCMDMY', 'B07N1L3NFC', 'B00LI2ETQK', 'B015GJJXZC', 'B06ZZLN6DP', 'B07MPWR2H7', 'B072KV2WP8', 'B00PE25S7Y', 'B0107NL9FE', 'B000R41QDY', 'B01CJO59OG', 'B000056Q09', 'B008VDLC4Q', 'B079LH8JFF', 'B0009OAGNS', 'B01L7LW3EG', 'B01N6NTZLK', 'B000GIL1UE', 'B00LPCI7K2', 'B00I0YYVUI', 'B000ZZQMCK', 'B07NWB1FZL', 'B07S39BPBR', 'B07K8CNBTK', 'B00KZ26G1U', 'B000XE8T4C', 'B07DNMZ7XN', 'B000XE7PV0', 'B077J8H9YL', 'B07215Q4VX', 'B07MKKKZKK', 'B00N9YKN4W', 'B00CK0B296', 'B00BOXSEBE', 'B004J1MNII', 'B002ZNJYSY', 'B005RJ11VG', 'B002RS6L10', 'B07FYGLGFY', 'B000C1VWRC', 'B01EJLBOZA', 'B071VVHNXQ', 'B07J184PHV', 'B00E4MI9XK', 'B07MVJZQTC', 'B0010ZYM26', 'B000P20U80', 'B07D256LK1', 'B01MTCI8UM', 'B00OPJYOAY', 'B06W2KWZ37', 'B01GIN2RYO', 'B00ER4SYYY', 'B07PCMP1J1', 'B074NX4RFD', 'B07BFX1PQC', 'B07RZKQDFL', 'B07NP23TT7', 'B00NFUM3PC', 'B00K6LAAKI', 'B0001ZWP6Q', 'B001N7SW9K', 'B000O7NLBE', 'B00QSL9ZUQ', 'B07DPBR94M', 'B01HVKDTKE', 'B00N8SASWQ', 'B07DCL7NC8', 'B01C0PY0N0', 'B00UDS5KAE', 'B000C21AC8', 'B00B9PRTMM', 'B076QHPRJK', 'B07FZTJ1YN', 'B0050N4DLE', 'B07NKCX2Q1', 'B01BLOTGBW', 'B005F5J60A', 'B000EMWFD4', 'B077SHM7S3', 'B01LX0QDKY', 'B07SBNRHNT', 'B07763R3PF', 'B07KH7SLYN', 'B00RZUO1W6', 'B01D7KPWZC', 'B078PXCG4X', 'B008NA8M8Q', 'B06W9NWK2N', 'B00HZSJZ9M', 'B01IE3GKSA', 'B07F2BBDDF', 'B073B13L4T', 'B00WI1LQBG', 'B07DQGW16W', 'B002RS6JSA', 'B0014XECEW', 'B017JEUL3A', 'B00JC30MW2', 'B00NHXLCVS', 'B07V8QF352', 'B073WC9SYT', 'B07NS6ZTQ4', 'B07JJ1RVL8', 'B071YV59TK', 'B0012RXS18', 'B0006V7Y8Y', 'B00B4IBBNC', 'B000MJZOPK', 'B00NAIM3H2', 'B007W1SLY2', 'B07V6VM8SQ', 'B0001LHCYK', 'B075JKKNV5', 'B07RN44GS6', 'B07NNPQ3KG', 'B000P20RAQ', 'B07C533XCW', 'B000E7YLF4', 'B00SQX9QQW', 'B0075HPJEI', 'B00FDV0NBW', 'B072HY4MYP', 'B000EH4TMY', 'B07Q5Z44SJ', 'B07Q42HFCB', 'B0765BH495', 'B0784LT314', 'B001PTFWSA', 'B000C1VWIQ', 'B00B4Y4N9K', 'B00AYNNX34', 'B01JM6NQVM', 'B005P0WGG6', 'B001R2IGEC', 'B00076XSHY', 'B07P64N1XF', 'B000C1VVGE', 'B000219ZSU', 'B0039W0UOM', 'B00021760Y', 'B06XGTBJTN', 'B0107NLMEM', 'B003YQ1UGA', 'B00JJ3A2S4', 'B01BH36VDS', 'B003V5KWWM', 'B07BSHR4KQ', 'B078SS5R36', 'B07KWB5SQC', 'B00MU5L9LC', 'B075F9ZLNP', 'B00SRGXY0W', 'B07HXLJMHB', 'B0017DI8QM', 'B07MCB84LT', 'B06XZDGTL1', 'B000RUD6EK', 'B01H3KNWLI', 'B00LPPDW6S', 'B0046MK6LG', 'B0016CTAZC', 'B01FK2S73Y', 'B00LE1K9FU', 'B07N7RLM7V', 'B0010XYUBQ', 'B001NRB5BM', 'B000C213M0', 'B013TKSUJK', 'B0084MP9WU', 'B01JC4XW8G', 'B01ELUGLUW', 'B078JLD3S1', 'B07DWNN5F5', 'B07NPCYWT4', 'B00720W9F0', 'B06XQKBFL2', 'B007B3T47Y', 'B0039VOSPU', 'B000V2EXL4', 'B01MRCI9BY', 'B07CV3XBDY', 'B007LV33ZU', 'B0716W58HL', 'B00MGHVUHM', 'B076SCLCXD', 'B07CJ7Q8B1', 'B074Q9BH7T', 'B002ZX56D6', 'B00C7ONQR6', 'B00I8ODO26', 'B00MR85RAQ', 'B01EBTBC6G', 'B01MQU4Q5J', 'B01ANA4T8K', 'B005DPBVGE', 'B07CZDNPPY', 'B002Q4UC06', 'B0010OKF7S', 'B000RGGOCU', 'B00H8GRIN6', 'B000IWY1XC', 'B0009OAI6I', 'B0083UCIRW', 'B000OF8C7E', 'B00E1GJLQ8', 'B071G5ZJ6C', 'B01KM4HELG', 'B01NAS712I', 'B078KDG5K9', 'B00MZB6YFC', 'B000P22UUG', 'B073VM4LC7', 'B07S5JQDZG', 'B07CYYWRKQ', 'B01MFC0T0A', 'B002FZAVOS', 'B07T7864KV', 'B07JQQTFWD', 'B071KG5HPB', 'B00P7DGNIS', 'B000C230QM', 'B07H3B2YG1', 'B00CC5X05S', 'B07RP1P6HQ', 'B00992L8E2', 'B004TZITTQ', 'B0006PLP8U', 'B000141N56', 'B00O3SGR6G', 'B07RXT1TB2', 'B00BOJV0KK', 'B0001Z66UM', 'B01H0IZ7ZC', 'B00MABHCXK', 'B004RDJ8BI', 'B071GPZN9H', 'B01N0YEAYW', 'B07GV5Z79D', 'B07MT53CZH', 'B07CJK81NG', 'B0759CXLFQ', 'B07KVCFL41', 'B00I2YI0QW', 'B07SLHH6X5', 'B07KSMH4KX', 'B004DHYZU2', 'B07M8SYTZV', 'B01C502P5U', 'B07CBMMCZ8', 'B000AADG0G', 'B01GSTR6Z8', 'B000HHSDU0', 'B078H3W133', 'B003E13O00', 'B00GP0Z96E', 'B00BR7BV9Y', 'B07RD6XBC6', 'B00BM1WDB0', 'B07PRQ4TVM', 'B07SH34DYW', 'B004UPZRNG', 'B0097XGQ5O', 'B0197GP2T6', 'B01G7QDI72', 'B004RRFWI2', 'B01M7UNQZA', 'B0002Z90RM', 'B07NNZPJ8R', 'B000GIH1MG', 'B07QHJ916M', 'B00EQ6958C', 'B01MDU538A', 'B005HTLJFY', 'B075JT6F3Q', 'B07QVW9KKZ', 'B000C23698', 'B00BZAWSS6', 'B07Q276WNB', 'B00VK5S2P4', 'B00GMOUNPA', 'B075S4N28B', 'B07KYVR13P', 'B000PYK34E', 'B004I6ORDI', 'B06XG7D665', 'B000Q7XDR4', 'B00JDROODA', 'B019CMTZYS', 'B013ZS9JC8', 'B07JFS6SD3', 'B074KD48N6', 'B00T6FNWLY', 'B002Z7FS26', 'B06XDHGGZR', 'B000C1UFDE', 'B07M6MX5QB', 'B00JJY15GQ', 'B07FG8285Y', 'B0725YRZ81', 'B0038RFM32', 'B004AZKLGE', 'B018AGNVSS', 'B000XE0DS2', 'B07J5H8DB9', 'B00HAQM3NO', 'B00KIZ2ZG4', 'B004IZJ2QG', 'B000H0U77O', 'B01I436MSS', 'B000R9KYH8', 'B008JHOUGQ', 'B07FY5X2YW', 'B07NFRMCFX', 'B00H8GT8G6', 'B009PAF1WS', 'B07PHGY5PP', 'B07FKDLB89', 'B000GFWIOU', 'B004AI5GM0', 'B000LNWUIG', 'B06XHJCXT3', 'B005IC3R4Q', 'B0039BCT56', 'B00180ZWDQ', 'B014Q9656I', 'B005EV9HPE', 'B07P35THXL', 'B0047DK2RW', 'B00CRJWIIE', 'B00023IXDQ', 'B0091X3MCA', 'B000E7SSCQ', 'B01MZE1BMN', 'B00JTYR8P8', 'B00WCJGH54', 'B000EZU8P8', 'B07NTY5ZFL', 'B000XE7P42', 'B0001BOGW6', 'B07253MW6W', 'B01D48SZ7O', 'B07992Q4YX', 'B000C1UBFQ', 'B07KFH655N', 'B00MU9UI06', 'B000JL5T7O', 'B06XJ8YBYH', 'B004FSM9IY', 'B07ND4N1RZ', 'B075H38DRN', 'B006OHM0JM', 'B000JL69XC', 'B00OM1LRQY', 'B07NVSTGCJ', 'B01BPL68EO', 'B06XSXP9XH', 'B000C231SE', 'B000782SQY', 'B07C2CF1F6', 'B003NOBXSI', 'B01N46DHU1', 'B01BCQOA0G', 'B07NP88V2H', 'B000C1Z29Q', 'B00WH1LWCU', 'B07B89ZJX1', 'B000PK4XTE', 'B01GSIU5AM', 'B00JGV0P68', 'B07QDBQ6BN', 'B000OWRZ0C', 'B0721V5686', 'B01N01UPGE', 'B076HVCS7H', 'B0796M51YK', 'B077V9N2Y9', 'B01N7PYPOD', 'B01JKWNM1W', 'B00AYKSQQ6', 'B000NN3H18', 'B00VTHCTK2', 'B075KHM8CF', 'B01IW02HX2', 'B01HFDCPF2', 'B005MYEOKQ', 'B00X7RCW4A', 'B07TXK7YFX', 'B07L6ZXBSR', 'B00VKEEY8E', 'B000H30EI8', 'B015CIV4OA', 'B00IPQDUOO', 'B07NP8NFMH', 'B001G7PPNI', 'B07GT8K7P8', 'B0755XSCT2', 'B00161LGFU', 'B07C3N6HP9', 'B073SHP2KV', 'B0099AL074', 'B00BJMSVKO', 'B07TF5P9P9', 'B00TF7ITPW', 'B078NBKW1Y', 'B00IN7XR9S', 'B01ETP6HIK', 'B01IPJSTPK', 'B076ZY657B', 'B01IAEFCM8', 'B07C6HVYKQ', 'B000LNG23A', 'B006PANUI8', 'B01MTYCE5N', 'B002XQ1YOK', 'B000FFYMYU', 'B07BKC85C1', 'B01N3SMTEC', 'B07J486K2T', 'B07NN4NBKB', 'B07BL61Q21', 'B00XM3VJES', 'B07L6MVPJ4', 'B073WBDHY2', 'B07GNVL27D', 'B07PCJKG2L', 'B07GNNGR8B', 'B077Y83TN1', 'B07FLB93FM', 'B007BDDNKS', 'B003BQIZX4', 'B0785RCKDB', 'B01FCB3IAK', 'B00OBSPJZI', 'B002SQ14BS', 'B017E3NE9O', 'B000RPGZB6', 'B01M31HY3S', 'B00CHO8O32', 'B07F6W3S65', '9790782152', 'B0711SK4SB', 'B01KKE6XVU', 'B001UE60E0', 'B002KV5JQW', 'B019S4JLSK', 'B002XN688A', 'B0006IHDR4', 'B07G824QR2', 'B00C3V6Q66', 'B0758DY36M', 'B007BMP726', 'B00UFMTTWS', 'B07PWL1BTF', 'B006OZEZME', 'B0087TY7DM', 'B00B5G5DIC', 'B01IPKP8HQ', 'B00I5MW01M', 'B07QH3CNZK', 'B00AR6M1F4', 'B00BMAWQA4', 'B07DR9H6TM', 'B07CGK8FDZ', 'B07KP4W179', 'B005IQ4994', 'B07LGX9VWF', 'B00HNXNMIE', 'B01J6633GQ', 'B0009V8N5E', 'B07GYRQKK9', 'B07M9JQSC4', 'B01BMOAGN8', 'B010SABDMA', 'B000E9WFN2', 'B07BSV1T35', 'B006R2MRA6', 'B00T5ABJLK', 'B0009OAI40', 'B01MR5EQSX', 'B00KIZ2ZRI', 'B0105B8M4O', 'B07C59DQ5M', 'B07G2XKXCL', 'B00O0IFOKE', 'B07LBPZWL4', 'B009DUJCVQ', 'B01GM0OUZC', 'B07QMBP78H', 'B01NBVVKDO', 'B000C1Z5AW', 'B00N65K8RQ', 'B002UU9Q6W', 'B00AHQWHL2', 'B07RCM3LJ2', 'B00AEM0XHE', 'B019H4T398', 'B07M65FP88', 'B00WI1LQFC', 'B00PX6SGNE', 'B00AO4EKSU', 'B079TH8JX9', 'B078JNM8WY', 'B0080D1Q66', 'B074QH7DWM', 'B013FEIAVS', 'B00HBYBFTI', 'B000JL3OYE', 'B000C1Z1B0', 'B00733JU1W', 'B07MCDK6MK', 'B002EOSVUQ', 'B00L6I28YQ', 'B005UZ4YZ2', 'B001B2K4LG', 'B072C4N1KY', 'B0752WCBCJ', 'B01I6124EO', 'B077GJNVSY', 'B07NN3JMB6', 'B001RTSU7I', 'B00RDEYOZ8', 'B005IUXIHY', 'B0170E4MHK', 'B07DPLTXXL', 'B01KMNLLCK', 'B07H444B4D', 'B000Q31MX0', 'B00065IZUG', 'B004RRFYGM', 'B07TC1N8GW', 'B005JIXI5C', 'B01G9NP6GE', 'B00SKDPUTU', 'B074T24YYP', 'B01C1SKJH2', 'B00KFQH0DE', 'B00N8SASCG', 'B0154BCWVY', 'B07CPF9XGV', 'B07DWP3NKK', 'B00L4FNIA4', 'B078XSWPG3', 'B00YESJNBG', 'B071KB9SBM', 'B013Q14D4S', 'B07FL41BW9', 'B07Q4BJL8K', 'B071G46QTX', 'B00GT2LC96', 'B076H2N2F8', 'B010E2EHM0', 'B06W55TJB6', 'B01N4G786C', 'B000MAPBTS', 'B000C1Z5RU', 'B00J5PL4HY', 'B00BOXSD60', 'B000NLQ262', 'B07BZSVW69', 'B000M92UF2', 'B07LBPFXD8', 'B0006O0IBG', 'B006OZEYYS', 'B002Z7FS3K', 'B01JEYRX8O', 'B01LTIAUDS', 'B07CV934TN', 'B01B36H7AK', 'B07F7PN85D', 'B003I6VKF2', 'B003PCAQP4', 'B079SKL3ZP', 'B07QZJLPTG', 'B07CTC8F3F', 'B07P5PQT3S', 'B06WW955KY', 'B06XC78FGF', 'B07PTBJVT1', 'B07CQ63CJL', 'B00GNJBHPO', 'B07TT7T7P4', 'B000GI0TXE', 'B07PJYYNBS', 'B078YGM8H2', 'B079XVK94J', 'B00JOR3IQ8', 'B075G1DC9S', 'B06XP1WYR3', 'B000OOSHAM', 'B003654SVS', 'B07GTP5ST7', 'B07KZ8XVYD', 'B0192EMZ7A', 'B07NP14NZH', 'B07RYXL4SX', 'B01ACF1QJQ', 'B07FCMJZTL', 'B075TXPDF9', 'B007IVYL18', 'B07MLT4D9L', 'B07N2PMDJ8', 'B07Q567YPY', 'B07NFRL4M5', 'B07TXXN891', 'B07CZJVZSY', 'B00O96B0O6', 'B00BU6QHGO', 'B07FVVWVN2', 'B003I8T6II', 'B00MU3ML0C', 'B07G2PL5F5', 'B01GSAYB0K', 'B002AMUGRI', 'B0001783KG', 'B07P1ZDD5H', 'B00L67RJEQ', 'B015UVIU00', 'B01513RQKC', 'B07NRZBJ9S', 'B005HIOTEI', 'B00BEYONDQ', 'B00EVY9ZFM', 'B071GPJBF6', 'B0012X3YZC', 'B0009OAHCS', 'B07NZX71KB', 'B00RDEYYI0', 'B074N8MP22', 'B003QAG3RU', 'B00JKUJGWO', 'B01NA7LTLY', 'B01M4J63QT', 'B07GXL55NM', 'B07Q19W283', 'B01MSWTBUM', 'B002SQ4SKW', 'B07BNJNK6T', 'B01NA97GC0', 'B01CKATNFA', 'B078HPD3ML', 'B06XKBJJJB', 'B07QN3RJHD', 'B07MWF2H6C', 'B0010SWICO', 'B004GIMUL4', 'B00176SJPY', 'B01COO5L4E', 'B000KVA9DW', 'B0784B3W7V', 'B00I4BUUT8', 'B01MQLTFI5', 'B012UIL2GA', 'B003NOI33G', 'B07DN76Z86', 'B002LQ0Y9S', 'B01MTIH0ZH', 'B0105B8MHQ', 'B01IADXP0U', 'B06WRNVT1N', 'B00VC8W38G', 'B01LYLA8H5', 'B01HFH4WH2', 'B07SMSSW36', 'B07PVJG86V', 'B01KU20W3M', 'B018UQEB6E', 'B001ET789M', 'B07CL3B1KZ', 'B07L5BX2C1', 'B076X857XT', 'B00ZV04C6M', 'B07CHG1TSH', 'B075S164DS', 'B07HGFMTKM', 'B00I5YIXNE', 'B01AE215DO', 'B01638974M', 'B01ENR67MK', 'B07C5BHTBQ', 'B07V7WJG13', 'B000UWH3SU', 'B00K9SB44E', 'B000CNTT9I', 'B01DDE3AOW', 'B0012RXAGG', 'B07FMDXFZC', 'B07V9YDF2W', 'B07V5VS53D', 'B00FW3HCHE', 'B00ESZVJW6', 'B00HA88UBQ', 'B01M8MUPJA', 'B00186JR8G', 'B07HX3SFXB', 'B00QMRUR6C', 'B07N2ND6R3', 'B00B8PRZRC', 'B06XCGGG7Y', 'B00U0P5ZRS', 'B01565VALG', 'B07CYZYWN8', 'B003HULFHM', 'B000AKB3JW', 'B07BMXV2CP', 'B07F262RT6', 'B01643HNGK', 'B00XQ9IRP2', 'B077GMVCVG', 'B00488B46E', 'B000EVKXKM', 'B07JNRK315', 'B07P38F57X', 'B00WJ0WEEE', 'B06Y44MMT6', 'B01LTI19EM', 'B01N6CI90P', 'B00Q23K7RA', 'B07MLT4D8K', 'B07MMM2K8N', 'B00VF344X0', 'B00WFH43I6', 'B002RT720I', 'B07BHB5SC5', 'B00013YZ0C', 'B071PBLCKM', 'B01EVQ39X8', 'B07TJP9CNR', 'B005KCPJKY', 'B008HP2AD0', 'B00JADHUAG', 'B00157FJFI', 'B00JJZN1HG', 'B000TTHUDW', 'B0193G2AEU', 'B06XX6D45F', 'B015D942VK', 'B004BCT8NS', 'B07DQBHWYL', 'B0037MQAE8', 'B00LLV8NNS', 'B01BGCGV94', 'B008XJ7F1W', 'B008HP2VRU', 'B07PTYY4TD', 'B00B0MD5Y0', 'B07HJ19K6W', 'B0037LOQQI', 'B001P97U58', 'B004BCX9UQ', 'B002BAW8R0', 'B010W0SBMQ', 'B07Q1K1BPG', 'B01JLFZE00', 'B004D2826K', 'B00M9EGO8W', 'B07BK2HX5P', 'B07GBXM3P1', 'B07Q3BHG2Z', 'B07RPZG25H', 'B07QFR3TVW', 'B000V3MGFS', 'B07CSJXSX6', 'B000NP7JME', 'B07DW6CBSY', 'B07H92T832', 'B07VCWLKYH', 'B07FYMBCS5', 'B0134QL1TK', 'B07KYG3BLH', 'B0719BB846', 'B07H45NFBF', 'B077D7TRS3', 'B07KJ4ZD3C', 'B002RS6JW6', 'B00BKH9HRE', 'B00112DWLK', 'B01M3ODKQF', 'B07QB6RQSS', 'B07HR13LGM', 'B00BSE0BAQ', 'B01KIUMITW', 'B01GOW023M', 'B00ZQ47F6M', 'B07HRV7RSX', 'B00ON1GRKE', 'B07NZB7FL4', 'B01GR3P0RQ', 'B07TJL5T8R', 'B0747P4MBD', 'B07NVFWKYF', 'B074WDX46V', 'B0144DJ97S', 'B07H5TCKH2', 'B07FQJRTGX', 'B00YHMQDC6', 'B000GZNGLE', 'B0056BR5K6', 'B0057RHH98', 'B0711LYH9J', 'B00MBWBF7M', 'B07F74V565', 'B00GB0I86Q', 'B01NBK7Y0K', 'B00U7HJPMU', 'B06XDZZHDZ', 'B001RQLU8M', 'B00QVLB1BO', 'B01K3ZXGDY', 'B00VODRK64', 'B002R2ATUA', 'B00BG14WOM', 'B07FMNKHKW', 'B07C1SZ576', 'B001S4C8MK', 'B0017WT49S', 'B016UMZFQU', 'B004BCZ68E', 'B00I3DJ7PU', 'B07QSCB5XZ', 'B00HE08KUQ', 'B00EZWS24A', 'B00DYQQ0KG', 'B004INIVS8', 'B01IJ7XQ5G', 'B008HCWQDW', 'B004UO67OU', 'B0013VY4AM', 'B07VF7ZL4J', 'B000PARERW', 'B07Q6WV4G3', 'B07DNPX5BF', 'B07Q5PD2YL', 'B07HKYDR1R', 'B00TKYFIKE', 'B07SDCH4ZB', 'B07GXNGT7T', 'B079KNMNLW', 'B07NKDK7WD', 'B01G6SALBM', 'B00CLASIBU', 'B07V3CZXZ9', 'B07JFKDXH3', 'B07PQ7PFRG', 'B00J39ABUS', 'B07PG9RBXC', 'B07SG56X97', 'B005FYJCE6', 'B004W6VTHG', 'B0082D9T0E', 'B07KNQTVXK', 'B07KP7T2TX', 'B016LH1CH0', 'B00YQ3WBJK', 'B0176TZLHE', 'B017LJQ0WE', 'B001FWXJ4G', 'B07H61DLHY', 'B0085UPVOW', 'B079FVW6X4', 'B004W55086', 'B07SFDQZJF', 'B002LFRRIK', 'B01MRR70S8', 'B07P2255G8', 'B0792T47WC', 'B07FMDTW8M', 'B00IZAW2JO', 'B07V31W954', 'B07MYY7NSJ', 'B01LY8TCIC', 'B015U1S7XA', 'B07T7GCVWB', 'B07M5SVHSV', 'B00AV14GTE', 'B07MM4MVR6', 'B07C231GWM', 'B07NF5XGBP', 'B00YX0TUPO', 'B07BHBK5FX', 'B06ZZJB2PR', 'B07HHHDH6R', 'B0000CNR0E', 'B00IZAWHTY', 'B00CQ5Z5NO', 'B07J59M2SY', 'B0779Q4BHQ', 'B0030O9LYY', 'B00YFPS65C', 'B07934CH65', 'B07B4QVRCH', 'B07SS6LFRG', 'B002H96420', 'B076MRRYQ1', 'B07L1VDNHW', 'B01N5HMCM8', 'B07QY73C5K', 'B001KWUHXW', 'B01I3K8GJA', 'B000FYVOJC', 'B07MQBK4S2', 'B003S517E2', 'B01IT09GL6', 'B01IJAJI9G', 'B079QSDB31', 'B001AXFGC8', 'B01E5WXTI8', 'B07HFBPSJ4', 'B01M01MOKA', 'B07KWBP9NS', 'B01IS0FW7O', 'B01J0BYBHW', 'B07585XG1H', 'B07W466LMN', 'B07D54XJZZ', 'B00VONQP2Y', 'B07C7KXY84', 'B074H75ZNR', 'B07W6WSHBF', 'B07TDNNQVD', 'B001E0WZVC', 'B074B57DCM', 'B07QQ1X7YP', 'B004K92DZW', 'B07HQWD991', 'B07GLWJC6K')"
        # query_all_sql = 'select * from amz_product where asin = "B079J64HRX"'
        # query_all_sql = 'select * from amz_product where asin = "B07BFSYZCV"'
        cursor.execute(query_all_sql)
        results = cursor.fetchall()
        return results

    def start_requests(self):
        results = self.query_product()
        # for product in results:
        # for product in results[0: 1000]:
        for product in results[5000: 10000]:
        # for product in results[2000: 3000]:
            product_id = product[0]
            product_class_id = product[1]
            product_url = product[3]
            is_new = product[8]
            meat = {'product_id': product_id, 'product_class_id': product_class_id, 'product_url': product_url, 'is_new': is_new}

            resp = scrapy.Request(product_url, meta=meat, callback=self.parse)
            yield resp

    def parse(self, response):
        item = GetProductDetailsItem()
        product_id = response.meta['product_id']
        product_class_id = response.meta['product_class_id']
        product_url = response.meta['product_url']
        is_new = response.meta['is_new']
        product_name = ''
        product_picture_url = ''
        product_price = ''
        product_stars = ''
        product_reviews = ''
        product_asin = ''
        product_big_class = ''
        product_small_class = ''
        shelf_time = ''
        sale_time = ''
        update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 目前分三种页面排版类型，根据不同的页面的排版来制定相应的方法解析数据
        if len(response.xpath('//div[@id="detail-bullets"]')) > 0:
            # 获取商品名称
            if len(response.xpath('//span[@id="productTitle"]/text()')) > 0:
                product_name = response.xpath('//span[@id="productTitle"]/text()').extract_first().strip()
            else:
                pass

            # 获取商品图片
            if len(response.xpath('//img[@id="landingImage"]')) > 0:
                product_picture_url_list = json.loads(response.xpath('//img[@id="landingImage"]/@data-a-dynamic-image').extract_first().strip())
                keys = []
                for key in product_picture_url_list:
                    keys.append(key)
                product_picture_url = keys[0]
            else:
                pass

            # 获取商品价格
            if len(response.xpath('//span[@id="priceblock_ourprice"]/text()')) > 0:
                product_price = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract_first().strip()
                # print('到这了11111', response.xpath('//span[@id="priceblock_ourprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_snsprice_Based"]/span')) > 0:
                product_price = response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract_first().strip()
                # print('到这了22222', response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract(), aaasin)

            if len(response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]')):
                product_price = response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract_first()
                # print('到这了33333', response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_pospromoprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract_first().strip()
                # print('到这了44444', response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="price_inside_buybox"]')) > 0:
                product_price = response.xpath('//span[@id="price_inside_buybox"]/text()').extract_first().strip()
                # print('到这了55555', response.xpath('//span[@id="price_inside_buybox"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_dealprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_dealprice"]/text()').extract_first().strip()

            if len(response.xpath('//div[@id="csxswImgcsd_0"]/div/span')) > 0:
                product_price = response.xpath('//div[@id="csxswImgcsd_0"]/div/span/text()').extract_first().strip()

            if len(response.xpath('//div[@id="olp-upd-new"]/span/a/text()')) > 0:
                product_price = response.xpath('//div[@id="olp-upd-new"]/span/a/text()').extract_first().split('from')[-1].strip()

            if len(response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span')) > 0:
                product_price = response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span/text()').extract_first().strip()

            # 获取商品star
            if len(response.xpath('//span[@id="acrPopover"]/@title')) > 0:
                product_stars = response.xpath('//span[@id="acrPopover"]/@title').extract_first().split('out of')[0].strip()
            else:
                pass

            # 获取商品reviews
            if len(response.xpath('//span[@id="acrCustomerReviewText"]/text()')) > 0:
                product_reviews = response.xpath('//span[@id="acrCustomerReviewText"]/text()').extract_first().split('customer')[0].strip().replace(',', '')
            else:
                pass

            # 获取商品大类
            if len(response.xpath('//li[@id="SalesRank"]/text()')) > 0:
                xpath_list = response.xpath('//li[@id="SalesRank"]/text()').extract()
                for j in xpath_list:
                    if '#' in j:
                        product_big_class = j.strip().replace(',', '').replace('#', '').split(' ')[0]
                    else:
                        pass
            else:
                pass

            # 获取商品小类
            if len(response.xpath('//li[@id="SalesRank"]/ul/li')) > 0:
                product_small_class = response.xpath('//li[@id="SalesRank"]/ul/li/span/text()').extract_first().strip().replace('#', '')
            else:
                pass

            # 上架时间
            shelf_time = ''
            # 售卖时间
            # sale_time = ''

            item['product_id'] = product_id
            item['product_class_id'] = product_class_id
            item['product_url'] = product_url
            item['product_name'] = product_name
            item['product_picture_url'] = product_picture_url
            item['product_price'] = product_price
            item['product_stars'] = product_stars
            item['product_reviews'] = product_reviews
            item['product_asin'] = product_url.split('/')[-2]
            item['product_big_class'] = product_big_class
            item['product_small_class'] = product_small_class
            item['shelf_time'] = shelf_time
            item['sale_time'] = sale_time
            item['update_time'] = update_time
            item['is_new'] = is_new
            print('detail-bullets形式', product_url, '\n')
        elif len(response.xpath('//table[@id="productDetails_detailBullets_sections1"]')) > 0:
            # 获取商品名称
            if len(response.xpath('//span[@id="productTitle"]/text()')) > 0:
                product_name = response.xpath('//span[@id="productTitle"]/text()').extract_first().strip()
            else:
                pass

            # 获取商品图片
            if len(response.xpath('//img[@id="landingImage"]')) > 0:
                product_picture_url_list = json.loads(response.xpath('//img[@id="landingImage"]/@data-a-dynamic-image').extract_first().strip())
                keys = []
                for key in product_picture_url_list:
                    keys.append(key)
                product_picture_url = keys[0]
            else:
                pass

            # 获取商品价格
            if len(response.xpath('//span[@id="priceblock_ourprice"]/text()')) > 0:
                product_price = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract_first().strip()
                # print('到这了11111', response.xpath('//span[@id="priceblock_ourprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_snsprice_Based"]/span')) > 0:
                product_price = response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract_first().strip()
                # print('到这了22222', response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract(), aaasin)

            if len(response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]')):
                product_price = response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract_first()
                # print('到这了33333', response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract(),aaasin)

            if len(response.xpath('//span[@id="priceblock_pospromoprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract_first().strip()
                # print('到这了44444', response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="price_inside_buybox"]')) > 0:
                product_price = response.xpath('//span[@id="price_inside_buybox"]/text()').extract_first().strip()
                # print('到这了55555', response.xpath('//span[@id="price_inside_buybox"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_dealprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_dealprice"]/text()').extract_first().strip()

            if len(response.xpath('//div[@id="csxswImgcsd_0"]/div/span')) > 0:
                product_price = response.xpath('//div[@id="csxswImgcsd_0"]/div/span/text()').extract_first().strip()

            if len(response.xpath('//div[@id="olp-upd-new"]/span/a/text()')) > 0:
                product_price = response.xpath('//div[@id="olp-upd-new"]/span/a/text()').extract_first().split('from')[-1].strip()

            if len(response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span')) > 0:
                product_price = response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span/text()').extract_first().strip()

            # 获取商品star
            if len(response.xpath('//span[@id="acrPopover"]/@title')) > 0:
                product_stars = response.xpath('//span[@id="acrPopover"]/@title').extract_first().split('out of')[0].strip()
            else:
                pass

            # 获取商品reviews
            if len(response.xpath('//span[@id="acrCustomerReviewText"]/text()')) > 0:
                product_reviews = response.xpath('//span[@id="acrCustomerReviewText"]/text()').extract_first().split('customer')[0].strip().replace(',', '')
            else:
                pass

            # 获取商品大小类
            if len(response.xpath('//table[@id="productDetails_detailBullets_sections1"]/tr')) > 0:
                for tr in response.xpath('//table[@id="productDetails_detailBullets_sections1"]/tr'):
                    if 'Best Sellers Rank' in tr.xpath('./th/text()').extract_first().strip():
                        if len(tr.xpath('./td/span/span[1]')) > 0:
                            product_big_class = tr.xpath('./td/span/span[1]/text()').extract_first().strip().replace('#', '').replace(',', '').split(' ')[0]
                        if len(tr.xpath('./td/span/span[2]')) > 0:
                            product_small_class = tr.xpath('./td/span/span[2]/text()').extract_first().strip().replace('#', '').replace(',', '').split(' ')[0]

            # 上架时间
            if len(response.xpath('//table[@id="productDetails_detailBullets_sections1"]/tr')) > 0:
                for tr in response.xpath('//table[@id="productDetails_detailBullets_sections1"]/tr'):
                    if 'first' in tr.xpath('./th/text()').extract_first().strip().lower():
                        if len(tr.xpath('./td')) > 0:
                            shelf_time = tr.xpath('./td/text()').extract_first().strip()

            # 售卖时间
            # sale_time = ''
            item['product_id'] = product_id
            item['product_class_id'] = product_class_id
            item['product_url'] = product_url
            item['product_name'] = product_name
            item['product_picture_url'] = product_picture_url
            item['product_price'] = product_price
            item['product_stars'] = product_stars
            item['product_reviews'] = product_reviews
            item['product_asin'] = product_url.split('/')[-2]
            item['product_big_class'] = product_big_class
            item['product_small_class'] = product_small_class
            item['shelf_time'] = shelf_time
            item['sale_time'] = sale_time
            item['update_time'] = update_time
            item['is_new'] = is_new
            print('表格形式的产品信息陈列！', product_url, '\n')

        elif len(response.xpath('//div[@id="detailBulletsWrapper_feature_div"]')) > 0:

            # 获取商品名称
            if len(response.xpath('//span[@id="productTitle"]/text()')) > 0:
                product_name = response.xpath('//span[@id="productTitle"]/text()').extract_first().strip()
            else:
                pass

            # 获取商品图片
            if len(response.xpath('//img[@id="landingImage"]')) > 0:
                product_picture_url_list = json.loads(response.xpath('//img[@id="landingImage"]/@data-a-dynamic-image').extract_first().strip())
                keys = []
                for key in product_picture_url_list:
                    keys.append(key)
                product_picture_url = keys[0]
            else:
                pass

            # 获取商品价格
            if len(response.xpath('//span[@id="priceblock_ourprice"]/text()')) > 0:
                product_price = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract_first().strip()
                # print('到这了11111', response.xpath('//span[@id="priceblock_ourprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_snsprice_Based"]/span')) > 0:
                product_price = response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract_first().strip()
                # print('到这了22222', response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract(), aaasin)

            if len(response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]')):
                product_price = response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract_first()
                # print('到这了33333', response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract(),aaasin)

            if len(response.xpath('//span[@id="priceblock_pospromoprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract_first().strip()
                # print('到这了44444', response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="price_inside_buybox"]')) > 0:
                product_price = response.xpath('//span[@id="price_inside_buybox"]/text()').extract_first().strip()
                # print('到这了55555', response.xpath('//span[@id="price_inside_buybox"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_dealprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_dealprice"]/text()').extract_first().strip()

            if len(response.xpath('//div[@id="csxswImgcsd_0"]/div/span')) > 0:
                product_price = response.xpath('//div[@id="csxswImgcsd_0"]/div/span/text()').extract_first().strip()

            if len(response.xpath('//div[@id="olp-upd-new"]/span/a/text()')) > 0:
                product_price = response.xpath('//div[@id="olp-upd-new"]/span/a/text()').extract_first().split('from')[-1].strip()

            if len(response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span')) > 0:
                product_price = response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span/text()').extract_first().strip()

            # 获取商品star
            if len(response.xpath('//span[@id="acrPopover"]/@title')) > 0:
                product_stars = response.xpath('//span[@id="acrPopover"]/@title').extract_first().split('out of')[0].strip()
            else:
                pass

            # 获取商品reviews
            if len(response.xpath('//span[@id="acrCustomerReviewText"]/text()')) > 0:
                product_reviews = response.xpath('//span[@id="acrCustomerReviewText"]/text()').extract_first().split('customer')[0].strip().replace(',', '')
            else:
                pass

            # 获取商品大小类
            if len(response.xpath('//li[@id="SalesRank"]')) > 0:
                for ite in response.xpath('//li[@id="SalesRank"]/text()').extract():
                    if '#' in ite:
                        product_big_class = ite.strip().replace('#', '').replace(',', '').split(' ')[0]
                if len(response.xpath('//li[@id="SalesRank"]/ul/li[1]/span[1]')) > 0:
                    product_small_class = response.xpath('//li[@id="SalesRank"]/ul/li[1]/span[1]/text()').extract_first().strip().replace('#', '').replace(',', '').split(' ')[0]

            # 上架时间
            if len(response.xpath('//div[@id="detailBullets_feature_div"]/ul/li')) > 0:
                for li_tag in response.xpath('//div[@id="detailBullets_feature_div"]/ul/li'):
                    if len(li_tag.xpath('./span/span[1]')) > 0 and 'first listed on' in li_tag.xpath('./span/span[1]/text()').extract_first() and len(li_tag.xpath('./span/span[2]')) > 0:
                        shelf_time = li_tag.xpath('./span/span[2]/text()').extract_first().strip()

            # 售卖时间
            # sale_time = ''
            item['product_id'] = product_id
            item['product_class_id'] = product_class_id
            item['product_url'] = product_url
            item['product_name'] = product_name
            item['product_picture_url'] = product_picture_url
            item['product_price'] = product_price
            item['product_stars'] = product_stars
            item['product_reviews'] = product_reviews
            item['product_asin'] = product_url.split('/')[-2]
            item['product_big_class'] = product_big_class
            item['product_small_class'] = product_small_class
            item['shelf_time'] = shelf_time
            item['sale_time'] = sale_time
            item['update_time'] = update_time
            item['is_new'] = is_new
            print('detailBulletsWrapper_feature_div形式', product_url, '\n')

        elif len(response.xpath('//div[@id="prodDetails"]')) > 0 and len(response.xpath('//table[@id="productDetails_detailBullets_sections1"]')) == 0:
            # 获取商品名称
            if len(response.xpath('//span[@id="productTitle"]/text()')) > 0:
                product_name = response.xpath('//span[@id="productTitle"]/text()').extract_first().strip()
            else:
                pass

            # 获取商品图片
            if len(response.xpath('//img[@id="landingImage"]')) > 0:
                product_picture_url_list = json.loads(response.xpath('//img[@id="landingImage"]/@data-a-dynamic-image').extract_first().strip())
                keys = []
                for key in product_picture_url_list:
                    keys.append(key)
                product_picture_url = keys[0]
            else:
                pass

            # 获取商品价格
            if len(response.xpath('//span[@id="priceblock_ourprice"]/text()')) > 0:
                product_price = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract_first().strip()
                # print('到这了11111', response.xpath('//span[@id="priceblock_ourprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_snsprice_Based"]/span')) > 0:
                product_price = response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract_first().strip()
                # print('到这了22222', response.xpath('//span[@id="priceblock_snsprice_Based"]/span/text()').extract(), aaasin)

            if len(response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]')):
                product_price = response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()').extract_first()
                # print('到这了33333', response.xpath('//div[@id="unqualified"]/div/span[@class="a-color-price"]/text()'),aaasin)

            if len(response.xpath('//span[@id="priceblock_pospromoprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract_first().strip()
                # print('到这了44444', response.xpath('//span[@id="priceblock_pospromoprice"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="price_inside_buybox"]')) > 0:
                product_price = response.xpath('//span[@id="price_inside_buybox"]/text()').extract_first().strip()
                # print('到这了55555', response.xpath('//span[@id="price_inside_buybox"]/text()').extract(), aaasin)

            if len(response.xpath('//span[@id="priceblock_dealprice"]')) > 0:
                product_price = response.xpath('//span[@id="priceblock_dealprice"]/text()').extract_first().strip()

            if len(response.xpath('//div[@id="csxswImgcsd_0"]/div/span')) > 0:
                product_price = response.xpath('//div[@id="csxswImgcsd_0"]/div/span/text()').extract_first().strip()

            if len(response.xpath('//div[@id="olp-upd-new"]/span/a/text()')) > 0:
                product_price = response.xpath('//div[@id="olp-upd-new"]/span/a/text()').extract_first().split('from')[-1].strip()

            if len(response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span')) > 0:
                product_price = response.xpath('//form[@id="sims-fbt-form"]/div[2]/fieldset/ul/li[1]/span/span/div/label/span/div/span[3]/span/text()').extract_first().strip()

            # 获取商品star
            if len(response.xpath('//span[@id="acrPopover"]/@title')) > 0:
                product_stars = response.xpath('//span[@id="acrPopover"]/@title').extract_first().split('out of')[0].strip()
            else:
                pass

            # 获取商品reviews
            if len(response.xpath('//span[@id="acrCustomerReviewText"]/text()')) > 0:
                product_reviews = response.xpath('//span[@id="acrCustomerReviewText"]/text()').extract_first().split('customer')[0].strip().replace(',', '')
            else:
                pass

            # 获取商品大小类
            if len(response.xpath('//li[@id="SalesRank"]/td[2]')) > 0:
                for td_value in response.xpath('//li[@id="SalesRank"]/td[2]/text()').extract():
                    if '#' in td_value:
                        product_big_class = td_value.strip().replace('#', '').replace(',', '').split(' ')[0]
                if len(response.xpath('//li[@id="SalesRank"]/td[2]/ul/li[1]')) > 0:
                    product_small_class = response.xpath('//li[@id="SalesRank"]/td[2]/ul/li[1]/span[1]/text()').extract_first().strip().replace('#', '').replace(',', '').split(' ')[0]

            if len(response.xpath('//tr[@id="SalesRank"]/td[2]')) > 0:
                for td_value in response.xpath('//tr[@id="SalesRank"]/td[2]/text()').extract():
                    if '#' in td_value:
                        product_big_class = td_value.strip().replace('#', '').replace(',', '').split(' ')[0]
                if len(response.xpath('//tr[@id="SalesRank"]/td[2]/ul/li[1]')) > 0:
                    product_small_class = response.xpath('//tr[@id="SalesRank"]/td[2]/ul/li[1]/span[1]/text()').extract_first().strip().replace('#', '').replace(',', '').split(' ')[0]

            # 上架时间
            shelf_time = ''
            # 售卖时间
            # sale_time = ''
            item['product_id'] = product_id
            item['product_class_id'] = product_class_id
            item['product_url'] = product_url
            item['product_name'] = product_name
            item['product_picture_url'] = product_picture_url
            item['product_price'] = product_price
            item['product_stars'] = product_stars
            item['product_reviews'] = product_reviews
            item['product_asin'] = product_url.split('/')[-2]
            item['product_big_class'] = product_big_class
            item['product_small_class'] = product_small_class
            item['shelf_time'] = shelf_time
            item['sale_time'] = sale_time
            item['update_time'] = update_time
            item['is_new'] = is_new
            print('detailBullets_feature_div形式', product_url, '\n')

        else:
            print('还有其他的！', product_url)
            item['product_id'] = product_id
            item['product_class_id'] = product_class_id
            item['product_url'] = product_url
            item['product_name'] = product_name
            item['product_picture_url'] = product_picture_url
            item['product_price'] = product_price
            item['product_stars'] = product_stars
            item['product_reviews'] = product_reviews
            item['product_asin'] = product_url.split('/')[-2]
            item['product_big_class'] = product_big_class
            item['product_small_class'] = product_small_class
            item['shelf_time'] = shelf_time
            item['sale_time'] = sale_time
            item['update_time'] = update_time
            item['is_new'] = is_new
            item['http_status_code'] = response.status
            # amzn = ''
            # amzn_r = ''
            # captcha = ''
            # soup = BeautifulSoup(response.text, 'lxml')
            # amzn = soup.select('form input')[0].get('value')
            # print(amzn)
            # amzn_r = soup.select('form input')[1].get('value')
            # print(amzn_r)
            # captcha_img_url = soup.select('div.a-row.a-text-center img')[0].get('src')
            # print(captcha_img_url)
            # resp = requests.get(captcha_img_url)
            # print(os.getcwd())
            # file_name = self.PATH + '/jpg/img/' + captcha_img_url.split('/')[-1]
            # with open(file_name, 'wb')as f:
            #     f.write(resp.content)
            #     f.close()
            #
            # captcha = process(file_name)
            # print(captcha)
            # url = self.base_url.format(amzn, amzn_r, captcha)
            # print(url)
            # resp_2 = requests.get(url, headers=self.header)
            # print(resp_2.text)
            # print('del ' + self.PATH + '/jpg/img/' + captcha + '.jpg')
            # os.system('del ' + self.PATH + '/jpg/img/' + captcha + '.jpg')

        yield item


