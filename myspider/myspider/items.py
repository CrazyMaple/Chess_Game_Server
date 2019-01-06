# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 排名
    ranking = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    score_num = scrapy.Field()


class DoubanReviewBestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名称
    movie_name = scrapy.Field()
    # 影评玩家名字
    player_name = scrapy.Field()
    # 影评时间
    player_time = scrapy.Field()
    # 影评名称
    review_title = scrapy.Field()
    # 影评内容
    review_content = scrapy.Field()
    # 赞同
    review_endorsed = scrapy.Field()
    # 反对
    review_negative = scrapy.Field()
    # 回应
    review_reply = scrapy.Field()