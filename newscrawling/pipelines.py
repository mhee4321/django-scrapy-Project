# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3
import os
from scrapy.exporters import JsonItemExporter

class NewscrawlingPipeline:
    def __init__(self):
        self.file = open("my_news.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

        self.setupDBCon()
        self.createTables()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)

        self.storeInDB(item)
        return item

    def setupDBCon(self):
        self.con = sqlite3.connect(os.path.abspath('/Users/mhee4/cloud-project/db.sqlite3'))
        # 장고의 db파일로 변겅 
        
        self.cur = self.con.cursor()

    def createTables(self):
        self.cur.execute("DROP TABLE IF EXISTS news")

        self.cur.execute("CREATE TABLE IF NOT EXISTS news(id INTEGER PRIMARY KEY NOT NULL, title TEXT, company TEXT, content TEXT, saved_time TEXT)")

    def storeInDB(self, item):
        self.cur.execute("INSERT INTO news(title, company, content, saved_time) VALUES( ?, ?, ?, ? )", (
            item.get('title',''),
            item.get('company',''),
            item.get('content',''),
            item.get('saved_time','')
        ))
        self.con.commit()
