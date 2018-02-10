# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os 
from scrapy.pipelines.images import ImagesPipeline
#from settings import IMAGES_STORE as images_store
import scrapy 

class DouyuPipeline(ImagesPipeline):
    def get_media_requests(self,item,info):
        image_link = item['image_link']
        yield scrapy.Request(image_link)

    def item_completed(self,results,item,info):
        images_store = "D:\\exercise_data\\scrapy\\pic_scrapy\\Douyu\images\\"
        image_path = [x['path'] for ok,x in results if ok]
        os.rename(images_store + image_path[0],images_store + item['nickname']+'.jpg')
        return item

