import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NovelSpider(CrawlSpider):
    name = "novel"
    allowed_domains = ["books.toscrape.com"]

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"

    def start_requests(self):
        yield scrapy.Request(url="https://books.toscrape.com", headers={'user_agent':self.user_agent})

    rules = (Rule(LinkExtractor(restrict_xpaths=("//article[@class='product_pod']/h3/a")), callback="parse_item", follow=True, process_request='set_user_agent'),
             Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"))
             )
    
    def set_user_agent(self,request,spider):
        request.headers['user_agent'] = self.user_agent
        return request

    def parse_item(self, response):
        img_link = response.xpath("//div[@class='item active']//img/@src").get()
        yield{
            'title' : response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
            'price' : response.xpath("//div[@class='col-sm-6 product_main']/p[1]/text()").get(),
            'img_link': response.urljoin(img_link),
            #'img_link': response.xpath("//div[@class='item active']//img/@src").get(),
            'book_link' : response.url,
            'available_stock': response.xpath("normalize-space(//*[@id='content_inner']/article/div[1]/div[2]/p[2]/text()[2])").get()

        }

