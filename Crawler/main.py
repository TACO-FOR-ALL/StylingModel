#main.py 
import argparse
from crawl import crawl_outfits_musinsa, crawl_outfits_29cm, crawl_outfits_lfmall
from download import download_images_musinsa
parser = argparse.ArgumentParser()
parser.add_argument('website', nargs='*', type=str, default=['musinsa'],
                    help='Website(s) to crawl, choose among [musinsa, 29cm, lfmall]')
parser.add_argument('--verbose', action='store_true',
                    help='Enable verbose mode')

parser.add_argument('--download', action='store_true',
                   help='Enable verbose mode')

args = parser.parse_args()
verbose = args.verbose
download = args.download
websites = args.website

for website in websites:
    if website == 'musinsa':
        print("Start crawling musinsa...")
        crawl_outfits_musinsa(verbose)
        print("Crawling musinsa End")
        
    elif website == '29cm':
        print("Start crawling 29cm...")
        crawl_outfits_29cm(verbose)
        print("Crawling 29cm End")
    elif website == 'lfmall':
        print("Start crawling lfmall...")
        crawl_outfits_lfmall(verbose)
        print("Crawling lfmall End")
    
    
if download:
    print("Downloading images...")
    #Execute utils.py script
    download_images_musinsa(verbose)