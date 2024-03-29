# main.py
from config import BASE_URLS, STYLE_TYPES, SORT, HEADER
import itertools
import scrapy
from scrapy.http import TextResponse
from utils.utils import fetch_page
from utils.parser import parse_outfits
from utils.storage import store_outfits

def crawl_outfits_single_page():
    headers = HEADER
    combinations = itertools.product(BASE_URLS,STYLE_TYPES,SORT)
    for base_url, style_type, sort_method in combinations:
        for page in range(10):
            url = f"{base_url}?style_type={style_type}&sort={sort_method}&page={page}"
            req = fetch_page(url,headers)
            response_html = TextResponse(req.url, body=req.text, encoding="utf-8")
            if response_html:
                outfits = parse_outfits(response_html)
                store_outfits(outfits, base_url, style_type, page)
            else :
                print(f"sth went wrong")

if __name__ == "__main__":
    crawl_outfits_single_page()