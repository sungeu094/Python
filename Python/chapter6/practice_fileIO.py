## 파일 입출력

'''
score_file = open("score.txt", "w", encoding="utf8")    # 쓰기 용도(덮어쓰기)
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()
'''

'''
score_file = open("score.txt", "a", encoding="utf8")    # 쓰기 용도(이어쓰기)
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()
'''

'''
score_file = open("score.txt", "r", encoding="utf8")    # 읽기 용도
print(score_file.read())        # 한번에 파일내용 전체 가져오기
score_file.close()
'''

'''
score_file = open("score.txt", "r", encoding="utf8")    # 읽기 용도
print(score_file.readline(), end="")        # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()
'''

'''
score_file = open("score.txt", "r", encoding="utf8")    # 읽기 용도
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()
'''

'''
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()      # list 형태로 저장
for line in lines :
    print(line, end="")             # list에서 한줄씩 불러와서 출력
score_file.close()
'''

