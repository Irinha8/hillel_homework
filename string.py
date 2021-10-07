"""
Задача 2.
Нужно реализовать модуль string.py для работы строками и реализовать там несколько функций:
has_substring(s, t) - функция проверяет есть ли в строке s подстрока t. Мы такую задачу решали в предыдущих заданиях.
is_number(s) - проверяет что строка является числом. Например, строка "1234" является числом, а строка "abc12" не является.
is_case_insensitive_equal(s, t) - проверяет что строки одинаковы, даже если отличаются регистром букв. Например, "AAbbAA"
одинаковая со строкой "aaBBaA". Эти строки состоят из тех же букв на тех же позициях просто в разных регистрах.
"""


def has_substring(s, t):
    if t in s:
        return True
    else:
        return False


def is_number(s):
    return s.isdigit()


def is_case_insensitive_equal(s, t):
    if s.lower() == t.lower():
        return True
    else:
        return False
