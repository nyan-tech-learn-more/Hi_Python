#args => anguments 任意數量的參數 * -> 參數就會被打包進一個 tuple 裡
#kwargs =>關鍵字 + args (keyword args) ** -> 參數就會被打包進一個 dictionary 裡


#傳統
def add(a,b):
    return a + b
print(add(1,2)) #3 #只能傳入固定的兩個，如果我要三個相加就不行


#args
def add2 (*args): #args => anguments 任意數量的參數 *
    total = 0
    for arg in args:
        print(f"args: {arg}")
        total += arg
       #每個args都加入total內
    return total
print(add2(1,2)) 
#args: 1
#args: 2
#3
print(add2(1,2,3,4)) 
# args: 1
# args: 2
# args: 3
# args: 4
# 10

#------
#kwargs =>關鍵字 + args (keyword args) ** -> 參數就會被打包進一個 dictionary 裡
def print_info(**kwargs): #字典型態ㄗ
    for key, value in kwargs.items(): #items可以印出key value
        print(f"key: {key} value: {value}")
print_info(name="Alice", age=25, city="New York", occupation="工程師") #關鍵字與數值，可傳入任意數量
# key: name value: Alice
# key: age value: 25
# key: city value: New York
# key: occupation value: 工程師
