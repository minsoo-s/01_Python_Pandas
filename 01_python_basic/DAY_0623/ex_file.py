# [ 파일 입출력(I/O) -> 파일 읽고 쓰기]-------------------------------------------------------------------------------------
filename= 'mydata.txt'

# [1. 파일 쓰기 ]--------------------------------------------------------------------------------=---------
# (1) 파일 열기
# mode 종류: r,w,a
# mode 'w' => 파일 없으면 생성 후 쓰기
#          => 파일 있으면 내용 지우고 쓰기
# mode 'a' => 파일 없으면 생성 후 쓰기
#          => 파일 있으면 덧붙이기(append)
file=open(filename, 'a', encoding='utf-8')

# (2) 파일에 데이터 쓰기(.write())
file.write('Good\n')
file.write('Bye\n')
file.write('12345\n')

# (3) 파일 닫기(.close())
file.close()

# [2. 파일 읽기 ]---------------------------------------------------------------------------------------------------
# mode='r' => read
# (1) 파일 열기
file=open(filename,'r')
# (2) 파일 읽기
# ● 파일 전체 데이터 가져오기 (문자개수를 적으면 그 문자까지만 읽음)
data1=file.read()
print(f'read data1 => {data1}')
print(f'read data1 type => {type(data1)}')

file.seek(0) # 파일포인트(커서?)를 제일 앞으로 이동시킴.
data2=file.read() # data1에서 처음부터 끝까지 읽었기 때문에 data2는 빈공간이 된다. 그래서 seek(0) 필요.
print(f'read data2 => {data2} len={len(data2)}')

# 파일 포인트 제일 앞으로 이동(.seek())
file.seek(0)
# ● 파일에서 1줄 읽기 (.readline())
data3=file.readline()
print(f'read data3 => {data3}')
data3=file.readline()
print(f'read data3 => {data3}')
data3=file.readline()
print(f'read data3 => {data3}')

# ● 한 줄씩 읽어서 리스트에 담아서 가져오기(.readlines())
data4=file.readlines()
print(f'read data4 => {data4}')
# (3) 파일 닫기
file.close()