import scrapy
from bs4 import BeautifulSoup as bs
from scrapy_spiders.items import ScrapySpidersItem
from scrapy.selector import Selector


class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/top250']

    # 注释默认的parse功能
    # def parse(self, response):
    #     pass

    # 爬虫启动时，引擎自动调用该方法，并且只会被调用一次，用于生成初始的请求对象(Request)
    # start_requests()方法读取start_urls列表中的URL并生成Request对象，发送给引擎。
    # 引擎再指挥其他组件向网站服务器发送请求，下载网页
    def start_requests(self):
        for i in range(10):
            url = f'https://movie.douban.com/top250?start={i*25}&filter='
            yield scrapy.Request(url=url, callback=self.parse)
            # url 请求访问的网址
            # callback 回调函数，引擎会将下载好的界面(Request对象)发给该方法，执行数据解析
            # 这里可以使用callback指定新的函数，不是用parse作为默认的回调参数

    # 解析函数

    def parse(self, response):
        # items = []
        soup = bs(response.text, 'html.parser')
        title_list = soup.find_all('div', {'class': 'hd'})
        for i in title_list:
            item = ScrapySpidersItem()
            title = i.find('a').find('span').text
            link = i.find('a').get('href')
            item['title'] = title
            item['link'] = link
            # items.append(item)
            yield scrapy.Request(
                url=link, meta={'item': item}, callback=self.parse2)
        # movies=Selector(response=response).xpath('//div[@class="opt mod"]/ol/li')
        # for movie in movies:
        #     link=movie.xpath('./span[@class="title"]/text')



    # 解析具体界面

    def parse2(self, response):
        item = response.meta['item']
        soup = bs(response.text, 'html.parser')
        content = soup.find(
            'div', {
                'class': 'related-info'}).get_text().strip()
        item['content'] = content
        yield item
