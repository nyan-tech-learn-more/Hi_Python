# 骰子遊戲

#骰出骰子之後，顯示總和圖案
# 使用 Unicode 字元來製作骰子的圖案

import random

#外層字典檔案, key是123456 ,內部是元祖tuple
dice_art = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐", # index:0
        "│ ●   ● │", # index:1
        "│ ●   ● │", # index:2
        "│ ●   ● │", # index:3
        "└───────┘", # index:4
    ),
}
#-----印出與呼叫骰子------
print(dice_art.get(6))

for i in range(5):
    print(dice_art.get(6)[i]) #印出key6的index0-4

#改寫
number = 5
for i in range(5):
  print(dice_art.get(number)[i]) #當number=5時，印出key5的index0-4

#方法包起來

def get_dice_number(number):
    for i in range(5):
      print(dice_art.get(number)[i]) #當number=5時，印出key5的index0-4
get_dice_number(3)


#-----丟骰子------

num_dice = int(input("請輸入要丟幾個骰子:"))
dice = [] #list
for i in range(num_dice): #使用者輸入的次數 num_dice
      dice_number = random.randint(1,6) #隨機丟出1-6之間的數子
      #丟完後要放到列表內，用append一個一個加入
      dice.append(dice_number) #存到列表中
      print(dice) #丟了幾次骰子
# 請輸入要丟幾個骰子3
# [6]
# [6, 6]
# [6, 6, 5]

#--呼叫方法去丟出相對應的骰子--
for i in dice:
    get_dice_number(i)
print("總和:", sum(dice)) #把dice這個list內數字加總印出總點數
  
# 請輸入要丟幾個骰子3
# [3]
# [3, 2]
# [3, 2, 1]
# ┌───────┐
# │ ●     │
# │   ●   │
# │     ● │
# └───────┘
# ┌───────┐
# │ ●     │
# │       │
# │     ● │
# └───────┘
# ┌───────┐
# │       │
# │   ●   │
# │       │
# └───────┘
# 總和: 3
