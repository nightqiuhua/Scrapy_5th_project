# -*- coding: utf-8 -*-
import scrapy
from Douyu.items import DouyuItem
import json

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    baseURL= 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    offset = 0
    start_urls = [baseURL + str(offset)]

    def parse(self, response):
        
        data_list = json.loads(response.body.decode(encoding='utf-8'))['data']
        if not len(data_list):
            return
        for data in data_list:
            item = DouyuItem()
            item['nickname'] = data['nickname']
            item['image_link'] = data['vertical_src']
            yield item

        self.offset += 20
        url = self.baseURL + str(self.offset)
        yield scrapy.Request(url,callback = self.parse)
