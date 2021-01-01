import scrapy
class QuotesSpider(scrapy.Spider):
    name = "scrap_books"
    def start_requests(self):
        url='https://books.toscrape.com/catalogue/page-1.html'
        yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        for q in response.css("article.product_pod"):
            link=q.css("div.image_container a img ::attr(src)").get()
            title=q.css('h3 a::attr(title)').get()
            price=q.css('p.price_color::text').get()
            yield{ 'image_url':link, 'book_title':title, 'product_price':price,  }
        next_page=response.css('li.next a').attrib['href']
        if next is not None:
            yield response.follow(next_page, callback=self.parse)