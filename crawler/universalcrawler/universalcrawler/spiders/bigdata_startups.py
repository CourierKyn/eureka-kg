# -*- coding: utf-8 -*-
import scrapy


class BigdataStartupsSpider(scrapy.Spider):
    name = 'bigdata-startups'
    allowed_domains = ['bigdata-startups.com']
    start_urls = ['http://bigdata-startups.com/']

    def parse(self, response):
        pass
