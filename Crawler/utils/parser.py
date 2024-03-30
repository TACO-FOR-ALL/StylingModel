#parser.py
import scrapy
from scrapy.http import TextResponse

def parse_outfits_musinsa(response):
    outfits = []
    outfit_elements = response.xpath('//li[@class="style-list-item"]')
    for outfit_element in outfit_elements:
        # Extracting 상품번호 from the onclick attribute of the <a> tag
        product_id = outfit_element.xpath('.//a/@onclick').re_first(r"goView\('(\d+)'\)")

        # Extracting 코디 페이지 링크 from the href attribute of the <a> tag
        page_link = outfit_element.xpath('.//a[@class="style-list-item__link"]/@href').get()

        # Extracting 코디 사진 링크 from the src attribute of the <img> tag
        image_link = outfit_element.xpath('.//img[@class="style-list-thumbnail__img"]/@src').get()

        # Extracting 업로드 날짜 from the <span> tag with class "post-information__text"
        upload_date = outfit_element.xpath('.//span[@class="post-information__text"][1]/text()').get()

        # Extracting 코디 이름 from the <strong> tag with class "style-list-information__title"
        outfit_name = outfit_element.xpath('.//strong[@class="style-list-information__title"]/text()').get()

        # Extracting 조회수 from the <span> tag with class "post-information__text"
        views_text  = outfit_element.xpath('.//span[@class="post-information__text"][2]/text()').get()
        # Remove "조회" prefix and convert to integer
        views = int(views_text.replace('조회', '').replace(',', '')) if views_text else None
        
        # Extracting 댓글수 from the <span> tag with class "post-information__text"
        # comments_text = outfit_element.xpath('.//span[@class="post-information__text"][3]/text()').get()
        comments_text = outfit_element.xpath('.//span[contains(text(), "댓글")]/text()').get()
        # Remove "댓글" prefix and convert to integer
        comments = int(comments_text.replace('댓글', '').replace(',', '')) if comments_text else None
        comments = comments if comments else 0
        
        gender = "woman"

        # Constructing outfit dictionary
        outfit = {
            '상품번호': product_id,
            '코디 페이지 링크': page_link,
            '코디 사진 링크': image_link,
            '업로드 날짜': upload_date,
            '코디 이름': outfit_name,
            '조회수': views,
            '댓글수': comments,
            '성별': gender
        }
        # print(outfit)
        outfits.append(outfit)
    return outfits
