import pytest


def unique(numbers):
    """
    Дна список чисел. Некоторые числа в нем могут повторяться.
    Верните новый список чисел, который состоит из чисел numbers, но уже без повторений.
    """
    numbers = set(numbers)
    return list(numbers)


@pytest.mark.parametrize("lst, expected",
                         [([1, 1, 2, 3, 4, 4, 5, 5], [1, 2, 3, 4, 5]),
                          ([1, 1, 1, 1], [1]),
                          ([], [])])
def test_unique(lst, expected):
    assert unique(lst) == expected


def count_words(string):
    """
    Дан список строк strings.
    Нужно для каждой строки посчитать сколько раз она встретилось в списке.
    """
    d = {}
    for word in string:
        quantity = string.count(word)
        d.update({word: quantity})

    return d


@pytest.mark.parametrize("words, counter", [(
        ["text", "text", "apple", "orange", "yellow", "orange"], {
            "text": 2,
            "orange": 2,
            "yellow": 1,
            "apple": 1
        }),
    (["text", "text", "text", "text", "text", "orange"], {
        "text": 5,
        "orange": 1,
    }),
    ([], {})])
def test_count_words(words, counter):
    assert count_words(words) == counter


def consistent_string(strings, allowed):
    """
    Дан список строк strings, и строка allowed, которая состоит из уникальных символов.
    Реализуйте функцию, которая из списка строк strings отфильтрует только те, которые состоят из символов
    содержащихся в allowed и не содержат других символов. Нужное вернуть множество(set) из нужных строк.
    """
    result = set()
    allowed = set(allowed)
    for word in strings:
        w_set = set(word)
        if w_set - allowed == set():
            result.add(word)
    return result


@pytest.mark.parametrize("strings, allowed, expected", [(["ad", "bd", "aaab", "baa", "badab"], "ab", {"aaab", "baa"}),
                                                        (["a", "b", "c", "ab", "ac", "bc", "abc"], "abc",
                                                         {"a", "b", "c", "ab", "ac", "bc", "abc"}),
                                                        (["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], "cad",
                                                         {"cc", "acd", "ac", "d"})])
def test_consistent_string(strings, allowed, expected):
    assert consistent_string(strings, allowed) == expected


def sort_desc(strings):
    """
    Дан список строк. Отсортируйте его в порядке обратном алфавитному.
    """
    strings.sort()
    strings.reverse()

    return strings


@pytest.mark.parametrize("strings, result",
                         [(["ad", "bd", "aaab", "baa", "badab"], ['bd', 'badab', 'baa', 'ad', 'aaab']),
                          (["a", "b", "c", "ab", "ac", "bc", "abc"],
                           ['c', 'bc', 'b', 'ac', 'abc', 'ab', 'a'])])
def test_sort_desc(strings, result):
    assert sort_desc(strings) == result


def filter_even(numbers):
    """
    При помощи встроенной функции фильтр, отфильтруйте только четные числа из списка numbers
    в отсортированном по возрастанию порядке
    """
    lst = list(filter(lambda number: number % 2 == 0, numbers))
    lst.sort()
    return lst


@pytest.mark.parametrize("numbers, expected", [
    ([1, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12], [2, 4, 6, 8, 10, 12]),
    ([2, 2, 4, 6, 6, 8, 10, 12], [2, 2, 4, 6, 6, 8, 10, 12]),
    ([1, 1, 2, 3], [2]),
    ([1, 3, 5], [])])
def test_filter_even(numbers, expected):
    assert filter_even(numbers) == expected
