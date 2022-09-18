# [ 파이썬 미리 만들어서 제공하는 클래스 ]---------------------------------------------------
# int, float, bool, str, list, tuple, dict, set
num = 123 #int자동   # 실제로는 int() 생성자 실행
num2 = int(444)     # 실제로는 str() 생성자 실행
print(num,num2)

# [ 클래스 만들기 ] ---------------------------------------------------------------------
# -> 평면에 좌표값을 저장하는 데이터
# 클래스명 : Point
# 속성/특징/변수 : x, y
# 역할/기능/함수 : Point 클래스로 메모레이 존재하는 객체(인스턴스) 생성하는 메서드.
# - __init__(self,x,y)
# - 객체(인스턴스)에 값을 읽어주는 메서드 -> get속성명() -> 현재 속성값 반환
# - 객체(인스턴스)에 값을 변경해주는 메서드 -> set속성명(설명값)
# - 내가 원하는 기능 메서드
# --------------------------------------------------------------------------------------
class Point:
   # point 인스턴스를 생성하는 메서드
    def __init__(self,x,y):
        self.x=x
        self.y=y

    # point 인스턴스에 저장된 속성(변수)값 읽어오는 메서드 => getter 메서드
    def getX(self): return self.x
    def getY(self): return self.y
    def getXY(self):return self.x, self.y

   # Point 인스턴스에 저장된 속성(변수) 값 저장하는 메서드 => setter메서드
    def setX(self, x): self.x=x
    def setY(self, y): self.y=y
    def setXY(self,x,y):
       self.x=x
       self.y=y

# [ Point 인스턴스 즉 객체 생성하기 ]
# p1=Point(10,5)
#
# p1.setX(5)
# print(p1.getX(), p1.x)
# print(p1.getX(), p1.x)

    # 내가 원하는 기능의 메서드 ------------------------------------------------------------------------------
    # - Point 인스턴스의 정보 출력하는 메서드(method)
    def showPoint(self):
        print(f" 현재 좌표값({self.x} , {self.y})")

    # Point 인스턴스에 해당하는 좌표를 그리는 메서드
    # x 값 => 가로로 이동. y값 => 다음줄 \n
    def drowPoint(self):
        if self.y >0 : print('_\n' * self.y, end='')
        print(' ' * self.x+' ★ ', end='')

#-----------------------------------------------------------------------------------------------------------
# Point 인스턴스 즉 객체 생성하기
p1=Point(10,5)
p1.drowPoint()

nums=[1,2,3,4,5,6,7,8]
points=[Point(10,10), Point(3,4),Point(4,2),Point(0,0)]

points[0].drowPoint()
points[3].setX(100)
p1.showPoint()
p1.drowPoint()