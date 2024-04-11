import os
path = "/home/runner/hiskio/"

#刪除檔案 os.remove
os.remove(f"{path}/Destination_file.txt") #已經刪除

#------------------------------
#刪除空資料夾 os.rmdir
os.rmdir(f"{path}/removeme_dir") #已經刪除removeme_dir這個資料夾

#如果資料夾有檔案又使用rmdir 會出錯，防呆
OSError: [Errno 39] Directory not empty: '/home/runner/hiskio//removeme_dir'

#------------------------------
#刪除資料夾與其內容
import shutil
#刪除資料夾下的東西(危險)
shutil.rmtree(f"{path}/removeme_dir")

#------------------------------
#丟到資源回收桶(windows)
import send2trash
send2trash.send2trash(f"{path}/Source.txt")
#windows要(fr{Path}"XXXX/XXX.txt")
