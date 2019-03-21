# -*- coding: utf-8 -*-
import scrapy


class AitopicsSpider(scrapy.Spider):
    name = 'aitopics'
    allowed_domains = ['aitopics.org']
    start_urls = ['http://aitopics.org/']

    def parse(self, response):
        pass
