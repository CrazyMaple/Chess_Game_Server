from scrapy import Request
from scrapy.spiders import Spider
from myspider.items import DoubanReviewBestItem


class DoubanReviewBestSpider(Spider):
    name = 'douban_review_best_spider'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/review/best/'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanReviewBestItem()
        movies = response.xpath('//div[@class="main review-item"]')
        for movie in movies:
            item['movie_name'] = movie.xpath(
                '/a/img/@title').extract()[0]
            item['player_name'] = movie.xpath(
                '/header/a[@class="name xh-highlight"]/text()').extract()[0]
            item['player_time'] = movie.xpath(
                '/header/span[@class="main-meta xh-highlight"]/text()'
                ).extract()[0]
            item['review_title'] = movie.xpath(
                '/div[@class="main-bd"]/h2/a/text()').extract()[0]
            # content_nodes = movie.xpath(
            #     '/div[@class="main-bd"]/div[1]/div[0]/div[0]/div
            # [@class="link-report"]/div[@class="review-content clearfix"]')
            content_str = "maple"
            # for node in content_nodes:
            #     content_str = content_str + movie.xpath(
            item['review_content'] = content_str
            item['review_endorsed'] = movie.xpath((
                '/div[@class="main-bd"]/div'
                '[@class="action"]/a[@class="action-btn up"]'
                '/span/text()')).extract()[0]
            item['review_negative'] = movie.xpath((
                '/div[@class="main-bd"]/div'
                '[@class="action"]/a[@class="action-btn down"]'
                '/span/text()')).extract()[0]
            item['review_reply'] = movie.xpath((
                '/div[@class="main-bd"]/div[@class="action"]'
                '/a[@class="reply"]/text()')).extract()[0]
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        print('Next Url Is %s' % (next_url))
        if next_url:
            next_url = 'https://movie.douban.com/review/best/' + next_url[0]
            yield Request(next_url, headers=self.headers)
