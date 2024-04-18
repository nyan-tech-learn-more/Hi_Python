#6-2_map()

#map (可迭代的[列表等等都可], 函式)

store = [ #列表
    ('襯衫', 20), #元組 #美金
    ('褲子', 30) ,
    ('外套', 9000),
    ('襪子', 10)
]
#lambda parameter_list: expression
to_enros = lambda data: (data[0], data[1]* 0.82) #取第一個欄位與第二個欄位，第二個欄位還要乘以0.82

store_enros = list(map(to_enros, store)) #用list把回傳數值(object) 轉換
print(store_enros)#[('襯衫', 16.4), ('褲子', 24.599999999999998), ('外套', 7380.0), ('襪子', 8.2)]
