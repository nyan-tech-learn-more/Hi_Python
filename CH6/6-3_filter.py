#filter 過濾
#可用來過濾可迭代的資料結構，例如列表等等

friend = [
    ('Alice', 18),
    ('Bob', 19),
    ('Susan', 16),
    ('CAT', 12)
]

age_filter = lambda data :data[1] >=18 

#filter
#filter 函數形式 : filter(function, sequnce)
can_drink_friend = list(filter(age_filter, friend)) #list列表才能正確顯示

for item in can_drink_friend:
        print(item[0])
        print(item[1])
# Alice
# 18
# Bob
# 19
