# [어제 내용 테스트]  ---------------------------------------------
# 1) 데이터를 입력 받아서 하나의 변수에 저장
#    5개의 데이터를 입력
#    5개의 데이터는 하나의 변수명에 저장
# -> List : 수정, 삭제, 추가
# -> Tuple : 수정X, 삭제X, 읽기만 가능

# 5개의 데이터를 저장할 수 있는 저장소
datas=[]  #---> 내용 삽입을 받을 때, 튜플 사용불가

# 키보드로 입력받기 => input("요청메시지")
# 입력받은 데이터 저장하기
data=input("저장하고 싶은 데이터 입력 : ")
datas.append(data)
data=input("저장하고 싶은 데이터 입력 : ")
datas.insert(1,data)  #---> insert 사용시 datas.insert(인덱스, 추가할 값) 형태를 취해야 함.
data=input("저장하고 싶은 데이터 입력 : ")
datas.append(data)
data=input("저장하고 싶은 데이터 입력 : ")
datas.append(data)
data=input("저장하고 싶은 데이터 입력 : ")
datas.append(data)

print('-'*25)
print(f'갯수: {len(datas)}, 데이터 : {datas}')
print('-'*25)
