import pandas as pd

###### 사용자가 변경할 내용 ######

# 데이터 처리 및 합병할 csv 파일 목록. 합병할 csv 파일이 3개라면, csv_files_path와 sex 리스트의 원소는 3개가 됩니다.
csv_files_path = ['m_girlish_w.csv', 'm_sporty_m.csv', 'm_sporty_w.csv'] 
# 위 csv파일들 각각에 추가할 성별. 'M' or 'F'
sex = ['F', 'M', 'F']    
# Column이름 변경. 기존 csv 파일의 열 순서와 동일한지 꼭 확인하세요!!
columns = ['id', 'title', 'imagelink', 'style', 'date', 'views', 'model', 'comment']  
# 새로 저장할 csv 파일 이름
new_csv_file_name = 'm_girlish_sporty.csv'     

################################


new_data = []
for i in range(len(csv_files_path)):
        
    data = pd.read_csv(csv_files_path[i], encoding='utf-8')
    # print(data.head())

    # column 이름 변경 
    data.columns = columns
    # data.rename(columns={'stylelistmodel': 'model'}, inplace=True)  # 특정 열 이름 변경

    # column에서 불필요한 한글 지우기
    data['model'] = data['model'].str.replace('모델 : ', '')
    data['views'] = data['views'].str.replace('조회 ', '')
    data['comment'] = data['comment'].str.replace('댓글 ', '')

    # 성별과 링크 column 추가
    data['sex'] = sex[i]
    data['link'] = 'https://www.musinsa.com/app/styles/views/' + data['id'].astype(str)

    # 열 순서 바꾸기
    data = data[['id', 'title', 'sex', 'style', 'date', 'views', 'model', 'comment', 'link', 'imagelink']]
    new_data.append(data)

merged_data = pd.concat(new_data, ignore_index=True,)
print(data.head())

# 새로운 CSV 파일로 저장
merged_data.to_csv(new_csv_file_name, index=False, encoding='utf-8')
print("Shape: ", merged_data.shape)
print("Saved successfully")

