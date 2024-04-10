#使用python進行檔案偵測

import os
from os.path import isfile
# 建立一個檔案 4-4_test.txt  (touch 4-4_test.txt))

#宣告字串
str = "/home/runner/hiskio/4-4_test.txt"
print(str)  #/home/runner/hiskio/4-4_test.txt

# Windows下要加入f跳脫字元，不然會顯示錯誤：
# C:\UserslLuka23\OneDrive\桌面\workspace
# str = f"C:\UserslLuka23\OneDrive\桌面\workspace"
#或多加入斜線
# C:\\UserslLuka23\\OneDrive\\桌面\\workspace

if os.path.exists(str):  #exist檢查檔案是否存在
  print("路徑存在")  #如果str路徑在
else:
  print("路徑不存在")

#str = "/home/runner/hiskio/4-4_test.txt" #檔案
str = "/home/runner/hiskio/"  #目錄
print(str)  #/home/runner/hiskio/4-4_test.txt
if os.path.isfile(str):  # isfile判斷路徑是否為檔案
  print("路徑為檔案")
elif os.path.isdir(str):  # isdir判斷路徑是否為目錄
  print("路徑為目錄")
else:
  print("other")
