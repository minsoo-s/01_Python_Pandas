# [ 변수의 스코프(Scope) ]--------------------------------------------------------------------
# - 지역변수(local Variable) : 함수에서만 사용, 파라미터, 함수 안에 변수들
# - 전역변수(Global Variable) : 파이썬 파일 안에 있는 변수,
#                              같은 파이썬 파일 안에 있는 함수에서 사용 가능.

isGame = False

# 게임 시작을 알리는 함수
def startGame():
    global isGame               # 지역변수 변경 : 함수 안에서 지역변수 변경-> 전역변수 변경으로 이어지려면 global 사용
    print('*** 게 임 시 작 ***')
    isGame = True

# 게임 화면을 그리는 함수
# 게임 중 O => 게임판 그리기
# 게임 중 X => 준비중 그리기
def drawGame():
    if isGame :                # 전역변수 불러오기 : 자기 안에 해당 지역변수가 없다면, 전역변수 불러옴. (!)불러오기만 하면 global 필요X
        print('************')
        print('*          *')
        print('*          *')
        print('*          *')
        print('*          *')
        print('************')
    else:
        print('* 준 비 중 *')

# 테스트
drawGame()
startGame()
drawGame()