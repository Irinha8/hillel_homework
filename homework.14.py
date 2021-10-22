""""
Напишите программа, которая считывает слова из файла 'in.txt", фильтрует все длина которых больше 5 и пишет их в файл
"out.txt".
Пример входных данных в файле:
a ab abc abcd abcde abcdef
Пример выходных данных в файле:
abcde abcdef
"""
path = "./in.txt"
reader = open(path, mode="r")
content = reader.read()