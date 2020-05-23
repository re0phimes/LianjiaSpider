# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd

class ScrapylianjiaPipeline:
    count = 0
    DF = pd.DataFrame(columns=['Name','Price','Areas','Rooms','Link','Date'])
    def process_item(self, item, spider):
        self.count = self.count + 1
        aItem = pd.Series([item['Name'],item['Price'],item['Areas'],item['Rooms'],item['Link'],item['Date']], index=['Name','Price','Areas','Rooms','Link','Date'])
        self.DF.append(aItem,ignore_index=True)
        return item
    print(DF)

