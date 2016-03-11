import scrapy

#This is a scrapy spider

class FirstSpider(scrapy.Spider):
    name = 'FirstSpider'
    allowed_domains = ["163.com"]
    start_urls = ['http://www.163.com']

    def parse(self, response):
        print response.body
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)

