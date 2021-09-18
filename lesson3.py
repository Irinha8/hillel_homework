"""
Задание 1(5 - баллов):
Напишите программу, которая преобразует из значение температуры из Цельсия в Фарангейты.
Значние температуры в Цельсиях вводится пользователем
Формулу погуглите))
"""

#  BEGIN
celc = float(input())
far = (celc * 9/5) + 32
print("Фаренгейты - ", far)


#  END

"""
Задание 2(5 - балоов):
В python кроме стандартных операций ==, !=, <, >
есть еще операции
1. >= это больше или равно 2 >= 1 -> True, 2 >= 2 -> True, 2 >= 3 -> False
2. <= это меньше или равно 2 <= 3 -> True, 2 <= 2 -> True, 2 <= 1 -> False
Напишите программу, которая вычисляет модуль числа.
Модуль числа это такая математическая функция:
|x| = x, если x >= 0
|x| = -x, если x < 0
Число вводится пользоваетелем.
"""
#  BEGIN
n = int(input())
if n >= 0:
    mod = n
else:
    mod = -n
print(mod)



#  END

"""
Задание 3(7 - баллов):
Напишите программу, которая считает функцию голосования.
Функция голосование это логическая функция f(x, y, z) от трех
логических(это значит они принимают значение либо True либо False) аргументов x, y, z
и вычисляется следющим образом:
f(x, y, x) = True, если ХОТЯ БЫ два из трех аргументов True, иначе она равна False
Пример: f(True, False, True) = True
В этом задании нужно считать три значение x, y, z.
0 будет отвечать за False
1 будет отвечать за True
И вывести на экран значение фукнции голосования от этих трех значений.
Пример взаимодействия:
0
1
1
>> True
Пример взаимодействия:
0
0
1
>> False
"""

#  BEGIN
x,y,z = int(input()), int(input()),int(input())
print(True) if (x + y + z) >= 2 else print(False)


#  END

"""
Задание 4(7 - баллов):
Напишите программу, которая для введенного целого числа n считает значение
факториала  n!. n! = 1 * 2 * 3 * ... * n
"""

#  BEGIN
n = int(input())
f = 1
for i in range(1, n+1):
    f *= i
print(f)

#  END


"""
Задание 5(8 - баллов):
Напишите программу, которая для введенного целого числа n считает значение произведения
всех четных чисел до n(n >= 2)включительно.
Пример: n = 6: 2 * 4 * 6 = 48
        n = 4: 2 * 4 = 8
        n = 2: 2
"""

#  BEGIN
n = int(input())
mult = 1
for i in range(2, n+1, 2):
    mult *= i
print(mult)




#  END


"""
Задание 6(8 - баллов):
Напишите программу, которая для введененой строки считает количество символов латинской 'a' в ней
и печатает на экран
Вводится строка только в нижнем регистре
Пример: для "margarita" это выведется 3
        для "python is the best" выведется 0
"""

#  BEGIN
word = input()
c = 0
for symbol in word:
    if symbol == "a":
        c += 1
print(c)

#  END


"""
Задание 7(10 - баллов):
Напишите программу, которая для введененой строки считает количество гласных букв в ней
и печатает на экран. Гласными считаются: a, e, i, o, u, y
Вводится строка только в нижнем регистре
Пример: для "margarita" выведется 4 (a - 3, i - 1)
        для "python is the best" выведется 5 (y - 1, o - 1, i - 1, e - 2)
"""
#  BEGIN
s = input()
vocals = 0
for symbol in s:
    if symbol == "a":
        vocals += 1
    elif symbol == "e":
        vocals += 1
    elif symbol == "i":
        vocals += 1
    elif symbol == "o":
        vocals += 1
    elif symbol == "u":
        vocals += 1
    elif symbol == "y":
        vocals += 1
print(vocals)


#  END


"""
Задание 7(10 - баллов):
Напишите программу, которая для введененой строки считает количество согласных букв в ней
и печатает на экран. В этой задаче будем считать, что строка не содержит пробелов.
Вводится строка только в нижнем регистре
Пример: для "margarita" выведется 5
"""
#  BEGIN
s = input()
vocals = 0
for symbol in s:
    if symbol == "a":
        vocals += 1
    elif symbol == "e":
        vocals += 1
    elif symbol == "i":
        vocals += 1
    elif symbol == "o":
        vocals += 1
    elif symbol == "u":
        vocals += 1
    elif symbol == "y":
        vocals += 1
print(len(s) - vocals)

# но можно и просто

s = input()
c = 0
for symbol in s:
    if symbol in "bcdfghjklmnpqrstvwxz":
        c += 1
print(c)

#  END


"""
Задание 8(20 - баллов):
Напишите программу, которая для введененой строки печатает ее символы в обрамном порядке
Пример: для "margarita" выведется "atiragram"
        для "python is the best" выведется "tseb eht si nohtyp"
Вводится строка только в нижнем регистре
"""
#  BEGIN
s = input()
new_s = ''
for i in range(len(s)-1, -1, -1):
    new_s += s[i]
print(new_s)


#  END


"""
Задание 9(20 - баллов):
Напишите программу, которая для введенного целого числа n печатает такую вот пирамиду
1
2 2
3 3 3
4 4 4 4
....
n n n ... n
В последней строке n раз напечатали n
"""

#  BEGIN
n = int(input())
for i in range(1, n + 1):
    print((str(i) + " ") * i)
    #коряво, но другое в голову не пришло)


#  END