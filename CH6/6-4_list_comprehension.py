#list comprehension 列表推導式


#寫了五行
def square(x):
    return x * x
    
list = [] #宣告空列表
for i in range(1,11):
        list.append(square(i)) #把1~11每一個都丟到square()內得到結果後加到list內
print(list)
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#列表推導式, 運算寫在前面
square2 = [i*i for i in range(1,11)]
print("列表推導式:", square2)
#列表推導式: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#----
#過濾學生成績
greades = []
grades = [100,90,66,80,82,77,29,50,59,]
pass_grades = [g for g in grades if g >= 60 ] 
print(pass_grades)
#[100, 90, 66, 80, 82, 77]

#[g for g in grades if g >= 60] 是一個列表生成式（List Comprehension）的語法：
# grades 是一個包含數字的列表，表示學生成績。
# [g for g in grades if g >= 60] 是一個用來過濾 grades 列表中成績大於等於 60 的元素的表達式。
# 在這個表達式中，g 是一個臨時變量，它代表 grades 列表中的每個元素。
# if g >= 60 是一個條件，只有當 g 大於等於 60 時，才會將 g 加入到新的列表中。
# 因此，[g for g in grades if g >= 60] 會返回一個新的列表，其中包含 grades 中所有大於等於 60 的成績。
# pass_grades 就是這個新的列表，其中包含了 [100, 90, 66, 80, 82, 77] 這些成績。這個列表生成式可以方便地過濾出符合特定條件的元素，並且以簡潔的方式創建新的列表。
