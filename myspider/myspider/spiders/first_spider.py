from scrapy.spiders import Spider
import time


class BlogSpider(Spider):
    name = 'woodenrobot'
    start_urls = ['http://woodenrobot.me']

    def parse(self, response):
        titles = response.xpath(
            '//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            timestr = (str.format(
                    'client connect time i'
                    's %s' % time.strftime("%Y-%m-%d %X", time.localtime())))
            print('Time:%s get title:%s' % (timestr, title.strip()))