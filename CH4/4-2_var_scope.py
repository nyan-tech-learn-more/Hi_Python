# Python 中的作用域
# 變數範圍與作用域
# LEGB 作用域順序 
# L - LocaL 區域
# E - enclosed
# G - Global 全域
# B - built-in

#變數範圍
a = 10 #global
def fucntion_one():
    a = 1
    print("a:", a)
    def function_two():
        b = 2 #local 
        print("b:", b) 
        print("a:", a) #a會往上找到functionone的a, a is enclosed
    function_two()

fucntion_one()

# a: 1
# b: 2
# a: 1



from math import e
print(e) #2.718281828459045
print(round(e)) #3

#e沒有被宣告但內建,build-in
