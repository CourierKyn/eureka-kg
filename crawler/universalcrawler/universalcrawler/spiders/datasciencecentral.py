# -*- coding: utf-8 -*-
import scrapy


class DatasciencecentralSpider(scrapy.Spider):
    name = 'datasciencecentral'
    allowed_domains = ['datasciencecentral.com']
    start_urls = ['http://datasciencecentral.com/']

    def parse(self, response):
        pass
