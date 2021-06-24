from selenium import webdriver

bro = webdriver.Chrome()
bro.get('https://www.amazon.com/')
bro.get('https://www.amazon.com/')
cookie = [
{
    "domain": ".amazon.com",
    "expirationDate": 1575426055.593071,
    "hostOnly": False,
    "httpOnly": False,
    "name": "a-ogbcbff",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1",
    "id": 1
},
{
    "domain": ".amazon.com",
    "expirationDate": 2206145215.59314,
    "hostOnly": False,
    "httpOnly": True,
    "name": "at-main",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "Atza|IwEBIPBkIhS3_zfZjCRbU_p3j8GYsrPSyOO4jquORjXEu9KN_cNasTr0FPBv-So2zoAPx2FULkJghZxDE993Br7Qb8R8-LjQ6YXJfKV_lFziGm32y1AeRodACGxXgp3PReU6o5df8ueyDj96Ku90S4lDg0NVENTvjFdxfQ4_6OLC7HUQCATMgzqiA3bC7M8ubnuYYMwMKPoLApW2zkzQaA0UX9_GpdwH-cL5DIX8AK8uA341P1Ki5cl4P9djTn7bcKGZvHYO6B1wpumEsvOVP8LAi8znvaKwv_-EKyMN6jR-jIdhLRSgY4MF1rAULWFuTJwYW1zJgvvWI9CH6HA6fwvJl-OWg_Opqlli7M4k-3450Mgc2uUs_x1hPuJVpGEbr6LrDTEI1CZlbgTID1LoWMcSUGQ98HMfGKYz-SXMF1-3s8DfvVEIxW84039DIjmhR5nG0Hg",
    "id": 2
},
{
    "domain": ".amazon.com",
    "expirationDate": 2082787193.948424,
    "hostOnly": False,
    "httpOnly": False,
    "name": "i18n-prefs",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "USD",
    "id": 3
},
{
    "domain": ".amazon.com",
    "expirationDate": 2206145215.593184,
    "hostOnly": False,
    "httpOnly": False,
    "name": "lc-main",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "en_US",
    "id": 4
},
{
    "domain": ".amazon.com",
    "expirationDate": 2206145215.593156,
    "hostOnly": False,
    "httpOnly": True,
    "name": "sess-at-main",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "\"BnxOqlSVaXUc3krKcbjEguuRSqbonhvQtMmJxslRaxA=\"",
    "id": 5
},
{
    "domain": ".amazon.com",
    "expirationDate": 2082787194.35568,
    "hostOnly": False,
    "httpOnly": False,
    "name": "session-id",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "143-7611113-5582127",
    "id": 6
},
{
    "domain": ".amazon.com",
    "expirationDate": 2082787194.355636,
    "hostOnly": False,
    "httpOnly": False,
    "name": "session-id-time",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "2082787201l",
    "id": 7
},
{
    "domain": ".amazon.com",
    "expirationDate": 2206145215.593114,
    "hostOnly": False,
    "httpOnly": False,
    "name": "session-token",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "\"TSDIK9VnlUo1CplslIXUzKWwjgN1WC5wx4ZL5O4fvHTe4K00RiB/RpNjxCnylq+qjrhH+oC6hDVlgwDi6WH2NNir87XwbYHsSuxzd6XR11/poTkYl71d4ujvKYQhIHPdSPfYlHTVWxICBIdREcy7Pe+6F68ZRcLYLl5dfKgu7ePTeVmluDLjS4ZKn83xccY42Zg1nTsQrxwvr1HbCfuxS5qaiTnHvPmxKyWTNtun+bg=\"",
    "id": 8
},
{
    "domain": ".amazon.com",
    "hostOnly": False,
    "httpOnly": False,
    "name": "skin",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": True,
    "storeId": "0",
    "value": "noskin",
    "id": 9
},
{
    "domain": ".amazon.com",
    "expirationDate": 2082787193.948448,
    "hostOnly": False,
    "httpOnly": True,
    "name": "sp-cdn",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "\"L5Z9:CN\"",
    "id": 10
},
{
    "domain": ".amazon.com",
    "expirationDate": 2206145215.593165,
    "hostOnly": False,
    "httpOnly": True,
    "name": "sst-main",
    "path": "/",
    "sameSite": "unspecified",
    "secure": True,
    "session": False,
    "storeId": "0",
    "value": "Sst1|PQFGDxUC579XQrV-tIcggmZOC5lYOw9x1gpvo8E0zxtdos-WpvIMLqn2PSVC7Y3GqMI29gWynb4XmdXtA6HpcdybS-6aqnxRn6kfAPJ8A141BKYNGU9DRfTqXdBH9THFgSCT3mV2i9foi8MH_wz_B6VdTNYT4-SVBtpI4bNqsf3MceVMO67MwrLtifxxGhN2YtZRTit5MgG7_wcDRRwK2Iet6no10aoJeNnWKbSvbgEtwW2pWPmg4t_eKtd10GSABJFC7cmPcHHSqSO0I9XlCeUIMhdwZtoIvUX0om-H8LuHKU0uTwmFE1qnqb7o5kLDEQCW5a7lgy42r08TvX0DE0A4nQ",
    "id": 11
},
{
    "domain": ".amazon.com",
    "expirationDate": 2082787194.355559,
    "hostOnly": False,
    "httpOnly": False,
    "name": "ubid-main",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "131-0824392-6783429",
    "id": 12
},
{
    "domain": ".amazon.com",
    "expirationDate": 2206145215.593129,
    "hostOnly": False,
    "httpOnly": False,
    "name": "x-main",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "\"LrOWm4Hzu0@TzE868et1CoEgk2tKFkd@gEKqhZhW2LdfidPi@6AIeFAACG6PzN3X\"",
    "id": 13
},
{
    "domain": ".amazon.com",
    "expirationDate": 2082787194.149744,
    "hostOnly": False,
    "httpOnly": False,
    "name": "x-wl-uid",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "1EiDTjfRv9WftZY0O1Kj3NwMlLK6V38eOB6bUrWpQwJjoeshN/B4ACVnYeiXFdIUVi6wv+m939S+RY4feETqNdQ==",
    "id": 14
},
{
    "domain": "www.amazon.com",
    "expirationDate": 1635905492,
    "hostOnly": True,
    "httpOnly": False,
    "name": "csm-hit",
    "path": "/",
    "sameSite": "unspecified",
    "secure": False,
    "session": False,
    "storeId": "0",
    "value": "tb:KDAXKPGCA4476FKEY8PN+s-H35GX1FNN0FCC70J0FX5|1575425492193&t:1575425492193&adb:adblk_no",
    "id": 15
}
]
for i in cookie:
    print(i)
    print(1)
    bro.add_cookie(i)
