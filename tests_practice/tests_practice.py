import unittest
import math
import mock

import tasks_practice


class Test(unittest.TestCase):
    def test_task_1_get_common_elements(self):
        a = [1, 2, 3]
        b = [2, 4, 5]
        result = set([1, 2, 3, 4, 5])
        self.assertEqual(tasks_practice.task_1_get_common_elements(a, b), result)

    def test_task_2_number_a_in_string(self):
        string = "I am a good developer. I am also A writer"
        self.assertEqual(tasks_practice.task_2_number_a_in_string(string), 5)

    def test_task_3_is_integer_power_of_three_true(self):
        self.assertEqual(tasks_practice.task_3_is_integer_power_of_three(81), True)

    def test_task_3_is_integer_power_of_three_false(self):
        self.assertEqual(tasks_practice.task_3_is_integer_power_of_three(20), False)

    def test_task_3_is_integer_power_of_three_3(self):
        self.assertEqual(tasks_practice.task_3_is_integer_power_of_three(3), True)

    def test_task_4_add_digits_of_integer(self):
        self.assertEqual(tasks_practice.task_4_add_digits_of_integer(34), 7)
        self.assertEqual(tasks_practice.task_4_add_digits_of_integer(48), 3)

    def test_task_5_move_zeros(self):
        list_example = [2, 0, 6, 0, 9]
        list_result = [2, 6, 9, 0, 0]
        self.assertEqual(tasks_practice.task_5_move_zeros(list_example), list_result)

    def test_task_6_sequence_is_progression(self):
        self.assertTrue(tasks_practice.task_6_sequence_is_progression([5, 7, 9, 11]))

    def test_task_7_find_non_duplicate_number(self):
        self.assertEqual(tasks_practice.task_7_find_non_duplicate_number([2, 5, 7, 9, 7, 5, 2]), 9)

    def test_task_8(self):
        self.assertEqual(tasks_practice.task_8_find_missing_number([1, 2, 3, 4, 6, 7, 8]), 5)

    def test_task_8_find_missing_number(self):
        self.assertEqual(tasks_practice.task_9_get_count_elements([1, 2, 3, 5, (1, 2), 3]), 4)

    def test_task_10_get_reverse_string(self):
        self.assertEqual(tasks_practice.task_10_get_reverse_string("Hello World and Coders"), "sredoC dna dlroW olleH")

    def test_task_11(self):
        self.assertEqual(tasks_practice.task_11_get_hours_and_minutes(83), "1 : 23")

    def test_task_11_get_hours_and_minutes(self):
        self.assertEqual(tasks_practice.task_12_get_largest_word("fun&!! time"), "time")

    def test_task_13_get_words_in_backwards_order(self):
        with mock.patch('builtins.input', return_value="My name is Michele"):
            self.assertEqual(tasks_practice.task_13_get_words_in_backwards_order("My name is Michele"), "Michele is name My")

    def test_task_14_fibonacci_sequence(self):
        with mock.patch('builtins.input', return_value=8):
            self.assertEqual(tasks_practice.task_14_fibonacci_sequence(8), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_task_15_get_even_elements(self):
        self.assertEqual(tasks_practice.task_15_get_even_elements([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]), [4, 16, 36, 64, 100])

    def test_task_16_get_sum_of_numbers(self):
        with mock.patch('builtins.input', return_value=4):
            self.assertEqual(tasks_practice.task_16_get_sum_of_numbers(4), 10)

    def test_task_17_get_factorial(self):
        with mock.patch('builtins.input', return_value=4):
            self.assertEqual(tasks_practice.task_17_get_factorial(4), math.factorial(4))

    def test_task_18_replace_letter_in_string(self):
        self.assertEqual(tasks_practice.task_18_replace_letter_in_string("zabncdz"), "AbcOdEA")

    def test_task_19_get_sorted_word(self):
        self.assertEqual(tasks_practice.task_19_get_sorted_word("edcba"), "abcde")
        self.assertEqual(tasks_practice.task_19_get_sorted_word("ababab"), "aaabbb")

    def test_task_20_number_compare(self):
        self.assertTrue(tasks_practice.task_20_number_compare(5, 10))
        self.assertFalse(tasks_practice.task_20_number_compare(1, -1))
        self.assertEqual(tasks_practice.task_20_number_compare(4, 4), -1)


if __name__ == "__main__":
    unittest.main()
