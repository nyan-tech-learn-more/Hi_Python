#使用者輸入輕鬆學



#填詞遊戲
adj_1 = input("請輸入第1格形容詞")
n = input("請輸入名詞")
adj_2 = input("請輸入第2格形容詞")
verb = input("請輸入動詞")
adj_3 = input("請輸入第3格形容詞")

print(f"今天我去一個{adj_1}的動物園，在展覽中我看到{n}的這個很{adj_2}，正在{verb}，我感到很{adj_3}")
#==========
#計算矩形面積
#長度乘以寬度

length = float(input("長度"))
width = float(input("寬度"))

area = length * width

print(f"面積為{area}")
print("length" , length , "width" , width, "相乘面積" , area )
#==========
#購物車程式碼
item = input("what do you want to buy?")
price = float(input("how much is it?"))
quantity = int(input("how many do you want to buy?"))

total = price * quantity
print(f"you bought {quantity} {item} ,Total {total} dollars")







