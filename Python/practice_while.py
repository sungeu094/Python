## while문
'''
while (조건) :

'''


customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 완료. 호출 {1}번".format(customer, index))
    index -= 1
    if index == 0:
        print("커피가 폐기됨")
print()

'''
멈춤 지시가 없기 때문에 멈추지 않으면 계속해서 코드 진행됨
customer1 = "아이언맨"
index1= 1
while True:
    print("{0}, 커피가 준비됨. 호출 {1}회".format(customer1, index1))
    index1 += 1
'''

customer2 = "그루트"
person = "Unknown"

while person != customer2 :
    print("{0}, 커피가 준비됨".format(customer2))
    person = input("이름? ")
