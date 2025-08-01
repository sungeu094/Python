## 다양한 출력 포멧

# 파이썬 format 문자열에서 옵션의 순서 ({채우기 문자}{정렬 옵션}{부호}{자릿수}{콤마})

'''
빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
'''
print("{0: >10}".format(500))   
# 빈 공간은 빈자리에 들어올 문자 의미. '>'는 오른쪽 정렬을 의미, 10은 자리 수 의미


'''
양수일 땐 +로 표시, 음수일 땐 -로 표시
'''
print("{0: >+10}".format(500))   
print("{0: >+10}".format(-500))     # '+'가 있든 없든 동일


'''
왼쪽 정렬하고, 빈칸을 _로 채움
'''
print("{0:_<10}".format(500))


'''
3자리마다 콤마(,)를 찍어주기(,만 넣으면 자동으로 3자리마다 콤마(,)를 찍어준다.)
'''
print("{0:,}".format(10000000000000))
print("{0:+,}".format(10000000000000))


'''
3자리마다 콤마(,)를 찍어주기 & 부호도 붙이기 & 자릿수 확보하기(^)
'''
print("{0:^<+30,}".format(100000000000))


'''
소수점 출력
'''
print("{0:f}".format(5/3))  # 기본적으로 소수점 아래 6자리까지 출력

'''
소수점 특정 자리까지만 표시
'''
print("{0:.2f}".format(5/3))    # 소수점 2째 자리까지만 표시