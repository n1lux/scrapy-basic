"""
Example code inspired in scrpay tutorial powered by Elias Dorneles
http://pythonclub.com.br/material-do-tutorial-web-scraping-na-nuvem.html

"""


import scrapy


class SimpleSpyder(scrapy.Spider):
    name = 'simplespider'
    start_urls = ('http://example.com',)

    def parse(self, response):
        self.log('Entering site: {}'.format(response.url))
        yield {'url': response.url, 'length': len(response.body)}


        next_url = 'http://www.google.com.br'
        self.log('Now will get this new url {}'.format(next_url))
        yield scrapy.Request(url=next_url, callback=self.handle_new)


    def handle_new(self, response):
         self.log('Entering site: {}'.format(response.url))

