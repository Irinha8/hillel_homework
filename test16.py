from lesson5 import unique, count_words, consistent_string, sort_desc, filter_even
import pytest


@pytest.mark.parametrize("lst, expected",
                         [([1, 1, 2, 3, 4, 4, 5, 5], [1, 2, 3, 4, 5]),
                          ([1, 1, 1, 1], [1]),
                          ([], [])])
def test_unique(lst, expected):
    assert unique(lst) == expected


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


@pytest.mark.parametrize("strings, allowed, expected", [(["ad", "bd", "aaab", "baa", "badab"], "ab", {"aaab", "baa"}),
                                                        (["a", "b", "c", "ab", "ac", "bc", "abc"], "abc",
                                                         {"a", "b", "c", "ab", "ac", "bc", "abc"}),
                                                        (["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"], "cad",
                                                         {"cc", "acd", "ac", "d"})])
def test_consistent_string(strings, allowed, expected):
    assert consistent_string(strings, allowed) == expected


@pytest.mark.parametrize("strings, result",
                         [(["ad", "bd", "aaab", "baa", "badab"], ['bd', 'badab', 'baa', 'ad', 'aaab']),
                          (["a", "b", "c", "ab", "ac", "bc", "abc"],
                           ['c', 'bc', 'b', 'ac', 'abc', 'ab', 'a'])])
def test_sort_desc(strings, result):
    assert sort_desc(strings) == result


@pytest.mark.parametrize("numbers, expected", [
    ([1, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12], [2, 4, 6, 8, 10, 12]),
    ([2, 2, 4, 6, 6, 8, 10, 12], [2, 2, 4, 6, 6, 8, 10, 12]),
    ([1, 1, 2, 3], [2]),
    ([1, 3, 5], [])])
def test_filter_even(numbers, expected):
    assert filter_even(numbers) == expected
