# 자료구조의 변경


menu = {"커피", "우유", "주스"}

menu = list(menu)
print(menu, type(menu))     # set -> list

menu = set(menu)
print(menu, type(menu))     # list -> set

menu = tuple(menu)
print(menu, type(menu))     # set -> tuple 

menu = list(menu)
print(menu, type(menu))     # tuple -> list

menu = tuple(menu)
print(menu, type(menu))     # list -> tuple

menu = set(menu)
print(menu, type(menu))     # tuple -> set

