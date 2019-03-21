# -*- coding: utf-8 -*-
import scrapy


class AiOfweekSpider(scrapy.Spider):
    name = 'ai.ofweek'
    allowed_domains = ['ai.ofweek.com']
    start_urls = ['http://ai.ofweek.com/']

    def parse(self, response):
        pass
