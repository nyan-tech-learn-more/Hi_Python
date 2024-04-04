#python : for loop 

#迭代

for x in range(1, 11):
    print(x)
#1 ~ 10


for x in reversed(range(1,11)): #倒過來要用reversed方法
    print(x)
print("Happy New Year!") #新年到數

credit_card = "1234-4567-9012-3456" #字串
for x in credit_card:
    if x == "-":
        continue #遇到"-"就跳過一次不印出x
        #break 會直接中斷整個回圈不走
    else:
        print(x) #一個一個印出來
#印出：123456790123456


#============================================
#字典dict
#key:value

my_dict = {"name": "Jack", "age": 26, "gender": "male"}
for x in my_dict:
    print(x) #這樣只會印出key, 不能印出value

print(my_dict.get("name")) #jack, get()取得value
print(my_dict['name']) #jack, 字典名稱[key]存取字典的值

for x, y in my_dict.items(): #items()會回傳key, value
    print(f"{x} : {y}")
#name : Jack
#age : 26
#gender : male
