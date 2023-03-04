cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
#print(cabinet[5])#여기서 프로그램 끝남 근데 get은 안그럼
print(cabinet.get(5))#오류 안나고 none으로 나옴
print(cabinet.get(5, "사용 가능"))#5에 값이 있으면 값을 가져오고 없으면 사용 가능 출력
print("hi")

print(3 in cabinet) # True(cabinet 안에 3 있음) 
print(5 in cabinet) # False(cabinet 안에 5 없음)
print("유재석" in cabinet) # value값은 안되나봄..

trunk = {"A-3":"유재석", "B-100":"김태호"}
print(trunk)
print(trunk["A-3"])
print(trunk["B-100"])
#print(trunk[0:3]) #에러가 뜨는걸 봐선 slice는 안되는듯

#새로운 손님 등장
trunk["C-20"] = "조세호" #만약 C-20이 이미 있다면 값이 업데이트 됨
trunk["A-3"] = "김종국" #유재석 -> 김종국
print(trunk)

#손님이 감
del trunk["A-3"] #A-3 값 삭제
#print(trunk)

#key 들만 출력
print(trunk.keys())

#value들만 출력
print(trunk.values())

#key value 쌍으로 출력

print(trunk.items())

#폐점
trunk.clear()
print(trunk) #trunk dict안에 있는 모든 데이터들을 날림