from scrapy import Request
from scrapy.spiders import Spider
from myspider.items import DoubanReviewBestItem
from scrapy_splash import SplashRequest
import scrapy


class DoubanReviewBestSpider(Spider):
    name = 'douban_review_best_spider'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        # url = 'https://movie.douban.com/review/best/'
        # yield Request(url, headers=self.headers)
        urls = [
           'https://movie.douban.com/review/best/',
        ]

        for url in urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        item = DoubanReviewBestItem()
        sel = scrapy.Selector(response)
        print('what %s ' % (sel))
        movies = response.xpath('//div[@class="main review-item"]')
        for movie in movies:
            # maple1 = movie.xpath(
            #     './header/a').extract()
            # maple2 = movie.xpath(
            #     './header/a[@class="name"]').extract()
            # maple3 = movie.xpath(
            #     './header/a[@class="name"]/text()').extract()
            # print('Sb Is %s %s %s' % (maple1, maple2, maple3))
            item['movie_name'] = movie.xpath(
                './a/img/@title').extract()[0]
            item['player_name'] = movie.xpath(
                './header/a[@class="name"]/text()').extract()[0]
            item['player_time'] = movie.xpath(
                './header/span[@class="main-meta"]/text()'
                ).extract()[0]
            item['review_title'] = movie.xpath(
                './div[@class="main-bd"]/h2/a/text()').extract()[0]
            content_nodes = movie.xpath(#这里获取有问题，需要点击
                './/div[@class="link-report"]'
                '/div[@class="review-content clearfix"]/p')
            content_str = ''
            for index, node in enumerate(content_nodes):
                content_str = content_str + node.extract()[index]
            item['review_content'] = content_str
            item['review_endorsed'] = movie.xpath((
                './div[@class="main-bd"]/div'
                '[@class="action"]/a[@class="action-btn up"]'
                '/span/text()')).re(r'(\d+)')[0] + '有用'
            item['review_negative'] = movie.xpath((
                './div[@class="main-bd"]/div'
                '[@class="action"]/a[@class="action-btn down"]'
                '/span/text()')).re(r'(\d+)')[0] + '无用'
            item['review_reply'] = movie.xpath((
                './div[@class="main-bd"]/div[@class="action"]'
                '/a[@class="reply"]/text()')).re(r'(\d+)回应')[0] + '回应'
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        print('Next Url Is %s' % (next_url))
        if next_url:
            next_url = 'https://movie.douban.com' + next_url[0]
            yield Request(next_url, headers=self.headers)
