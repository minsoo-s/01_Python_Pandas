# -------------------------------------------------------------------------
# 집합 자료형(set) 전용의 함수 => 메서드 (add, update, remove)
# --------------------------------------------------------------------------

# 비어 있은 set 객체 변수 생성
datas=set()

# 비어 있는 set 객체에 데이터 한 개씩 넣기 => add(데이터)
datas.add(10)
datas.add(4)
datas.add(4) #---> 중복은 하나만 들어감.
datas.add(2)
print(f'datas 갯수: {len(datas)}  데이터 : {datas}')

# update => 여러 개의 데이터를 한 번에 넣기
datas.update([1,2,3,4,5,6])
print(f'datas 갯수: {len(datas)}  데이터 : {datas}')

datas.update("good")
print(f'datas 갯수: {len(datas)}  데이터 : {datas}')

# remove => 요소 제거하는 메서드
datas.remove('d')
datas.remove(1)
print(f'datas 갯수: {len(datas)}  데이터 : {datas}')