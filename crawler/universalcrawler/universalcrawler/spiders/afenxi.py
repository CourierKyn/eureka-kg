# -*- coding: utf-8 -*-
import scrapy


class AfenxiSpider(scrapy.Spider):
    name = 'afenxi'
    allowed_domains = ['afenxi.com']
    start_urls = ['http://afenxi.com/']

    def parse(self, response):
        pass
