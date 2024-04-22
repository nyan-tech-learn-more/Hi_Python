
#https://requests.readthedocs.io/en/latest/user/quickstart/
import requests

#Make a Request
r = requests.get('https://api.github.com/events')


#Response Content
print(r.text)

#JSON Response Content
r = requests.get('https://api.github.com/events')
print(r.json())


#------------------
#pip install BeautifulSoup4
from bs4 import BeautifulSoup #透過BeautifulSoup與Request套件拿到網頁內的文字內容

response = requests.get('https://lukahuang.github.io/simple_pages/page_1.html')
soup = BeautifulSoup(response.text, "html.parser") #使用text讀取response, 使用html解析器

#print(soup.prettify()) #soup這個物件美化，soup就是的html_doc解析的結果

print(soup.find("h1")) #找到H1開頭的段落的文字
#<h1>The First Page</h1>
print(soup.find("h1").getText) #getText只要裡面的文字
#The First Page

print(soup.find("p")) #找到H1開頭的段落的文字
# <p>
#     If you like, you can switch to the
#     <a href="./page_2.html">
#       Second Page</a>.
#   </p>
