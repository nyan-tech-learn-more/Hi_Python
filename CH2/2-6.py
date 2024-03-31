#python MATH

#指數
banana = 3
banana = banana ** 2 #二次方
#banana **= 2
print(banana)
apples = 3
apples = apples ** 3 #三次方
#apple **= 3
print(apples)


#模數
#10 mod 3 = 3 餘數1
print(10 % 3)
#11 mod 3 = 3 餘數2
print(11 % 3)
#12 mod 3 = 4 餘數0
print(12 % 3)

#數學函式

#次方 pow()
print(pow(3,2)) #3的2次方=9

#最大數值 max()
x = 1
y = 2 
z = 3
print(max(x,y,z)) #3
#最小值 min()
print(min(x,y,z)) #1

#四捨五入 round()
a = 3.14195 
print(round(a,2)) #3.14

#絕對值 abs()
c = -4 
print("絕對值:", abs(c))

import math #數學函數
#無條件進位 ceil()
x = 9.5
print(math.ceil(x)) #10
#無條件捨去 floor()
print(math.floor(x)) #9

#圓周率 pi()
print(math.pi) #3.141592653589793

#圓周長 2piR
R = float(input("輸入圓的半徑R")) #input 10
c = 2 * math.pi * R # 2 x pi x R
print(f"圓周長為：{round(c,2)}") #62.83

#圓面積piR平方
R = float(input("輸入圓的半徑R")) #input 20
area = math.pi * (R ** 2) #pi x R平方
print(f"圓周長為：{round(area,2)}") #1256.64
