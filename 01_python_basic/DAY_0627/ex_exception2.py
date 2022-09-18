# [ 프로그램 기능 구현상 강제로 예외 발생시키기 ]-----------------------------------------------------
# raise 예외 객체
num=int(input("3의 배수 입력 : "))
try:
    if num%3 !=0:
        print(f"{num}은 3의 배수가 아닙니다.")
        raise Exception("3의 배수 오류")
except Exception:
    print('ERROR 발생')

class Bird:
    def fly(self):
        raise NotImplementedError # fly함수 오버라이딩 꼭 해라.(강제 오버라이딩)

class Eagle(Bird):
    pass

    # def fly(self):    예외처리 없어짐.
    #     print('Aaaa')
e=Eagle()
e.fly()