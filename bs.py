import requests
import pandas as pd
import re
import time
from bs4 import BeautifulSoup



url = 'https://apps.apple.com/cn/app/id1459749978'
header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        }
#request请求
html=requests.get(url,headers=header)
#beautifulsoup解析网址
soup = BeautifulSoup(html.content,'lxml')
appPrice = soup.find('li', attrs={'class': re.compile(r"inline-list__item inline-list__item--bulleted app-header__list__item--price")})
hasInAppPurchase = soup.find('li', attrs={'class': re.compile(r"inline-list__item inline-list__item--bulleted app-header__list__item--in-app-purchase")})
# inAppPurchaseTitle = soup.find('span', attrs={'class': re.compile(r"list-with-numbers__item__title")})
inAppPurchaseTitle = soup.find('span', attrs={'class': re.compile(r"truncate-single-line truncate-single-line--block")})
inAppPurchasePrice = soup.find('span', attrs={'class': re.compile(r"list-with-numbers__item__price small-hide medium-show-tablecell")})
# inAppPurchase = soup.find('li', attrs={'class': re.compile(r"list-with-numbers__item")})
# print(inAppPurchase)
print(appPrice)
print(hasInAppPurchase)
print(inAppPurchaseTitle)
print(inAppPurchasePrice)


# <li class="inline-list__item inline-list__item--bulleted app-header__list__item--price">¥8.00</li>
# <li class="inline-list__item inline-list__item--bulleted app-header__list__item--in-app-purchase">提供 App 内购买项目</li>
# <span class="list-with-numbers__item__title"><span class="truncate-single-line truncate-single-line--block">PDF导出功能</span></span>
# <span class="list-with-numbers__item__price small-hide medium-show-tablecell">¥25.00</span>
