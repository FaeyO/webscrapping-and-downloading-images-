import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from library_books.items import LibraryBooksItem

#class ImagesToScrapeSpider(scrapy.Spider):
class ImagesToScrapeSpider(CrawlSpider):
    name = "image"
    allowed_domains = ["books.toscrape.com"]
    #start_urls = ["http://books.toscrape.com"]

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(url="https://books.toscrape.com", headers={'User-Agent':self.user_agent})

    rules = (Rule(LinkExtractor(restrict_xpaths=("//article[@class='product_pod']/h3/a")), callback="parse_item", follow=True),
             Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a") ,process_request='set_user_agent', follow=True)
             )
    def set_user_agent(self,request,spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self,response):
        for article in response.xpath("//article[@class='product_pod']"):
            loader = ItemLoader(item=LibraryBooksItem(), selector=article)
            relative_url = article.xpath(".//div[@class='image_container']/a/img/@src").get()
            absolute_url = response.urljoin(relative_url)
            loader.add_value('image_urls', absolute_url)
            loader.add_xpath('book_name', ".//h3/a/@title")
            yield loader.load_item()

    