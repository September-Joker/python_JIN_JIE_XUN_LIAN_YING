import requests
from lxml import etree

url='https://movie.douban.com/subject/1292052/'

user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

header={'user-agent':user_agent}

response=requests.get(url,headers=header)

selector=etree.HTML(response.text)

film_name=selector.xpath('//*[@id="content"]/h1/span[1]/text()')
plan_date=selector.xpath('//*[@id="info"]/span[10]/text()')
rating=selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')

my_info = [film_name,plan_date,rating]

import pandas as pd

movie1=pd.DataFrame(my_info)

movie1.to_csv('./movie1.csv',encoding='utf8',index=False,header=False)