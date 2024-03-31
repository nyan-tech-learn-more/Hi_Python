#username
name = "code shiba 程式柴"
# 幾個字元
Length = len(name)
print("您的全名共有", Length, "個字元。")
      
# 找到第一個空格
#可以使用 find() 函數找到字串中某個子串的位置
#如果找不到子串，則 find() 函數返回 -1。
space_pos = name.find(" ") #4
print(space_pos)
print("第一個空格出現在第", space_pos,"個字元。")



# capitalize()
#The capitalize() method returns a string where the first character is upper case, and the rest is lower case
name_capitalized = name.capitalize()
#code -> Code
print("您的全名（第一個字母大寫）:", name_capitalized)

# upper() 和 Lower(）函數
name_upper = name.upper() #都變成大寫


#Lower()
name_lower = name.lower() #都變成小寫
print("您的全名（全部小寫）：" ,name_lower)

#count() 計算總和
phone_number = input("請輸入電話號碼")
dash_count = phone_number.count("-") #計算有幾個-
print("DashCount", dash_count, "個短橫線")

#replace() 替換字串
dash_bye = phone_number.replace("-", "") 
print("電話號碼把短橫線取代成沒有東西", dash_bye)

# 程式練習：驗證使用者輸入的合法性
# -您的使用者名稱不能超過 12 個字元。
#-您的使用者名稱不能包含空格。
#-您的使用者名稱不能包含數字。
#-如果都符合的話，顯示 歡迎 +使用者名稱
username = input("請輸入使用者名稱")

if len(username) > 12:
    print("使用者名稱不能超過 12 個字元。")
elif " " in username:
    print("使用者名稱不能包含空格")
elif not username.isalpha(): #isalpha() 判斷是否都是字母,加上not代表判斷如果不是都為字母時
#如果字符串至少有一个字符并且所有字符都是字母则返回True，否则返回False
    print("不能有字母以外的")
else:
    print("welcome!!")


