## 문자열 포멧

# 방법 1
print("나는 %d살이다." %20)             # 정수를 원할 때 (digit)
print("나는 %s를 좋아한다." %"python")  # 문자열을 원할 때(string)
print("Apple은 %c로 시작한다." %"A")    # 문자를 원할 때(character)

# %s로 변환 가능.
print("나는 %s살이다." %20)
print("나는 %s색과 %s색을 좋아한다." %("파란", "빨간"))


# 방법 2
print("나는 {}살입니다.".format(20))    # 중괄호에 format속 인자를 집어넣기
print("나는 {}색과 {}색을 좋아한다.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아한다.".format("파란", "빨간"))  # {}속 숫자는 몇번째 인자를 가져올지이다.

## format은 객체 메서드이기 때문에 첫 번째 인자로 self(객체 자신)이 들어간다. 즉, str.format(인자)와 동일한 역할이다.
print(str.format("나는 {1}색과 {0}색을 좋아한다.", "파란", "빨간"))


# 방법 3
print("나는 {age}살이며, {color}색을 좋아한다.".format(age = 20, color="빨간")) # 변수처럼 가져올 수 있다.


# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아한다.")   # f-string : 실제 변수 값을 {}속 변수 이름을 통해 사용할 수 있다.
