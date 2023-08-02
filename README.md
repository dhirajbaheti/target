Start the crawl for a list of urls provided in the input file

### Environment Setup
1. Create a conda environment
```
conda create -n target-env python=3.10
```
2. Activate conda environment and change directory to project directory.
```
conda activate target-env
cd path/to/target
```
3. Install requirements.txt
```
python -m pip install -r requirements.txt
```


### Crawling from a given list of product urls
You need to specift a list of URLs that you want a spider
to scrape without extracting any further URLs from those pages.

Save a column of URLs (without a header) in a file called `urls_to_crawl`:
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
```
