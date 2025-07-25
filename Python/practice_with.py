## with (파일에 대한 작업을 할 때 파일 열고 작업을 수행한 후 파일 닫기를 했는데 이걸 좀 더 편하게 작업 가능)

import pickle

with open("profile.pickle", "rb") as profile_file :     # open(), close()를 사용할 필요가 없음
    print(pickle.load(profile_file))

'''
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하기")
'''

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())