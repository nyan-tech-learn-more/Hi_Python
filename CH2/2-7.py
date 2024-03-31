#if else elif

# Boolean 
for_sale = True
if for_sale:
    print("This item is for sale")
else:
    print('未出售')

age = int(input("請輸入年齡"))
if age >= 18:
    print("OK")
else:
    print("No")

#elif = lese if  
age = int(input("請輸入年齡"))
if age >= 100:
    print("Dead")
elif age >= 18:
    print("Good")
elif age < 0:
    print("Not yet")
else:
    print("You Need 18")
