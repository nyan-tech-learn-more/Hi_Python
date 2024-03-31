#python 計算機

operator = input("請輸入運算符號(+,-,*,/):")
number1 = float(input("請輸入第一個數字:"))
number2 = float(input("請輸入第二個數字:"))

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    result = number1 / number2
else:
    print('operator無效')

print(result)
