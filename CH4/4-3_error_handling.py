# Python 中的例外處理 (Error Handling, 異常處理）
# exception


# #try:
# x = int(input("輸入一個整數:")) #10
# y = int(input("輸入一個整數:")) #0
# print(x/y) #ZeroDivisionError: division by zero

try:
    x = int(input("輸入一個整數:")) #9
    y = int(input("輸入一個整數:")) #1.0
    print(x/y) #請輸入整數
except ZeroDivisionError:
    print("除數不可以為0")
except ValueError as VE: 
    print("請輸入整數", VE)
#在實際開發中，有時候我們需要處理多種不同的例外。為了實現這一點，我們可以在try-except語句中使用多個except語句
except (NameError,SyntaxError):
    print("出現錯誤請重新輸入")
else:
    print("else") #上面都沒有的才會跑到這一段
finally:
    print('管他有沒有錯，一定都會輸出！')    # 不論有沒有錯都會執行這行 
#pass :略過 
#except Exception: 不要捕獲所有例外 可以選擇只捕獲特定的例外
