from fake_useragent import UserAgent
import json

ua = UserAgent()
for i in range(10):
    # print(ua.ie)
    # print("'" + ua.chrome + "',")
    # print("'" + ua.ie + "',")
    # print("'" + ua.firefox + "',")
    # print("'" + ua.opera + "',")
    # print("'" + ua.safari + "',")
    # print(ua.random)
    # print(ua.data)
    pass
# print(dict(ua.data_browsers))
for i in dict(ua.data_browsers):
    for j in dict(ua.data_browsers)[i]:
        print("'" + j + "',")