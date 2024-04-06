import random

#randint() 指定a到b之間的整數 #隨機一個1~10之間的整數
print(random.randint(1,10))  #9

#random() 找到0-1之間的浮點數
print(random.random()) #0.53394449896628

#列表中隨機選擇一個元素, random.choce()
options = ["剪刀","石頭","布"] #list
rand_option = random.choice(options)
print("電腦選擇的是：", rand_option)
#第一次數入：剪刀
#第二次輸入：石頭

#將列表打亂 random.shuffle()
cards = ["2", "3", "4","5","6","7","8","9","10"]
random.shuffle(cards)
print(cards) #輸出三次:
#['8', '6', '10', '9', '3', '5', '4', '7']
#['8', '6', '9', '7', '4', '2', '3', '5', '10']
#['7', '8', '2', '9', '5', '4', '6', '3', '10']

#-----------------------------------------
#系統會產生1-100之間的整數
#如果我們猜得比這數字大，系統會告訴我們太大了，反之猜得太小會被通知猜的太小

#number = random.randint(1,100)
low = 1
high = 100
number = random.randint(low,high)
guesses = 0
while True: #沒猜對就會重複執行ㄓ
    #讓玩家猜數字
    guess = int(input(f'猜猜一個介於{low}到{high} 之間的數字')) #暫存一個輸入數
    guesses += 1 #儲存使用者猜了幾次,每次都會加1
    if guess < number: #如果使用者輸入的數字<正確答案number
        print("猜的數字太小了")
    elif guess > number:
        print("猜的數字太大了")
    else:
        print(f"猜中了!答案是{number}")
        print(f"你猜了{guesses}次")
        break #猜對跳出while
#output:
# 猜猜一個介於1到100 之間的數字5
# 猜的數字太小了
# 猜猜一個介於1到100 之間的數字10
# 猜的數字太小了
# 猜猜一個介於1到100 之間的數字50
# 猜的數字太小了
# 猜猜一個介於1到100 之間的數字80
# 猜的數字太小了
# 猜猜一個介於1到100 之間的數字90
# 猜的數字太大了
# 猜猜一個介於1到100 之間的數字85
# 猜的數字太小了
# 猜猜一個介於1到100 之間的數字86
# 猜中了!答案是86
# 你猜了7次
# 猜猜一個介於1到100 之間的數字
