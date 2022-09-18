# [ 문제 1 ] 사용자가 입력한 댓글을 파일로 저장하기-------------------------------------------------
# [조건]
# - 키보드로 댓글 입력받기.
# - 입력 받은 댓글은 누적된다.
# - q 또는 Q 입력시 댓글 입력 종료.
#-------------------------------------------------------------------------------------------
#방법1 : open,close
'''
filename='comment.txt'
file=open(filename,'a',encoding='utf8')
while True:
    user = input("댓글 입력: ")
    if user=='q'or user=='Q':
        break
    else:
        file.write(user+'\n')
file.close()

#방법2 : with ~ as ~
filename='comment.txt'
with open(filename,'a',encoding='utf8') as file:
    while True:
        user=input("댓글 입력: ")
        if user in ['q'or'Q']:break
        file.write(user+'\n')

# [ 문제 2 ]---------------------------------------------------------------------------------------
# [조건]
# - home.html 파일을 복사해서 home.txt 파일로 만들기
# - 함 수 명 : fileCopy
# - 매개변수 : 파일명
# - 반   환 : 없음
#--------------------------------------------------------------------------------------------------
# < 내 답 >
filename='home.html'
def fileCopy(filename):
    file1=open(filename,'r',encoding='utf8')
    data=file1.read()
    file1.close()

    filename = 'home.txt'
    file2=open(filename,'w',encoding='utf8')
    file2.write(data)
    file2.close()
fileCopy(filename)
'''

# < 강사님 답 >
def fileCopy(filename):
    # 원본 파일 열고 데이터 꺼내기
    file1=open(filename,'r',encoding='utf8')
    data=file1.read()
    file1.close()
    
    # 복사본 파일에 데이터 쓰기
    filename=filename[:filename.rindex(".")]+'.txt' #-> 오른쪽에서 첫 번째 콤마 다음부터 모두 가져오기.
    file2=open(filename,'w',encoding='utf8')
    file2.write(data)
    file2.close()
fileCopy('home.html')
fileCopy('../mydata.txt')
fileCopy('a.html')

# < with ~ as ~ :
def fileCopy(filename):
    newfilename=filename[:filename.rindex(".")]+'.txt'

    with open(filename,'r',encoding='utf8') as file1:
        with open(filename,'w',encoding='utf8') as file2:
            file2.write(file1.read())

