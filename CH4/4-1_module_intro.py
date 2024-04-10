# Python 中的模組 Module

#標準模組
import math as m #m是別名,比較簡潔

#help(math) #列出所有方法

print(m.pi) #3.141592653589793
print(m.pow(3,2)) #次方 3的2次方＝9.0

# ceil 
# floor
# round

num = 20.6
print(m.ceil(num)) #21 無條件進位
print(m.floor(num)) #20 無條件捨去
print(round(num)) #21 四捨五入，這個版本已經是內建方法所以不用math()

# 引用子模組
from math import pi
print(pi) #單獨引用子模組可直接呼叫不用輸入math #3.141592653589793

 
#引用自己的模組
import 41mymodule as mm #引入自己的模組
print(mm.pi) #3.14555
print(mm.square(5)) #25
print(mm.cube(5)) #125
print(mm.area(3)) #28.26
