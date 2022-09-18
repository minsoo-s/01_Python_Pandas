YEAR=2022

def printYear():
    print(f'올해는 {YEAR}')

# for i in range(5): # 위 모듈을 다른 파일에서 사용할 시, 이 코드까지 실행되는 문제점이 있음
#    printYear()

# [ __name__ 활용 ]
print(f'[ex_func]__name => {__name__}') #[ex_func]__name => ex_main : 현재 파일에서 실행할 때 모습
                                        #[ex_func]__name => ex_func : 다른 파일에서 사용될 떄 모습

if __name__=='__main__':                # __name__ 으로 파일 구별해서 동작 제어.
    for i in range(5): printYear()
    print(f'[ex_func]__name => {__name__}')
