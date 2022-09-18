#----------------- 기본 자료형(int, float, str, bool) ---------------------------------
# 1.숫자형 -> int 정수 : integer (ex) 양수, 음수, 0
#            float 실수 : floting point (ex) 2.4, -3.2
# 2.문자형 -> str 문자열 : string (ex) ' '," ",''' ''',""" """,
# 3.논리형 -> bool 논리 : boolean (ex) True, False
#------------------------------------------------------------------------
# 논리 데이터 타입 -bool 타입
# 2가지 데이터만 저장 가능 ==> True, False
#------------------------------------------------------------------------
isok=True
print(f'isok=> {isok} , type=> {type(isok)}')
isok=False
print(f'isok=> {isok} , type=> {type(isok)}')


#--------------- 비교연산자(==,!=, >, >=, <, <=) ------------------------------------
# 결과는 참과 거짓 (True, False)
# == :같다
# != :같지 않다
# >  :크다
# >= :크거나 같다
# <  :작다
# <= :작거나 같다
#-----------------------------------------------------------------------
data1=10
data2=5
print(f'{data1} == {data2} : {data1 == data2}')
print(f'{data1} != {data2} : {data1 != data2}')
data1='AbC'
data2='ABc'
print(f'{data1} == {data2} : {data1 == data2}')
print(f'{data1} != {data2} : {data1 != data2}')
print(f'{data1} >= {data2} : {data1 >= data2}')
print(f'{data1} <= {data2} : {data1 <= data2}')


#------------------ 논리연산자(and, or, nat) ------------------------------------
# 결과는 참과 거짓 (True, False)
# and : 그리고 : 왼쪽 and 오른쪽 : 왼쪽, 오른쪽 모두 True
# or  : 또는   : 왼쪽 or 오른쪽  : 왼쪽, 오른쪽 중 한 개 이상 True
# not : 부정   : not True, not False 토글링(Toggle)
#-----------------------------------------------------------------------
age=20
gender='F'
print(f'{age>=30} and {gender=="M"} : {age>=30 and gender=="M"}')
print(f'{age<=30} and {gender=="M"} : {age<=30 and gender=="M"}')
print(f'{age<=30} and {gender=="F"} : {age<=30 and gender=="F"}')
print('\n')
print(f'{age>=30} or {gender=="M"} : {age>=30 or gender=="M"}')
print(f'{age<=30} or {gender=="M"} : {age<=30 or gender=="M"}')
print(f'{age<=30} or {gender=="F"} : {age<=30 or gender=="F"}')
print('\n')
print(f'not {age}>=30 : {not age>=30}')


#-------------------- 데이터 자료형과 논리값 --------------------------------
# 123 => 문자형 변환  str(123)
# '23.4' => 숫자형 변환 float('23.4')
# 'ABC => 논리형 변환 bool('ABC')
# 문자형은 칸 차지가 없을 때 False, 공백이라도 있으면 True
# 숫자형은 0일 때 False
#------------------------------------------------------------------------
print(f'bool("ABC") => {bool("ABC")}, type : {type(bool("ABC"))}')
print(f'bool("") => {bool("")}, type : {type(bool(""))}')
print(f'bool(" ") => {bool(" ")}, type : {type(bool(" "))}')

print(f'bool(123) => {bool(123)}, type : {type(bool(123))}')
print(f'bool(-123) => {bool(-123)}, type : {type(bool(-123))}')
print(f'bool(0) => {bool(0)}, type : {type(bool(0))}')


#------------- 여러개 data를 저장하기(문자열, 리스트, 튜플, 딕셔너리, 집합)------------------
# 문자열, 리스트, 튜플 은 index를 가지는 공통점이 있다.
# 문자열 'ABC'
#        012
# 리스트 [D1, D2,....,DN]
#         0  1       N
# 튜플  (D1, D2,...,DN)
#        0  1      N

# 딕셔너리
# 집합