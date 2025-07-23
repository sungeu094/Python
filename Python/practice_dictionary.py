## 사전 -> <K, V>로 이루어짐.

cabinet = {3:"유재석", 100:"김태호"}
print(cabinet)

print(cabinet[3])       # key를 통해 value를 가져올 수 있다.
print(cabinet.get(3))   # 가져오는 방법은 다양하다.

'''
print(cabinet[5])       # 배열 형식의 value를 뽑는 과정에서 없는 키가 나온다면 오류 발생 뒤 바로 프로그램 종료 
'''
print(cabinet.get(5))   # get을 이용해 가져오려고 할 경우 없으면 None 반환 뒤 프로그램이 종료 안함
print(cabinet.get(5, "사용 가능"))  # 두번째 인자를 적어준다면 None 대신 해당 값이 반환
print("hi")  

print(3 in cabinet)     # 사전 자료형 안에 Key 값이 있는지 확인 (return : bool)
print(5 in cabinet)

cabinetA = {"A-3" : "유재석", "B-100" : "김태호"}   # Key값이 꼭 정수형일 필요는 없음
cabinetA["A-20"] = "조세호"     # 만약 해당 key가 존재하지 않으면 key-value 추가, 존재한다면 value 업데이트
print(cabinetA)

del cabinetA["A-20"]    # key-value 삭제. 없는 key라면 error 발생
print(cabinetA)

cabinetA["A-40"] = "남창희"
print(cabinetA)

print(dict(sorted(cabinetA.items(), key=lambda x: x[1])))   # value값으로 정렬.
# lambda는 익명함수 사용하기 위해서 씀
'''
 key = lambda x : x[1]

 def A(x) :
    return x[1]
'''


'''
Q. 내가 궁금한건 sorted는 결국 object 메서드일거 아니야. 그러면 dict에 상속될거 같아서 물어보는거야. 그렇다면 cabinetA.sorted()나 cabinetA.items().sorted()가 가능한거 아니냐는거지
'''


print(cabinetA.keys())      # key들만 출력
print(cabinetA.values())    # value들만 출력
print(cabinetA.items())     # key, value 쌍으로 출력

cabinetA.clear()    # dict의 모든 값 삭제
print(cabinetA)