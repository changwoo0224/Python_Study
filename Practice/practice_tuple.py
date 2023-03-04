#tuple
#list와는 다르게 변경이 불가능하나 속도는 빠름

menu = ("돈까스","치즈까스")
print(menu[0])
print(menu[1])
#menu.add("생선까스") # 튜플은 데이터 변경이 불가능하므로 에러가 뜸

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

#tuple 활용시
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)