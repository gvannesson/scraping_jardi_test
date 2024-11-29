# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

def serialize_price(value):
        return f"€ {str(value)}"

class bricospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ProductItem(scrapy.Item):

    #url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    marque = scrapy.Field()
    nombre_consommateur = scrapy.Field()
    nbre_rater = scrapy.Field()
    src = scrapy.Field()
    id_product = scrapy.Field()