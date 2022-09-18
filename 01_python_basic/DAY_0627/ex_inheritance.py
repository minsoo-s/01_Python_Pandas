# [ 상속(Inheritance) ] " 재사용 또는 확장 "
# - 기존 클래스의 모든 것을 가져와 사용하는 것
# ● 표 현 : school 클래스명( 클래스명 ):
class A:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def displayInfo(self):
        print(f'A => {self.x}{self.y}')


class B(A):
    def clac(self):
        print(self.x * self.y)

class C(B):
    def add(self):
        print(self.x +self.y)

    # 오버라이딩(overriding) 부모 클래스에 있던 기존 기능을 덮어쓰기.
    def calc(self):
        print(self.x +self.y, self.x *self.y, self.x/ self.y)

b=B(1,2)
b.displayInfo()

c=C(1,2)
c.displayInfo()
c.calc()