# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouSpiderItem(scrapy.Item):
    
   title = scrapy.Field() 
   location = scrapy.Field()
   publish_time = scrapy.Field()
   company_name = scrapy.Field()
   money = scrapy.Field()
   experience = scrapy.Field()
   industry = scrapy.Field()

