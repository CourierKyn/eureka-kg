# -*- coding: utf-8 -*-
import scrapy


class StaceyoniotSpider(scrapy.Spider):
    name = 'staceyoniot'
    allowed_domains = ['staceyoniot.com']
    start_urls = ['http://staceyoniot.com/']

    def parse(self, response):
        pass
