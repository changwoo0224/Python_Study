# subway = [10,20,30] #list

# print(subway)


# subway = ["유재석", "박명수", "조세호"]
# print(subway)
# print(subway.index("조세호"))

# subway.append("하하")
# print(subway)


# subway.insert(1,"정형돈")
# print(subway)

# # print(subway.pop())
# # print(subway)

# #같은 이름의 사람이 몇명 있는지 확인

# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

#뒤집기
# num_list.reverse()
# print(num_list)

#모두 지우기

# num_list.clear()
# print(num_list)

#다양한 자료형 사용 가능
num_list = [5,2,4,3,1]
mix_list = ["조세호", 20, True]
# print(mix_list)

#리스트 확장
num_list.extend(mix_list)
print(num_list)
