import string
import math

from typing import List


def task_1_get_common_elements(a: List, b: List):
    """
    write a program that returns a list
    that contains only the elements
    that are common between the lists (without duplicates).
    """
    return set(a + b)


def task_2_number_a_in_string(text: str):
    """
    Return the number of times that the letter “a”
    appears anywhere in the given string
    """
    return text.lower().count('a')


def task_3_is_integer_power_of_three(num: int):
    """
    Write a Python program to check
    if a given positive integer is a power of three
    """
    x = math.log(num, 3)
    return int(x) == x


def task_4_add_digits_of_integer(num):
    """
    Write a Python program to add the digits
    of a positive integer repeatedly
    until the result has a single digit.
    """
    while True:
        digits_count = sum(int(digit) for digit in str(num))
        if digits_count < 10:
            return digits_count
        num = digits_count


def task_5_move_zeros(ls: List):
    """
    Write a Python program to push all zeros to the end of a list.
    """
    for i in range(len(ls)):
        ls.remove(0)
        ls.append(0)
    return ls


def task_6_sequence_is_progression(seq: List):
    """
    Write a Python program to check a sequence of numbers
    is an arithmetic progression or not.
    """
    if len(seq) < 2:
        return False
    else:
        start = seq[0]
        step = seq[1] - seq[0]
        stop = seq[-1]
        return list(range(start, stop + 1, step)) == seq


def task_7_find_non_duplicate_number(ls: List):
    """
    Write a Python program to find the number
    in a list that doesn't occur twice.
    """
    for i in range(len(ls)):
        if ls.count(ls[i]) == 1:
            return ls[i]


def task_8_find_missing_number(ls: List):
    """
    Write a Python program to find a missing number from a list.
    """
    for i in range(len(ls)):
        if ls[i] != i + 1:
            return i + 1


def task_9_get_count_elements(ls: List):
    """
    Write a Python program to count the elements
    in a list until an element is a tuple.
    """
    count_ls = 0
    for i in range(len(ls)):
        if type(ls[i]) != tuple:
            count_ls += 1
        else:
            return count_ls


def task_10_get_reverse_string(text: str):
    """
    Write a program that will take the str parameter
    being passed and return the string in reversed order.
    For example: if the input string is "Hello World and Coders"
    then your program should return the string sredoC dna dlroW olleH.
    """
    return text[::-1]


def task_11_get_hours_and_minutes(num: int):
    """
    Write a program that will take the num parameter being passed
    and return the number of hours and minutes the parameter
    converts to (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    """
    return str(num // 60) + " : " + str(num % 60)


def task_12_get_largest_word(text: str):
    """
    Write a program that will take the parameter
    being passed and return the largest word in the string.
    If there are two or more words that are the same length,
    return the first word from the string with that length.
    Ignore punctuation.
    """
    return max(text.split())


def task_13_get_words_in_backwards_order(text: str):
    """
    Write a program (using functions!) that asks the user
    for a long string containing multiple words.
    Print back to the user the same string,
    except with the words in backwards order.
    """
    text = input("Write a text\n")
    return str(' '.join(text.split()[::-1]))


def task_14_fibonacci_sequence(num: int):
    """
    Write a program that asks the user
    how many Fibonacci numbers to generate and then generates them.
    Take this opportunity to think about how you can use functions.
    Make sure to ask the user to enter the number
    of numbers in the sequence to generate.
    """
    num_fib = int(input("enter the number of numbers in the sequence to generate\n"))

    def fib(num_fib):
        a, b = 0, 1
        for i in range(num_fib):
            yield a
            a, b = b, a + b

    return list(fib(num_fib))


def task_15_get_even_elements(a: List[int]):
    """
    Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a
    and makes a new list that has only the even elements of this list in it.
    """
    return [i for i in a if i % 2 == 0]


def task_16_get_sum_of_numbers(num: int):
    """
    Write a program that will add up all the numbers
    from 1 to input number. For example: if the input is 4
    then your program should return 10 because 1 + 2 + 3 + 4 = 10.
    """
    num = int(input("enter the number\n"))
    return sum([i for i in range(num + 1)])


def task_17_get_factorial(num: int):
    """
    Write a program that will take the parameter
    being passed and return the factorial of it.
    For example: if num = 4, then your program
    should return (4 * 3 * 2 * 1) = 24.
    """
    num = int(input("enter the number\n"))

    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)

    return factorial(num)


def task_18_replace_letter_in_string(word: str):
    """
    Write a program that will take the str parameter being passed
    and modify it using the following algorithm.
    Replace every letter in the string with the letter
    following it in the alphabet (ie. cbecomes d, zbecomes a).
    Then capitalize every vowel in this new string (a, e, i, o, u)
    and finally return this modified string.
    """
    vowels = "aeiou"
    return ''.join([chr(ord(i) + 1).replace('{', 'A').upper() if chr(ord(i) + 1) in vowels
                    else chr(ord(i) + 1).replace('{', 'A') for i in word])


def task_19_get_sorted_word(word: str):
    """
    Write a program that will take the str string parameter
    being passed and return the string with the letters
    in alphabetical order (ie. hello becomes ehllo). Assume numbers
    and punctuation symbols will not be included in the string.
    """
    return ''.join(sorted(word))


def task_20_number_compare(a, b: int):
    """
    Write a program that will take both parameters being passed
    and return the true if num2 is greater than num1,
    otherwise return the false. If the parameter values are equal
    to each other then return the string -1
    """
    if b > a:
        return True
    elif a > b:
        return False
    elif a == b:
        return -1
