
# 簡易碼表倒數計時器


#正著數
import time
from time import sleep
#Python 的標準函式「time」提供不少處理時間的方法，除了可以取得目前的時間或轉換時間，也能夠透過像是 sleep() 的方法將程式暫停，進一步做出許多跟時間有關的應用。
# time.sleep(1) #停一秒

my_time = int(input("請輸入秒數:"))

for t in range(my_time):
    print(t)
    time.sleep(1)
print("時間到")

#倒著數

my_time = int(input("請輸入到數秒數:"))

for t in range(my_time, 0, -1): #從my_time數到X,這裡是0, -1會變成 倒著數
    print(t)
    time.sleep(1)
print("時間到")

#-----------------------------------------------
#變成碼表顯示的樣態 XX:XX
my_time = int(input("請輸入到數秒數:"))

for t in range(my_time, 0, -1): 
    #02:00
    seconds = t % 60 #取餘數為秒數
    minutes = t // 60 % 60 #取商為分鐘數
  #//運算子不管除數、被除數的型別為何，回傳的都是無條件捨去的結果。如果都是整數，就回傳整數，如果有任一為浮點數，則回傳浮點數：
  #/運算子只保留「真除法」，也就是說不管除數、被除數的型別都可以得到更精確的結果
    print(f"{minutes:02}:{seconds:02}") # :2 顯示兩位數並補0
  #:02是格式化指示符（format specifier），用來指示輸出的數字應該以至少兩位數的形式呈現，不足兩位的話會在前面補0。這樣的格式化可以確保輸出的時間格式是兩位數的分鐘和秒數，例如01:05或者10:30。
    time.sleep(1) #停一秒
print("時間到")
# input:10秒, output:
# 請輸入到數秒數:10
# 00:10
# 00:09
# 00:08
# 00:07
# 00:06
# 00:05
# 00:04
# 00:03
# 00:02
# 00:01
# 時間到
