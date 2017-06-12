# -*- coding: utf-8 -*-
import scrapy
from lagou_spider.items import LagouSpiderItem


class PythonSpiderSpider(scrapy.Spider):
    name = 'python_spider'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/Python/']

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse,
                    errback=self.errback,
                    dont_filter=True)


    def parse(self, response):
        for job in response.css('div.list_item_top'):
            item = LagouSpiderItem()
            item['title'] = job.css('div.position > div.p_top > a > h2::text').extract_first()
            item['location'] = job.css('div.position > div.p_top > a > span > em::text').extract_first()
            item['publish_time'] = job.css('div.position > div.p_top > span::text').extract_first()
            item['company_name'] = job.css('div.company > div.company_name > a::text').extract_first()
            item['money'] = job.css('div.position > div.p_bot > div > span::text').extract_first()
            item['experience'] = job.css('div.position > div.p_bot > div::text').extract_first()
            item['industry'] = job.css('div.company > div.industry::text').extract_first().strip()
            yield item

        next_page = response.css('div.item_con_pager > div > a:nth-last-child(1)::attr(href)').extract_first()
        if next_page is not None:
            #yield response.follow(next_page, self.parse)
            pass

    def errback(self, failure):
        pass
