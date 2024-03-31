#python 邏輯運算子

#and or not

temp = int(input('溫度')) #input 輸入
if temp > 0 and temp < 30: # 溫度大於0且小於30度 兩邊符合
    print("溫度合適") #很適合
else:
    print("不合適")

temp = int(input('溫度')) 
if temp <= 0 or temp >= 30: # 這裡的意思是 假如溫度小於0 或 大於30，單邊成立就會往下執行
  print("溫度不合適") #不適合
else:
  print("合適")
