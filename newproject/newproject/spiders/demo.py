import scrapy
import csv

class DemoSpider(scrapy.Spider):
    name = "demo"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        filename = 'quotes.csv'
        with open(filename,'a',encoding='utf-8') as quote_file:
            fieldnames = ['quote', 'author', 'tags']
            quote_writer = csv.DictWriter(quote_file,fieldnames=fieldnames)
            quote_writer.writeheader()
            for quote in response.css('div.quote'):
                text= quote.css('span.text::text').get()
                author= quote.css('small.author::text').get()
                tags= quote.css('div.tags a.tag::text').getall()
                print(text)

                quote_writer.writerow({'quote':text,'author':author,'tags':tags})
        next_page = response.css('li.next a::attr(href)').get()
        # # print(next_page)
        if next_page is not None:
            return response.follow(next_page,callback=self.parse)
    
  

