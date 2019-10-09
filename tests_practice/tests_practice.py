import unittest
import math
import mock

from tasks_practice import (
    task_1, task_2, task_3, task_4,
    task_5, task_6, task_7, task_8,
    task_9, task_10, task_11, task_12,
    task_13, task_14, task_15, task_16,
    task_17, task_18, task_19, task_20
)


class Test(unittest.TestCase):
    def test_task_1(self):
        a = [1, 2, 3]
        b = [2, 4, 5]
        result = set([1, 2, 3, 4, 5])
        self.assertEqual(task_1(a, b), result)

    def test_task_2(self):
        string = "I am a good developer. I am also A writer"
        self.assertEqual(task_2(string), 5)

    def test_task_3_true(self):
        self.assertEqual(task_3(81), True)

    def test_task_3_false(self):
        self.assertEqual(task_3(20), False)

    def test_task_3_3(self):
        self.assertEqual(task_3(3), True)

    def test_task_4(self):
        self.assertEqual(task_4(34), 7)
        self.assertEqual(task_4(48), 3)

    def test_task_5(self):
        list_example = [2, 0, 6, 0, 9]
        list_result = [2, 6, 9, 0, 0]
        self.assertEqual(task_5(list_example), list_result)

    def test_task_6(self):
        self.assertTrue(task_6([5, 7, 9, 11]))

    def test_task_7(self):
        self.assertEqual(task_7([2, 5, 7, 9, 7, 5, 2]), 9)

    def test_task_8(self):
        self.assertEqual(task_8([1, 2, 3, 4, 6, 7, 8]), 5)

    def test_task_9(self):
        self.assertEqual(task_9([1, 2, 3, 5, (1, 2), 3]), 4)

    def test_task_10(self):
        self.assertEqual(task_10("Hello World and Coders"), "sredoC dna dlroW olleH")

    def test_task_11(self):
        self.assertEqual(task_11(83), "1 : 23")

    def test_task_12(self):
        self.assertEqual(task_12("fun&!! time"), "time")

    def test_task_13(self):
        with mock.patch('builtins.input', return_value="My name is Michele"):
            self.assertEqual(task_13("My name is Michele"), "Michele is name My")

    def test_task_14(self):
        with mock.patch('builtins.input', return_value=8):
            self.assertEqual(task_14(8), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_task_15(self):
        self.assertEqual(task_15([1, 4, 9, 16, 25, 36, 49, 64, 81, 100]), [4, 16, 36, 64, 100])

    def test_task_16(self):
        with mock.patch('builtins.input', return_value=4):
            self.assertEqual(task_16(4), 10)

    def test_task_17(self):
        with mock.patch('builtins.input', return_value=4):
            self.assertEqual(task_17(4), math.factorial(4))

    def test_task_18(self):
        self.assertEqual(task_18("zabncdz"), "AbcOdEA")

    def test_task_19(self):
        self.assertEqual(task_19("edcba"), "abcde")
        self.assertEqual(task_19("ababab"), "aaabbb")

    def test_task_20(self):
        self.assertTrue(task_20(5, 10))
        self.assertFalse(task_20(1, -1))
        self.assertEqual(task_20(4, 4), -1)


if __name__ == "__main__":
    unittest.main()
