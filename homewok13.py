"""
Напишите программа, которая считывает числа из файла 'in.txt", сортирует и пишет их в файл
"out.txt".
Пример входных данных в файле:
2 3 1 4 5 9 7
Пример выходных данных в файле:
1 2 3 4 5 7 9
"""
path = "./in.txt"
reader = open(path, mode="r")
content = reader.read()
numbers = sorted([int(number) for number in content.split()])
string_numbers = " ".join(map(str, numbers))
path = "./out.txt"
writer = open(path, mode='w')
result = writer.write(string_numbers)

