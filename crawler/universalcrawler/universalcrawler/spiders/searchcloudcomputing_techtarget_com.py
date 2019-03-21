# -*- coding: utf-8 -*-
import scrapy


class SearchcloudcomputingTechtargetComSpider(scrapy.Spider):
    name = 'searchcloudcomputing.techtarget.com'
    allowed_domains = ['searchcloudcomputing.techtarget.com']
    start_urls = ['http://searchcloudcomputing.techtarget.com/']

    def parse(self, response):
        pass
