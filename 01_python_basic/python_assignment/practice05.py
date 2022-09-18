# [ 딕셔너리와 집합 자료형과 for반복문 이해 220524] -------------------

# 1. 딕셔너리 자료형(dict) 다루는 문제입니다.
# 1-1. 아래 데이터를 사용하여 문제를 해결하세요.
# 이름	|	가격
# 폴라포	|	300
# 빵빠레	|	400
# 월드콘	|	250
# 메로나	|	1000
# (1-1) icecream이라는 변수에 위에 데이터를 저장하세요.
icecream={"폴라포":300, "빵빠레":400, "월드콘":250, "메로나":1000 }
print(icecream)
# (1-2) icecream['누가바']에서 오류가 발생하는 이유를 설명해 주세요.
# A) dict는 key에 대응하는 value가 있어야 함.

# (1-3) 키(Key)만 출력해주세요.
print(icecream.keys())

# (1-4) 가장 큰 값, 가장 작은 값을 출력해 주세요.
print(icecream.values())
print(max(icecream.values()))
print(min(icecream.values()))
# (1-5) 키와 값을 쌍으로 묶어서 출력해 주세요.
print(icecream.items())

# (1-6) 돼지바 – 1200을 추가해 주세요.
icecream.update({"돼지바":1200})
print(icecream)

# 1-2. 다음 아이스크림 데이터에 대한 부분 문제를 해결하세요.
# 이름  | 가격 | 재고
# 메로나| 300  | 20
# 비비빅| 400  |  3
# 죠스바| 250  | 100

# (2-1)	딕셔너리 타입으로 데이터를 저장하세요.
icecream={"메로나":[300,20] ,"비비빅": [400,3],"죠스바":[250,100]}

# (2-2)	저장된 딕셔너리 데이터에서 비비빅의 가격을 출력해주세요.
print(icecream.get("비비빅")[0]) #---> key를 가져와서 value 출력. value=[,] 형태이므로 인데스0(가격) 출력

# (2-3)	저장된 딕셔너리 데이터에서 재고를 기준으로 오름차순 정렬해 주세요.
item=list(icecream.items())  #---> 재고를 비교하기 위해 key, value 모두 소환하여 list로 변환
print(sorted(item, key= lambda x:x[1][1])) #---> 'lambda 요소:변화 ' 를 통해 key 기준에서 value 기준으로 전환

# (2-4)	저장된 딕셔너리 데이터에서 죠스바를 삭제해 주세요.
del icecream["죠스바"]
print(icecream)

# (2-4)	'팥빙수'- 2700, '아맛나'-1000 2개 데이터를 한꺼번에 추가해 주세요.
icecream.update({"팥빙수":2700,"아맛나":1000})
print(icecream)

# 1-3. keys = ("apple", "pear", "peach"),	vals = (300, 250, 400) 2개 튜플 데이터를 딕셔너리 타입으로 저장해 주세요.
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
fruit={keys[0]:vals[0],keys[1]:vals[1],keys[2]:vals[2]}
print(fruit)

# 1-4. 사용자로부터 이름, 나이, 전화번호, 이메일 정보를 입력 받아 딕셔너리 타입 으로 저장하세요.
name=input("이름:")
age=input("나이:")
call=input("전화번호:")
mail=input("이메일:")
Info={"이름":name,"나이":age,"전화번호":call,"이메일":mail}
print(Info)

# 1-5. 1-1문제에서 생성된 icecream 객체에 아래 데이터를 추가하는 코드를 작성 하세요.
# 이름	|	가격
# 빠삐코	|	1200
# 돼지바	|	900
# 비비빅	|	1000
icecream.update({"빠삐코":1200,"돼지바":900,"비비빅":1000})
print(icecream)

# 1-6. 1-5문제에서 생성된 icecream 객체에서 아래 조건에 만족하는 코드를 작성 하세요.
# (1) icecream 데이터에서 key값만 가져오기
icecream.keys()
print(icecream)
# (1) icecream 데이터에서 value값만 가져오기
icecream.values()
print(icecream)
# (1) icecream 데이터에서 key와 value를 묶어서 가져오기
icecream.items()
print(icecream)
# (2) icecream 데이터에서 dict자료형 메서드를 사용하여 돼지바 가격 출력
print(icecream.get("돼지바"))
# (1) icecream 데이터에서 dict자료형 메서드를 사용하여 메로나 데이터 추출
print(icecream.get("메로나"))

# 2. 집합 자료형(set)을 다루는 문제입니다.
# 2-1. 비어 있는 집합(set)을 생성해 보세요.
a=set()
print(type(a))

# 2-2. 1~100범위에서 3의 배수 리스트와 7의 배수 리스트를 생성 한 후 두 리스트 에서 중복을 제거한 데이터만 담는 리스트를 생성하세요.
l1=list(range(3,101,3))
l2=list(range(7,101,7))
l=set(l1+l2) #----> (!) 리스트나 튜플은  변수=set() 형태를 취해야 함. {} 불가능.
print(l1)
print(l2)
print(l)

# 2-3. nums=[5, 2, 1, 6, 1, 6, 8, 11, 2, 3, 5]에서 중복 제거한 리스트를 생성하세요.
nums=[5, 2, 1, 6, 1, 6, 8, 11, 2, 3, 5]
nums=list(set(nums))
print(nums)

# 2-4.s1 = set(['a', 'b', 'c', 'd', 'e']) ,	s2 = set(['c', 'd', 'e', 'f', 'g']) 데이터를 사용해 아래 문제를 해결하세요.
s1 = set(['a', 'b', 'c', 'd', 'e'])
s2 = set(['c', 'd', 'e', 'f', 'g'])

# (2-4-1) s1과 s2의 차집합 출력 ----> 합: | , 차: - , 교: &
s_minus=s1-s2
print(s_minus)
# (2-4-2) s1과 s2교집합 출력
s_same= s1 & s2
print(s_same)
# (2-4-3) s1의 합집합 출력
s_plus=s1 | s2
print(s_plus)