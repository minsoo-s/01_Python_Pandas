# [튜플(Tuple)] ---------------------------------------------------------------
# Read Only List (저장하고 변경되면 안되는 데이터들)
# 수정, 삭제 불가능. 오직 저장된 요소 읽기만 가능. (인덱싱, 슬라이싱, 더하기, 곱하기는 가능)
# 소괄호를 사용하여 여러개의 데이터를 저장하는 타입.
# (!)꼭 변경해야 하는 경우 => List로 형변환
# (!) 요소가 하나일 때, 콤마 찍어줘야 튜플로 인지됨.
# 형태 : (값2, 값2,..., 값N) 또는 값1,값2,..., 값N'
# 요소 : 인덱스로 읽기
#-----------------------------------------------------------------------------
data=('F',123,9.023,True)
print(type(data), data, len(data))
print(data[0],data[-1],data[1:-1], data[1:])

# data[0]='M'  ---> 변경 불가능
# del data[0]  ---> 삭제 불가능

# 꼭 변경해야하는 경우 => List로 형변환
data=list(data)
data[0]='여자'
data=tuple(data)
print(data[0],data[-1],data[1:-1], data[1:])

print(data.count(True)) #--->True 개수
print(data.index(True)) #--->True 인덱스

mydata=('110101-1234567')
print(mydata, type(mydata))
mydata=('110101-1234567',) #---> (!) 요소가 하나일 때, 콤마 찍어줘야 튜플로 인지됨.
print(mydata, type(mydata))
mydata2=10,
print(mydata2, type(mydata2))
