## 숫자 처리 함수

print(abs(-5))  # 절대값
print(pow(4,2)) # (첫번째 인자) ^ (두번째 인자)
print(max(5,12))    # 두 인자 값 중 큰 값
print(min(5,12))    # 두 인자 값 중 작은 값
print(round(3.14))  # 반올림
print(round(3.141592, 2))  # 소수점 둘째 자리에서 반올림
print(sum([1,2,3,4,5]))  # 합계
print(sum(range(1, 11)))  # 1부터 10까지의 합계
print(divmod(7, 3))  # (몫, 나머지) 튜플로 반환

from math import *  # math 라이브러리의 모든 함수와 변수 가져오기
print(floor(4.99))  # 내림
print(ceil(3.01))   # 올림
print(sqrt(16))  # 제곱근 변환 (하지만 float 자료형이기 때문에 int로 변환하려면  int() 사용)
print(gcd(24, 36))  # 최대공약수  (greatest common divisor)
print(lcm(24, 36))  # 최소공배수  (least common multiple)
print(factorial(5))  # 5! (5 팩토리얼)
print(pi)  # 원주율
print(e)  # 자연상수 e
print(sin(pi / 2))  # sin 함수
print(cos(pi))  # cos 함수
print(tan(pi / 4))  # tan 함수 (정확한 pi 값을 2진수로 나타낼 수 없기 때문에 오차 발생. round()로 반올림 가능)
print(log(100, 10))  # 로그 함수 (밑이 10인 로그) - float 자료형
print(log2(8))  # 밑이 2인 로그 - float 자료형
print(log10(1000))  # 밑이 10인 로그 - float 자료형