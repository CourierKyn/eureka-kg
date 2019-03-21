# -*- coding: utf-8 -*-
import scrapy


class CloudOfweekSpider(scrapy.Spider):
    name = 'cloud.ofweek'
    allowed_domains = ['cloud.ofweek.com']
    start_urls = ['http://cloud.ofweek.com/']

    def parse(self, response):
        pass
