## Continue & Break

absent = [2, 5]
no_book = [7]
for student in range(1,11):
    print("{0}, 책 읽어봐".format(student))
    if student not in absent :      # if문도 in을 사용할 수 있다. (해석 : 리스트 속 포함된 값이라면)
        print("결석처리.")
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지. {0}는 교무실로.".format(student))
        break


a = 3
b = 5
print(a+b)
'''
궁금증 : if문이든 for문이든 함께 오던 in은 무슨 의미인가?

Sol) if-while문에 오는 in과 for문에 오는 in은 동작이 다르다.

if-while문의 in은 연산자로 멤버십 연산자라고 한다. 멤버십 연산자는 특정 값이 시퀀스(데이터가 나열된 자료형)에 포함되는지 확인하는 연산자이다. 해당 연산자를 사용하면 내부적으로 해당 객체의 __contains()__를 호출한다.

for문의 in은 반복 연산자로써 반복 대상을 지정하는 역할을 한다. 해당 연산자를 사용하면 내부적으로 해당 객체의 __iter__() 메서드를 호출해 iterator를 얻고, 해당 iterator의 __next__()를 반복 호출하여 하나씩 값을 꺼낸다.


궁금증 : in을 클릭해서 해당 코드가 나오게 된 과정을 보려했는데, 왜 갑자기 __contains__나 __iter__로 넘어갈까?

Sol)
- 파이썬의 in 연산자는 언어 차원에서 특별히 약속된 문법(키워드)이다.
- in을 사용하면, 파이썬 인터프리터(CPython)가 내부적으로 __contains__ 또는 __iter__ 같은 매직 메서드를 자동으로 호출하도록 C 코드에 규칙이 내장되어 있다.
- 그래서 in을 코드에서 추적하면, 실제로는 클래스의 __contains__ 또는 __iter__ 메서드 정의로 이동하게 된다.
- 이 연결 과정은 파이썬 코드가 아니라 인터프리터의 내부(C 코드)에서 처리되므로, 파이썬 코드로 직접 추적하거나 확인하기 어렵다.
- 더 깊이 알고 싶다면 CPython의 소스코드를 참고해야 한다.
'''