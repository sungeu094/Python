## 함수

def open_account():
    print("새로운 계좌 생성")

open_account()


## 전달값과 반환값

def deposit(balance, money):
    print("입금이 완료. 잔액은 {0}원입니다".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money :
        print("출금 완료. 잔액은 {0}원.".format(balance - money))
        return balance - money
    else :
        print("출금 불가능. 잔액은 {0}원.".format(balance))
        return balance
    
def withdraw_night(balance, money):
    commission = 100 # 수수료 100원
    return commission, balance - money - commission     # 튜플 형식으로 보내는 것.


balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
commision, balance = withdraw_night(balance, 300)
print("수수료 {0}원, 잔액 {1}원".format(commision, balance))


## 기본값

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))    

profile("유재석", 20, "python")
profile("김태호", 25, "java") 


# 만약 이름만 다를 뿐 나머지가 동일하다면? age, main_lang 같은 경우에는 값을 계속해서 사람이 생길때마다 정의해줄 필요가 없음 -> 이때 발생한 것이 결국 기본값

def profile1(name, age = 17, main_lang = "python"):     # 만약 age나 main_lang에 값을 적지 않으면 해당 기본값으로 출력된다는 뜻이다.
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}".format(name, age, main_lang))    

profile1("유재석")
profile1("김태호")