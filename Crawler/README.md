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

## TODO
1. iterate over pages
2. 성별
