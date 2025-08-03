## 모듈 - 현재 파일과 같이 필요한 부분들이 모인 파일 (유지보수와 코드의 재사용을 위해서 중요하다)

'''
import practice_module_theater

practice_module_theater.price(3)                # 3명이서 영화보러 갔을 때 가격
practice_module_theater.price_morning(4)        # 4명이서 조조할인 영화보러 갔을 때
practice_module_theater.price_soldier(5)        # 5명이서 군인이 영화보러 갔을 때
'''

'''
import practice_module_theater as pmt

pmt.price(3)
pmt.price_morning(4)
pmt.price_soldier(5)
'''

'''
from practice_module_theater import *       # 해당 모듈 안 전부를 그냥 사용하겠다는 의미

price(3)
price_morning(4)
price_soldier(5)
'''

"""
from practice_module_theater import price, price_morning
    '''
    해당 모듈 안 price, price_morning 메서드만 사용하겠다는 의미
    import 뒤에는 전역 변수가 와도 된다. 꼭 메서드만 올 수 있는 것은 아니다.
    '''
    price(3)
    price_morning(4)
"""

from practice_module_theater import price_morning as priceM, price_soldier as priceS
# 여러개를 import하면서 이름을 정해주고 싶으면 as와 ,를 이용해주면 된다.
priceM(4)
priceS(5)