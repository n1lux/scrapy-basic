"""
Example code inspired in scrpay tutorial powered by Elias Dorneles
http://pythonclub.com.br/material-do-tutorial-web-scraping-na-nuvem.html

"""

import scrapy
from extruct.w3cmicrodata import LxmlMicrodataExtractor



class QuoteSpyderMicrodata(scrapy.Spider):
    name = "quotes-microdata"
    start_urls = ('http://spidyquotes.herokuapp.com/',)
    download_delay = 1.5

    def parse(self, response):
        extractor = LxmlMicrodataExtractor()
        items = extractor.extract(response.body_as_unicode(), response.url)['items']

        for item in items:
            yield item['properties']

        next_url = response.css('li.next a::attr("href")').extract_first()
        if next_url:
            yield scrapy.Request(response.urljoin(next_url))
