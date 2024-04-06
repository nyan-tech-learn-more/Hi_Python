#key -> Value 


#宣告
#大括號
#無順序
#可變
#不允許重複的Key

capital = {
    "United States": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "Russia": "Moscow" #最後一個不用逗號
}

# 訪問 'France' 的值
print(capital['France']) # 輸出 'Paris'

#get()取得key value
#可以使用 get() 方法來訪問字典中的值。如果字典中沒有指定的鍵，則 get() 方法將返回None，而不是引發 KeyError，如下所示
print(capital.get("Japan"))

#update 更新key, value
capital.update({"Germany": "Berlin"}) #要大括號
print(capital)


#用update()把另一個字典更新到自己身上
d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}
d1.update(d2) #d2字典掛到d1
d1.update(d3) #d3字典掛到d1, 
print(d1) # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


#刪除key, value
#pop(), 拿出key
capital.pop("United States")
print(capital) #{'France': 'Paris', 'Japan': 'Tokyo', 'Russia': 'Moscow', 'Germany': 'Berlin'}


#values() 取得字典所有的Value
print(capital.values()) #dict_values(['Paris', 'Tokyo', 'Moscow', 'Berlin'])

#items() 取得所有的key value
print(capital.items()) #dict_items([('France', 'Paris'), ('Japan', 'Tokyo'), ('Russia', 'Moscow'), ('Germany', 'Berlin')])
