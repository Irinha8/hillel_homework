calculate = input().split()

number1 = int(calculate[0])
number2 = int(calculate[2])
operation = calculate[1]

import calc
if operation == "+":
    res = calc.summa(number1, number2)
if operation == "-":
    res = calc.difference(number1, number2)
if operation == "*":
    res = calc.product(number1, number2)
if operation == "/":
    res = calc.division(number1, number2)
print(res)
