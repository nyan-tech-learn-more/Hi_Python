#關鍵字參數

def hello(greeting, title, first_name, lastname):
    print(f"{greeting}, {title}, {first_name} {lastname}")

hello("你好!", "Mr", "Orange", "H") #你好!, Mr, Orange H
#這種方式順序不能改變 並且你要去反覆的確認這個順序

hello(greeting="你好!",title="Mr", first_name="西瓜", lastname="Chen")
#你好!, Mr, 西瓜 Chen
#避免帶入錯數值
#直接將關鍵字指定好
#-----------------------------

#獲得電話號碼練程式
def get_phone(country_code, area_code, first, last): #定義關鍵字參數
    return f"{country_code}--{area_code}--{first}--{last}" #回傳
str = get_phone(country_code = "886", area_code = "02", first = "2456", last = "7890") #get_phone return是一個字串，所以要印出來,故放到str內
print(str) #886--02--2456--7890
#如果你有一個帶有多個參數的函式
#有更好的可讀性
#關鍵字參數是一個很好的選擇
