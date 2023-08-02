import json
import re
import logging
from datetime import datetime
from scrapy.http import Request
from scrapy.spiders import CrawlSpider

from target.items import productItem

logger = logging.getLogger(__name__)

crawl_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')


class ProductSpider(CrawlSpider):
    name = "product"

    def start_requests(self):
        target_urls = self.get_urls('urls_to_crawl')
        for target_url in target_urls:
            try:
                yield Request(target_url, callback=self.extract_product)
            except ValueError:
                logger.error("Invalid url: {}".format(target_url))

    def extract_product(self, response):
        item = productItem()

        regex = '__TGT_DATA__.*JSON.parse\("({.*})"\)\),'
        data = json.loads(re.search(regex, response.text).group(1).replace(r'\\\"', "'").replace(r'\"', '"'))

        product = None
        try:
            for tag in data["__PRELOADED_QUERIES__"]['queries']:
                if tag[0][0] == "@web/domain-product/get-pdp-v1":
                    product = tag[1]['product']
                    break
        except Exception as e:
            logger.warning('Unable to parse the page data. {}'.format(e))

        item["url"] = product.get('item', {}).get('enrichment', {}).get('buy_url')
        item["tcin"] = product.get('tcin')
        item["upc"] = product.get('item', {}).get('primary_barcode')
        item["price_amount"] = product.get('price', {}).get('current_retail')
        item["currency"] = re.sub(r'[\d.]+', '', product.get('price', {}).get('formatted_current_price', {}))
        item["description"] = product.get('item', {}).get('product_description', {}).get('downstream_description')
        item["specs"] = [re.sub(r'</?B>', '', val) for val in
                         product.get('item', {}).get('product_description', {}).get('bullet_descriptions', [])]
        for val in product.get('item', {}).get('product_description', {}).get('bullet_descriptions', []):
            if 'Contains' in val:
                item["ingredients"] = \
                    [ing.strip() for ing in re.sub(r'</?B>', '', val).split(':')[1].strip().split(',')]
                break
        item["bullets"] = product.get('item', {}).get('product_description', {}).get('soft_bullets', {}).get("bullets")
        item["features"] = [re.sub(r'</?B>', '', val) for val in
                            product.get('item', {}).get('product_description', {}).get('bullet_descriptions', [])]
        item["crawl_date"] = crawl_date

        yield item

    def get_urls(self, filename):
        """
        Returns a generator that yields the URLs from a file of the form:
        https://www.target.com/p/-/A-79344798
        https://www.target.com/p/-/A-16666753
        :param str - name of file to read from
        """
        with open(filename, "r") as f:
            for next_url in f.readlines():
                if next_url.strip():
                    yield next_url.strip()
