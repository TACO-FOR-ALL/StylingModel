八爪鱼를 통해 남/녀를 구분하여 수집한 무신사 코디숍 데이터를 정리하여 하나로 합치는 코드입니다.
"모델 : xxx", "댓글 2" 등 반복되는 불필요한 한글을 지우고, 코디 링크와 성별 column을 추가합니다.
최종 열 리스트는 아래와 같습니다.
##### ['id', 'title', 'sex', 'style', 'date', 'views', 'model', 'comment', 'link', 'imagelink']


코드에 나와있듯 아래 내용들만 수정해주시면 됩니다.

/# 데이터 처리 및 합병할 csv 파일 목록. 합병할 csv 파일이 3개라면, csv_files_path와 sex 리스트의 원소는 3개가 됩니다.

csv_files_path = ['m_girlish_w.csv', 'm_sporty_m.csv', 'm_sporty_w.csv'] 

/# 위 csv파일들 각각에 추가할 성별. 'M' or 'F'

sex = ['F', 'M', 'F']    

/# Column이름 변경. 기존 csv 파일의 열 순서와 동일한지 꼭 확인하세요!!

columns = ['id', 'title', 'imagelink', 'style', 'date', 'views', 'model', 'comment']  

/# 새로 저장할 csv 파일 이름

new_csv_file_name = 'm_girlish_sporty.csv' 

