## 클래스

'''
# ex. 스타크래프트

# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
name = "마린"
hp = 40
damage = 5
print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있음(일반 모드 / 시즈 모드)
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{0} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))


def attack(name, location, damage):
    print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

attack(name, "1시", damage)
attack(tank_name, "2시", tank_damage)

#해당 코드 문제점 : 만약 동일한 유닛이 여러개가 생성되면 ~~1, ~~2와 같이 하드코딩을 하게된다.
'''

# Solution - class 사용 (서로 연관이 있는 변수와 함수의 집합이라고 생각하면 된다.)

# 일반 유닛
class Unit :    # class의 이름의 첫 글자는 관례적으로 대문자를 사용한다. 
    def __init__(self, name, hp, speed):     # 파이썬 생성자(객체가 생성될 때 자동으로 호출되는 부분)
        self.name = name
        self.hp = hp
        self.speed =speed
        # self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        # print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

'''
# 불가능한 예시(생성자에 매개변수는 다 필요함)
marine3 = Unit("마린")  
'''

'''
# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80)
print("유닛 이름 : {0}".format(wraith1.name))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("레이스", 80)
wraith2.clocking = True             # 객체 외부에서 변수를 추가로 할당해서 사용 가능

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
'''
    

"""
print(wraith1.__dict__)
print(wraith2.__dict__)

# print(dir(wraith2))
# print(wraith2.__dir__())  

'''
dict : 객체에서 직접 지정해준 필드와 메서드 정보만 나옴
dir : 해당 객체에 대한 상속받은 속성/메서드를 포함한 정보가 나옴.
'''
"""


## method

import inspect

# 공격 유닛
class AttackUnit(Unit):        # Unit은 AttackUnit의 부모 클래스이다.(AttackUnit은 자식 클래스이다)
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))
        frameinfo = inspect.getframeinfo(inspect.currentframe())    # getframeinfo 메서드의 인자로 프레임 객체(실행 중인 코드의 상태 정보를 담고 있는 객체)가 와야한다.
        print("현재 줄 정보 : {0}".format(frameinfo.lineno))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

'''
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격을 두번 받아서 파괴되는지 확인
firebat1.damaged(25)
firebat1.damaged(25)
'''


## 다중 상속 (자식 클래스가 부모 클래스 2개 이상에서 상속 받을 때)

# 날 수 있는 기능을 가진 클래스
class FlyableUnit:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스(FlyableUnit 클래스와, AttackUnit 클래스를 부모로 가지는 다중 상속)
class FlyableAttackUnit(AttackUnit, FlyableUnit) :      # 상속은 매개변수로 받기
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상에서의 speed는 0으로 처리해줌
        FlyableUnit.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)   # 메서드 오버라이딩 : 부모 클래스에서 상속받은 메서드를 자식 클래스에서 재정의하여 쓰고 싶을 때 (해당 상황에서는 Unit에 사용했던 메서드를 덮어쓴 것이다.)


'''
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")
'''

'''
# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")
'''

# 건물
class BuildingUnit(Unit) :
    def __init__(self, name, hp, location):
        '''
        pass    # 아무 속성도 만들어지지 않고, 아무 동작도 하지 않는다. 그럼에도 필요한 이유는 파이썬에서 클래스나 함수의 본문이 반드시 있어야 하기 때문이다.
        '''
        # Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0) # 위와 동일하다. 자신이 상속받는 class를 super()로 대체하는 것이다.
        self.location = location
# 서플라이 디폿 : 건물, 1개 건물 = 8개 유닛 생성 (현재 pass로 초기화가 되어있기 때문에 아무 동작하지 않음)
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass

game_start()
game_over()

'''
보통 pass를 사용하는 건 추상 클래스(or 인터페이스)에서 메서드만 정의할 때 사용한다.
'''

# Ex
class Animal:
    def speak(self):
        pass  # 아직 구현하지 않음, 자식 클래스에서 반드시 오버라이딩해야 함

class Dog(Animal):
    def speak(self):
        print("멍멍!")

class Cat(Animal):
    def speak(self):
        print("야옹!")

dog = Dog()
dog.speak()

# 현재 상황을 보면 반드시 자식 클래스에서 구현하도록 하기 위해서 pass를 사용한 걸 볼 수 있음.