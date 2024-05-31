~~_cloth 파일은 어떤 카테고리나 특징이 있는지를 나타내는 파일입니다.
~~_img 파일은 옷 이미지 데이터들 각각의 카테고리나 특징을 나타내는 파일입니다.

본 README는  1. relabel.py 설명   2. category label 설명    3. attribute label 설명   으로 나뉘어 있습니다.


---------------------------------------------------

=========================
relabel.py설명
=========================

유용하게 사용하실 수 있는 함수는 3가지입니다.

1. get_label(filename)     
    ~_attr_cloth.txt나 ~_category_cloth.txt파일의 라벨들을 라벨명 리스트와 라벨명+타입 리스트로 반환

2. save_target_label_imgs(attr_img_filepath, attr_cloth_filepath, target_label_name)   
    target_label_name이라는 특징을 가진 이미지 30개를 check라는 폴더를 만들어 저장.

3. get_img_data(filepath)    
    _img.txt 파일에서 이미지 경로와 특징을 리스트 형식으로 반환

더 자세한 설명은 relabel.py의 함수 설명을 참고해주세요.

---------------------------------------------------



=========================
CATEGORY LABELS
=========================

--------------- list_category_cloth.txt --------------

First Row: number of categories
Second Row: entry names

Rest of the Rows: <category name> <category type>

--------------- list_category_img.txt --------------

First Row: number of images
Second Row: entry names

Rest of the Rows: <image name> <category label>

---------------------------------------------------

Notes:
1. In category type, "1" represents upper-body clothes, "2" represents lower-body clothes, "3" represents full-body clothes;
2. The order of category labels accords with the order of category names;
3. In category labels, the number represents the category id in category names;
3. Category prediction is treated as a 1-of-K classification problem.

---------------------------------------------------

Detail:
기존 50가지 카테고리를 11가지로 줄였습니다. 줄이는 과정에서 애매한 데이터 약 650개는 삭제하였습니다.
카테고리는 1부터 11까지의 인덱스를 가지며, 모든 옷은 하나의 카테고리에 속합니다. 이는 new_category_img.txt에서 확인하실 수 있습니다.
선별 방식은 Categories 엑셀 파일을 참고해주세요.

11
category_name  category_type
Jacket	    1
Blouse	    1
Shirt	    1
Top	        1
Tee	        1
Jeans	    2
Pants	    2
Shorts	    2
Skirt	    2
Dress	    3
Coat	    3

---------------------------------------------------



=========================
ATTRIBUTE LABELS
=========================

--------------- new_attr_cloth.txt --------------

First Row: number of attributes
Second Row: entry names

Rest of the Rows: <attribute name> <attribute type>

--------------- new_attr_img.txt --------------

First Row: number of images
Second Row: entry names

Rest of the Rows: <image name> <attribute labels>

---------------------------------------------------

Notes:
1. In attribute type, 
    "1" represents texture-related attributes, "2" represents fabric-related attributes,   
    "3" represents shape-related attributes, "4" represents part-related attributes, "5" represents style-related attributes;
2. The order of attribute labels accords with the order of attribute names;
3. In attribute labels, "1" represents positive while "0" represents negative;
4. Attribute prediction is treated as a multi-label tagging problem.

---------------------------------------------------

Detail:
기존 list_attr_cloth의 1000개의 특징 중, 자주 나오거나 중요하다고 생각되는 특징 위주로 31개를 선별하였습니다.
기존 1000개 특징의 경우, 한 특징이 유사한 여러개의 특징으로 분류가 됩니다.
(ex: long sleeve, long-sleeve, long-sleeved  / knit, cotton knit, classic knit 등)
이 점을 고려하여 라벨명이 포함된 모든 특징 중 하나라도 1일 경우 new_attr_img에서도 1이 되도록 특징을 합쳤습니다.
(ex: knit, cotton knit, classic knit 등 중 하나라도 1이면, new_attr_img에서 'knit' == 1)
그럼에도, 값이 1인 특징의 수는 굉장히 적습니다. 기존 데이터들도 일반적으로 겨우 5개 내외의 특징을 가지고 있기에, 변환 후에는 2개 내외입니다. (1count.txt 참고)
1000개 중 어떠한 특징들이 선별에 사용되었는지는 new_attr_candidates.txt를 참고해주세요.

총 이미지 수는 288569이며, 어떤 특징도 포함하지 않은 all_0 이미지를 제외하면 175155개입니다. (new_attr_img_without0.txt에 저장함)

---------------------------------------------------

아래는 특징 설명입니다.
31
attribute_name   attribute_type   meaning
floral               1            꽃무늬
graphic              1            그림이 포함된
striped              1            줄무늬의
embroidered          1            자수의
pleated              1            주름이 있는
solid                1            단색의?
lattice              1            격자
print                1            프린팅
denim                2            데님
chiffon              2            비단, 나일론
cotton               2            면
leather              2            가죽
knit                 2            니트
mesh                 2            망사, 그물
fur                  2            털
lace                 2            레이스
long-sleeve          4            긴팔
sleeveless           4            소매 없음
crew-neck            4            둥근 목선
v-neck               4            v넥
turtle-neck          4            터틀넥
round-neck           4            라운드(round)
collar               4            카라가 있는
collarless           4            카라가 없는
tie                  4            넥타이
zip                  4            지퍼
loose                5            루즈핏(relaxed 포함)
fit                  5            핏한, 정장
skinny               5            스키니
retro                5            레트로
sporty               5            스포티

---------------------------------------------------
