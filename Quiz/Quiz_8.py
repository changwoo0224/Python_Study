# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년



# 내 풀이

class House:
    def __init__(self,location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):
        print("{0} {1} {2} {3} ".format(self.location,self.house_type,self.price,self.completion_year))
    
Gangnam = House("강남", "아파트", "매매", "10억", "2010년")
Mapo = House("마포", "오피스텔", "전세", "5억", "2007년")
Songpa = House("송파", "빌라", "월세", "500/50", "2000년")

Gangnam.show_detail()
Mapo.show_detail()
Songpa.show_detail()

# 나도 코딩 풀이

class House:
    def __init__(self,location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    def show_detail(self):
        print(self.location, self.house_type,self.deal_type,self.price, self.completion_year)


houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3)

print("총 {0}대의 매물이 있습니다.".format(len(houses)))
for house in houses:
    house.show_detail()