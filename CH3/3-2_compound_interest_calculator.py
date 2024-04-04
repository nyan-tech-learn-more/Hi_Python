#複利計算機
#總金額 = 本金*（1+（利率/100））**時間
#總金額 = 10000 * 1.05 * 1.05 (累計)
#總金額 = 10000 * 1.05 ** 2 (改寫成指數)
#總金額 = 10000 * (1 + 5/100) ** 2 (改寫)

amount = 0 #初始化使用者金額

while amount <= 0:
    amount = float(input("請輸入本金"))
    if amount <= 0: #如果還是<=0
        print("請重新輸入")
print(amount)


#rate 利率
rate = 0
while rate <= 0:
    rate = float(input("請輸入利率:"))
    if rate <= 0:
        print("利率不能小於或等於0")
print("利率:", rate)

#時間
time = 0
while time <= 0:
    time = int(input("請輸入時間:"))
    if time <=0 :
        print("時間不能小於0")
print("時間:", time)


#計算複利
#總金額 = 10000 * (1 + 5/100) ** 2 (改寫)
total = amount * (1 + (rate/100)) ** time
print("總金額:"total)
