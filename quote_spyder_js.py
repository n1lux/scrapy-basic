"""
Example code inspired in scrpay tutorial powered by Elias Dorneles
http://pythonclub.com.br/material-do-tutorial-web-scraping-na-nuvem.html

"""

import scrapy
import js2xml



class QuoteSpiderJs(scrapy.Spider):
    name = "quote-js"
    start_urls = ("http://spidyquotes.herokuapp.com/js/", )
    download_delay = 1.5


    def parse(self, response):
       script = response.xpath('//script[contains(., "var data =")]/text()').extract_first()
       sel = scrapy.Selector(root=js2xml.parse(script))
       quotes = sel.xpath('//var[@name="data"]/array/object')

       for quote in quotes:
           tags = quote.xpath('./property[@name="tags"]//string/text()').extract()
           author = quote.xpath('string(./property[@name="author"]//property[@name="name"]//string/text())').extract_first()
           text = quote.xpath('string(./property[@name="text"]//string/text())').extract_first()

           yield {'author': author, 'text': text, 'tags': tags}

       next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
       if next_url:
           yield scrapy.Request(url=response.urljoin(next_url))
