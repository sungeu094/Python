'''
Quiz) 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

- X 주차 주간보고 -
부서 :
이름 :
업무 요약 :

1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만든다.
'''


'''
# Solution 1
import os
os.chdir("C:/Users/sunge/OneDrive/Desktop/PythonWorkspace/Python/Quiz7")
print(os.getcwd()) 

for i in range(1,6):
    weekend_report = str(i) +"주차.txt"
    with open(weekend_report, "w", encoding="utf-8") as report:
        report.write("- {0}주차 주간보고 -".format(i))
        report.write("\n부서 : ")
        report.write("\n이름 : ")
        report.write("\n업무 요약 : ")
'''

# Solution 2
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

for i in range(1,7):
    weekend_report = str(i) + "주차.txt"
    report_file = open(weekend_report, "w", encoding="utf-8")
    
    report_file.write("-- {0}주차 주간보고 --".format(i))
    report_file.write("\n부서 : ")
    report_file.write("\n이름 : ")
    report_file.write("\n업무 요약 : ")

    report_file.close()