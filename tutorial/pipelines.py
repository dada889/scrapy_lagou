# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from sqlalchemy import create_engine
import pandas as pd

class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item


class ProxyPipeline(object):

    def __init__(self, host, dbname, user, passwd, table):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.passwd = passwd
        self.table = table

    @classmethod
    def from_crawler(cls, crawler):
        return cls(host=crawler.settings.get('MYSQL_HOST'),
                   dbname=crawler.settings.get('MYSQL_DBNAME'),
                   user=crawler.settings.get('MYSQL_USER'),
                   passwd=crawler.settings.get('MYSQL_PASSWD'),
                   table=crawler.settings.get('MYSQL_TABLE')
                   )

    def open_spider(self, spider):
        mysql_config = "mysql://%s:%s@%s/%s?charset=utf8" % \
                      (self.user, self.passwd, self.host, self.dbname)
        self.engine = create_engine(mysql_config, encoding='utf8', pool_recycle=3306)
        self.conn = self.engine.connect()

    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, item, spider):
        df = pd.DataFrame(item['ip_table'])
        df.to_sql(self.table, self.engine, flavor='mysql', index=False, if_exists='append', chunksize=10)
        return df


