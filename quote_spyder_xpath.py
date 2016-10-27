"""
Example code inspired in scrpay tutorial powered by Elias Dorneles
http://pythonclub.com.br/material-do-tutorial-web-scraping-na-nuvem.html

"""

import scrapy



class QuoteSpiderXpath(scrapy.Spider):
    name = "quotes-xpath"
    start_urls = ("http://spidyquotes.herokuapp.com/tableful/",)
    download_delay = 1.5

    def parse(self, response):
        quotes = response.xpath('//tr[./following-sibling::tr[1]/td[starts-with(., "Tags:")]]')
        for quote in quotes:
            text, author = quote.xpath('normalize-space(.)').re('(.+) Author: (.+)')
            tags = quote.xpath('./following-sibling::tr[1]//a/text()').extract()

            yield {'author': author, 'text': text, 'tags': tags}

        next_url = response.xpath('//a[contains(., "Next")]/@href').extract_first()
        yield scrapy.Request(url=response.urljoin(next_url))
