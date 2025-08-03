'''
Quiz) 당신은 Cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

조건1 : 승객별 운행 소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
조건2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[]  2번째 손님 (소요시간 : 50분)
...
[] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분

'''

# Solution
from random import *

count = 0

for i in range(1,51):
    operateTime = randint(5,50)   # 위의 코드와 동일한 값 발생 
    '''
    operateTime = int(random()*46) + 5  # random()은 정수 난수를 만들 때는 randrange(), randint()를 더 많이 사용하기 때문에 실수 난수를 만들 때 주로 사용된다고 보면 된다.
    '''
    
    isOperate = 5 <= operateTime <= 15
    
    if isOperate:
        count += 1 
    
    print("{0} {1}번째 손님 (소요시간 : {2}분)".format("[0]" if isOperate else "[]", i, operateTime))

print("총 탑승 승객 : {}분".format(count))
