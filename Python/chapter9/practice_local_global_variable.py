## 지역 변수 (함수 내에서만 사용 가능한 변수) && 전역 변수 (프로그램 어디서나 부를 수 있는 변수)

'''
gun = 10

def checkpoint(soliders):
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

# 에러 발생 : 현재 checkpoint 함수에서는 gun이라는 값이 정의되지 않았기 때문이다. 현재 코드 형태로는 전역 변수를 함수 내에서 사용하려고 했던건데 그러려면 전역 변수임을 의미하는 코드가 추가적으로 필요하다.
'''

gun = 10

def checkpoint(soliders):
    global gun  # 전역 공간에 있는 gun을 해당 함수에서 사용하겠다는 뜻이다.
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soliders):
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))

# checkpoint(2)
gun = checkpoint_ret(gun,2)         # 전역변수를 많이 쓰면 코드 관리가 어려워지기 때문에 파라미터로 계산하는게 제일 좋은 방법이다.

print("남은 총 : {0}".format(gun))

