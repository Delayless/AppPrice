import requests
import pandas as pd
import re
import time
from bs4 import BeautifulSoup


def get_key_info(url):
    header = {
            'accept': 'text/html,application/xhtml+xml,application/xml',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
            }
    #request请求
    html=requests.get(url,headers=header)
    #beautifulsoup解析网址
    soup = BeautifulSoup(html.content,'lxml')
    appTitleBlock = soup.find_all("title")
    appPriceBlock = soup.find_all('li', attrs={'class': re.compile(r"inline-list__item inline-list__item--bulleted app-header__list__item--price")})
    hasInAppPurchaseBlock = soup.find_all('li', attrs={'class': re.compile(r"inline-list__item inline-list__item--bulleted app-header__list__item--in-app-purchase")})
    inAppPurchaseTitleBlock = soup.find_all('span', attrs={'class': re.compile(r"truncate-single-line truncate-single-line--block")})
    inAppPurchasePriceBlock = soup.find_all('span', attrs={'class': re.compile(r"list-with-numbers__item__price small-hide medium-show-tablecell")})

    # 提取App名字
    appName = appTitleBlock[0].text.replace("\u200eApp\xa0Store 上的", "").replace('“', '').replace('”', '')
    appPrice = appPriceBlock[0].text.replace("¥", "")
    print(appName)
    appInfo = (appName + ": ￥" + appPrice,)
    if (len(inAppPurchaseTitleBlock) == 0):
        appInfo = appInfo + (("无内购应用!"),)
        return [appInfo]
    for i in range(len(inAppPurchaseTitleBlock)):
        inAppPurchasePrice = inAppPurchasePriceBlock[i].text.replace("¥", "")
        inAppPurchaseTitle = inAppPurchaseTitleBlock[i].text
        appInfo = appInfo + (inAppPurchaseTitle + ": ￥" + inAppPurchasePrice,)
    return [appInfo]


# url = 'https://apps.apple.com/cn/app/id1459749978' # List背单词
# url = 'https://apps.apple.com/cn/app/id1348317163' # marginnote
# url = 'https://apps.apple.com/cn/app/id535886823' # chrome
apps = ["id1459749978", "id1348317163", "id535886823"]
for item in apps:
    url = 'https://apps.apple.com/cn/app/'+item
    print(url)
    while True:
        try:
            info = get_key_info(url)
            print(info)
            data2 = pd.DataFrame(info)
            data2.to_csv('appPrice.csv', header=False, index=False, mode='a+',encoding="utf-8-sig")
            break
        except:
            time.sleep(2)
