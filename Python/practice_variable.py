## 변수

# 애완동물 소개.
print("강아지의 이름은 A이다.")
print("A는 4살이며, 산책을 아주 좋아한다")
print("A는 어른일까? True")
'''
만약 A가 아닌 다른 이름이라면 결국 바꿔줘야 한다.
하지만 해당 코드에서는 한번에 바꿔줄 수 없다.
그렇기 때문에 변수를 사용한다.
'''

animal = "강아지"
name = "A"
age = 4
hobby = "산책"
is_adult = age >= 3
print(animal + "의 이름은 " + name + "이다.")
name = "B" 
# 변수값을 변화시키면 뒷 코드부터는 해당 변수값이 사용된다.

print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아한다") 
# 정수형을 출력하기 위해서 문자형으로 바꿔주는 것이다. 정수형이든 불 자료형이 제일 앞에 위치한다고 하더라도 문자형과 같이 사용하려면 str()을 사용해야 한다.

print(name, "는 어른일까? ", is_adult)
# 하지만 만약 + 대신 ,를 사용한다면 문자형 간의 띄어쓰기가 발생하긴 하지만 불 자료형, 정수형과 같은 문자형이 아닌 것을 꼭 str()을 이용해서 문자형으로 바꾸지 않아도 된다.


