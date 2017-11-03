# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JokeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
     author = scrapy.Field()
     sex = scrapy.Field()
     age = scrapy.Field()
     picture = scrapy.Field()
    #Parting line
     content = scrapy.Field()
     vote = scrapy.Field()
     comment = scrapy.Field()


