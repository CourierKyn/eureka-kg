# -*- coding: utf-8 -*-
import scrapy


class HibtcSpider(scrapy.Spider):
    name = 'hibtc'
    allowed_domains = ['hibtc.org']
    start_urls = ['http://hibtc.org/']

    def parse(self, response):
        pass
