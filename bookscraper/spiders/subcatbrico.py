import scrapy
from bookscraper.spider_functions import get_random_user_agent
import csv

class BricospiderSpider(scrapy.Spider):
    name = "bricospider2"
    # start_urls = ["https://www.jardiland.com"]
    start_urls = ["https://www.jardiland.com"]

    def parse(self, response):

        for start_url in self.start_urls:
            yield scrapy.Request(
                url=start_url,
                headers=get_random_user_agent(),
                callback=self.parse_subcat,
            )
    def parse_subcat(self, response):
        with open("../bricospider.csv", newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
            




    # print("############################coucou#####################""")
    # def parse_category(self, response):
    #     print("############################salut#####################""")
       
    #     categories = response.css("a.ens-main-navigation-items__link.ds-ens-anchor.ds-ens-anchor--link.ens-main-navigation-items__link")
    #     for categorie in categories:
    #         #print(categorie.css(".ens-main-navigation-items__link-label::text").get())

    #         yield{
    #         "titre_categorie":categorie.css(".ens-main-navigation-items__link-label::text").get(),
    #         "url_categorie":"https://www.jardiland.com"+categorie.attrib['href']
    #     }
    #         pass

