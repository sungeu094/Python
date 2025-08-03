# 유닛들의 기본
from random import *

# annotation을 자체 제작(데코레이터 -> 함수를 감싸서 실행 전후에 추가 동작을 넣을 수 있도록 하는 파이썬 기능)
def with_bar(func):
    def wrapper(*args, **kwargs):   # *args : 여러 개의 위치 인자를 받을 때 사용한다.(튜플 형태) **kwargs : 여러 개의 키워드 인자를 받을 때 사용한다.(딕셔너리 형태)
        print("="*100)
        result = func(*args, **kwargs)
        print("="*100)
        print()
        return result
    return wrapper
    

# 유닛들의 기본 성질
class Unit :
    def __init__(self, name, hp, speed, damage):
        self.name = name
        self.hp = hp
        self.speed =speed
        self.damage = damage
        print("[{0}] 유닛이 생성 되었습니다.".format(self.name))
        
    def move(self, location):
        self.location = location
        print("{0} 방향으로 이동합니다. [속도 {1}]".format(self.location, self.speed))

    def damaged(self, damage):
        print("{0} 데미지를 입었습니다.".format(damage), end=" ")
        self.hp -= damage
        if self.hp > 0:
            print("현재 체력 : {0}".format(self.hp))

# 공중 기능을 가진 유닛
class FlyableUnit:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} 방향으로 날아갑니다. [속도 {1}]".format(location, self.flying_speed))


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed, damage)

    def attack(self, location):
        print("{0} 방향으로 적군을 공격 합니다. [공격력 {1}]".format(location, self.damage))


# 공중 공격 유닛 (공중 기능 + 공격 기능)
class FlyableAttackUnit(AttackUnit, FlyableUnit) :
    def __init__(self, name, hp, flying_speed, damage):
        AttackUnit.__init__(self, name, hp, 0, damage)
        FlyableUnit.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)   


