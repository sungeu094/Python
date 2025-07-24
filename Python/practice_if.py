## if문
'''
if 조건:
    실행 명령문
'''

weather = input("오늘 날씨는 어때요? ")     # 입력을 받음(해당 입력은 str)
if weather == "비" or weather == "눈":
    print("우산을 챙기기")
elif weather == "미세먼지":
    print("마스크를 챙기기")
else:
    print("준비물 필요 없음")


temp = int(input("기온은 어때요? "))
if 30 <= temp :
    print("더운 날씨")
elif 10 <= temp and temp < 30:      # python은 연속 비교가 가능
    print("괜찮은 날씨")
elif 0 <= temp < 10:                # 어짜피 if문을 위에서 충족하기 때문에 굳이 temp < 10이라는 조건을 안써도 되지만 코드의 명확성과 가독성을 위해서 써주는게 좋음        
    print("쌀쌀한 날씨")
else :
    print("추운 날씨")