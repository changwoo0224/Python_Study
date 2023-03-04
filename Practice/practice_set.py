# set(집합)
# 중복 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set) # 중복 안되기 때문에 출력하면 1,2,3만 뜸

java = {"유재석", "김태호","양세형"}
python = set(["유재석","박명수"])

# 교집합 출력(java와 python 모두 가능한 사람)
print(java &  python)
print(java.intersection(python))

# 합집합 (java python 둘 다 할 수 있는 사람)

print(java | python)
print(java.union(python))

# 차집합(java 가능 python은 불가능)\

print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

#java를 까먹음
java.remove("김태호")
print(java)
