import scrapy
from bookscraper.spider_functions import get_random_user_agent
import time, random as rd

class BricospiderSpider(scrapy.Spider):
    name = "bricospider"
    # start_urls = ["https://www.jardiland.com"]
    start_urls = ["https://www.jardiland.com"]

    # def parse(self, response):

    #     for start_url in self.start_urls:
    #         yield scrapy.Request(
    #             url=start_url,
    #             # headers=get_random_user_agent(),
    #             headers="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    #             callback=self.parse_category,
    #         )

    
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


    # print("############################coucou#####################""")
    def parse(self, response):
        print("############################salut#####################""")
        categories = response.css("a.ens-main-navigation-items__link.ds-ens-anchor.ds-ens-anchor--link.ens-main-navigation-items__link")
        for categorie in categories:
            url_du_moment="https://www.jardiland.com"+categorie.attrib['href']
            titre_du_moment=categorie.css('.ens-main-navigation-items__link-label  ::text').get()
            print(url_du_moment)
            print("")
            if "promotions" in url_du_moment or "conseils-idees" in url_du_moment\
                or "animalerie"in url_du_moment or "plante"in url_du_moment or "jardinage"in url_du_moment\
                or "amenagement-exterieur"in url_du_moment or "maison" in url_du_moment:
                print(f"categorie eliminée    {url_du_moment}")
                continue

            print(url_du_moment)
            # time.sleep(rd.uniform(1, 3))

            yield response.follow(
                url=url_du_moment,
                callback=self.parse_subcategorie,
                meta={'cat_parente': self.start_urls[0],'titre_du_moment':titre_du_moment, "ma_cat_actuelle": url_du_moment}
            )


    def check_categorie(self, response):
        return response.css('a.ens-product-list-categories__item')
    

    def parse_subcategorie(self, response):
        print("############################hello#####################""")
        sub_categories = response.css('a.ens-product-list-categories__item')
        print(sub_categories)
        classe_parente = response.meta['cat_parente']
        for sub_categorie in sub_categories:
            print(f"------------------{sub_categorie}")
            url_du_moment="https://www.jardiland.com"+sub_categorie.attrib['href']
            print(f"------------------{url_du_moment}")
            title_du_moment = sub_categorie.css("::text").get()
            print(f"#############{title_du_moment}")
            print(f'~~~~~~~~~~~~~~{response.follow(url=url_du_moment,callback=self.check_categorie)}')
            

            # if url_du_moment.css('.ens-product-list-categories__item') is not None:
            #     page_val = 0
            # else: 
            #     page_val = 1
                
            print(f"le titre de la sous categorie qui vient d etre yieldé {title_du_moment}")
            # print(f"la prochaine sub cat est {response.follow(url=url_du_moment).css('a.ens-product-list-categories__item')}")
            yield response.follow(
                url=url_du_moment,
                callback=self.parse_subcategorie,
                meta={'cat_parente': classe_parente,'titre_du_moment':title_du_moment, "ma_cat_actuelle": url_du_moment}
            )

        yield{
            "titre_categorie":response.meta['titre_du_moment'],
            "url_categorie":response.meta['ma_cat_actuelle'],
            'is_page_list':False if sub_categories else True
            }

            # break


            # sub_cat_title = response.css('a.ens-product-list-categories__item ::text')
            # print(sub_cat_title)
            # sub_category_1 = sub_categories[1].attrib['href']

            # title = sub_category.css('article h2 ::text').get()
            # try:
            #     response.css('a.ens-product-list-categories__item')
            #     "is_page_list":0
            # except:
            #    "is_page_list":1







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