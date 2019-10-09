import pytest
import math

from _pytest import monkeypatch

from tasks_practice import (task_1, task_2, task_3, task_4,
                            task_5, task_6, task_7, task_8,
                            task_9, task_10, task_11, task_12,
                            task_13, task_15, task_16, task_17,
                            task_18, task_19, task_20
                            )


def test_task_1():
    a = [1, 2, 3]
    b = [2, 4, 5]
    result = set([1, 2, 3, 4, 5])
    assert task_1(a, b) == result


def test_task_2():
    string = "I am a good developer. I am also a writer"
    assert task_2(string) == 5


def test_task_3_true():
    assert task_3(81) is True


def test_task_3_false():
    assert task_3(20) is False


def test_task_3_3():
    assert task_3(3) is True


def test_task_4():
    assert task_4(34), 7
    assert task_4(48), 3


def test_task_5():
    list_example = [2, 0, 6, 0, 9]
    list_result = [2, 6, 9, 0, 0]
    assert task_5(list_example) == list_result


def test_task_6():
    assert task_6([5, 7, 9, 11]) is True


def test_task_7():
    assert task_7([2, 5, 7, 9, 7, 5, 2]) == 9


def test_task_8():
    assert task_8([1, 2, 3, 4, 6, 7, 8]) == 5


def test_task_9():
    assert task_9([1, 2, 3, 5, (1, 2), 3]) == 4


def test_task_10():
    assert task_10("Hello World and Coders") == "sredoC dna dlroW olleH"


def test_task_11():
    assert task_11(83) == "1 : 23"


def test_task_12():
    assert task_12("fun&!! time") == "time"


def test_task_13(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: "My name is Michele")
    assert task_13("My name is Michele") == "Michele is name My"


def test_task_15():
    assert task_15([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]) == [4, 16, 36, 64, 100]


def test_task_16(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 4)
    assert task_16(4) == 10


def test_task_17(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 4)
    assert task_17(4) == math.factorial(4)


def test_task_18():
    assert task_18("zabcd") == "AbcdE"


def test_task_19():
    assert task_19("edcba") == "abcde"
    assert task_19("ababab") == "aaabbb"


def test_task_20():
    assert task_20(5, 10) is True
    assert task_20(1, -1) is False
    assert task_20(4, 4) == -1
