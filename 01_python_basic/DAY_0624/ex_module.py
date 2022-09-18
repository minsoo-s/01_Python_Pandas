# [ 모듈(Module) ] ----------------------------------------------------------------------------------
# - 하나의 파이썬(.py) 파일
# - 특정 목적에 관련된 변수, 함수, 클래스 존재
# - 필요한 파일에서 사용 가능함.
# ◎ 사용법 : import 모듈명
#---------------------------------------------------------------------------------------------------
# Python Standard Library에서 탐색해서 사용할 것.
# 1.모듈 포함하기                               # math우클릭-> goto -> implementation:설명
# import math                                # 전체 모듈 불러오기 : math.~
# import math as m                           # 모듈명 간소화 : math.~ -> m.~
# from math import factorial                 # 낱개 모듈기능 불러오기 : m.작성하지 않아도 됨.

# 2.모듈 안의 기능 사용하기
# print(math.factorial(5))
# print(m.factorial(5))
# print(factorial(5))

#from math import *                          # 형태로 사용시, 내장 모듈 vs 사용자 정의 모듈 겹칠 떄, 사용자 모듈부터 동작.

import ex_func
print(ex_func.YEAR, ex_func.printYear())     # 사용자 정의 모듈 예시


