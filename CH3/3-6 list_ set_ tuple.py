#python:list, set and tuple

#---------------------------------------------
# list 列表
# 使用方括號包起來

#宣告
fruits = ["蘋果", "柳橙", "香蕉", "椰子"]
#印出
print(fruits[0]) #印出蘋果
#for印出所有
for f in fruits:
    print(f)

#加入元素到最後面
fruits.append("芭樂")
print(fruits) #['蘋果', '柳橙', '香蕉', '椰子', '芭樂']


#刪除element
fruits.remove("椰子")
print(fruits) #['蘋果', '柳橙', '香蕉', '芭樂']


#找到元素的索引位置
print(fruits.index("柳橙")) #1

#列表可以加入同樣的內容！！！
fruits.append("蘋果")
fruits.append("蘋果")
print(fruits) #['蘋果', '柳橙', '香蕉', '芭樂', '蘋果', '蘋果']
#知道特定元素有幾個
print(fruits.count("蘋果")) #3個


#反轉列表 reverse()
fruits.reverse()
print(fruits) #['蘋果', '蘋果', '芭樂', '香蕉', '柳橙', '蘋果']

#---------------------------------------------
#Set 集合
#使用大括號包起來
fruits_set = {'蘋果', '芭樂', '香蕉'}
print(fruits_set) #每次印出來順序都不同
#在set集合中，不可以重複、沒有順序性

fruits_set.add("蘋果") #故意加入重複的元素
for f in fruits_set: #印出值
    print(f, end=" ") #香蕉 芭樂 蘋果
  
#集合不會有重複的數值

#判斷元素是否在集合
fruits_set = {'蘋果', '芭樂', '香蕉'}
if "蘋果" in fruits_set:
    print("有一顆蘋果")
if '芭樂' in fruits_set:
    print("有一顆芭樂")
else:
    print("沒有西瓜")

#---------------------------------------------
#Tuple 元祖
#不能改變了禁止改變tuple
#有順序
#小括號

#小括號宣告
fruits_tuple = ('蘋果', '芭樂', '香蕉','蘋果')
print(fruits_tuple.count('蘋果')) #2

#找到特定元素的索引 index()
print(fruits_tuple.index('芭樂')) #1

#故意新增元素到tuple 
fruits_tuple.add('柳丁') #Tuple 無法被改變，會跳錯誤
# AttributeError: 'tuple' object has no attribute 'add'

