## 가변 인자

def profile(name,age,lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "java", "c", "c++", "c#")   # 더 적지 못하는 상황
profile("김태호", 25, "Kotiln", "Swift", "", "", "")        # 덜 적지 못하는 상황


def profileVariableArguments(name,age,*language):
    print("이름 : {0}\t나이 : {1}\t".format(name,age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profileVariableArguments("유재석", 20, "python", "java", "c", "c++", "c#", "go")
profileVariableArguments("김태호",25, "swift", "kotiln")
