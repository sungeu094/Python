## 피클(프로그램 상에서 사용중인 데이터를 파일 형태로 저장)

import pickle

'''
profile_file = open("profile.pickle","wb")         # wb : pickle을 쓰기 위해서는 binary Type으로 해야한다. 이때, encoding 기능을 사용할 수는 없다.
profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)      # profile에 있는 정보를 file에 저장
profile_file.close()
'''

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)     # 파일에 있는 내용을 가져와 데이터 형태로 불러옴
'''
Q. pickle은 모듈이라 알고있음. 근데 pickle속 내부 클래스에 load라는 메서드가 있는건데 어떻게 pickle.load()로 출력이 가능한건가?

A. pickle.py 맨 아래를 보면 튜플로 load = _load가 연결되어 있는걸 볼 수 있음. 그 메서드는 내부적으로 _Unpickler 클래스를 사용해서 객체를 복원하는 것이기 때문에 pickle.load()가 가능한 것이다.
** 언더바(_)를 메서드나 클래스 앞에 사용하는 이유는 내부 구현용(모듈 내부에서만 사용하기 위한 것)이라는 것이다.
'''
print(profile)
profile_file.close()