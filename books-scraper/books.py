import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        for book in response.xpath("//article[@class='product_pod']"):
            yield {
                "title": book.xpath(".//h3/a/@title").get(),
                "price": book.xpath(".//p[@class='price_color']/text()").get(),
                "rating": book.xpath(".//p[contains(@class, 'star-rating')]/@class").get().split()[-1]
            }

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
