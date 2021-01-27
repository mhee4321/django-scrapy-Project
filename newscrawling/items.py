# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewscrawlingItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()
    company = scrapy.Field()
    saved_time = scrapy.Field()
