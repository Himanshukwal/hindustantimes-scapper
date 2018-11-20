import scrapy
import csv

class HtSpider(scrapy.Spider):
    name = "htimes"

    def start_requests(self):
        urls = [
            'https://www.hindustantimes.com/',
        ]
        
        yield scrapy.Request(url=urls[0], callback=self.parse)

    def parse(self, response):
        print(response.xpath('//a'))

        selector = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "trc_ellipsis", " " ))] | //*[contains(concat( " ", @class, " " ), concat( " ", "clearfix", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "para-txt", " " ))]//a | //*[contains(concat( " ", @class, " " ), concat( " ", "random-heading", " " ))]//a | //*[contains(concat( " ", @class, " " ), concat( " ", "headingfive", " " ))]//a | //*[contains(concat( " ", @class, " " ), concat( " ", "headingfour", " " ))]//a | //*[contains(concat( " ", @class, " " ), concat( " ", "top-thumb-rgt", " " ))]//a | //*[contains(concat( " ", @class, " " ), concat( " ", "subhead4", " " ))]//a')

        #list of all the headlines
        hlines = [i.xpath('text()').extract() for i in selector if len(i.xpath('text()').extract())!=0 ]

        print(hlines)
        with open('headlines.csv','w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(hlines)

        csvfile.close()


        self.log('Done')