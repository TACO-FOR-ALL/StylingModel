from PIL import Image
from tqdm import tqdm
import os

'''
사용할 만한 함수 목록
get_label(filename)     # 라벨들을 라벨명 리스트와 라벨명+타입 리스트로 반환
save_target_label_imgs(attr_img_filepath, attr_cloth_filepath, target_label_name)   # target_label_name에 해당하는 특징을 가진 이미지 30개 저장
get_img_data(filepath)    # _img.txt 파일에서 이미지 경로와 특징을 리스트 형식으로 반환

맨 밑에 예제 참고해서 사용하시면 됩니다.


사용할 필요 없는 내부 함수
make_new_category_img()
make_temp_attr_candidate()
get_new_attr_idx()
reduce_attr()
'''


def get_label(filename):  
    '''
    라벨 목록 파일을 읽어오는 함수입니다.
    첫번째 반환자는 라벨명들의 리스트입니다. ['label1', 'label2', ....]
    두번째 반환자는 라벨명과 타입이 담긴 리스트의 리스트입니다. [['label1','type'], ['label2','type'], ....]
    category의 경우: {1:상의, 2:하의, 3:상하의 일체형}
    attribute의 경우: {1:texture, 2:fabric, 3:shape, 4:part, 5:style}
    더 자세한 설명은 README_new.txt를 참고해주세요.
    '''
    f = open(filename, 'r')
    lines = f.readlines()
    labels_types = []
    labels = []
    for line in lines:
        line = line.split()
        label_name = line[0]
        for i in range(1, len(line)-1):
            label_name = label_name + ' ' + line[i]
        labels.append(label_name)
        labels_types.append([label_name, line[-1]])
    f.close()
    return labels[2:], labels_types[2:]



def save_target_label_imgs(attr_img_filepath, attr_cloth_filepath, target_label_name):
    '''
    Deepfashion 데이터셋에서 특정 옷 attribute를 가지고 있는 이미지 최대 30개를 check폴더에 저장할 수 있는 함수입니다.
    filepath 파일의 라벨명 중, 확인하고 싶은 라벨 이름을 인수로 넣어주세요.
    예시: save_target_label("list_attr_img.txt", "list_attr_cloth.txt", "cowl neck")
    '''
    attr_cloth, attr_cloth_type = get_label(attr_cloth_filepath)
    attr_cloth.insert(0, 'img')
    # print(len(attr_cloth))
    target = attr_cloth.index(target_label_name)
    print(target)
    
    with open(attr_img_filepath, 'r') as f:
        total_len = int(f.readline())
        f.readline()
        count = 0
        directory = "check"
        if not os.path.exists(directory):
            os.makedirs(directory)
        for _ in range(total_len):
            line = f.readline().split()
            if line[target] == '1':
                image = Image.open(line[0])
                path = directory + "/" + str(count) + ".jpg"
                image.save(path)
                count += 1
            if count > 30: break
        if count == 0: print("No such attribute, save failed")
        else: print(f"Image saved to folder name '{directory}'")
        


def get_img_data(filepath):
    '''
    _img.txt 파일의 데이터를 리스트 형태로 읽어오는 함수입니다.
    _category_img.txt가 입력될 경우, [[img1.jpg, cate1], [img2.jpg, cate2], ... ] 형식이 반환됩니다.
    _attr_img.txt가 입력될 경우, [[img1.jpg, 0,0,1, ..., 0], [img2.jpg, 1,0,1, ..., 0] ] 형식이 반환됩니다.
    구현이 어렵지 않으므로 참고해서 변형해서 사용하시면 됩니다.
    '''
    img_data = []
    with open(filepath, 'r') as f:
        total_len = int(f.readline()) #len
        f.readline()  #ignore 2nd line
        for _ in range(total_len):
            line = f.readline().split()
            img_data.append(line)
        print(f"Number of data in '{filepath}': ", total_len)
    return img_data




trans = [0,1,1,2,1,3,1,3,10,4,4,1,5,1,1,2,4,5,5,4,4,7,7,0,8,0,6,6,7,7,7,0,8,9,7,8,8,10,0,11,0,10,10,10,10,0,0,10,10,0,0]

def make_new_category_img():
    '''
    기존 50가지 category를 11가지로 줄여서 새롭게 new_category_img.txt를 생성합니다.
    카테고리는 다음과 같으며, 최승환의 개인적인 판단으로 분류했습니다.
    {
        1: Jacket
        2: Blouse
        3: Shirt
        4: Top
        5: Tee
        6: Jeans
        7: Pants
        8: Shorts
        9: Skirt
        10: Dress
        11: Coat
    } 
    '''
    f_bef = open("list_category_img.txt", 'r')
    f_deleted = open("deleted_img.txt", 'w')
    f_bef.readline() # number of img
    with open("new_category_img.txt", 'w') as f:
        f.write("288568")  # number of img 수동으로 추가
        f.write(f_bef.readline())
        count = 0
        while True:
            line = f_bef.readline()
            if not line: 
                break
            line = line.split()
            if trans[int(line[1])] != 0:
                f.write(f"{line[0]}     {str(trans[int(line[1])])}\n") 
                count += 1
            else:
                f_deleted.write(line[0]+'\n')
        print(count)  #txt 파일 첫 줄에 이미지 갯수 count는 수동으로 추가. 288568개 (기존 289222개)
    f_bef.close()
    f_deleted.close()

        

