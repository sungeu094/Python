## 외장 함수

# list of python modules

'''
# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
print(glob.glob("*.py"))    # 확장자가 py인 모든 파일
'''


'''
# os : 운영체제에서 제공하는 기본 기능
import os
print(os.getcwd())  # 현재 디렉토리

folder = "sample_dir"

if os.path.exists(folder):      # 해당 folder가 있는가?
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, " 폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)         # 해당 folder가 없을 경우 폴더를 생성
    print(folder, " 폴더를 생성하였습니다.") 
print(os.listdir())         # glob와 비슷하게 현재 경로의 파일 리스트를 보여줌
'''


'''
# time : 시간 관련 함수를 제공하는 외장 함수
import time

print(time.localtime())     # 현재 시간
print(time.strftime("%Y-%m-%d %H:%M:%S"))
# time.strftime(format[,t]) -> [,t]는 format은 필수적인 매개변수이고, t는 선택적인 매개변수로 존재를 꼭 해야하는 매개변수가 아니라는 것을 나타내기 위한 기호이다. (리스트와 같은 표시가 아닌 생략 가능이란 뜻)
'''

# datetime : 시간 관련 함수를 제공하는 또다른 외장 함수
import datetime
# print("오는 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()       # 오늘 날짜 저장
td = datetime.timedelta(days=100)   # 100일 저장
print("우리가 만난지 100일은", today + td)  # 오늘부터 100일 후 (오늘 날짜 + 100일)  