"""Comentario"""


import unittest
import json
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Comentario"""

    def test_init(self):
        """Comentario"""
        r_1 = Rectangle(2, 4)
        self.assertEqual(2, r_1.width)
        self.assertEqual(4, r_1.height)
        self.assertEqual(0, r_1.x)
        self.assertEqual(0, r_1.y)
        self.assertEqual(12, r_1.id)
        self.assertRaises(TypeError, Rectangle, "3", 2)
        self.assertRaises(TypeError, Rectangle, 2, "6")
        self.assertRaises(ValueError, Rectangle, -1, 3)
        self.assertRaises(ValueError, Rectangle, 3, -1)
        self.assertRaises(ValueError, Rectangle, 0, 1)
        self.assertRaises(ValueError, Rectangle, 1, 0)
        self.assertIsInstance(Rectangle(10, 2), Base)
        r_2 = Rectangle(1, 2, 3, 4)
        self.assertEqual(1, r_2.width)
        self.assertEqual(2, r_2.height)
        self.assertEqual(3, r_2.x)
        self.assertEqual(4, r_2.y)
        self.assertEqual(20, r_2.id)
        self.assertRaises(TypeError, Rectangle, 4, 5, "2", 1)
        self.assertRaises(TypeError, Rectangle, 4, 5, 2, "1")
        self.assertRaises(ValueError, Rectangle, 4, 5, -2, 1)
        self.assertRaises(ValueError, Rectangle, 4, 5, 2, -1)

    def test_width(self):
        """Comentario"""
        r_3 = Rectangle(1, 2)
        r_3.width = 100
        self.assertEqual(100, r_3.width)

    def test_height(self):
        """Comentario"""
        r_4 = Rectangle(1, 2)
        r_4.height = 200
        self.assertEqual(200, r_4.height)

    def test_x(self):
        """Comentario"""
        r_5 = Rectangle(1, 2, 3)
        r_5.x = 44
        self.assertEqual(44, r_5.x)

    def test_y(self):
        """Comentario"""
        r_6 = Rectangle(1, 2, 3, 4)
        r_6.y = 66
        self.assertEqual(66, r_6.y)

    def test_area(self):
        r_7 = Rectangle(15, 15, 3, 3)
        self.assertEqual(225, r_7.area())

    def test_display(self):
        r_8 = Rectangle(2, 2)
        self.assertEqual(None, r_8.display())

    def test_str(self):
        r_14 = Rectangle(3, 3)
        out = r_14.__str__()
        self.assertEqual(out, r_14.__str__())

    def test_update(self):
        r_9 = Rectangle(20, 20, 20, 20)
        self.assertEqual(None, r_9.update(height=1))
        x_1 = Rectangle(10, 10, 10, 10)
        x_1.update(5)
        self.assertEqual(5, x_1.id)
        self.assertEqual(10, x_1.width)
        self.assertEqual(10, x_1.height)
        self.assertEqual(10, x_1.x)
        self.assertEqual(10, x_1.y)

        x_2 = Rectangle(20, 20, 20, 20)
        x_2.update(x=2)
        self.assertEqual(x_2.x, 2)
        self.assertEqual(x_2.y, 20)
        self.assertEqual(x_2.width, 20)
        self.assertEqual(x_2.height, 20)
        self.assertEqual(x_2.id, 31)

        x_2.update(x=3, id=100, height=7, y=4, width=10)
        self.assertEqual(x_2.x, 3)
        self.assertEqual(x_2.y, 4)
        self.assertEqual(x_2.width, 10)
        self.assertEqual(x_2.height, 7)
        self.assertEqual(x_2.id, 100)


    def test_to_dictionary(self):
        """Comentario"""
        r_10 = Rectangle(56, 34, 24, 12)
        out = {'id': 26, 'width': 56, 'height': 34, 'x': 24, 'y': 12}
        self.assertEqual(out, r_10.to_dictionary())
        r_11 = Rectangle(10, 4, 3)
        out = {'id': 27, 'width': 10, 'height': 4, 'x': 3, 'y': 0}
        self.assertEqual(out, r_11.to_dictionary())
        r_12 = Rectangle(5, 5)
        out = {'id': 28, 'width': 5, 'height': 5, 'x': 0, 'y': 0}
        self.assertEqual(out, r_12.to_dictionary())
        r_13 = Rectangle(5, 5, 5, 5, 99)
        out = {'id': 99, 'width': 5, 'height': 5, 'x': 5, 'y': 5}
        self.assertEqual(out, r_13.to_dictionary())


if __name__ == '__main__':
    unittest.main()
