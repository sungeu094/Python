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

class Unit :    # class의 이름의 첫 글자는 관례적으로 대문자를 사용한다. 
    def __init__(self, name, hp, damage):     # 파이썬 생성자(객체가 생성될 때 자동으로 호출되는 부분)
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

'''
# 불가능한 예시(생성자에 매개변수는 다 필요함)
marine3 = Unit("마린")  
'''

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True             # 객체 외부에서 변수를 추가로 할당해서 사용 가능

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
