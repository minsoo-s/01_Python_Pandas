# [ 벽돌 깨기 프로그램 만들기 ] -------------------------------------------------------------------------------
import tkinter as t

# 게임하는 사람의 정보를 저장하는 변수들
class player:
    def __init__(self, nickname, level=0, score=0, rank=0):
        self.nickname=nickname
        self.level=0
        self.score=0
        self.rank=0

    # 클래스의 인스턴스 변수들의 값을 업데이트 또는 읽기 하는 메서드
    # set 메서드 - get 메서드
    def setNickname(self, Nickname):
        self.Nickname = Nickname
    def setlevel(self, level):
        self.level=level
    def setScore(self, score):
        self.score=score
    def setRank(self, rank):
        self.rank=rank
    def setUpdate(self, level, score, rank):
        self.level = level
        self.score = score
        self.rank = rank

    def getNickname(self):
        return self.nickname
    def getLevel(self):
        return self.nickname
    def getScore(self):
        return self.nickname
    def getRank(self):
        return self.nickname

print(player("a"))

player1=None
player2=None

# 게임하는 사람의 정보 입력 받기
# 함 수 명 : setPlayer
# 파라미터 :
# 반 환 값 : 없음
def setPlayer():
    global player1,player2
    nickName = input("닉네임: ").split(",")
    if player1 == None:
        player1= player(nickName)
    else:
        player2 =player(nickName)

# 메뉴 출력하기
# 함수명 : displatMenu
# 파라미터 : 없음
# 반환값 : 없음
def dispalyMenu():
    print('1.회원가입')
    print('2.게임시작')
    print('3.랭킹보기')
    print('4.종   료')

def palyGame():
    level=3
    score=14
    rank=22

# 프로그램 코드---------------------------------------------------------------------------------------------
while True:
    dispalyMenu()
    select=input("메뉴 선택: ")
    if select == '4':
        # 파일에 기록 후 종료
        break
    elif select=='1' :
        setPlayer()
    elif select=='2':
        playGame()
