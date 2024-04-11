#python複製檔案

import shutil

#shutil.copyfile ->只會複製文件內容，不複製檔案資訊
#shutil.copy ->只複製內容不複製資訊，但目錄也可以用
#shutil.copy2 -> 會複製內容，也能複製文件資訊，權限，檔案資訊
w = "/home/runner/hiskio" #w代替路徑
source = f"{w}/Source.txt" #路徑{w}+檔案名稱,來源檔案
destination = f"{w}/Destination_file.txt" #路徑{w}+檔案名稱,目的地
shutil.copyfile(source, destination) #來源文件/目的文件
#複製Source.txt 去 產出Destination_file.txt

