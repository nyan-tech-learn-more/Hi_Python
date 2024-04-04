#巢狀迴圈

#1-9在同一行

for x in range(1,10):
    print(x, end=" ") #print結尾內建換行，end=" "改成空格
#1 2 3 4 5 6 7 8 9


for y in range(5): #跑5次,0-4
    for x in range(1,10): #輸出1-9
       print(x, end=" ") #print結尾內建換行，end=" "改成空格
    print()#換行

#請使用者輸入行 and 列 and 符號，形成一個長方形都是符號組成
rows = int(input("請輸入行數:"))
cols = int(input("請輸入列數:"))
symbol = input("請輸入符號:")

for R in range(rows): #大圈，換幾行
    for C in range(cols): #小圈，每行幾個
      print(symbol, end= " ")#print結尾內建換行，end=" "改成空格
    print() #每行跑完都換行

# input : 2, 4, @ , 兩行（橫）四列（直）每行四個@
# @@@@
# @@@@

#input : 6, 3, @ （六行三列）換六行，每行三個$
# $$$
# $$$
# $$$
# $$$
# $$$
# $$$
