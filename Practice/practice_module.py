# 1번째
import theater_module

theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
theater_module.price_morning(4) # 4명이서 조조 할인 가격
theater_module.price_soldier(5) # 5명 군인

# 2번째
import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_soldier(5)

# 3번째
from theater_module import *
price(3)
price_morning(4)
price_soldier(5)

# 4번째
from theater_module import price, price_morning
price(5)
price_morning
price_soldier(4)

# 5번째
from theater_module import price_soldier as ps
ps(5)

