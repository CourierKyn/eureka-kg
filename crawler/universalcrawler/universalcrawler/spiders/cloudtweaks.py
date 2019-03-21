# -*- coding: utf-8 -*-
import scrapy


class CloudtweaksSpider(scrapy.Spider):
    name = 'cloudtweaks'
    allowed_domains = ['cloudtweaks.com']
    start_urls = ['http://cloudtweaks.com/']

    def parse(self, response):
        pass
