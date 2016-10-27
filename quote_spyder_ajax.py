""""
Example code inspired in scrpay tutorial powered by Elias Dorneles
http://pythonclub.com.br/material-do-tutorial-web-scraping-na-nuvem.html

"""

import scrapy
import json




class QuoteSpiderAjax(scrapy.Spider):
    name = "quotes-ajax"
    quote_urls = "http://spidyquotes.herokuapp.com/api/quotes?page={}"
    start_urls = (quote_urls.format(1), )
    download_delay = 1.5

    def parse(self, response):
        data = json.loads(response.text)
        for d in data.get('quotes'):
            yield {'author': d['author']['name'],
                   'text': d['text'],
                   'tags': d['tags']
            }

        if 'has_next' in data and data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(self.quote_urls.format(next_page))
