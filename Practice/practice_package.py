# package module들 모아둔 집합
# import travel.thailand # 모듈이나 패키지만 가능함
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # 이럴땐 class 까지 ㅆㄱㄴ
# trip_to = ThailandPackage()
# trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

