# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DmozItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()


class ProxyItem(scrapy.Item):
    ip_table = scrapy.Field()


class LagouMainItem(scrapy.Item):
    job_href = scrapy.Field()
    tj_id = scrapy.Field()
    tj_no = scrapy.Field()
    job_name = scrapy.Field()


class LagouItem(scrapy.Item):
    job_title = scrapy.Field()

    pass



