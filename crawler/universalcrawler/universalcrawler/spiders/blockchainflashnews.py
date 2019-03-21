# -*- coding: utf-8 -*-
import scrapy


class BlockchainflashnewsSpider(scrapy.Spider):
    name = 'blockchainflashnews'
    allowed_domains = ['blockchainflashnews.com']
    start_urls = ['http://blockchainflashnews.com/']

    def parse(self, response):
        pass
