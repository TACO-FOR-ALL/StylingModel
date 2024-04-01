# utils.py

import requests
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
