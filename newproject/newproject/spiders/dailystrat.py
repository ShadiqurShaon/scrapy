# -*- coding: utf-8 -*-
import scrapy
import csv
import re

class MydomainSpider(scrapy.Spider):

    name = "dailystar"
    start_urls = [
        'https://www.thedailystar.net/'
       
    ]

    status = True

    def parse(self, response):
        with open('dailystar.csv','a',encoding='utf-8') as quote_file:
            fieldnames = ['news','category']
            quote_writer = csv.DictWriter(quote_file,fieldnames=fieldnames)

            if self.status == True:
                quote_writer.writeheader()
                self.status=False
                for link in response.css('ul.menu li a::attr(href)').getall():
                    if 'http://' not in link:
                        new_url = response.url+link[1:]
                        x=re.search("https://www.thedailystar.net/.[^/]*", new_url)
                        if x is not None:
                            self.start_urls.append(new_url)
            date = 
            for quote in response.css('div.four-25 h4 a::text,div.four-25 h3 a::text').getall():
                text = quote
                category= response.url.split("/")[-1]
                # tags= response.url
                print(category)
                quote_writer.writerow({'news':text,'category':category})
        # yield{"url":response.url}
        if len(self.start_urls)!= 0:
            url = self.start_urls.pop()
            print(url)
            if url is not None:
                return response.follow(url,callback=self.parse)
        
