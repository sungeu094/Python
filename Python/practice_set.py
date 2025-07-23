## 집합 (중복 X, 순서 X)

my_set = {1,2,3,3,3}    # list = [1,2,3,3,3]    dict = {key : value, key : value}, tuple = (1,2,3)
print(my_set)           # 중복이 허용되지 않기 때문에 중복 값은 없어짐

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])      # 다른 set 정의 방법

print(java & python)
print(java.intersection(python))
# 교집합(java와 python을 둘 다 할 수 있는 개발자)

print(java | python)
print(java.union(python))
# 합집합(java나 python 둘 중 하나 이상 할 수 있는 개발자)

print(java - python)
print(java.difference(python))
# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)

java.remove("김태호")
print(java)
python.add("김태호")
print(python)
# 집합(set)은 추가&삭제가 가능

