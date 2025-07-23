## 문자열 처리 함수

python = "Python is Amazing"
print(python.upper())   # 해당 문자열을 대문자로 변화
print(python.lower())   # 해당 문자열을 소문자로 변화

print(python[0].isupper())  # 해당 문자가 대문자인지 체크
print(python[0].islower())  # 해당 문자가 소문자인지 체크

print(len(python))  # python 길이 반환

print(python.replace("Python", "Java")) # 첫번째 인자 값을 두번째 인자 값으로 교환

index = python.index("n")
print(index)    # 문자의 index를 확인

index = python.index("n", index + 1)
print(index)

print(python.find("java"))
# print(python.index("java"))  """ find에서는 원하는 값이 없을 경우 -1을 반환하지만 index는 에러를 반환한다."""

print(python.count("n"))    # n이 총 몇번 등장하는지 확인
