# 猜拳遊戲
# 猜拳遊戲是一種流行的遊戲，通常由兩個人玩，但也可以由一個人和電腦玩。
# 遊戲的目標是在三種手勢中選擇一個，並以某種規則來決定勝負。以下是猜拳遊戲的規則：

#   石頭(Rock) 赢剪刀 (Scissors)
#   剪刀 (Scissors)赢布(Paper）
#   布 (Paper)赢石頭 (Rock)

# 班遊戲開始之前，每個玩家都必須選擇石頭、剪刀或布之一，而在決定勝負時，則根據上述規則進行比較。
# 如果兩個玩家選擇相同的手勢，則比賽以平局結束。

#隨機出拳功能 import random
import random
#尚未出拳

player = None #玩家選擇
computer = None #電腦選擇

running = True #遊戲是否要運行，預設要運行
options = ("剪刀", "石頭", "布")
#建立迴圈詢問玩家是否要出拳
running = True #用runing代替True, 判斷是否要繼續玩
while running:
      player = input("請輸入剪刀、石頭或是布")
      while player not in options:
          print("輸入錯誤，請輸入剪刀石頭.")
      computer = random.choice(options) #模擬電腦隨機選擇一個
      print(f"玩家出：{player} | 電腦出：{computer}")
      #開始撰寫遊戲規則邏輯
      if player == computer:
          print("平手")
      elif player == "剪刀" and computer == "布":
          print("玩家贏")
      elif player == "石頭" and computer == "剪刀":
          print("玩家贏")
      elif player == "布" and computer == "石頭":
          print("玩家贏")
      else:
          print("電腦贏") #已經列出所有玩家贏方式，其他都是電腦勝利
      play_agin = input("再玩一局？(y/n)").lower()
      if play_agin =='n':
          running = False #把while改成false , 跳出迴圈
print('謝謝遊玩')
  
      
