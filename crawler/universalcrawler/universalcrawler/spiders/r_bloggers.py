# -*- coding: utf-8 -*-
import scrapy


class RBloggersSpider(scrapy.Spider):
    name = 'r-bloggers'
    allowed_domains = ['r-bloggers.com']
    start_urls = ['http://r-bloggers.com/']

    def parse(self, response):
        pass
