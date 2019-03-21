# -*- coding: utf-8 -*-
import scrapy


class ArtificialintelligenceNewsSpider(scrapy.Spider):
    name = 'artificialintelligence-news'
    allowed_domains = ['artificialintelligence-news.com']
    start_urls = ['http://artificialintelligence-news.com/']

    def parse(self, response):
        pass
