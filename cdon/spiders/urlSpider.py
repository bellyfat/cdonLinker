# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class UrlspiderSpider(CrawlSpider):
    name = 'urlSpider'
    allowed_domains = ['cdon.se']
    start_urls = (
        "http://cdon.se/",
    )

    rules = (Rule(LinkExtractor(allow=('merchant')), callback='parse_page', follow=True),)

    def parse_page(self, response):
        yield {'URL': response.url}
