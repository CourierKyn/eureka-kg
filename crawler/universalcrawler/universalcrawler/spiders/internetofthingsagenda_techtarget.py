# -*- coding: utf-8 -*-
import scrapy


class InternetofthingsagendaTechtargetSpider(scrapy.Spider):
    name = 'internetofthingsagenda.techtarget'
    allowed_domains = ['internetofthingsagenda.techtarget.com']
    start_urls = ['http://internetofthingsagenda.techtarget.com/']

    def parse(self, response):
        pass
