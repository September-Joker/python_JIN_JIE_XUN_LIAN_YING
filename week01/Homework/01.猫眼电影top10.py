# 爬取猫眼电影的前十个电影名称，电影类型和上映时间，并以utf-8字符集保存到csv格式的文件中

import requests
from bs4 import BeautifulSoup as bs
import time
import random
# import logging


def get_url():
    link = []
    n = 1
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    myurl = 'https://maoyan.com/films?showType=3'
    header = {'user-agent': user_agent}
    response = requests.get(myurl, headers=header)
    print(response.status_code)
    bs_info = bs(response.text, 'html.parser')
    print(bs_info)
    for tags in bs_info.find_all(
            'div', attrs={'class': 'movie-item-hover'}):
        for atag in tags.find_all('a'):
            if n > 10:
                return link
            # print(atag.get('href'))
            else:
                film_link = 'maoyan.com' + str(atag.get('href'))
                link.append(film_link)
                n += 1

# link=get_url()
# print(link)


def get_film_info(url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    # myurl = 'https://maoyan.com/films?showType=3'
    header = {'user-agent': user_agent}
    response = requests.get(url, headers=header)
    # print(response.text)
    bs_info = bs(response.text, 'html.parser')
    # print(bs_info)
    film_name = bs_info.find('h1', attrs={'class': 'name'}).text
    # film_name = bs_info.find_all('h1', {'class': 'name'})
    print(film_name)
    film_type = bs_info.find('li', attrs={'class': 'ellipsis'}).text
    print(film_type)


link = get_url()
print(link)
for i in link:
    print(i)
    get_film_info(i)
    time.sleep(random.randint(1, 100) / 1000)
