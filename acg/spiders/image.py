#coding=utf-8
#update at 2018-4-20
from http.client import IncompleteRead
from acg.items import ImageItem
import scrapy
import numpy as np
import os
import re

class acgimages(scrapy.Spider):
	"""docstring for acgimages"""
	name = 'images'
	start_urls = [
		#"https://www.pixiv.net/search.php?word=%E8%83%8C%E6%99%AF%20users%E5%85%A5%E3%82%8A&order=date_d&p=1"
		"https://acg12.com/category/pixiv"
	]
	page = 1
	count = 0
	#抓取多少页的数据
	MAX_CATCH_PAGES = 100
	item = ImageItem()
	def parse(self,response):
		
		#imgs = response.xpath('//a[@class="PKslhVT"]//div/@style').re(r'https://i.pximg.net/c/240x240/img-master/img/.+\.jpg')
		#imgs = response.xpath('//a[@class="inn-archive__item__thumbnail__container inn-card_painting__item__thumbnail__container inn-card__thumbnail__container inn-card__thumbnail__container_painting"]//img/@src').re(r'https://static.acg12.com/uploads/.+\.jpg')
		#aaa = re.findall(r'src="(.*?\.jpg)"',response.body.read())
		 
		#print(response.xpath('//article//div//a//img').re(r'data-src="(.*?\.jpg)"'))
		imgs = response.xpath('//article//div//a//img').re(r'data-src="(.*?\.jpg)"')
		usedImgs = []
		for img in imgs:
			if img not in usedImgs:
				usedImgs.append(img)
 
		print(usedImgs)
		self.item['url'] = "https://acg12.com/category/pixiv/page/%d" % self.page
		#self.item['url'] = "https://www.pixiv.net/search.php?word=%E8%83%8C%E6%99%AF%20users%E5%85%A5%E3%82%8A&order=date_d&p=%d" % self.page
		self.item['images'] = usedImgs
		yield self.item
		
		if self.page < self.MAX_CATCH_PAGES:
			self.page = self.page + 1
		next_url = "https://acg12.com/category/pixiv/page/%d" % self.page
		#next_url = "https://www.pixiv.net/search.php?word=%E8%83%8C%E6%99%AF%20users%E5%85%A5%E3%82%8A&order=date_d&p==%d" % self.page
		yield scrapy.Request(next_url, callback = self.parse)
