# -----------------------------------------------------------------------
# 리스트 데이터의 요소를 모두 출력
# -----------------------------------------------------------------------
# 1~50 범위에서 3의 배수로 구성된 데이터 만들기

print('---- for문으로 풀어보기 ----')
# for문으로 풀어보기

for num in nums:
    print(num)

# tuple로 구성된 list
print('---- tuple로 구성된 list ----')

a=[(1,2),(3,4),(5,6.)]
for(first, last) in a:
    print(first+last)

# tuble로 구성된 list
print('---- tuble로 구성된 list ----')
a=([1,2],[3,4],[5,6])
for(first, last) in a:
    print(first+last)

# 학생 점수 출력 -------------------------------------------------------
print('---- 학생 점수 출력 ----')
n=1
scores=[87,23,64,87,94,70]
for score in scores:
    print('%d번째 학생 점수 : %d'%(n, score))
    print('{}번째 학생 점수: {}'.format(n,score))
    print(f'{n}번째 학생 점수: {score}')
    n=n+1

#요소와 인덱스를 함께 제공하는 내장함수 = enumerate()
print('---- enumerate() 활용 ----')
for index,score in enumerate(scores):
    print(f'{index+1}번째 학생 점수: {score}')