bro.get('https://www.amazon.com/')
print(bro.get_cookies())


# bro = webdriver.Chrome()
# bro.get('https://www.taobao.com/')
# bro.get('https://www.taobao.com/')
# cookie = [
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1606964626.468439,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "_cc_",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "U%2BGCWk%2F7og%3D%3D",
#     "id": 1
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "_l_g_",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "Ug%3D%3D",
#     "id": 2
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "_nk_",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "%5Cu6211%5Cu662F%5Cu5C0F%5Cu5F3A%5Cu6211%5Cu7231%5Cu6DD8",
#     "id": 3
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "_tb_token_",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "ee8e0ee4eea0a",
#     "id": 4
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 2203895631,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "cna",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "h71KFsRLNHYCAXFu/032g9cq",
#     "id": 5
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "cookie1",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "VWfFTzoC0QnkHmYHNyg1h0%2BXD2fPLUfkzYgt4MKSJiI%3D",
#     "id": 6
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "cookie17",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "Uoe0azMwQtKxbA%3D%3D",
#     "id": 7
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "cookie2",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "11ca54348f8bc9dbfc8253b8d6814c2d",
#     "id": 8
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "csg",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "bcafea9c",
#     "id": 9
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "dnk",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "%5Cu6211%5Cu662F%5Cu5C0F%5Cu5F3A%5Cu6211%5Cu7231%5Cu6DD8",
#     "id": 10
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1888535639.81362,
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "enc",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": True,
#     "session": False,
#     "storeId": "0",
#     "value": "YY2KqyUIJTtqhWb0kNzcIZ7G1nuwXmNUkMNK%2Fmh2%2BJN%2FaFNKEmjFRRMVoXMYGy7wc%2BGCcBAhS0McxaKa%2Fw9QVw%3D%3D",
#     "id": 11
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "existShop",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "MTU3NTQyODYzMw%3D%3D",
#     "id": 12
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1604711640.619555,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "hng",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "CN%7Czh-CN%7CCNY%7C156",
#     "id": 13
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1590980650,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "isg",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "BAcHYWmqFnkHO5LWCGsPWdC5lrsRpLKWkCqDDdn0Axa9SCcK4dxrPkUK7gAWoLNm",
#     "id": 14
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1590980641,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "l",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "dBO-ZHTVqZLlDv81BOfNCuIRQj79aIRb4sPzw4NfSICPOT595KeAWZKkNgYpCnGNH6DXR3Jt3efYBeYBq_EwfdW2w8VMURHqndC..",
#     "id": 15
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1578020626.468186,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "lgc",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "%5Cu6211%5Cu662F%5Cu5C0F%5Cu5F3A%5Cu6211%5Cu7231%5Cu6DD8",
#     "id": 16
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1576033432.998659,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "mt",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "ci=23_1",
#     "id": 17
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "sg",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "%E6%B7%9840",
#     "id": 18
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "skt",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "e3c08619098aa398",
#     "id": 19
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1583204626.468211,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "t",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "00615f9f1eee68f93551287f1cd4ac6d",
#     "id": 20
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1629428626.468491,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "tg",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "0",
#     "id": 21
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1604279640,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "thw",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "cn",
#     "id": 22
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1606964626.468358,
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "tracknick",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "%5Cu6211%5Cu662F%5Cu5C0F%5Cu5F3A%5Cu6211%5Cu7231%5Cu6DD8",
#     "id": 23
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "uc1",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie21=VFC%2FuZ9ajC0X15Rzt0LhxQ%3D%3D&cookie15=UtASsssmOIJ0bQ%3D%3D&existShop=False&pas=0&cookie14=UoTbmE%2Bueb%2FF5g%3D%3D&tag=8&lng=zh_CN",
#     "id": 24
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1578020626.468105,
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "uc3",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "vt3=F8dByus8gtZqvR1hFZA%3D&id2=Uoe0azMwQtKxbA%3D%3D&nk2=rUtEoefJD2QUl1zpdIU%3D&lg2=WqG3DMC9VAQiUQ%3D%3D",
#     "id": 25
# },
# {
#     "domain": ".taobao.com",
#     "expirationDate": 1578020626.468321,
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "uc4",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": False,
#     "storeId": "0",
#     "value": "nk4=0%40r7rCNY1%2FjBuXRJRsUlfB1OBfFLzwceHQvg%3D%3D&id4=0%40UO%2BymBOs6z8Vx6I9CHObr%2Fj4A9x7",
#     "id": 26
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": True,
#     "name": "unb",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "1606573484",
#     "id": 27
# },
# {
#     "domain": ".taobao.com",
#     "hostOnly": False,
#     "httpOnly": False,
#     "name": "v",
#     "path": "/",
#     "sameSite": "unspecified",
#     "secure": False,
#     "session": True,
#     "storeId": "0",
#     "value": "0",
#     "id": 28
# }
# ]
# for i in cookie:
#     print(i)
#     print(1)
#     bro.add_cookie(i)
# bro.get('https://www.taobao.com/')
# print(bro.get_cookies())
