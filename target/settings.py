# Scrapy settings for target project
from datetime import datetime

BOT_NAME = 'target'

SPIDER_MODULES = ['target.spiders']
NEWSPIDER_MODULE = 'target.spiders'

ROBOTSTXT_OBEY = True

LOG_LEVEL = 'DEBUG'

DOWNLOAD_DELAY = 0
REACTOR_THREADPOOL_MAXSIZE = 20
CONCURRENT_REQUESTS = 40
COOKIES_ENABLED = True
FEED_FORMAT = 'jsonlines'
FEED_URI = f"crawled_products_{datetime.today().strftime('%Y-%m-%d')}.jsonl"

ITEM_PIPELINES = {
    'target.pipelines.ValidatePipeline': 100,
    'target.pipelines.DeduplicatePipeline': 200,
}

DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,de;q=0.8,ro;q=0.7",
    "Upgrade-Insecure-Requests": "1",
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
}

HTTPCACHE_POLICY = 'scrapy.extensions.httpcache.RFC2616Policy'

# Setup up a proxy pool for running it on higher scale!
# os.environ["http_proxy"] = "http://{proxy_ip}:{proxy_port}/"
# os.environ["https_proxy"] = "https://{proxy_ip}:{proxy_port}/"
