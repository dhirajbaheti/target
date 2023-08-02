# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging

from scrapy.exceptions import DropItem


class ValidatePipeline(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def process_item(self, item, spider):
        # Add a criteria to drop a product
        if item.get('price_amount') == 0:
            self.logger.error("Invalid 'price_amount' in {}".format(item))
            raise DropItem("invalid price_amount")

        return item


class DeduplicatePipeline(object):
    def __init__(self):
        self.ids_seen = set()
        self.logger = logging.getLogger(__name__)

    def process_item(self, item, spider):
        # Add a criteria to filter duplicates
        if item['tcin'] in self.ids_seen:
            self.logger.error("Duplicate 'tcin' in {}".format(item['tcin']))
            raise DropItem("duplicate tcin")
        else:
            self.ids_seen.add(item['tcin'])
            return item
