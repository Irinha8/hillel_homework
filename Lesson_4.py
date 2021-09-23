def count_greater_or_equal(numbers, x):
    """
    Функия принимает на вход список чисел numbers и число x.
    Возращает количество элементов списка numbers больше либо равных x.
    """
    counter = 0
    for number in numbers:
        if number >= x:
            counter += 1
    return counter

def test_count_greater_or_equal():
    assert count_greater_or_equal([1, 2, 3, 4, 5], 2) == 4
    assert count_greater_or_equal([1, 2, 3, 4, 5], 1) == 5
    assert count_greater_or_equal([1, 2, 3, 4, 5], 0) == 5
    assert count_greater_or_equal([0, 1], 2) == 0
    assert count_greater_or_equal([], 2) == 0
    print("Great your solution works!")

test_count_greater_or_equal()

def rotate(numbers, n):
    """
    Функия принимает на вход список чисел numbers и число n.
    Применяет к этому списку операцию вращения направо n раз и возвращает его.
    Функция возращает ссылку на исходный список(повернутый нужное кол-во раз), а не создает новый.
    Операция вращения работает так: 0-ой элемент становится 1-м, 1-ый становится вторым, 2-ой третьим и т д.
    Последний становится первый. Примеры смотреть в тестовой функции.
    """
    for i in range(n):
        if len(numbers) != 0:
            number = numbers.pop()
            numbers.insert(0, number)
        else:
            numbers = []
    return numbers

def test_rotate():
    assert rotate([1, 2, 3], 1) == [3, 1, 2]
    assert rotate([1, 2, 3], 2) == [2, 3, 1]
    assert rotate([1, 2, 3], 3) == [1, 2, 3]
    assert rotate([1, 2, 3], 0) == [1, 2, 3]
    assert rotate([1], 1) == [1]
    assert rotate([1], 0) == [1]
    assert rotate([], 2) == []

    print("Great your solution works!")

test_rotate()

def extend(a, b):
    """
    Даны два списка, надо их обеъединить и получить один список.
    Надо расширить список a элементами из списка b.
    """
    a = a + b
    return a

def test_extend():
    assert extend([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert extend([4, 5, 6], [1, 2, 3], ) == [4, 5, 6, 1, 2, 3]
    assert extend([], [4, 5, 6]) == [4, 5, 6]
    assert extend([1, 2, 3], []) == [1, 2, 3]
    assert extend([1], [4]) == [1, 4]
    print("Great your solution works!")
test_extend()

def is_prime(n):
    """
    Дано число n.
    Если n простое число верните True, иначе False.
    Определние простого числа https://ru.wikipedia.org/wiki/%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5_%D1%87%D0%B8%D1%81%D0%BB%D0%BE
    """
    if n <= 1:
        return False
    if n > 1:
        counter = 0
        for i in range(1, n):
            if n % i == 0:
                counter += 1
        if counter > 2:
            return False
        else:
            return True

def test_is_prime():
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(24) is False
    assert is_prime(5) is True
    assert is_prime(0) is False
    assert is_prime(107) is True
    assert is_prime(19) is True
    print("Great your solution works!")
test_is_prime()

def merge(a, b):
    """
    Сложная задача. Если самостоятельно решите без Гугла, вы большой молодец.
    Даны два отсортированных по возрастанию списка чисел a, b.
    Надо объединить их в один список, так чтобы результирующий список тоже был отсортирован.
    Нельзя пользоваться  методом sort у списка. Нельзя пользоваться стандартной функцией sorted.
    """
    a = a + b
    result = []
    while len(a) != 0:
        result.append(min(a))
        a.remove(min(a))
    return result
def test_merge():
    assert merge([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge([4, 5, 6], [1, 2, 3]) == [1, 2, 3, 4, 5, 6]
    assert merge([2, 4, 6], [1, 3, 5]) == [1, 2, 3, 4, 5, 6]
    assert merge([4, 5, 6], []) == [4, 5, 6]
    assert merge([], [1, 3, 5]) == [1, 3, 5]
    assert merge([], []) == []
    print("Great your solution works!")
test_merge()


def has_substring(s, t):
    """
    Даны две строки s и t.
    Верните True если строка s содержит строку t в качестве подстроки, иначе верните False
    Нельзя пользоваться оператором in или любой другой встроенной опрецией проверки на подстроку.
    Делаем все руками :)
    """
    if len(s) < len(t):
        return False
    elif len(t) == 0:
        return True
    elif (len(s) >= len(t)) and len(t) > 0:
        for i in range(len(s)):
            if s[i] == t[0]:
                count = 0
                for j in range(len(t)):
                    if t[j] != s[i+j]:
                        return False
                    else:
                        count += 1
                if count == len(t):
                    return True

def test_has_substring():
    assert has_substring("some text", "text") is True
    assert has_substring("some text", "some") is True
    assert has_substring("", "text") is False
    assert has_substring("text", "") is True  # любая строка содержит в себе пустую подстроку
    assert has_substring("", "") is True  # даже пустая строка содержит в себе пустую подстроку :)
    print("Great your solution works!")
test_has_substring()



