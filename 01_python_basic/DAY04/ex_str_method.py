#--------------------------------------------------------------------------------------------------------------------
#                          문자열 데이터 타입(str) 전용의 함수. 즉, 메서드(method)
# 형태: str.메서드()
# 형태: 문자열 변수명.메서드()
#--------------------------------------------------------------------------------------------------------------------
data = "Happy Summer Happy Summer"
#       0123456789
# 문자열 안에서 특정 문자(열)의 개수 체크하는 메서드
data.count("m")
print(data.count("m")) #함수호출1------------> 결과를 다시 쓸 일이 없는 경우, 1번 출력하고 끝.
value=data.count("py") #함수호출2------------> 결과를 계속해서 사용할 경우, 변수 지정해둘 것.
print(value)

# 문자열 안에서 특정 문자(열)의 인덱스 찾는 메서드
# str.find(), str.index()
# str.find() 는 (왼쪽 끝에서 시작) 찾는 문자열의 첫 글자 인덱스를 알려줌,
# str.rfind() 는 (오른쪽 끝에서 시작)찾는 문자열의 첫 글자 인덱스를 알려줌,
value=data.find('S')
print(f'\'S\' 인덱스 : {value}')
value=data.find('mer')
print(f'\'mer\' 인덱스 : {value}')
value=data.find('py')
print(f'\'py\' 인덱스 : {value}')
value=data.rfind('py')                     #str.rfind()
print(f'\'py\' 인덱스 : {value}')

#find는 찾는 값이 없으면 -1 불러옴.
#index는 찾는 값 없으면 오류 발생.
value=data.find('zoo')
print(f'\'zoo\' 인덱스 : {value}')
value=data.index('zoo')
print(f'\'zoo\' 인덱스 : {value}')