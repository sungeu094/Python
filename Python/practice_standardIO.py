## 표준 출력

print("python", "google.com", sep ="@")  # sep : 콤마(,) 사이사이에 뭐가 들어갈지 정해주는 인자이다. 기본형은 " "
print("뭔가요 이건", end ="?")           # end : 문장의 끝부분을 정해주는 인자이다. 기본형은 \n 
print()


import sys
print("Python", "Java", file=sys.stdout)    # 표준 출력으로 처리
print("Python", "Java", file=sys.stderr)    # 표준 에러로 처리


# 시험 성적
scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items() :
    print(subject.ljust(3), str(score).rjust(4), sep=":")


# 은행 대기순번표 (001,002,003처럼 앞에 0이 붙음)
for num in range(1,21):
    print("대기번호 : " + str(num).rjust(3,"0"))
    print("대기번호 : " + str(num).zfill(3))        # 위의 코드와 동일한 결과값 발생.


## 표준 입력
    
answer = input("아무 값이나 입력하세요 : ")     # 정수를 입력했다고 하더라도 타입은 str이다.
print("입력하신 값은 " + answer + "입니다.")



