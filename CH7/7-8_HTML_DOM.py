from bs4 import BeautifulSoup
#透過BeautifulSoup與Request套件拿到網頁內的文字內容
import requests

response = requests.get('https://lukahuang.github.io/simple_pages/amazon_jp.html')
soup = BeautifulSoup(response.text,"html.parser")  #使用text讀取response, 使用html解析器
#print(soup) #太多要做處理

#amazonjp 用開發人員工具找到商品標題，該行是span, id="productTitle"
#https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
print('Title : ')
print(soup.find('span', id="productTitle").getText())

#開發人員工具同樣手法找到價錢
#Title : 
#Nintendo Switch 本体 (ニンテンドースイッチ) Joy-Con(L) ネオンブルー/(R)ネオンレッド 
print('Pirce : ')
print(soup.find('span', id="priceblock_ourprice").getText())
#Pirce : 
#¥32,970
