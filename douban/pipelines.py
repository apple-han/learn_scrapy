# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from douban.config import from_object
from douban import settings


class DoubanPipeline(object):
    def process_item(self, item, spider):
        return item

import MySQLdb

class MysqlPipeline(object):
    middle = from_object(settings)
    def __init__(self):
        self.conn = MySQLdb.connect(self.middle["host"], self.middle["user"],  self.middle["password"], self.middle["db_name"], charset=self.middle["charset"], use_unicode = True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = '''
                INSERT INTO movie(rate, title, cover, playable)
                VALUE(%s, %s, %s, %s)
            '''
        self.cursor.execute(insert_sql, (item["rate"],item["title"],item["cover"],item["playable"]))

        self.conn.commit()
