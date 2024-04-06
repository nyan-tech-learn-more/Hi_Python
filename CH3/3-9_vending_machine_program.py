#電影院內食物販賣機程式
#選擇菜單後加入購入車並加總金額

#Menu
#用字典建立餐點

menu ={
    "Pizza": 300,
    "Hamburger": 200,
    "French Fries": 100,
    "Coke": 50,
    "Fanta": 50,
    "Sprite": 50
}
#顯示菜單
print("菜單")
print("-----------------------------------")
for item, price in menu.items():  #items()可印出字典的key, value
    print(f"{item} : {price}")
  
#Cart 儲存使用者所選擇的菜單項目
cart = [] #list
total = 0 #int, 預設等於0元
#讓使用者重複輸入要的東西，繼續使用while迴圈
while True:
    food = input("請輸入你所要點的食物，若輸入end結束 \n")
    if food == 'end':
        break
    elif menu.get(food) is None: #如果使用者輸入的食物(food)不在（is None) menu菜單上(Menu.get(food))
        print("沒有這個食物")
    else:
        cart.append(food) #用apped()讓每次輸入的food加總到cart []內
        total = total + menu.get(food) #使用者輸入的food去比對menu上的價格ㄑ
        print(food, end= " ") #換行
print(f"總金額：{total}元")

# input / output:
# 菜單
# -----------------------------------
# Pizza : 300
# Hamburger : 200
# French Fries : 100
# Coke : 50
# Fanta : 50
# Sprite : 50
# 請輸入你所要點的食物，若輸入end結束 
# Pizza
# Pizza 請輸入你所要點的食物，若輸入end結束 

# 沒有這個食物
# 請輸入你所要點的食物，若輸入end結束 
# Coke
# Coke 請輸入你所要點的食物，若輸入end結束 
# Hamberger
# 沒有這個食物
# 請輸入你所要點的食物，若輸入end結束 
# Hamburger
# Hamburger 請輸入你所要點的食物，若輸入end結束 
# end
# 總金額：550元
