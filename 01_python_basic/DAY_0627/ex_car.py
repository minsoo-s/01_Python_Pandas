# [ Q. Class 생성 : 현대자동차를 표현하는 데이터 타입 ]
# 클래스명 : Car
# 속성/특징 : 제조사, 차번호, 차종류, 색상       -> 변수
# 역할/기능 : 이동한다, 정지한다, 차정보 출력한다. -> 함수

# 변 수)
# 함 수) 이동: (차번호)를 (장소1)에서 (장소2)로 이동했다.
#       정지: (차번호)를 (장소)에서  정지했다.
#       정보: (제조사),(차번호),(차종류),(색상)

class Car:
    company="현대자동차"

    def __init__(self,num,name,color):
        self.num=num
        self.name=name
        self.color=color

    def goto(self,go,to):
        print(f"{self.num}번호 차량이 {go}에서 {to}으로 이동했다.")

    def stop(self,to):
        print(f"{self.num}번호 차량이 {to}에서 정지했다.")

    def info(self):
        print(f"제조사: {Car.company}")
        print(f"차번호: {self.num}")
        print(f"차종류: {self.name}")
        print(f"색상  : {self.color}")

C1 = Car("가1234","그랜저","블랙")
C2 = Car("나3423","아반테","화이트")
C3 = Car("다2020","모닝","그레이")

C1.goto("집","학교")
C2.stop("하늘")
C3.info()


# nums=[]
# for n in range(10):nums.append(n*10)
#
# cars=[]
# for n in range(10):
#     num, type, color=input("차번호, 차종류, 차색상: ").split(',')
#     cars.append(Car(num,type,color))
#
# for car in cars:
#     print(f"{Car.Num}")
#     car.use()
