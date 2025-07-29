'''
다중 상속의 경우에는 MRO(Method Resolution Order)에 따라서 호출된다.
'''

class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

    def a(self, name):
        self.name = name
        print(self.name)

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)


# 수송만 가능한 유닛
dropship = FlyableUnit()    # super 메서드를 사용하면 맨 처음에 상속받는 클래스로 상속이 된다.

'''
다중 상속을 할 때는 모든 클래스를 클래스 이름으로 해주는게 맞다.
'''