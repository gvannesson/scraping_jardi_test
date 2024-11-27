import scrapy
from bookscraper.spider_functions import get_random_user_agent

class BricospiderSpider(scrapy.Spider):
    name = "bricospider"
    # start_urls = ["https://www.jardiland.com"]
    start_urls = ["https://www.jardiland.com"]

    def parse(self, response):

        for start_url in self.start_urls:
            yield scrapy.Request(
                url=start_url,
                headers=get_random_user_agent(),
                callback=self.parse_category,
            )

    
    # def parse_page_list(self, response):
    #     print("############################bonjour#####################""")
    #     print("############################bonjour#####################""")
    #     print("############################bonjour#####################""")
    #     print("############################bonjour#####################""")
    #     print("############################bonjour#####################""")


    #     sacs_croquettes = response.css('a.ens-product-list__link')
    #     print(f"----------------------------{sacs_croquettes}")

    #     sac = sacs_croquettes[0]

    #     title = sac.css('article h2 ::text').get()
    #     price = sac.css('.ds-ens-pricing__price-amount--xxl.ds-ens-pricing__price-amount--l.ds-ens-pricing__price-amount--bold::text').get()
    #     marque = sac.css('.ds-ens-product-card__brand ::text').get()
    #     nombre_cnosommateur = sac.css(' .idf-rating__label::text').get()
    #     nbre_rater = sac.css('.ds-ens-product-card__rating span:nth-child(2)::text').get()
    #     src = sac.css('.ds-ens-product-card__visual.idf-image.ds-ens-product-card__visual').attrib['src']
    #     print(title)
    #     print(price)
    #     print(marque)
    #     print(nombre_cnosommateur)
    #     print(nbre_rater)
    #     print(src)


    print("############################coucou#####################""")
    def parse_category(self, response):
        print("############################salut#####################""")
        # category = response.css('a.ens-main-navigation-items__link.ds-ens-anchor.ds-ens-anchor--link.ens-main-navigation-items__link')
        # print(f"----------------------------{category}")
        # animalerie = category[1].attrib['href']
        # animalerie_url = "https://www.jardiland.com" + animalerie
        # print(animalerie_url)
        categories = response.css("a.ens-main-navigation-items__link.ds-ens-anchor.ds-ens-anchor--link.ens-main-navigation-items__link")
        for categorie in categories:

            #print(categorie.css(".ens-main-navigation-items__link-label::text").get())
            next_url="https://www.jardiland.com"+categorie.attrib['href']
            if "collection-noel" in next_url:
                continue
            yield{
            "titre_categorie":categorie.css(".ens-main-navigation-items__link-label::text").get(),
            "url_categorie":"https://www.jardiland.com"+categorie.attrib['href'],
            "is_page_list":0
        
            
        }
            yield response.follow(
                url=next_url,
                callback=self.parse_subcategorie
                

            )
            break

    def parse_subcategorie(self, response):
        print("############################hello#####################""")
        sub_categories = response.css('a.ens-product-list-categories__item')


        for sub_categorie in sub_categories:
            next_url="https://www.jardiland.com"+sub_categorie.attrib['href']
            yield{
            "titre_subcategorie":sub_categorie.css("::text").get(),
            "url_categorie":"https://www.jardiland.com"+sub_categorie.attrib['href'],
            "is_page_list": 0 if response.follow(url=next_url, callback=self.parse_subcategorie)==[]else 1

            
            }

            yield response.follow(
                url=next_url,
                callback=self.parse_subcategorie
            )

            break


            # sub_cat_title = response.css('a.ens-product-list-categories__item ::text')
            # print(sub_cat_title)
            # sub_category_1 = sub_categories[1].attrib['href']

            # title = sub_category.css('article h2 ::text').get()
            # try:
            #     response.css('a.ens-product-list-categories__item')
            #     "is_page_list":0
            # except:
            #    "is_page_list":1

        print("")






        # animalerie = categorie[0].css(".ens-main-navigation-items__link-label::text").get()
        # print(animalerie)
        
        #print(categorie[0].attrib["href"])
        

    # def parse_product(self,response):
    #     print("############################hello#####################""")
    #     produits = response.css('a.ens-product-list__link')
    #     produit = produits[0]

    #     title = produit.css('article h2 ::text').get()
    #     price = produit.css('.ds-ens-pricing__price-amount--xxl.ds-ens-pricing__price-amount--l.ds-ens-pricing__price-amount--bold::text').get()
    #     marque = produit.css('.ds-ens-product-card__brand ::text').get()
    #     nombre_cnosommateur = produit.css(' .idf-rating__label::text').get()
    #     nbre_rater = produit.css('.ds-ens-product-card__rating span:nth-child(2)::text').get()
    #     src = produit.css('.ds-ens-product-card__visual.idf-image.ds-ens-product-card__visual').attrib['src']

    #     print(title)
    #     print(price)
    #     print(marque)
    #     print(nombre_cnosommateur)
    #     print(nbre_rater)
    #     print(src)

    # def parse_subcategory(self,response):
        # print("############################hello#####################""")
        # sub_categories = response.css('a.ens-product-list-categories__item')
        # sub_category = sub_categories[0].attrib['href']
        # sub_cat_title = response.css('a.ens-product-list-categories__item ::text')
        # print(sub_cat_title)
        # sub_category_1 = sub_categories[1].attrib['href']

        # title = sub_category.css('article h2 ::text').get()


        # print(sub_category)
        # print(sub_category_1)

        # titre = animalerie.css('span.ens-main-navigation-items__link-label ::text').get()
        # print(titre)

    # def parse(self, response):
    #     print("############################hello#####################""")
    #     croquettes = response.css('article.product_pod')
    #     for croq in croquettes:
    #         relative_url = croq.css('h3 a ::attr(href)').get()

    #         if 'catalogue/' in relative_url:
    #             book_url = "https://books.toscrape.com/" + relative_url
    #         else:
    #             book_url = "https://books.toscrape.com/catalogue/" + relative_url
    #         yield response.follow(book_url, callback = self.parse_book_page)
        # print(ti)
    
        # print("############################bonjour#####################""")

        # if 'catalogue/' in relative_url:
        #     book_url = "https://books.toscrape.com/" + relative_url
        # else:
        #     book_url = "https://books.toscrape.com/catalogue/" + relative_url
        # yield response.follow(book_url, callback = self.parse_book_page)