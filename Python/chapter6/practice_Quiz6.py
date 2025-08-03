'''
Quiz) 표준 체중을 구하는 프로그램을 작성하시오

* 표준 체중 : 각 개인의 키에 적당한 체중

(성별에 따른 공식)
남자 : 키(m) * 키(m) * 22
여자 : 키(m) * 키(m) * 21

조건 1 : 표준 체중은 별도의 함수 내에서 계산
        * 함수명 : std_weight
        * 전달값 : 키(height), 성별(gender)

조건 2 : 표준 체중은 소수점 둘째자리까지 표시

(출력 예제)
키 175cm 남자의 표준 체중은 67.38kg 입니다.

'''
#Solution
from math import *
def std_weight(height, gender) : 
    height /= 100
    if gender == "여자" :
        differenceMul = 21
    else:
        differenceMul = 22

    return pow(height,2)* differenceMul

height = 175
gender = "남자"

print("키 {0}cm {1}의 표준 체중은 {2:.2f}kg 입니다.".format(height, gender, std_weight(height,gender)))
'''
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, round(std_weight(height,gender),2)))
# round를 쓸 때 95 -> 100처럼 정수형을 반올림하고 싶으면 10단위로 -1씩 늘려가면 된다.(Ex. 100단위 반올림은 -2)

'''