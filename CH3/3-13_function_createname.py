#fuction #方法
# 使用def + 函數名稱 + 括號 + 冒號
#3 usages
def say_Hello():
  print("嗨！世界你好！")
say_Hello()
#嗨！世界你好！

#傳遞參數

def greeting(name): #傳遞name進去
    print(f"你好, {name}")
greeting("Bob") #傳遞一個字串

#如果函數需要返回一個值 我們可以使用 return 語句
#return語句用來將函數結束執行並返回給調用者

#兩數之和

def add(x, y):
    return x + y
print(add(3,4)) #return 7


def sub(x, y):
    return x-y
print(sub(4,3)) #1


#建立一個名字function

def create_name(first, last):
    first = first.capitalize() #capitalize 讓first變成大寫
    last = last.capitalize() #capiatlize 讓last變成大寫
    return first + " " + last

print(create_name("Jonh", "wick")) #建立名字的函式
#Jonh Wick
