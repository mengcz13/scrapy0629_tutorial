import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
	name="dmoz"
	allowed_domains=["dmoz.org"]
	start_urls=["http://www.dmoz.org/Society/Law/Legal_Information/Computer_and_Technology_Law/Internet/"]
	
	def parse(self,response):
		for sel in response.xpath('//ul/li'):
			item=DmozItem()
			item['title']=sel.xpath('a/text()').extract()
			item['link']=sel.xpath('a/@href').extract()
			item['desc']=sel.xpath('text()').extract()
			yield item
			
		next_page = response.css("ul.navigation > li.next-page > a::attr('href')")
		if next_page:
			url = response.urljoin(next_page[0].extract())
			yield Request(url, self.parse_articles_follow_next_page)