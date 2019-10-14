import pytest
import math

from _pytest import monkeypatch

import tasks_practice


def test_task_1_get_common_elements():
    a = [1, 2, 3]
    b = [2, 4, 5]
    result = set([1, 2, 3, 4, 5])
    assert tasks_practice.task_1_get_common_elements(a, b) == result


def test_task_2_number_a_in_string():
    string = "I am a good developer. I am also a writer"
    assert tasks_practice.task_2_number_a_in_string(string) == 5


def test_task_3_is_integer_power_of_three_true():
    assert tasks_practice.task_3_is_integer_power_of_three(81) is True


def test_task_3_is_integer_power_of_three_false():
    assert tasks_practice.task_3_is_integer_power_of_three(20) is False


def test_task_3_3():
    assert tasks_practice.task_3_is_integer_power_of_three(3) is True


def test_task_4_add_digits_of_integer():
    assert tasks_practice.task_4_add_digits_of_integer(34), 7
    assert tasks_practice.task_4_add_digits_of_integer(48), 3


def test_task_5_move_zeros():
    list_example = [2, 0, 6, 0, 9]
    list_result = [2, 6, 9, 0, 0]
    assert tasks_practice.task_5_move_zeros(list_example) == list_result


def test_task_6_sequence_is_progression():
    assert tasks_practice.task_6_sequence_is_progression([5, 7, 9, 11]) is True


def test_task_7_find_non_duplicate_number():
    assert tasks_practice.task_7_find_non_duplicate_number([2, 5, 7, 9, 7, 5, 2]) == 9


def test_task_8_find_missing_number():
    assert tasks_practice.task_8_find_missing_number([1, 2, 3, 4, 6, 7, 8]) == 5


def test_task_9_get_count_elements():
    assert tasks_practice.task_9_get_count_elements([1, 2, 3, 5, (1, 2), 3]) == 4


def test_task_10_get_reverse_string():
    assert tasks_practice.task_10_get_reverse_string("Hello World and Coders") == "sredoC dna dlroW olleH"


def test_task_11_get_hours_and_minutes():
    assert tasks_practice.task_11_get_hours_and_minutes(83) == "1 : 23"


def test_task_12_get_largest_word():
    assert tasks_practice.task_12_get_largest_word("fun&!! time") == "time"


def test_task_13_get_words_in_backwards_order(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "My name is Michele")
    assert tasks_practice.task_13_get_words_in_backwards_order("My name is Michele") == "Michele is name My"


def test_task_15_get_even_elements():
    assert tasks_practice.task_15_get_even_elements([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == [4, 16, 36, 64, 100]


def test_task_16_get_sum_of_numbers(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 4)
    assert tasks_practice.task_16_get_sum_of_numbers(4) == 10


def test_task_17_get_factorial(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 4)
    assert tasks_practice.task_17_get_factorial(4) == math.factorial(4)


def test_task_18_replace_letter_in_string():
    assert tasks_practice.task_18_replace_letter_in_string("zabcd") == "AbcdE"


def test_task_19_get_sorted_word():
    assert tasks_practice.task_19_get_sorted_word("edcba") == "abcde"
    assert tasks_practice.task_19_get_sorted_word("ababab") == "aaabbb"


def test_task_20_number_compare():
    assert tasks_practice.task_20_number_compare(5, 10) is True
    assert tasks_practice.task_20_number_compare(1, -1) is False
    assert tasks_practice.task_20_number_compare(4, 4) == -1
