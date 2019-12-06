import scrapy
import csv

class DemoSpider(scrapy.Spider):
  
    name = "news"

    start_urls = [
        'https://www.thedailystar.net/',
    ]

    def parse(self, response):
        filename = 'news.csv'
        with open(filename,'a',encoding='utf-8') as quote_file:
            fieldnames = ['news', 'author', 'tags']
            quote_writer = csv.DictWriter(quote_file,fieldnames=fieldnames)
            quote_writer.writeheader()
            for quote in response.css('div.four-25 h4 a::text,div.four-25 h3 a::text').getall():
                text= quote
                author= "The Daily star"
                tags= "national"
                print(text)

                quote_writer.writerow({'news':text,'author':author,'tags':tags})
        next_page = response.css('li.next a::attr(href)').get()
        # print(next_page)
        if next_page is not None:
            return response.follow(next_page,callback=self.parse)
    
  

