## 반복문

#반복문 안 쓸 때
'''
print("대기번호 : 1")
print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")
'''

# for문 사용할 때
for waiting_num in [1,2,3,4]:
    print("대기번호 : {0}".format(waiting_num))     # for A in B에서 B에는 반복 가능한 객체라면 모두 사용 가능하다.(Ex. tuple, string, set, range ..)
print()

for waiting_num1 in {1,2,3,3,4,5,3}:
    print("대기번호 : {0}".format(waiting_num1))    # set으로 할 경우 중복 허용이 안되기 때문에 중복되는 요소 삭제 후 값 계산
print()

for (waiting_person, waiting_num2) in {"A" : 1, "B" : 2, "C" : 3}.items():
    print("성함 : {0}, 대기번호 : {1}".format(waiting_person, waiting_num2))
print()
'''
동일한 결과 발생시키는 코드
waiting = {"A" : 1, "B" : 2, "C" : 3}
for name in waiting:
    print("성함 : {0}, 대기번호 : {1}".format(name, waiting[name]))
print()
'''

for waiting_num3 in range(1,6):
    print("대기번호 : {0}".format(waiting_num3))    # 1부터 5까지의 값이 나오도록 해준다.
print()

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks :
    print("{0}, 커피가 준비되었습니다.".format(customer))
print()