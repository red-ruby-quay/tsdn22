import scrapy
import urllib.parse
import logging


class SpiderSpider(scrapy.Spider):
    name = 'marketplace_scrapper'

    def __init__(self, keyword=None, *args, **kwargs):
        super(SpiderSpider, self).__init__(*args, **kwargs)
        self.keyword = urllib.parse.quote_plus(keyword)
        self.allowed_domains = ['www.tokopedia.com', 'ta.tokopedia.com']
        self.start_urls = [f'https://www.tokopedia.com/search?st=product&q={self.keyword}&srp_component_id=01.07.00.00&srp_page_id=&srp_page_title=&navsource=']

    def parse(self, response):
        products = response.xpath("//div[@class='css-974ipl']").getall()
        # products = response.xpath("//a[@class=pcv3__info-content css-gwkf0u']").getall()
        for product in products:
            name = product.xpath(".//a/@title").extract_first()
            price = product.xpath(".//a/div/div[@class='prd_link-product-price css-1ksb19c']/text()").extract_first()
            print(name)
            print(price)

