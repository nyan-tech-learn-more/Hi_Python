#體重轉換，你要先有體重，接著

weight = float(input("你的體重是？"))
unit = input('KG?LB?').upper() #upper可以讓英文變成大寫

#一公斤＝2.2磅

if unit == "KG":
    weight = weight * 2.2
    new_unit = 'LB'
elif unit == "LB":
    weight = weight / 2.2
    new_unit = 'KG'
else :
    print('不正確輸入')
    exit()
print(f'你的體重是 {round(weight)} {new_unit}')
