# -*- coding: utf-8 -*-
import scrapy


class PlanetbigdataSpider(scrapy.Spider):
    name = 'planetbigdata'
    allowed_domains = ['planetbigdata.com']
    start_urls = ['http://planetbigdata.com/']

    def parse(self, response):
        pass
