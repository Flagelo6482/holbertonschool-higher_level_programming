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
        self.assertEqual(9, r_1.id)
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
        self.assertEqual(17, r_2.id)
        self.assertRaises(TypeError, Rectangle, 4, 5, "2", 1)
        self.assertRaises(TypeError, Rectangle, 4, 5, 2, "1")
        self.assertRaises(ValueError, Rectangle, 4, 5, -2, 1)
        self.assertRaises(ValueError, Rectangle, 4, 5, 2, -1)


if __name__ == '__main__':
    unittest.main()
