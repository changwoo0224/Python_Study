# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만난느 점(.) 이후 부분은 제외 =>naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내'e' 갯수 + "!"로 구성
#                     (nav)       (5)      1())           (!)
# 예) 생성된 비밀번호 :  nav51!

#내풀이
site = "http://naver.com"

A = site[7:]
B = A[:A.find(".")]
print(B)
C = str(B[:3]) + str(len(B))+str(B.count("e")) + "!"
print(C)

   
#나도코딩 풀이

url = "http://naver.com"
my_str = url.replace("http://","") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2 my_str[0:5] 0~5까지
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e"))+"!"
print("{0}의 비밀 번호는 {1} 입니다".format(url, password))
print(f"{url}의 비밀 번호는 {password} 입니다") #이건 내가 해본거