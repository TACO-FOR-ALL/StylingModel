# 코디 이미지 크롤러

## Description
코디 추천 모델 데이터 수집을 위한 간단한 이미지 크롤러입니다.
각각의 코디에 대해 다음과 같은 정보들을 수집합니다.  
1. 상품번호
2. 코디 페이지 링크
3. 코디 사진 링크
4. 업로드 날짜
5. 코디 이름
6. 조회수
7. 댓글수
8. 성별

!자세한 사항은 DB 관련 문서 참고.  

## MODULES

### `config.py`
configuration parameters들을 포함합니다.  
주로 base url(무신사, 29cm, LF몰)와 수집할 카테고리를 정의할 수 있습니다.  

### `parser.py`
request로 받아온 데이터에서 필요한 HTML content를 파싱하는 역할을 합니다.  

### `main.py`
main script

### `storage.py`
크롤링한 데이터들을 로컬이나 클라우드 저장소로 옮기는 역할을 합니다.  
각 쇼핑몰마다 directory를 만들고,
각 directory에서의 파일명은 `{카테고리}-outfits.csv` 입니다.  
예) data/musinsa/highteen_outfits.csv

## How to use
```python
python main.py {website} --verbose
```
로 간단하게 실행 가능합니다.  
`website`는 "musinsa", "29cm", "lfmall" 중고르시면 되고, 2개이상 크롤링도 가능합니다.  
아무것도 입력하지 않을경우 default값은 musinsa입니다.  

`--verbose`는 크롤링하는 과정을 세세하게 출력할지 말지를 결정하는 flag입니다.  

## CAUTION!
혹시 몰라서 crawl하는 도중에, 매`fetch_page`전에 2초의 쉬는 텀을 가지도록 하였습니다.  
답답하신 분들은 주석처리하고 실행하셔도 좋습니다.  


## TODO
1. 성별
