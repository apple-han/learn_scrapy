# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy import Request
from urllib import parse

from douban.items import DoubanItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com/explore']
    start_urls = ['https://movie.douban.com/j/search_subjects?'
                  'type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&'
                  'page_limit=20&page_start=0']
    origin_num = 0

    def parse(self, response):
        yield Request(url=parse.urljoin(response.url, self.start_urls[0]), callback=self.parse_detail, dont_filter=True)

    def parse_detail(self, response):

        movie_rank = DoubanItem()
        result = response.text
        items = json.loads(result).get("subjects", "")

        if items:
            self.origin_num = self.origin_num + 1
            url = '/j/search_subjects?'\
                  'type=movie&tag=热门&sort=recommend&'\
                  'page_limit=20&page_start={0}'

            next_url = url.format(self.origin_num*20)

            for item in items:
                rate = item.get("rate", "")
                title = item.get("title", "")
                url = item.get("url", "")
                playable = item.get("playable", "")

                movie_rank["rate"] = rate
                movie_rank["title"] = title
                movie_rank["cover"] = url
                movie_rank["playable"] = playable

                yield movie_rank

            yield Request(url=parse.urljoin(response.url, next_url), dont_filter=True, callback=self.parse_detail)
