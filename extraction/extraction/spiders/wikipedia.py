import scrapy
from ..items import ExtractionItem


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"]

    def parse(self, response):
        items = ExtractionItem()

        table = response.css('tr')

        for section in table:
            items["name"] = section.css('b a::text').get()
            items["tenure"] = section.css('td b + br + span::text').extract()
            items["party"] = section.css('th + td + td + td + td + td a::text').get()

            if items["name"] is None:
                pass
            else:
                yield items
        


