# [ PATH : 경로 ]-----------------------------------------------------------------------------------
# 절대경로 : 파일 및 폴더 존재하는 위치의 경로 예) C:\WUsers\anece\...
# 상대경로 : 현재 코드 파일 기준으로 경로를 지정
#  . -> 현재 위치
# .. -> 상위 한단계 위
filename=r'C:\Program Files\HP\Shared' # 절대경로 : 문장 가장 앞의 r로 이 문장에 이스케이프 문자 없도록 만들기.
filename='../Data/home.html'           # 상대경로1
filename= 'html/home.html'  # 상대경로2

# [문제 1. home.html 파일을 라인 단위로 읽어서 화면에 출력하기 ]
file=open('./html/home.html','r',encoding='utf8') # 인코딩 오류 시, encoding='utf8' 로 해결.
while True:
    line=file.readline()
    if not line: break
    line=line.strip() # strip: 양쪽 공백 제거 -> 들여쓰기 삭제, 줄 띄어쓰기 1줄 줄어듬.
    if len(line)>0:print(line) # 아무 것도 없는 라인은 표시하지 않음.
file.close()

# [ with ~ as 구문 ] -> close를 하지 않아도 됨.
with open(filename,mode='r',encoding='utf8') as file: # 경로 이름을 file로 하면 오류 발생함.
    while True:
        line = file.readline()
        if not line: break
        line = line.strip()  # strip: 양쪽 공백 제거 -> 들여쓰기 삭제, 줄 띄어쓰기 1줄 줄어듬.
        if len(line) > 0: print(line)  # 아무 것도 없는 라인은 표시하지 않음.
