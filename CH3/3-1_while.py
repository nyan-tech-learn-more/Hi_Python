#python- while loop
name = input("Enter your name: ")

if name == "":
    print("You did not enter your name!")
else:
    print(f"你好, {name}")

#use while改寫
#name = input("Enter your name: ")
name = "" #一開始就跳入while
while name == "": #space
    name = input("Enter your name: ")
print(f"你好, {name}")

#example 2
food = input("what is your favorite food?")

while food != "q": #不等於q我就會印出他的食物，等於q就會跳出迴圈
    print(f"you like {food}")
    food = input("what is your favorite food?") #少這樣會一直無限迴圈，不等於q他就瘋狂loop沒有中斷
print("再見")


#example 3 
#請使用者輸入1-10整數，超過跳出無效
#驗證使用者輸入是否有效，很多用途
number = int(input("請輸入一到十整數")) #沒有int的話型別不一樣，while的number 會跳錯
while number < 1 or number > 10 :
    print("請重新輸入")
    number = int(input("請輸入一到十整數"))
print(f"你輸入了{number}!")
