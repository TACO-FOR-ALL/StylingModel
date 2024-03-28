# main.py
from config import BASE_URL, STYLE_TYPES,SORT, HEADER
import itertools
import scrapy
from scrapy.http import TextResponse
from utils.utils import fetch_page
from utils.parser import parse_outfits
from utils.storage import store_outfits

def crawl_outfits():
    headers = HEADER
    combinations = itertools.product(BASE_URL,STYLE_TYPES,SORT)
    for base_url, style_type, sort_method in combinations:
        url = f"{BASE_URL}?style_type={style_type}&sort={sort_method}"
        req = fetch_page(url,headers)
        response = TextResponse(req.url, body=req.text, encoding="utf-8")
        if response:
            outfits = parse_outfits(response)
            store_outfits(outfits)
        else :
            print(f"sth went wrong")

if __name__ == "__main__":
    crawl_outfits()