# [조건문과 while 반복문 이해 220525] -----------------------------------
runnumber= input("runnumber: ")

if  runnumber=="1":

    #  1. 조건문을 다루는 문제입니다.
    # 1-1. 점수를 입력 받아서 학점(A ~ F )을 출력하는 코드 작성하세요.
    # [입력] 점수를 입력하세요.91
    # [출력] 당신은 ‘A’학점입니다.
    # printf(“점수를 입력하세요.”)
    # scanf(“ % d”)
    #
    # input(“점수를 입력하세요.”)
    score=input("점수를 입력하세요: ")
    score=float(score)
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="F"
    print(f"당신은 {grade}학점입니다.")
    # -------------------------------------------------------------------------
    # 1-2. 다음 데이터를 저장하세요. 그리고 사용자로부터 금액과 통화명을 입력 받아
    # 원화로 환전한 금액을 출력하세요.
    # 통화명  | 환율
    # 달러   | 1167
    # 엔     | 1.096
    # 유로   | 1268
    # 위안   | 171
    # [입력 ] 금액 및 통화명: 100달러
    # [출력] 환전 금액: 116700.00원
    money=input("금액과 통화명 입력(예: 100달러) : ")
    if "달러" in money:
        money=int(money[:money.find("달러")])*1167
        print(f'환전 금액: {money}원')
    elif "엔" in money:
        money=int(money[:money.find("엔")])*1.096
        print(f'환전 금액: {money}원')
    elif "유로" in money:
        money=int(money[:money.find("유로")])*1268
        print(f'환전 금액: {money}원')
    elif "위안" in money:
        money=int(money[:money.find("위안")])*171
        print(f'환전 금액: {money}원')


    #--------------------------------------------------------------------------
    # 1-3. 다음 데이터를 저장하세요.
    # 그리고 사용자로부터 전화번호를 입력 받고 통신사 정보를 출력하세요.
    # 번호 |통신사
    # 011 | SKT
    # 016 | KT
    # 019 | LGU
    # 010 | 알수없음
    # [입력] 전화번호: 016 - 222 - 1234
    # [출력] 통신사 : KT
    num=input("전화 번호를 입력해주세요: " )
    if num[:3]=="011":
        server= "SKT"
    elif num[:3]=="016":
        server= "KT"
    elif num[:3]=="019":
        server= "LGU"
    else:
        server= "알수없음"
    print(f"전화번호: {num}\n통신사: {server}")
    #------------------------------------------------------------------------------
    # 1-4. 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다.
    # 예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.
    # 01234567789
    # 강북구:010,011,012
    # 도봉구:013,014,015
    # 노원구:016,017,018,019
    # 사용자로 부터 5자리 우편번호를 입력받고 구를 판별하여 주세요.
    #  [ 입력 ] 우편번호 : 01500
    #  [ 출력 ] 지 역: 도봉구
    nums=input("우편번호(5자리) : ")
    if nums[2]=="0" or nums[2]=="1" or nums[2]=="2" :
        print(f"지역: 강북구")
    elif nums[2]=="3" or nums[2]=="4" or nums[2]=="5" :
        print(f"지역: 도봉구")
    else:
        print(f"지역: 노원구")
    #-----------------------------------------------------------------------
    # 1-5. 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데,
    # 1, 3은 남자   2, 4는 여자를 의미한다.
    # 사용자로부터 13자리의 주민등록번호를 입력 받은 후
    # 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
    #  [ 입력 ] 주민번호 : 990103-1079700
    #  [ 출력 ] 성 별 : 남자
    #  나 이 : 24세

    nums=input("주민등록번호 입력(예시:901212-1234567): ")
    if nums[7]== "1" or nums[7]== "3":
        print("성별 : 남자")
    else:
        print("성별 : 여자")
    #-----------------------------------------------------------------------
    # 1-6. 컴퓨터와 가위바위보 게임 프로그램을 구현하자.
    #  조건1 - 컴퓨터에서 가위바위보 중 하나 선정
    #  조건2 - 사용자 입력 값과 선정된 값 비교 후 결과 출력
    #  [ 입력 ] [사용자] 가위바위보~ : 가위
    #  [ 출력 ] [결 과] 당신이 졌군요ㅜㅜ
    #  [ 입력 ] [사용자] 가위바위보~ : 보
    #  [ 출력 ] [결 과] 축하 축하 당신이 이겼어요 ^^
    #  [ 입력 ] [사용자] 가위바위보~ : 바위
    #  [ 출력 ] [결 과] 비겼답니다~
    what=input("가위바위보~ :")
    com= "가위"
    if what=="가위":
        print('비겼답니다~')
    elif what=="바위":
        print('축하 축하 당신이 이겼어요 ^^')
    else:
        print("당신이 졌군요ㅠㅠ")
    #-----------------------------------------------------------------------



