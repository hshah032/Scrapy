# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['www.quotes.toscrape.com']
    start_urls = ['http://www.quotes.toscrape.com/']

    def parse(self, response):
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = resposne.xpath('//*[@class = "tag-item"]/a/text()').extract()

        yield {'H1 Tag': h1_tag, 'Tags':tags}

