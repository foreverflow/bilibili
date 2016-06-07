# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
	
from scrapy.item import Item, Field

class BiliItem(Item):
    url        = Field()
    avNo       = Field()
    title      = Field()
    time       = Field()
    click      = Field()
    dm         = Field()
    coin       = Field()
    sc         = Field()
    category   = Field()
    comment    = Field()
    up         = Field()