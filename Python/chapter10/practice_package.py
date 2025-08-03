## 패키지 - 하나의 디렉토리에 모듈들을 모아놓은 집합
## 패키지, 모듈 위치

'''
import travel.thailand      # 주의점 - import의 맨 뒷부분은 모듈이나 패키지만 가능하다. 만약 from A import B의 구조(A - 모듈)라면 B에 클래스 함수가 올 수 있다.

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
'''

'''
from travel import vietnam

trip_to = vietnam.VietnamePackage()
trip_to.detail()
'''

'''
# from random import *
from travel import *    # travel 패키지 속 모든 것을 가져온다는 뜻이긴 하지만 공개할지 비공개할지는 설정해 주어야 한다.

trip_toV = vietnam.VietnamePackage()
trip_toV.detail()
print(vietnam.__name__)     # 모듈의 이름을 담고 있는 특별한 변수? - 해당 파일 직접 실행 -> __name__ = "__main__", import되어 실행 -> __name__ = "모듈명" or "패키지.모듈명"

trip_toT = thailand.ThailandPackage()
trip_toT.detail()
'''

# 어느 위치에 해당 모듈, 패키지가 있는지 확인하기 위해 사용하는 import
import inspect
from travel import *
import random
print(inspect.getfile(random))      # random이라는 파일을 어디서 가져왔는지 출력
print(inspect.getfile(thailand))    # thailand라는 파일을 어디서 가져왔는지 출력