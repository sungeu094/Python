## 튜플 (내용 변경이나 추가는 불가능하지만 속도가 list보다 빠르기 때문에 변경되지 않는 목록에 사용)

menu = ("돈가스", "치즈까스")
print(menu[0])
print(menu[1])

'''
menu.add("생선까스") # 튜플은 추가나 삭제가 불가능.
'''

'''
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)
'''


(name,age,hobby) = ("김종국", 20, "코딩")   # 변수 지정할 때 한번에 가능
print(name,age,hobby)