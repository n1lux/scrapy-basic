"""
Example code inspired in scrpay tutorial powered by Elias Dorneles
http://pythonclub.com.br/material-do-tutorial-web-scraping-na-nuvem.html

"""

import scrapy



class QuoteSpider(scrapy.Spider):
    name = 'quotespider'
    start_urls = ("http://spidyquotes.herokuapp.com/",)
    download_delay = 1.5

    def parse(self, response):
        for sel in response.css('.quote'):
            yield {
                'text': sel.css('span::text').extract_first(),
                'author': sel.css('small::text').extract_first(),
                'tags': sel.css('.tags a::text').extract(),
            }

        next_url = response.css('li.next a::attr("href")').extract_first()
        if next_url:
            yield scrapy.Request(url=response.urljoin(next_url))

