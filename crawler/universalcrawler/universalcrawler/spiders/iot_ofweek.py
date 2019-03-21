# -*- coding: utf-8 -*-
import scrapy


class IotOfweekSpider(scrapy.Spider):
    name = 'iot.ofweek'
    allowed_domains = ['iot.ofweek.com']
    start_urls = ['http://iot.ofweek.com/']

    def parse(self, response):
        pass
