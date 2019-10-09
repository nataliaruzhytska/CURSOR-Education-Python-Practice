import math
import unittest

from homework import Rectangle


class RectangleValidValues(unittest.TestCase):

    def setUp(self):
        self.rect1 = Rectangle(3, 5)
        self.rect2 = Rectangle(3, 3)

    def test_get_rectangle_perimeter(self):
        self.assertEqual(self.rect1.get_rectangle_perimeter(), 16)
        self.assertEqual(self.rect2.get_rectangle_perimeter(), 12)

    def test_get_rectangle_square(self):
        self.assertEqual(self.rect1.get_rectangle_square(), 15)
        self.assertEqual(self.rect2.get_rectangle_square(), 9)

    def test_get_sum_of_corners(self):
        with self.subTest():
            for num in range(1, 5):
                self.assertEqual(self.rect1.get_sum_of_corners(num), num * 90)

    def test_get_rectangle_diagonal(self):
        self.assertEqual(self.rect1.get_rectangle_diagonal(), math.sqrt(34))
        self.assertEqual(self.rect2.get_rectangle_diagonal(), math.sqrt(18))

    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(self.rect1.get_radius_of_circumscribed_circle(), math.sqrt(34) / 2)
        self.assertEqual(self.rect2.get_radius_of_circumscribed_circle(), math.sqrt(18) / 2)

    def test_get_radius_of_inscribed_circle(self):
        self.assertEqual(self.rect2.get_radius_of_inscribed_circle(), math.sqrt(18) / (2 * math.sqrt(2)))


class RectangleInvalidValues(unittest.TestCase):

    def setUp(self):
        self.rect3 = Rectangle(4, 0)
        self.rect4 = Rectangle(-5, 7)
        self.rect5 = Rectangle(2, 7)

    def test_incorrect_parameter_raises(self):
        with self.subTest():
            with self.assertRaises(ValueError):
                self.rect3.get_rectangle_square()
                self.rect4.get_rectangle_square()
                self.rect3.get_rectangle_perimeter()
                self.rect4.get_rectangle_perimeter()
                self.rect5.get_radius_of_inscribed_circle()

    def test_incorrect_num_corners_raises(self):
        for num in range(5, 10):
            with self.subTest():
                with self.assertRaises(ValueError):
                    self.rect5.get_sum_of_corners(num)
                    

if __name__ == "__main__":
    unittest.main()
