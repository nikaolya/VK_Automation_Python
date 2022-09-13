from collections import Counter

import pytest


def sum_integers(a, b):
    return a + b


def test_should_sum_two_integers():
    assert sum_integers(1, 100) == 101


@pytest.mark.parametrize("variable,expected_type",
                         [(1, "<class 'int'>"), ("two", "<class 'str'>"), ({"three": 3}, "<class 'dict'>")])
def test_return_correct_input_variable_type(variable, expected_type):
    assert str(type(variable)) == expected_type


@pytest.mark.parametrize("string, value, expected_result", [("one", 3, "oneoneone"), ("one", 0, ""), ("one", -5, ""),
                                                            (("one", "two"), 2, ('one', 'two', 'one', 'two'))])
def test_should_multiply_string_by_value(string, value, expected_result):
    assert string * value == expected_result


def subtract_strings(str1, str2):
    return str1 - str2


def test_should_not_subtract_strings():
    with pytest.raises(TypeError):
        subtract_strings("string", "ring")


def delete_from_dict_while_iterating():
    dictionary = {1: "elephant"}
    for key, value in dictionary.items():
        if value == "elephant":
            del dictionary[key]
    return dictionary


def test_dict_should_not_change_by_iterating():
    try:
        dictionary = delete_from_dict_while_iterating()
    except RuntimeError as e:
        assert str(e) == "dictionary changed size during iteration"


def add_to_dict_new_value(element_to_add):
    dictionary = {1: "one"}
    dictionary[2] = element_to_add
    values = dictionary.values()
    counter = Counter(values)
    return str(dict(counter))


def test_should_add_to_dict_new_value():
    assert add_to_dict_new_value("one") == "{'one': 2}"
