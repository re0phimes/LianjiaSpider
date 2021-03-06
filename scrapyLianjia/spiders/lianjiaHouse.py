# -*- coding: utf-8 -*-
import scrapy
from scrapyLianjia.items import ScrapylianjiaItem

class LianjiahouseSpider(scrapy.Spider):
    # 爬虫名称
    name = 'lianjiaHouse'
    # 作用范围
    allowed_domains = ['lianjia.com/']
    # 通过翻页形式的url范围
    url = 'https://bj.lianjia.com/chengjiao/'
    offset = 0
    # 起始url
    start_urls = [url + str(offset)]
    page = 1


    def parse(self, response):
        houses = response.css('ul.listContent li')
        for house in houses:
            item = ScrapylianjiaItem()
            item['Name'] = house.css('li div div.title a::text').extract_first().split()[0]
            item['Link'] = house.css('li a.img::attr(href)').extract_first()
            item['Price'] = house.css('div.totalPrice span::text').extract_first()
            item['Date'] = house.css('div.dealDate::text').extract_first()
            yield scrapy.Request(url=item['Link'], callback=self.parse_detail,dont_filter=True, meta={'item':item})

        if self.page < 5:
            self.page = self.page + 1
            print(self.page)
            nexturl = self.url + 'pg' + str(self.page)
            yield scrapy.Request(url=nexturl, callback=self.parse,dont_filter=True)

    def parse_detail(self, response):
        item = response.meta['item']
        item['Rooms'] = response.css('div.content ul li::text').extract_first()
        item['Areas'] = response.css('div.content ul li:nth-child(3)::text').extract_first()
        print(item['Name'])
        yield item
