# -*- coding: utf-8 -*-
import scrapy


class EjiaokuaiSpider(scrapy.Spider):
    name = 'ejiaokuai'
    allowed_domains = ['ejiaokuai.com']
    start_urls = ['http://ejiaokuai.com/']

    def parse(self, response):
        pass