def make_temp_attr_candidate():
    '''
    전체 attribute중 축소된 신규 attribute를 포함하는 것들만 뽑아내기 위해 사용했고, 추가로 사용하실 필요는 없습니다.
    '''
    new_attr_cloth, new_attr_cloth_type = get_label("new_attr_cloth.txt")
    attr_cloth, attr_cloth_type = get_label("list_attr_cloth.txt")
    # print(new_attr_cloth_type)
    # print(len(new_attr_cloth_type))
    new_labels = {}
    new_labels_type = {}
    for label in new_attr_cloth:
        key = label
        value_label = []
        value_type = []
        if label == 'round-neck':
            label = 'round'
        elif label == 'long-sleeve':
            label = 'long'
        elif label == 'crew-neck':
            label = 'crew'
        elif label == 'loose':
            value_label.append('relaxed')
            value_type.append(['relaxed', '5'])
        
        for attr in attr_cloth_type:
            if label in attr[0]:
                value_label.append(attr[0])
                value_type.append(attr)
        new_labels[key] = value_label
        new_labels_type[key] = value_type
    
    f = open("new_attr_candidates.txt", 'w')
    #print(new_labels_type)
    for x in new_labels:
        s = f"{x}: ({len(new_labels[x])})  {new_labels[x]}"
        f.write(s + '\n')
    f.close()
    f = open("temp_attr_type_candidates.txt", 'w')  
    #temp파일 생성 후, 인공으로 직접 필터링을 다시 진행하여 new_attr_type_candidates.txt를 만들었습니다.
    for x in new_labels_type:
        s = x
        for candi in new_labels_type[x]:
            s += f",{candi[0]},{candi[1]}"
        f.write(s + '\n')
    f.close()


def get_new_attr_idx():
    '''
    reduce_attr()를 위해 사용되는 함수로, 새로 만들어질 attr 후보들이 기존 list_attr_img.txt에서 가지는 인덱스를 반환합니다.
    '''
    f = open("new_attr_type_candidates.txt", 'r')
    new_attr_dict = {}
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.split(',')
        key = line[0]
        value = []
        for i in range(2, len(line)-1, 2):
            value.append(line[i])
        new_attr_dict[key] = value
    
    #print(new_attr_dict)
    attr_cloth, attr_cloth_type = get_label("list_attr_cloth.txt")
    attr_cloth.insert(0, 'img')
    new_attr_idx = {}
    for key in new_attr_dict:
        idxs = []
        for label in new_attr_dict[key]:
            idx = attr_cloth.index(label)
            idxs.append(idx)
        new_attr_idx[key] = idxs
    #print(new_attr_idx)
    return new_attr_idx


def reduce_attr():
    '''
    앞서 진행된 모든 전처리 결과를 이용하여 최종 new_attr_img.txt를 생성합니다.
    현재는 new_attr_img_without0.txt를 만드는 용도로 수정된 상태입니다. 
    f_new 이름과 isAll0만 수정하면 기존 상태로 돌아갑니다.
    '''
    new_attr_idx = get_new_attr_idx()
    deleted = []
    with open("deleted_img.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            deleted.append(line[:-1])
    #print(deleted)
    
    f_img = open("list_attr_img.txt", 'r')
    f_new = open("new_attr_img_without0.txt", 'w')
    total_len = int(f_img.readline()) # 289222
    f_new.write(str(total_len - len(deleted)) + '\n')  # 288568. 그런데 실제로는 288569, 하나가 지워지지 않았음. 찾기는 불가
    f_new.write(f_img.readline())
    # f_1 = open("1count.txt", 'w')
    count = 0
    for _ in tqdm(range(total_len)):
        line = f_img.readline().split()
        
        # s1 = line[0] + "     "
        # c = 0
        # for i in range(1, len(line)):
        #     if line[i] == '1':
        #         s1 += f' {str(i)}'
        #         c += 1
        # f_1.write(s1 + f'  [{c}]\n')

        if line[0] in deleted:
            continue
        s = line[0] + "          "
        isAll0 = True
        for key in new_attr_idx:  # 모든 attr에 대해서, 해당 attr의 후보들 중 하나라도 1이라면 해당 attr는 1, 아님 0
            isTrue = False
            for idx in new_attr_idx[key]:
                if line[idx] == '1': 
                    isTrue = True
                    isAll0 = False
                    break
            if isTrue:
                s += ' 1'
            else:
                s += ' 0'
        s += '\n'
        if not isAll0:
            f_new.write(s)
            count += 1
    f_new.close()
    f_img.close()
    # f_1.close()
    print(count)
       
# make_new_category_img()
# reduce_attr()


# ----------------------------------------

# # main
# cate_cloth, cate_cloth_type = get_label("list_category_cloth.txt")
# attr_cloth, attr_cloth_type = get_label("list_attr_cloth.txt")
# print(attr_cloth)

save_target_label_imgs("new_attr_img.txt", "new_attr_cloth.txt", "knit")

category_img = get_img_data("new_category_img.txt")
attr_img = get_img_data("new_attr_img.txt")
#print(category_img)