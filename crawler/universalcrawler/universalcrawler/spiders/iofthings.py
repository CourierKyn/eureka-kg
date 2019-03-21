# -*- coding: utf-8 -*-
import scrapy


class IofthingsSpider(scrapy.Spider):
    name = 'iofthings'
    allowed_domains = ['iofthings.org']
    start_urls = ['http://iofthings.org/']

    def parse(self, response):
        pass
