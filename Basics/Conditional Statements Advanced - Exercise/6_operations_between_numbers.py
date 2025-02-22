# 6. Operations between numbers

num1 = int(input())
num2 = int(input())
operator = input()

if operator == '+' :
    result = num1 + num2
    if result % 2 == 0 :
        print(f"{num1} + {num2} = {result} - even")
    else :
        print(f"{num1} + {num2} = {result} - odd")
elif operator == '-' :
    result = num1 - num2
    if result % 2 == 0:
        print(f"{num1} - {num2} = {result} - even")
    else:
        print(f"{num1} - {num2} = {result} - odd")
elif operator == '*' :
    result = num1 * num2
    if result % 2 == 0:
        print(f"{num1} * {num2} = {result} - even")
    else:
        print(f"{num1} * {num2} = {result} - odd")
elif (operator == '/') and (num1 != 0 and num2 != 0) :
    print(f"{num1} / {num2} = {num1 / num2}")
elif (operator == '%') and (num1 != 0 and num2 != 0) :
    print(f"{num1} % {num2} = {num1 % num2}")
else :
    if num1 == 0 :
        print(f"Cannot divide {num2} by zero")
    else :
        print(f"Cannot divide {num1} by zero")