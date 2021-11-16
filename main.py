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
    appTitle = soup.find_all("title")
    appPrice = soup.find_all('li', attrs={'class': re.compile(r"inline-list__item inline-list__item--bulleted app-header__list__item--price")})
    hasInAppPurchase = soup.find_all('li', attrs={'class': re.compile(r"inline-list__item inline-list__item--bulleted app-header__list__item--in-app-purchase")})
    inAppPurchaseTitle = soup.find_all('span', attrs={'class': re.compile(r"truncate-single-line truncate-single-line--block")})
    inAppPurchasePrice = soup.find_all('span', attrs={'class': re.compile(r"list-with-numbers__item__price small-hide medium-show-tablecell")})

    # data1=[(comment_time_list[jj].string,
    #     use_name_list[jj].a.string,
    #     comment_list[jj].string,
    #     rating_list[jj].get('class')[0],
    #     rating_list[jj].get('title'))]
    # data2 = pd.DataFrame(data1)
    # data2.to_csv('douban_movie1.csv', header=False, index=False, mode='a+',encoding="utf-8-sig")
    print(appTitle[0].string)
    print(appPrice[0].string)
    try:
        print(hasInAppPurchase[0].text)
        for i in range(len(inAppPurchaseTitle)):
            print(inAppPurchaseTitle[i].text)
            print(inAppPurchasePrice[i].text)
    except AttributeError:
        print("无内购应用!")



# url = 'https://apps.apple.com/cn/app/id1459749978' # List背单词
url = 'https://apps.apple.com/cn/app/id1348317163' # marginnote
# url = 'https://apps.apple.com/cn/app/id535886823' # chrome
while True:
    try:
        get_key_info(url)
        break
    except:
        time.sleep(2)
