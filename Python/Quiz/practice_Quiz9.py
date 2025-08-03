'''
Quiz) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
대기 손님ㅇ의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
시스템 코드를 확인하고 적절한 예외처리 구문을 넣으시오.

조건1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError로 처리
        출력 메시지 : "잘못된 값을 입력하였습니다."

조건2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정
        치킨 소진 시 사용자 정의 에러[SoldOutError]를 발생시키고 프로그램 종료
        출력 메시지 : "재고가 소진되어 더 이상 주문을 받지 않습니다."
      
'''

# Solution
import traceback

def print_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if isinstance(e, SoldoutError):
                raise   # 현재 except 블록에서 잡은 예외를 다시 바깥(상위)으로 전달(재발생)하라는 의미로 데코레이터에서 SoldoutError를 처리하는 것이 아닌 바깥의 try-except에서 해당 예외를 잡을 수 있도록 했따.  
            tb = traceback.extract_tb(e.__traceback__)
            line = tb[-1].lineno
            error_type = type(e).__name__
            # 현재 ValueError일 때만 추가적인 메세지를 출력하면 되기 때문에
            if isinstance(e, ValueError):
                print("잘못된 값을 입력하였습니다.")
            print("[예외 발생] {0} (종류) : {1} (라인) : {2} ".format(e, error_type, line))
        # finally:
        #     print("감사합니다. 다음에 또 이용해주세요.")
    return wrapper

class SoldoutError(Exception):
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
       return self.msg

class ChickenZip :
    def __init__(self, chicken, waiting):
        self.chicken = chicken
        self.waiting = waiting
    
    @print_error    
    def orderChicken(self):    
        print("[남은 치킨 : {0}]".format(self.chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? "))    # int로 해주었기 때문에 만약 숫자가 아닌 문자가 들어오면 ValueError 발생
        if order <= 0:
            raise ValueError
        
        if order > self.chicken:
            print("{0}마리만 주문이 가능합니다.".format(self.chicken))
            print()
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(self.waiting, order))
            self.waiting += 1
            self.chicken -= order
            print()

        if self.chicken == 0:
            raise SoldoutError("재고가 소진되어 더 이상 주문을 받지 않습니다.")


chickenZip = ChickenZip(10,1)
while(True) :
    try:
        chickenZip.orderChicken()
    except SoldoutError as e:
        print(e)
        break