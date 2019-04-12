# -*- coding: utf-8 -*-
import scrapy

from movie.items import MovieItem
 
class MeijuSpider(scrapy.Spider):
    name = "meiju"
    allowed_domains = ["youtube.com"]
    start_urls = ['https://m.youtube.com/watch?v=2qAgE7fzXGs']
 
    def parse(self, response):
        # html=response.xpath('//html').extract()[0]
        # print(html)
        jsonObj = response.xpath('//div[@id="initial-data"]').extract()[0]
        jsonObj= jsonObj.replace('<div id="initial-data"><!--','');
        jsonObj= jsonObj.replace('--></div>','');
        print('jsonObj:'+jsonObj)
     # with open("my_meiju.html",'w') as fp:
        #     fp.write(html)
        # movies = response.xpath('//div[@class="slim-video-metadata-header"]')
        # title = response.xpath('//meta[@itemprop="name"]/@content').extract()[0]
        # view_count = response.xpath('//meta[@itemprop="interactionCount"]/@content').extract()[0]
        # like_count = response.xpath('//button[@title="I like this"]//span[@class="yt-uix-button-content"]/text()').extract()[0]
        # dislike_count = response.xpath('//button[@title="I dislike this"]//span[@class="yt-uix-button-content"]/text()').extract()[0]
        # print('title:'+title)
        # print('view count:'+view_count)
        # print("like_count:"+like_count)
        # print("dislike_count:"+dislike_count)
        # for each_movie in movies:
        #     item = MovieItem()
        #     #  print(each_movie)
        #     item['name'] = each_movie.xpath('./h5/a/@title').extract()[0]
        #     print(item['name'])
        # yield item