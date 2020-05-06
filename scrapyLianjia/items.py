# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapylianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Areas = scrapy.Field()
    Rooms = scrapy.Field()
    Price = scrapy.Field()
    Link = scrapy.Field()
    Location = scrapy.Field()
    Date = scrapy.Field()
    pass
