# -*- coding: utf-8 -*-
import scrapy


class CloudcomputingNewsSpider(scrapy.Spider):
    name = 'cloudcomputing-news'
    allowed_domains = ['cloudcomputing-news.net']
    start_urls = ['http://cloudcomputing-news.net/']

    def parse(self, response):
        pass
