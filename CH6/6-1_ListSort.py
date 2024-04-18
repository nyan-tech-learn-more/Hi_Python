#列表排序
num_list = [1,3,5,2,4]

num_list.sort()

print(num_list) # [1, 2, 3, 4, 5]

#列表的反過來排序
num_list2 = [1,4,3,5,2,4]

num_list2.sort(reverse=True)
print(num_list2) #[5, 4, 4, 3, 2, 1]
#--------------------
#字串的排序
str_list = ['Jack', 'Lin', 'Huang', 'Andy']
str_list.sort()
print(str_list) #['Andy', 'Huang', 'Jack', 'Lin'] 照字母開頭大小排 
#字串反過來，第一個字母一樣才會比第二個字母
str_list2 = ['Jack', 'Lin', 'Huang', 'Andy']
str_list2.sort(reverse=True)
print(str_list2) #反過來 ['Lin', 'Jack', 'Huang', 'Andy']
#-----
#元組的排列 Tuple
#列表內的元組
student = [
    ("小明",170, "C"),
    ("小華",180, "B"),
    ("老王",190, "A")
]
#lambda parameter_list: expression
sorted_stu = sorted(student, key=lambda student: student[1])
#依據[1]身高續排序
print(sorted_stu) #[('小明', 170, 'C'), ('小華', 180, 'B'), ('老王', 190, 'A')]


