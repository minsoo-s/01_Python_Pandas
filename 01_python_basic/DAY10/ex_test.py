# [문제 1] ------------------------------------------------------------------
#  2개의 문자를 입력받아서 하나의 문자열로 반환하는 함수
# 입력-> Good, Luck 출력-> Good luck
# --------------------------------------------------------------------------
# 함수명 : joinStrs
# 파라미터 :str1,str2
# 반환값 : 합쳐진 문자열

def joinStrs(str1, str2):
    return str1+" "+str2

# 함수 사용하기
datas=input("문자열 2개 입력 예)A,B : ")

# 데이터 전처리
datas=datas.split(',') #["A", "B"] <---" A,B "
print(datas)

# 입력된 데이터 공백 제거 => strip, lstrip, rstrip
# datas[0]=datas[0].strip()
# datas[1]=datas[1].strip()
datas=[d.strip() for d in datas]  #list comprehension 방식 : 리스트 안의 요소들을 하나씩 꺼내서 양옆 공백 제거
print(datas)

# 함수 호출
print(joinStrs(datas[0],datas[1]))


'''a=input("2개 문자 입력: ")
a=a.split(',')
a="".join(a)
print(a)
'''

# [문제 2]---------------------------------------------------------------
# 숫자 데이터 리스트를 입력 받아서 평균을 반환하는 함수
# 출력 => 평균 XX.XXX
# -----------------------------------------------------------------------

def getAverage(nums):
    count = len(nums)
    total=0
    for num in nums:
        total=total+num
    return total/count if count>0 else "데이터가 없습니다."

datas=[1,2,3,4]

print(f"{datas} 평균: {getAverage(datas)}")

'''
avr=0
for num in datas:
    avr= (avr+num)/len(datas)
print(f'평균은 {avr}')
'''

# [문제 3]---------------------------------------------------------------------------
# 입력받은 정수의 code 값을 16진수로 반환하는 함수
# 단, 입력되는 정수의 갯수는 유동적 ---> 가변인자
# 입력 =>2,3 출력 => 0x32, 0x33
# 입력 =>2   출력 => 0x32
# --------------------------------------------------------------------------
# 함수명 : getCode
# 파라미터 :*num
# 반환값 : 16진수

def getCode(*num):
    strMsg=''
    for n in num:
      # 문자 -> 코드값 반환 내장함수 ord(문자 1개)
        code = ord(str(n))
        strMsg = strMsg + hex(code)+ ', '

    return strMsg[:-2] #---> 가장 마지막 콤마와 공백 제거

# 함수 사용
print(f'3의 코드값 : {getCode(3,5,7)}')