import itertools
import time
from scrapy.http import TextResponse
from config import BASE_URLS, STYLE_TYPES, SORT, HEADER
from utils import *

# musinsa
def crawl_outfits_musinsa(verbose):
    headers = HEADER
    combinations = itertools.product(BASE_URLS,STYLE_TYPES,SORT)
    for base_url, style_type, sort_method in combinations:
        # 남성 & 여성
        # TODO
        
        # find out how many pages are there
        url = f"{base_url}?style_type={style_type}&sort={sort_method}&page=1"
        req = utils.fetch_page(url,headers)
        response_html = TextResponse(req.url, body=req.text, encoding="utf-8")
        
        # Extract the number of pages text
        page_info_text = response_html.xpath('//span[@class="pagingNumber"]/span[@class="totalPagingNum"]/text()').get()

        # Extract the number of pages from the text
        number_of_pages = int(page_info_text.strip())

        for page in range(number_of_pages):
            # time.sleep(2) # 필요없으면 삭제해도 됌
            url = f"{base_url}?style_type={style_type}&sort={sort_method}&page={page+1}"
            print(f"start fetching {url}") if verbose else None
            req = utils.fetch_page(url,headers)
            response_html = TextResponse(req.url, body=req.text, encoding="utf-8")
            if response_html:
                outfits = parser.parse_outfits_musinsa(response_html)
                storage.store_outfits(outfits, base_url, style_type, page+1)
                print("parsing and storing successful") if verbose else None
            else :
                print("sth went wrong.")

#29cm
def crawl_outfits_29cm(verbose):
    print("Haven't implemented yet")

#lfmall
def crawl_outfits_lfmall(verbose):
    print("Haven't implemented yet")