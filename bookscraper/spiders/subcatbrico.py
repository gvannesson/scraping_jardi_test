import scrapy
from bookscraper.spider_functions import get_random_user_agent
import csv
from scrapy import Request
from bookscraper.items import ProductItem
from bookscraper.pipelines import BookscraperPipeline

class BricospiderSpider(scrapy.Spider):
    name = "bricospider3"
    # start_urls = ["https://www.jardiland.com"]
    # start_urls = ["https://www.jardiland.com/c/conservation-des-aliments"]
    with open("/home/addeche/Documents/Projets Python/Projet scraping/bookscraper/bookscraper/spiders/jardi_test10.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        start_urls=[]
        for row in reader:
            if row['is_page_list'] == "True":
                start_urls.append(row["url_categorie"])

    # def start(self):
    #     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #     request = Request(url=self.start_urls, callback=self.parse)
    #     print("___________________________")
    #     yield request


    def parse(self, response):
        print("hello############################")
        for start_url in self.start_urls:
            yield scrapy.Request(
                url=start_url,
                headers=get_random_user_agent(),
                callback=self.parse_product,
            )


    def parse_product(self,response):
        print("############################hello#####################")
        produits = response.css('a.ens-product-list__link')
        product_number = response.css(".ens-product-list-template__products-counter span ::text").get()
        number = int(str(product_number.split()[-1]))//50
        for produit in produits:
            product_item = ProductItem()

            product_item["title"] = produit.css('article h2 ::text').get(),
            product_item["price"] = produit.css('.ds-ens-pricing__price-amount--xxl.ds-ens-pricing__price-amount--l.ds-ens-pricing__price-amount--bold::text').get(),
            product_item["marque"] = produit.css('.ds-ens-product-card__brand ::text').get(),
            # product_item["nombre_consommateur"] = produit.css(' .idf-rating__label::text').get(),
            # product_item["nbre_rater"] = produit.css('.ds-ens-product-card__rating span:nth-child(2)::text').get(),
            product_item["src"] = produit.css("a.ens-product-list__link").attrib['href']

            yield product_item
        


            # yield{
            #     "title" : produit.css('article h2 ::text').get(),
            #     "price" : produit.css('.ds-ens-pricing__price-amount--xxl.ds-ens-pricing__price-amount--l.ds-ens-pricing__price-amount--bold::text').get(),
            #     "marque" : produit.css('.ds-ens-product-card__brand ::text').get(),
            #     "nombre_cnosommateur" : produit.css(' .idf-rating__label::text').get(),
            #     "nbre_rater" : produit.css('.ds-ens-product-card__rating span:nth-child(2)::text').get(),
            #     "src" : produit.css('.ds-ens-product-card__visual.idf-image.ds-ens-product-card__visual').attrib['src']
            #     }
        for i in range(number):
            url_des_produits_scrapes = response.url
            print(f"mon url de produits scrapés     {url_des_produits_scrapes}")
            if "?" in url_des_produits_scrapes:
                text = response.url
                head, sep, tail= text.partition("?")
                print("OOOOOOOOOOOOOOOOOOKKKKKKKKKKKKKK")
                url_des_produits_scrapes = head
                print(f"mon url de produits scrapés après    {url_des_produits_scrapes}")
                next_page_url = url_des_produits_scrapes +f"?p={i+2}"
                yield response.follow(next_page_url, callback = self.parse_product)

            else:
                next_page_url = url_des_produits_scrapes +f"?p={i+2}"
                print(f"la prochaine url scrapée sera {next_page_url}")
                    # if 'catalogue/' in next_page:
                    #     next_page_url = "https://books.toscrape.com/" + next_page
                    # else:
                    #     next_page_url = "https://books.toscrape.com/catalogue/" + next_page
                yield response.follow(next_page_url, callback = self.parse_product)

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

