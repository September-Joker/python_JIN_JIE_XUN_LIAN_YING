# 使用requests库获取豆瓣影评
# url=https://movie.douban.com/top250

import requests

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'

header = {'user-agent': user_agent}

myUrl = "https://movie.douban.com/top250"

response = requests.get(myUrl, headers=header)

print(response.text)
print(f"返回码：{response.status_code}")
