# [ File & Dir 관련 모듈 ] ----------------------------------------------------------------------
import os.path as path
import os

# [ 1.특정 폴더 존재 여부 => 폴더 없으면 폴더 생성하기 : os.mkdir, os.makedirs]
import time

DIR_PATH='./DATA'
#print(path.exists(DIR_PATH))
DIR_PATH='./Image/jpg'
if not path.exists(DIR_PATH) :
#    os.mkdir(DIR_PATH)            # os.mkdir : 1개 폴더 생성
    os.makedirs(DIR_PATH)          # os.makedirs : 하위 폴더까지 생성

# [ 2.특정 파일 존재 여부 체크 : path.exist]
DATA_FILE=DIR_PATH+'/flower.jpg';
if not path.exists(DATA_FILE):
    print('파일 없음')

# [ 3.폴더 경로안에 존재하는 내용 리스트화 : os.listdir]
datalist=os.listdir('./AddAddressBook')
print(datalist)

# [ 4. 시간 관련 모듈 time]
import time as t

print(t.time())
print(t.localtime(t.time()))

curTime=t.localtime(t.time())
print(curTime.tm_year,curTime.tm_hour,curTime.tm_wday)

# [ 5. 일정 시간 간격 두고 루프 : time.sleep()]
for num in range(10):
    t.sleep(1.0)
    print('[num]', end='')