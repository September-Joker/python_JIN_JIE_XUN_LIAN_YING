# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs

myurl='https://movie.douban.com/top250'

user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

header={'user-agent':user_agent}

response=requests.get(myurl,headers=header)

bs_info=bs(response.text,'html.parser')

for tags in bs_info.find_all('div',attrs={'class':'hd'}):
    for atag in tags.find_all('a'):
        # 获取所有链接
        print(atag.get('href'))
        # 获取所有电影名字
        print(atag.find('span').text)
