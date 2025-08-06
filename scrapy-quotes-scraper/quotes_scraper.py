import scrapy

class QuotesScraperSpider(scrapy.Spider):
    name = "quotes-scraper"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            tags = quote.css('div.tags a.tag::text').getall()
            yield {
                'text': text,
                'author': author,
                'tags': tags
            }

        # Make sure this is NOT inside the loop
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