elif runnumber=="2":
    # 2. while 반복문에 대한 문제입니다.
    # 2 - 1.
    # fruits = ["사과", "귤", "수박", “딸기”, “바나나”]에서 요소를
    # while 반복문 사용하여 모두 출력하세요.
    fruits = ['사과', '귤', '수박', '딸기', '바나나']
    n=0
    while n<len(fruits):
        print(fruits[n])
        n=n+1

    #-------------------------------------------------------------------------
    # 2-2. 1~10000 범위에서 3의 배수와 7의 배수로 데이터를 저장한 후
    # 모든 요소를 출력하는 코드를 while 반복문을 사용하여 작성하세요.
    #num3=set(range(3,10001,3))
    #num7=set(range(7,10001,7))
    #nums=num3|num7
    #print(nums)

    nums=list(range(1,10001))
    num3=[]
    count=0
    while count<10000:
        if nums[count]%3==0:
            num3.append(nums[count])
        count=count+1
    print(f"3의 배수: {num3}")

    num7=[]
    count=0
    while count<10000:
        if nums[count]%7==0:
            num7.append(nums[count])
        count=count+1
    print(f'7의 배수: {num7}')

    count=0
    numall=num3+num7
    while count< len(num3+num7):
        print(numall[count])
        count=count+1

#------------------------------------------------------------------------
    # 2 - 3.
    # dataEng = [‘Happy’, ‘Good’, ‘Dog’, ‘Cat’] 데이터에서 모든 요소를
    # 소문자로 출력하는 코드를 while 반복문을 사용하여 작성하세요.
    dataEng = ["Happy", "Good", "Dog", "Cat"]
    dataEng2=[]
    count=0
    while count<len(dataEng):
        dataEng2.append(dataEng[count].lower())
        print(dataEng2[count])
        count=count+1


    # 2 - 4.
    # com = ["SK하이닉스", "삼성전자", "LG전자", “카카오”]
    # 모든 요소 길이를 출력 하는 코드를 while 반복문을 사용하여 작성하세요.
    com = ["SK하이닉스", "삼성전자", "LG전자", "카카오"]
    count=0
    com2=[]
    while count<len(com):
        com2.append(com[count])
        print(f'{com[count]}의 길이:{len(com[count])}')
        count=count+1

    # count=0
    # com3=[]
    # while count<len(com):
    #     com3=com[count]
    #     print(f'{com[count]}의 길이:{len(com[count])}')
    #     count = count + 1
    #-------------------------------------------------------------------------

    # 2 - 5.
    # numList = [13, 21, 12, 14, 30, 18, 9, 2, 3, 8, 11, 23] 에서
    # 짝수번째 요소만 모두 더한 결과를 출력하는 코드를 while 반복문을 사용하여 작성하세요.
    numList = [13, 21, 12, 14, 30, 18, 9, 2, 3, 8, 11, 23]
    count=0
    num2=0
    while count<len(numList):
        if numList[count]%2==0:
            num2=num2+numList[count]
        count=count+1
    print(num2)
    #-----------------------------------------------------------------------

    # 2 - 6. 사용자로부터 원하는 단을 입력 받아서 해당 구구단을 출력하세요.
    # [입력] 좋아하는 단: 3
    # [출력]
    # === 3단 ===
    # 3 * 1 = 3
    # 3 * 2 = 6
    # .....
    # 3 * 9 = 27
    dan=input("좋아하는 단: ")
    dan=int(dan)
    gugu=list(range(1,10))
    count=0
    print(f"=== {dan}단 ===")
    while count<len(gugu):
        result=dan*gugu[count]
        print(f"{dan} * {gugu[count]} = {result}")
        count=count+1
    #--------------------------------------------------------------------------

    # 2-7. 컴퓨터와 업-다운 게임 프로그램을 구현하자.
    # 조건1 - 컴퓨터에서 임의의 자연수를 하나 선정
    # 조건2 - 사용자 입력 숫자와 선정된 자연수가 동일한면 입력 받기 중단
    # 조건3 - 사용자 입력 숫자가 선정 자연수보다 큰 수 인지 작은 수 인지 힌트 출력
    #  [ 입력 ] 빙고 넘버 : 3
    #  [ 출력 ] 힌트 - 3보다 큰 수
    #  [ 입력 ] 빙고 넘버 : 5
    #  [ 출력 ] 힌트 - 5보다 작은 수
    #  [ 입력 ] 빙고 넘버 : 4
    #  [ 출력 ] 정답 - *~ 빙고 ~*
    user=input("숫자를 고르세요: ")
    user=int(user)
    com=4
    while user:
        if user> com:
            print(f"{user}보다 작은 수")
            user = input("숫자를 고르세요: ")
            user = int(user)
        elif user< com:
            print(f"{user}보다 큰 수")
            user = input("숫자를 고르세요: ")
            user = int(user)
        else:
            print("정답~ *~ 빙고 ~*")
            break
        #---------------------------------------------------------------------

    #2-8.
    # 로또 게임 프로그램을 구현 후 로또 번호 출력하세요.
    # 조건1 – 1 ~ 45 범위의 자연수
    # 조건2 – 6개의 자연수 추출
    # 조건3 – 6개 자연수 중복 불가
    # [ 출력 ] 오늘의 로또 번호 추천 => 9 4 12 45 1 28
    import random                 # ---> import random
    rand_num=random.randint(1,45) #      변수 = random.randint(~,~) : ~이상 ~이하의 정수를 랜덤 불러옴.
    result=[]
    while rand_num:
        rand_num = random.randint(1, 45)
        result.append(rand_num)

        if len(list(set(result)))==6:
            break
    print(f'오늘의 로또 번호 추천 => {list(set(result))}') #-> 중복 제거를 위해 list-> set-> list로 변환