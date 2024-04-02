# utils.py

import requests
from datetime import datetime

def fetch_page(url, headers):
    req = requests.get(url, headers = headers)
    if req.status_code == 200:
        # with open("output.html", "w", encoding="utf-8") as file:
        #     file.write(req.text)
        return req
    else:
        print(f"Failed to fetch {url}")
        return None

def check_website(url):
    if 'musinsa' in url:
        return 'musinsa'
    elif '29cm' in url:
        return '29cm'
    elif 'lfmall' in url:
        return 'lfmall'
    else:
        return None


def format_date(date_str):
    # Parse the date string using strptime
    parsed_date = datetime.strptime(date_str, "%y.%m.%d")
    # Format the parsed date using strftime
    formatted_date = parsed_date.strftime("%Y/%m/%d")
    return formatted_date
