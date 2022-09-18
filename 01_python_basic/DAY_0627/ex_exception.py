# [ EXCEPTION Handling : 예외 처리 ]
# - 프로그램 실행 시 발생하는 오류(Error)에 대한 처리
# - 오류가 발생해도 멈추지 않는 함수
import fileinput

try:
    num1, num2=10, 0
    print(f'{num1}/{num2 } = {num1/num2}')

except Exception as x:
    print("에러발생".ex)

finally:
    # 오류 발생 상관X
    # 무조건 실행
    print('FINAL')

import os

if os.path.exists("a.jpg"):
    file.open('a.jpg','r')
    print(file.read())
    file.close()

    print(f"에러 발생:{e}")

try:
    file.open('a.jpg','r')
    print(file.read())
    file.close()
except Exception as e:
    print(f"에러 발생:{e}")

