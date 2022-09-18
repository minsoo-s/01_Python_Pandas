# -------------------------------------------------------------
# 리스트 컨프리헨션 (List Comprehension) ---> 아래 경우들은 일반적인 for문보다 list comprehension이 빠름.
# - list 안에 for 문이 포함되어 있는 구문
# - 조건부 표현식 포함되는 구문
# -------------------------------------------------------------
nums=[1,2,3,4,5]

# [문제1] nums 데이터 요소들에 3을 곱한 값을 저장하는 리스트 생성
nums2=[]
for num in nums:
    nums2.append(num*3)

# list Comprehension
nums22= [num*3 for num in nums]

print(nums2, nums22)

# [문제2] nums 데이터 중에서 2의 배수만 3을 곱해서 새로운 리스트 생성
for num in nums:
    if num%2==0:
        nums2.append(num*3)

# list Comprehension
nums22 = [num*3 for num in nums if num%2==0]

print(nums2,nums22)

# [문제3] nums 데이터 중에서 2의 배수만 3을 곱하고 나머지는 원래 값 그대로 하여 새로운 리스트 생성

for num in nums:
    if num % 2 == 0:
        nums2.append(num * 3)
    else:
        nums2.append(num)

# list Comprehension
nums22 = [num * 3 if num % 2 == 0 else num for num in nums ] #---> else 사용시 True조건식이 for문 앞으로 온다.

print(nums2, nums22)
