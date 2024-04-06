#shopping_cart.py

#list, set, tuple

#儲存商品和價格
goods = [] #list 商品名稱
prices = [] #list 商品價格

#使用無窮迴圈來對user詢問商品,
while True:
    #請使用者輸入想購買的物品
    good = input("請輸入想購買的物品:")
    if good.lower() =="end":
        break #如果使用者輸入end就跳出while迴圈,否則會一直問一下去
    price = float(input(f"請輸入 {good} 價格:"))
    #輸入了商品和價格後要儲存到列表中
    goods.append(good) #用append把輸入的goodㄧ個一個取出放進去goods
    prices.append(price)  #用append把輸入的priceㄧ個一個取出放進prices
print("商品列表:", goods)
print("價格列表:", prices)

# 請輸入想購買的物雨衣 
# 請輸入 雨衣 價格:100
# 請輸入想購買的物品安全帽
# 請輸入 安全帽 價格:500
# 請輸入想購買的物品end
# 商品: ['雨衣', '安全帽']
# 價格: [100.0, 500.0]

#enumerate() 函數用於將一個可遍歷對象（如列表、元組、字典等）轉換為帶有索引的枚舉對象，通常用於 for 迴圈中。

for index, good in enumerate(goods):
#    print("索引 index:", index)
#    print("商品名稱 good:", good)
    print(f"{index+1}. {good} 價格: {prices[index]:.2f}")
    #第幾個商品(index+1)+名稱(good)+商品索引對應價格(price)的索引


total = sum(prices) #sum() 函數用於計算列表或元組中的所有元素的總和
print(f"總價格：${total}")

# Output:
# 請輸入想購買的物品:phone
# 請輸入 phone 價格:30000
# 請輸入想購買的物品:pen
# 請輸入 pen 價格:152
# 請輸入想購買的物品:juice
# 請輸入 juice 價格:20
# 請輸入想購買的物品:end
# 商品列表: ['phone', 'pen', 'juice']
# 價格列表: [30000.0, 152.0, 20.0]
# 1. phone 價格: 30000.00
# 2. pen 價格: 152.00
# 3. juice 價格: 20.00
# 總價格：$30172.0
