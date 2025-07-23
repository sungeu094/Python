## 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

famousPerson = ["유재석", "조세호", "박명수"]
print(famousPerson)
print(repr(famousPerson))
print(famousPerson.__repr__())
print(str(famousPerson))  # repr(), str()과 같은 코드들은 object에서 메서드로 구현이 되어 있기 때문에 자식들인 list, str과 같은 곳에서도 사용이 가능함. 하지만 해당 코드들은 C로 구현이 되어있기 때문에 ...으로 되어있어서 직접 확인하기 어려움. 실제 동작은 CPython의 C 소스코드에 들어있음.

print(famousPerson.index("조세호"))

famousPerson.append("하하")
print(famousPerson)
# 하하를 배열 제일 뒤에 넣기

famousPerson.insert(1, "정형돈")
print(famousPerson)
# 정형돈을 유재석과 조세호 사이에 끼우기

print(famousPerson.pop())
print(famousPerson)
# 배열에 있는 사람을 한 명씩 뒤에서 꺼냄

famousPerson.append("유재석")
print(famousPerson)
print(famousPerson.count("유재석"))
# 같은 이름의 사람이 몇 명 있는지 확인

num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)     # 정렬
num_list.reverse()
print(num_list)     # 역순 정렬
'''
num_list.clear()
print(num_list)     # list속 모든 내용 삭제
'''

mix_list = ["조세호", 20, True]
print(mix_list)
# 자료형에 구애받지 않고, 섞어서 list 만들기 가능

num_list.extend(mix_list)
print(num_list)
#리스트 확장
 