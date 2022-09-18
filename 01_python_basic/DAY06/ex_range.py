# [범위] --------------------------------------------------------------
# range(시작숫자,끝숫자+1,간격) =>수의 범위 즉, ~부터 ~까지 라는 범위 설정하는 함수
# 기본값: 시작숫자=0, 간격=1
# 내장함수임. (메서드 X)
# range, list 변환 가능.
# range를 통해 방대한 양의 list를 쉽게 제작 가능.
#---------------------------------------------------------------------
# 1~100까지 정수로 구성된 리스트를 생성하기.
nums=[1,2,3,4,...,100]
nums=range(1,101) #---> 1~100 범위지정.
print(nums, type(nums),nums[0],nums[-1])
nums=list(range(1,101)) #---> range를 list로 변환
print(nums, type(nums),nums[0],nums[-1])
nums=range(101) #---> 시작 숫자 생략
print(nums, type(nums),nums[0],nums[-1])

# Q) 1~10 범위에서 2의 배수만 출력 ---> 2,4,6,8,10
nums=list(range(2,11,2))
print(nums, type(nums),nums[0],nums[-1])

# Q) 1~50 범위에서 7의 배수만 리스트로 출력
nums=list(range(7,51,7))
print(nums, type(nums),nums[0],nums[-1])
