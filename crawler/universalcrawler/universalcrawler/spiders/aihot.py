# -*- coding: utf-8 -*-
import scrapy


class AihotSpider(scrapy.Spider):
    name = 'aihot'
    allowed_domains = ['aihot.net']
    start_urls = ['http://aihot.net/']

    def parse(self, response):
        pass
