## 랜덤 함수

## *를 사용하는 경우는 모든 함수가 import 되는 것이기 때문에 내가 중복되는 이름의 함수를 만들 시 해당 함수를 import하는 경우가 발생할 수 있다.
from random import *

print(random())  # 0.0 이상 1.0 미만의 랜덤 실수
print(random() * 10)    # 0.0 이상 10.0 미만의 랜덤 실수
print(int(random() * 10) + 1)   # 1 이상 10 이하의 랜덤 정수

print("로또 번호")
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)
print(int(random() * 45) + 1)

print(randrange(1,46))  # 1 이상 46 미만의 임의의 값 생성
print(randint(1,45))    # 1 이상 45 이하의 임의의 값 생성