import requests
from bs4 import BeautifulSoup as bs
import random
import time


def get_url_name(my_url):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    header = {'user-agent': user_agent}
    response = requests.get(my_url, headers=header)

    bs_info = bs(response.text, 'html.parser')

    for tag in bs_info.find_all('div', {'class': 'hd'}):
        for atag in tag.find_all('a'):
            print(atag.get('href'))
            print(atag.find('span').text)


urls = tuple(
    f'https://movie.douban.com/top250?start={page * 25}&filter=' for page in range(10))

print(urls)

for page in urls:
    get_url_name(page)
    time.sleep(random.randint(1, 100) / 100)
