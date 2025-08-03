"""
Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

예) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성 => (nav + 5 + 1 + ! => nav51!)

"""

# Sol)
url = "http://naver.com"

#rule1 = url[len("http://"):]
rule1 = url.replace("http://", "")
print(rule1)

rule2 = rule1[:rule1.index(".")]
print(rule2)

rule3 = rule2[:3] + str(len(rule2)) + str(rule2.count('e')) + "!"
print(rule3)

print("{0}의 비밀번호는 {1}입니다".format(url, rule3))