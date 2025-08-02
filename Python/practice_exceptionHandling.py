## 예외 처리 (try-except)

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
    return wrapper

# 계산기
@print_error_line
def calc():
    print("나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))       # 입력값으로 숫자가 아닌 문자가 오는 경우 ValueError가 발생.
    print("{0} / {1} = {2}".format(num1, num2,int(num1/num2)))

calc()