## 한 줄 for문

# 출석 번호 1, 2, 3, 4  => 101, 102, 103, 104
students = list(range(1,6))
print(students)
students = [i+100 for i in students]    # i+100을 넣을건데 해당 i는 students list에 있는 i이다.(List Comprehension)
'''
위의 코드는 리스트 내포 문법 사용. 밑에 코드는 풀어서 쓴 동일한 코드.
new_students = []
for i in studnets:
    new_students.append(i+100)
students = new_students
'''

# 학생 이름을 길이로 변환 (str -> int)
students_name = ["Iron man", "Thor", "I am groot", "Denfenser"]
print(students_name)
students_nameLength = [len(i) for i in students_name]   # students_name 배열에 덮어쓰기가 가능하지만 처음 배열을 원해도 다시 호출할 수 없음.
print(students_nameLength)
students_nameUpper = [i.upper() for i in students_name]
print(students_nameUpper)
students_nameLower = [i.lower() for i in students_name]
print(students_nameLower)
