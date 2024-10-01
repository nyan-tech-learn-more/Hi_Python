#Email 字串分析

email = "codeshiba@gmail.com"
index = email.index("@") #@在第幾個存到index

print(index) #9
print(email[0:9]) #codeshiba
print(email[0:index]) #codeshiba
print(email[:index]) #codeshiba,不輸入就是第一個開始
print(email[index+1:]) #gmail.com,@下一個開始
