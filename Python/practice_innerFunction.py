## 내장 함수
'''
# input : 사용자 입력을 받는 함수
language = input("무슨 언어를 좋아하세요? ")
'''

# dir : 어떤 객체를 넘겨줬을 때 해당 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())

import random   # 외장 함수
print(dir())

import pickle
print(dir())

print(dir(random))

lst = [1,2,3]
print(dir(lst))     # 리스트에서 쓸 수 있는 내용들이 나옴.

name = "Jim"
print(dir(name))
print(help(__name__))
# list of python builtins