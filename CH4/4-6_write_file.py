#寫入檔案

str = "/home/runner/hiskio/New_File.txt"
text = '嗨！\n祝你順利進行!'

#write
#先打開檔案,填上路'徑str, 模式為write 'w'
with open(str, 'w') as file:
    file.write(text)  #把text內容寫入到file,使用.write()方法寫入

# shell output:
# ~/hiskio$ cat New_File.txt 
# 嗨！
# 祝你順利進行!

#A 插入模式 可以插到最後一行
with open(str, 'a') as file:
  file.write('\n go go go')
#Shell output:
# ~/hiskio$ cat New_File.txt 
# 嗨！
# 祝你順利進行!
#  go go go~

#再執行一次 w 模式, 會覆蓋掉所有資料, w寫入時會全部覆蓋, gogogo會消失
with open(str, 'w') as file:
  file.write(text) 
#shell output:
# ~/hiskio$ cat New_File.txt 
# 嗨！
# 祝你順利進行!
