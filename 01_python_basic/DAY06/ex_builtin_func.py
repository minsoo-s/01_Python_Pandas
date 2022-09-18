#---------------------------------------------------------------------------
# 함수(Funtion) : 자주 사용되는 코드 묶음의 이름을 붙임
#                해당 코드가 필요한 경우, 이름을 불러서 사용
#                => 함수 호출
# 종류 - (1) 내장함수(Builtin function) : print(), len(), type(), id()
#     - (2) 사용자정의함수
#---------------------------------------------------------------------------
greeting="Hello~!"

# print() => 화면애 출력하기
print(greeting)

# len() => 문자열(str)안에 문자가 몇 개 있는지 알려주는 함수
print(f'{greeting}의 문자 개수: {len(greeting)}')

# type() => 데이터 타입 알려주는 함수
print(f'{greeting}의 타입 : {type(greeting)}')

# id() => 변수에 저장된 주소값 확인 함수
print(f'greeting 변수 저장값 : {id(greeting)}')

# list => 여러 개의 데이터를 저장하는 타입
score=[30,5,4,19,2,94, 87, 100]
print(f'score 리스트의 갯수 : {len(score)}')

greeting="Hello~!"
nums=[10,20,30]
