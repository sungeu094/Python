''' 
의도적인 에러 만들기
사용자 정의 예외처리
finally - 예외처리 구문에서 정상적인 실행이 되든 안되든(에러 발생) 무조건 실행하는 구문
'''
import traceback
# 예외 라인 찾는 데코레이터
def print_error_line(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            tb = traceback.extract_tb(e.__traceback__)
            line = tb[-1].lineno
            error_type = type(e).__name__
            print("[예외 발생] {0} (종류) : {1} (라인) : {2} ".format(e, error_type, line))
            # e가 어떻게 출력되는지 보면 알 수 있듯이 클래스 속 __str__(없으면 __repr__) 메서드가 호출되어 그것의 반환값이 호출된다.
        finally :
            print("계산기 이용 완료")   # 에러가 발생하든 안하든 무조건 실행되는 부분
    return wrapper


class BigNumberError(Exception) :   # Exception class를 상속받음
    def __init__(self, msg):
        self.msg = msg
        
    def __str__(self):
        return self.msg     # Java의 toString()처럼 원하는 값으로 출력되게 만들어주는 역할을 한다.

# 계산기
@print_error_line
def calc():
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        # raise ValueError    ## raise : 어떤 에러인지 정해주기 위한 문법 
        # assert num1 < 10 and num2 < 10, "한 자리 숫자만 입력하세요."    # False시 AssertionError가 발생하게 하는 문법
        raise BigNumberError("한 자리 숫자만 입력하세요.")
    print("{0} / {1} = {2}".format(num1, num2,int(num1/num2)))  # 예외 발생시 해당 문장으로 접근되지 않고, 예외처리를 하게 된다.

calc()