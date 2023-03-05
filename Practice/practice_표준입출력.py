# 표준입출력

# print("Python","Java", "JavaScript", sep=" vs ")
# print("Python","Java", "JavaScript", sep=",",end="?") # 마지막을 ?을 넣음으로서 한 줄 띄어쓰기가 안됨
# print("무엇이 더 재미있을까요?")

# import sys
# print("Python","Java", file=sys.stdout) # 표준 출력
# print("Python","Java", file=sys.stderr) # 표준 에러

scores = {"수학" : 0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    print(subject.ljust(8),str(score).rjust(4), sep = ":")


# 은행 대기순번표

# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) #3크기만큼 확보하고 그 공간을 0으로 채우는것

answer = input("아무값이나 입력하세요 : ") # 입력된 값은 다 string
print("입력하시 갑은" + str(answer) + "입니다.")