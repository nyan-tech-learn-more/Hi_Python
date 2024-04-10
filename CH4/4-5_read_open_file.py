#str = "/home/runner/hiskio/4-4_test.txt" #正確檔案
str = "/home/runner/hiskio/4-4_test.tx" #錯誤檔案名稱
try:
    with open(str) as file: #open讀取路徑、給一個代稱叫做file
        print(file.read()) #read()讀txt檔案 #apple this is tes for python
except FileNotFoundError: #檔名打錯等問題發生
    print("無此檔案，檔案不存在")
