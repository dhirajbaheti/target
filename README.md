This project allows crawling the product specific details from the given set of urls from www.target.com 

Start the crawl for a list of urls provided in the input file.

### Environment Setup
1. Create a conda environment
```
conda create -n target-env python=3.10
```
2. Activate conda environment and change directory to project directory.
```
conda activate target-env
cd ../target
```
3. Install requirements.txt
```
python -m pip install -r requirements.txt
```

### Crawling product specific urls from command line
You need to specify a list of URLs on command line that you want a spider
to scrape without extracting any further URLs from those pages.

Then run below command to start crawling:

```
scrapy crawl product -a urls="https://www.target.com/p/-/A-16666753,https://www.target.com/p/-/A-79344798" 2>crawl_product.err >crawl_product.log
```

### Crawling urls listed in a file urls (Recommanded for high number of URLs)
You need to specify a list of URLs that you want to scrape without extracting any further URLs from those pages.

Save a column of URLs (without a header) in a file called `urls`:
```
https://www.target.com/p/-/A-79344798
https://www.target.com/p/-/A-13493042
https://www.target.com/p/-/A-85781566
https://www.target.com/p/-/A-16666753
...
```
Then run below command to start crawling:

```
scrapy crawl product 2>crawl_product.err >crawl_product.log
```
By default, the crawled product data will be stored in below file. 
If the format of filename needs to be changed it can be done through settings.py file

```
crawled_products_{crawl_date}.jsonl
```
You may use jq or similar utilities to analyse the results.
```
cat crawled_products_2023-08-03.jsonl | jq '[.tcin, .upc, .price_amount, .url]'

e.g.
cat crawled_products_2023-08-03.jsonl | head -5 | jq '[.tcin, .url]' 
[
  "79344798",
  "https://www.target.com/p/baby-trend-expedition-race-tec-jogger-travel-system-8211-ultra-gray/-/A-79344798"
]
[
  "16666753",
  "https://www.target.com/p/brownie-bites-11-81oz-favorite-day-8482/-/A-16666753"
]
[
  "79653286",
  "https://www.target.com/p/kaysville-curved-back-wood-counter-height-barstool-threshold-designed-with-studio-mcgee/-/A-79653286"
]
[
  "13493042",
  "https://www.target.com/p/good-humor-strawberry-shortcake-frozen-dessert-bars-6pk/-/A-13493042"
]
[
  "79344798",
  "https://www.target.com/p/baby-trend-expedition-race-tec-jogger-travel-system-8211-ultra-gray/-/A-79344798"
]
```


