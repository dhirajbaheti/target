
from scrapy.item import Item, Field


class productItem(Item):
    url = Field()
    tcin = Field()
    upc = Field()
    price_amount = Field()
    currency = Field()
    description = Field()
    specs = Field()
    ingredients = Field()
    bullets = Field()
    features = Field()
    crawl_date = Field()
