#--------------------------------------------------------------------------
# 문제 1) BMI 건강지수 프로그램 만들기
# - 키와 몸무게를 입력하면 '저체중, 정상, 과체중' 결과를 알려주는 프로그램 작성 (BMI공식 참고)
# - BMI= 몸무게[kg]/키**2[m]
# - 0 저체중 ／ 18.5 정상 | 23 과체중 ／ 25 경도비만 | 30 중등도비만
#--------------------------------------------------------------------------
print("-"*40)
print(f' BMI 건강지수 프로그램')
print("-"*40)

# [1] 키, 몸무게 입력받기
height=input("키를 입력해주세요(cm) :")
weight=input("몸무게를 입력해주세요(kg) :")
height=float(height)
height=height/100
weight=float(weight)

# [2] 입력받은 값 확인
print(f'신장: {height}[m],몸무게:{weight}[kg]')

#[3] BMI 계산
BMI=weight/height**2
BMI=int(BMI)

#[4] BMI 건강지수 출력
if BMI < 18.5:
    print("-" * 40)
    print(f'당신의 BMI는 {BMI}이므로 저체중입니다.')
elif BMI <23:
    print("-" * 40)
    print(f'당신의 BMI는 {BMI}이므로 정상입니다.')
elif BMI<25:
    print("-" * 40)
    print(f'당신의 BMI는 {BMI}이므로 과체중입니다.')
elif BMI<30:
    print("-" * 40)
    print(f'당신의 BMI는 {BMI}이므로 경도비만입니다.')
else:
    print("-" * 40)
    print(f'당신의 BMI는 {BMI}이므로 중등도비만입니다.')
