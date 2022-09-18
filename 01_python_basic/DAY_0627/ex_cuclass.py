# [ 사용자 정의 클래스 ]------------------------------------------------------------------------------

# [ Q1 ] Class 만들기 : 학생을 표현하는 데이터 타입
# - 변수(필드/속성) : 학교, 학년, 반 , 성적
# - 함수(메서드) : 공부, 등교, 시험

# school Student:
#     def __init__(self,school,grade,classroom,score):
#         self.school=school
#         self.grade=grade
#         self.classroom=classroom
#         self.score=score
#     def goto(self,school,grade,classroom):
#         print(f" 저는{school} {grade}학년 {classroom}반으로 등교합니다.")

# [ 강사님 답 ]
class Student:

    # 클래스 변수 :모든 인스턴스가 함께 사용함. : 메모리 절약을 위해
    school='대구중학교'

    # 인스턴스(객체) 생성 시 초기화 메서드
    def __init__(self,stdNum,yearNum,grade):
        self.stdNum=stdNum
        self.yearNum=yearNum
        self.grade=grade

    # student의 클래스 역할/기능 메서드 : 000이 ~ 과목을 공부한다.
    def study(self,subject):
        print(f"{self.stdNum}은 {subject} 과목을 공부한다.")

    # 000이 000시험을 친다.
    def test(self,title):   # title과 같이 __init__ 외에 추가할 변수만 추가.
        print(f"{self.stdNum}은 {title} 시험을 친다.")

    # 학생 정보 출력 기능 : 학교,학년,학번 정보 출력
    def info(self):
        print(f"학교: {Student.school}")
        print(f"학년: {self.grade}")
        print(f"학번: {self.stdNum}")

# 객체 student 인스턴스(Instance) 생성
S1=Student("std001",4,4)
S2=Student("std002",3,5)
S3=Student("std003",2,10)

S1.test("중간고사")
S1.study("빅데이터")
S1.info()