## 공격 유닛 - 마린
class Marine(AttackUnit):
    count_marine = 0

    def __init__(self):
        Marine.count_marine += 1
        self.unit_id = Marine.count_marine
        super().__init__("마린{0}".format(self.unit_id), 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 본인 체력 10 감소
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("[{0}] 스팀팩을 사용합니다. 현재 체력 : {1}".format(self.name, self.hp))
        else:
            print("[{0}] 체력이 부족하여 스팀팩을 사용하지 않습니다. 현재 체력 : {1}".format(self.name, self.hp))


## 방어 유닛 - 탱크
class Tank(AttackUnit):
    count_tank = 0

    def __init__(self):
        Tank.count_tank += 1
        self.unit_id = Tank.count_tank      # 해당 객체의 속성으로 사용하기 위해서 self를 붙여서 인스턴스 변수로 사용하는 것이다. 현재는 모든 객체가 개개인의 번호를 가질 것이기 때문에 겹치지 않기 위해 처음에는 클래스 변수로 설정했다가 인스턴스 변수로 옮겨서 개개인의 번호를 사용할 수 있도록 한 것이다.
        super().__init__("탱크{0}".format(self.unit_id), 150, 1, 35)
        self.seize_mode = False

    # 시즈모드 : 더 높은 파워로 공격이 가능하지만 이동이 불가능
    seize_developed = False   # 시즈모드 개발여부

    def set_seize_mode(self) :
        if Tank.seize_developed == False:
            print("[{0}] 현재 시즈모드 개발이 되지 않았습니다.".format(self.name))
            return
        
        if self.seize_mode == False:
            print("[{0} 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False    


## 공중 공격 유닛 - 레이스
class Wraith(FlyableAttackUnit):
    count_wraith = 0

    def __init__(self):
        Wraith.count_wraith += 1
        self.unit_id = Wraith.count_wraith    # 먼저 인스턴스 변수로 설정했는지 확인 후 없다면 클래스 변수로 설정했는지 확인.
        super().__init__("레이스 {0}".format(self.unit_id), 80, 5, 20)
        self.clocked = False # 클로킹 모드 (해제 상태)

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정합니다.".format(self.name))
            self.clocked = True

# unit manager class - 유닛 관리. 현재 있는 Marine, Tank, Wratih 유닛에 관한 정보 관리
class UnitManager:
    def __init__(self):
        self.units = []
    
    def makeUnit(self, unit_type):     # 유닛 생성
        if unit_type == "Marine":
            unit = Marine() 
        elif unit_type == "Tank":
            unit = Tank()
        elif unit_type == "Wraith":
            unit = Wraith()
        else :
            return None
        
        self.units.append(unit)

    def deleteUnit(self, unit, unit_hp):   # 유닛 삭제
        if unit_hp <= 0:
            self.units.remove(unit)
            print("해당 유닛이 파괴되었습니다.")

    def searchUnit(self, unit_name):   # 유닛 상태검색(이름, 위치, 피상태 ...)
        found = False
        for unit in self.units:
            if unit.name == unit_name:
                print("{0} (현재 위치 : {1}, 체력 : {2}, 스피드 : {3}, 공격력 : {4}))".format(unit.name, unit.location,  unit.hp, unit.speed, unit.damage))
                found = True
        if not found:
            print("{0} 유닛을 찾을 수 없습니다.".format(unit_name))


class GameProcess:
    game_manager = UnitManager()

    @staticmethod
    def game_start():
        print("[알림] 새로운 게임을 시작합니다.")
        print()

    @with_bar
    def process_makeUnit(self):
        unit_plan = [ ("Marine", 3), ("Tank", 2), ("Wraith", 1)]

        for unit_type, count in unit_plan:
            for _ in range(count):
                GameProcess.game_manager.makeUnit(unit_type)

    @with_bar
    def process_moveUnit(self):
        for unit in GameProcess.game_manager.units:
            print("[{0}] 이동 명령 : ".format(unit.name), end=" ")
            unit.move("1시")

    @with_bar
    def process_prepareAttackUnit(self):
        for unit in GameProcess.game_manager.units:     
            if isinstance(unit, Marine):        # Marine class의 인스턴스인가?
                unit.stimpack()
            elif isinstance(unit, Tank):
                unit.set_seize_mode()
            elif isinstance(unit, Wraith):
                unit.clocking()
    
    @with_bar
    def process_attack(self, location):
        for unit in GameProcess.game_manager.units:
            print("[{0}] 공격 명령 : ".format(unit.name), end=" ")
            unit.attack(location)

    @with_bar
    def process_damaged(self):
        for unit in GameProcess.game_manager.units[:]:   # 리스트 자체를 순환하는 것이 아닌 복사본 순회
            print("[{0}]".format(unit.name), end=" ")
            unit.damaged(randint(5,50))     # 공격은 랜덤으로 받음
            GameProcess.game_manager.deleteUnit(unit, unit.hp)

    @with_bar
    def process_searchUnit(self, name):
        GameProcess.game_manager.searchUnit(name)

    @staticmethod
    def game_over():
        print("Player : gg")
        print("[Player] 님이 게임에서 퇴장하셨습니다.")



## 실제 게임 진행 (현재까지 사용한 문법(Ex. for문)을 사용해서 리팩토링은 내일 천천히 진행해보기.)
gameProcess = GameProcess()

GameProcess.game_start()

# 생성 명령
gameProcess.process_makeUnit()

#전군 이동
gameProcess.process_moveUnit()

# 탱크 시즈모드 개발
#Tank.seize_developed = True
#print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비 ( 마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
gameProcess.process_prepareAttackUnit()

# 공격 명령
gameProcess.process_attack("1시")

# 전군 피해
gameProcess.process_damaged()

# 유닛 현재 상황 파악
gameProcess.process_searchUnit("마린1")

# 게임 종료
GameProcess.game_over()

