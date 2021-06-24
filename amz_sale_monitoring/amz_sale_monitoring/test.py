import requests
import json
req_url = 'https://unidemo.dcloud.net.cn/api/picture/posts.php?page=0&per_page=100000'
results = requests.get(req_url).text
print(results)
for i in json.loads(results):
    print(i)

# # from selenium import webdriver
# #
# url = 'https://www.amazon.fr/gp/offer-listing/B07QS8X7F8'
# header = {
#     #'cookie': 'session-id-time=2082787201l; session-id=130-9086340-7074154; ubid-main=130-0736566-9403533; sp-cdn="L5Z9:UM"; sst-main=Sst1|PQFV-XxZrs_RWWe4bZn8b204C2N6zWxJdPzz7g0-Itlmm2-8CF1iTI-cH_7Jpg24x-AIG_go_pXE_G1O931bKzICOdU3489YvhDwmc21DBhMGdDuIfmK_VsGQ0xIrw6IDpd5kJrhKO2jZkBCK0c77atxXhHcYlrAtFsteDjcyxOL-1FrjDKUsM0fvlArlfi8Wd-UodtqLPQD_20WIX4SROZ4s1Z2nTZ7f-Z6RwwvYtfY5_Gh4LDaS6LvepyJVlsDzkZxsJJLmCXlDheu2c5eAY7WnJpqbI8tEQ6pIUAD2rr6yXtWw6nP7v2THChZbv3IAWqkciGKz-lGznrU9VBZyiP2lA; i18n-prefs=USD; session-token=rqu+W6cvxuPC96AJVLGukWnGlrRI3t3uFrd25CFwYACLLJ6o00zc6hSPzyin7dTla0M+Pf6z+qOtrV4kqzLbvE4zkku5+JEtgUZ4RkTPfjvokxneQPxWRGDGKViDUSMrhkqpAe8u8UEr9wKZ5IWJRtHujUTkxuJCcHpFIAURPP8a/bj9cCFsH04W1IQUY9Ikg1w0GgEtzkgsR/tEuVz3bWE4BnlbsJxcNWK9g4/f1uOBwoOhQCxv3+gb57xleOhq; s_pers=%20s_fid%3D158CE4CD3FE83D21-0953BD0EFD2BA519%7C1735638258251%3B%20s_dl%3D1%7C1577787258252%3B%20gpv_page%3DProject%2520Zero%253A%2520Home%7C1577787258254%3B%20s_ev15%3D%255B%255B%2527NSBaidu%2527%252C%25271577785458256%2527%255D%255D%7C1735638258256%3B; x-wl-uid=1YGLlB4sarOeeU5OBsRmJcj2pP6xtF5Em5f2heGt4iCr9y1+b3Np3DIjHlqgEG1uzpVZCWfWszdTvq+mwx/98HQ==; csm-hit=tb:GF76G4M5TY2PVH624Y60+s-GF76G4M5TY2PVH624Y60|1578019468267&t:1578019468267&adb:adblk_no',
#     'cookie': 'x-wl-uid=13SjBf7DbyOHu4HDOsoGjohNL/aA5b+klJG1c0Ohwv4v2EJvcpauS978NiENAHvYRmQUGikOgGAU=; session-id=259-9716847-6053542; ubid-acbfr=259-5117998-6265262; x-amz-captcha-1=1576727107109272; x-amz-captcha-2=BJ+FnTm1r3gsbfAN3VwXZQ==; i18n-prefs=EUR; session-token=mH8KguhMYyLZpywYfUeLh79PTNjkZ94cMbHY8kplT8TWvXcb2uL4juY1mTj3kvpqK5N+rBdp9+gUxqXTbAvGfj/JsCcQB04eMRHRufJht55o4ujKN40MZovXlun1onZFWOY0HNAFv10N72UJ2kBpkMNdsFYfFTnuhJk8jRSp8WCTUxPfi/bbShjjIyWCq7OE; session-id-time=2082754801l; csm-hit=tb:YYTZ3SRGW9FAMR2A624F+s-YYTZ3SRGW9FAMR2A624F|1579227096248&t:1579227096248&adb:adblk_no',
#     'referer': 'https://www.amazon.com',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
# }
#
# resp = requests.get(url, headers=header)
# print(resp.text)
#
# # bb = webdriver.Chrome()
# # for i in range(10):
# #     bb.get(url)
import win32api
import win32con
import win32gui
import time

# win32api.ShellExecute(1, 'open',
#  r'"D:\Program Files (x86)\Tencent\QQ\Bin\QQ.exe"',
#  '', '', 1)
# para_hld = win32gui.FindWindow(None, "QQ")
# print(para_hld)
# title = win32gui.GetWindowText(para_hld)
# print(title)
# time.sleep(5)
# print(win32api.GetCursorPos())
# xy = win32api.GetCursorPos()
# print(type(win32api.GetCursorPos()))
# win32api.SetCursorPos(xy)
# win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, xy[0], xy[1], 0, 0)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, xy[0], xy[1], 0, 0)
# win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)







