from typing import List, Dict, Union, Generator, ItemsView
import string

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> str:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    return [{k: (v.capitalize() if k == 'name' else v) for (k, v) in d.items()} for d in data]


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    return [{k: v for (k, v) in d.items() if k not in redundant_keys} for d in data]


def task_3_find_item_via_value(data: DT, value) -> List[Dict[str, Union[str, int]]]:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    return [d for d in data if {v for v in d.values() if v == value}]


def task_4_min_value_integers(data: List[int]) -> int:
    """
    Find and return minimum value from list
    """
    return min(data) if data else None


def task_5_min_value_strings(data: List[Union[str, int]]) -> str:
    """
    Find the longest string
    """
    if data:
        for i in range(len(data)):
            data[i] = str(data[i])
        return min(data, key=len)


def task_6_min_value_list_of_dicts(data: DT, key: str) -> str:
    """
    Find minimum value by given key
    Returns:

    """
    return min([d for d in data if d.get(key)], key=lambda x: x[key])


def task_7_max_value_list_of_lists(data: List[List[int]]) -> int:
    """
    Find max value from list of lists
    """
    return max([i for d in data for i in d])


def task_8_sum_of_ints(data: List[int]) -> int:
    """
    Find sum of all items in given list
    """
    return sum(data) if data else 0


def task_9_sum_characters_positions(text: str) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    return sum(ord(s) for s in text)


def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    for number in range(2, 201):
        for i in range(2, number):
            if number % i == 0:
                break
        else:
            yield number
