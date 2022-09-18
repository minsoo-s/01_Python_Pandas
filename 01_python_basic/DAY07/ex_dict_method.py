#----------------------------------------------------------------------------------------
# [딕셔너리 자료형(dict) 전용함수 => 메서드(method) 실습] keys, values, items, get, pop, update, clear
#-----------------------------------------------------------------------------------------
# 사람 정보 => 이름, 나이, 성별, 전화번호, 주소
personInfo={"name":"마징가"}
personInfo["age"]=250
personInfo["gender"]="M"
personInfo["phone"]="010-2222-1112"
personInfo["addr"]="Daegu"
print(f'personInfo 타입 : {type(personInfo)}\n데이터:{personInfo}\n갯수: {len(personInfo)}')


# 변수명.keys()  => dict 데이터에서 키(key)만 가져오는 메서드
myKeys=personInfo.keys()
print(f'myKeys => {myKeys}, type : {type(myKeys)}')

# 변수명.values() => dict 데이터에서 값(Value)만 가져오는 메서드
myValues=personInfo.values()
print(f'myValues => {myValues}')
for value in myValues:
    print(value)

# 변수명.items() => dict 데이터에서 키와 값을 튜플 묶음으로 가져오는 메서드
myItems=personInfo.items()
print(f'myItems => {myItems}')


#print(myKeys[0], myKeys[-1]) ---> list가 아니라서 인덱싱 사용불가. list로 형변환 필요.
# 읽기 방법 (1) for ~ in ~:
for key in myKeys: #---> key값을 순차적으로 불러옴.
    print("나야",key)
# 읽기 방법 (2) list(데이터) 형변환
myKeys=list(myKeys)
print(myKeys)


# dict 데이터에서 key로 Value를 가져오는 메서드 => 변수명.get(key)
# 해당 key가 dict 데이터 안에 없으면, None(값이 없으) 결과로 돌려줌.
print(personInfo.get("name"))
print(personInfo["name"])

print(personInfo.get("email")) #---> get은 없는 key여도 오류 안남.(None 출력됨)
# print(personInfo["email"]) ---> 해당 키가 dict 데이터 안에 없으면 오류남.
print(personInfo.get("email","이메일 없음")) #---> (!) 해당 key가 없으면 None 대신 "이메일 없음" 돌려줌.

print(personInfo.pop("name"))  # ---> pop은 해당 키를 불러온 뒤 원본 삭제, get은 불러오기만 함.

# update( dict 타입) =>여러개의 데이터를 dict에 추가하는 메서드
personInfo.update({1:100,2:200,3:300})
print(personInfo, '\n', len(personInfo))

# clear => 전체 데이터 삭제
personInfo.clear()
print(personInfo)