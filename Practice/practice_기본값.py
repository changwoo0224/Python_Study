# 기본값

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
#           .format(name, age, main_lang))
    
# profile("유재석",20,"파이썬")
# profile("김태호",25,"자바")


# 같은 학교 같은 학년 같은 반 같은 수업.

def profile(name, age = 17, main_lang= "Python"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"\
          .format(name, age, main_lang))

profile("유재석")
profile("김태호") # 그런데 내가 age를 여기서 임의로 수정하면 수정 됨