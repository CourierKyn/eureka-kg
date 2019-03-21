# -*- coding: utf-8 -*-
import scrapy


class TheinternetofthingsSpider(scrapy.Spider):
    name = 'theinternetofthings'
    allowed_domains = ['theinternetofthings.eu']
    start_urls = ['http://theinternetofthings.eu/']

    def parse(self, response):
        pass
