# -*- coding: utf-8 -*-
import scrapy


class ArtificialIntelligenceSpider(scrapy.Spider):
    name = 'artificial-intelligence'
    allowed_domains = ['artificial-intelligence.blog']
    start_urls = ['http://artificial-intelligence.blog/']

    def parse(self, response):
        pass
