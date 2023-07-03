"""Comentario"""


import unittest
import json
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Comentario"""

    def test_init(self):
        """Comentario"""
        s1 = Square(5)
        out = s1.__str__()
        self.assertEqual("[Square] (38) 0/0 - 5", out)
        self.assertEqual(s1.width, s1.height)
        self.assertEqual(s1.x, s1.y)
        self.assertEqual(38, s1.id)
        s2 = Square(5, 4)
        out = s2.__str__()
        self.assertEqual("[Square] (39) 4/0 - 5", out)
        s3 = Square(5, 4, 10)
        out = s3.__str__()
        self.assertEqual("[Square] (40) 4/10 - 5", out)
        s4 = Square(5, 4, 10, 11)
        out = s4.__str__()
        self.assertEqual("[Square] (11) 4/10 - 5", out)
        s5 = Square(1, 2, 3, -4)
        out = s5.__str__()
        self.assertEqual("[Square] (-4) 2/3 - 1", out)
        self.assertRaises(ValueError, Square, 0, 0, 0, 0)
        self.assertRaises(TypeError, Square, "1")
        self.assertRaises(TypeError, Square, 1, "5")
        self.assertRaises(TypeError, Square, 1, 2, "3")
        self.assertRaises(ValueError, Square, -1, 2, 3, 4)
        self.assertRaises(ValueError, Square, 1, -2, 3, 4)
        self.assertRaises(ValueError, Square, 1, 2, -3, 4)

    def test_save_to_file(self):
        """Comentario"""
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)


if __name__ == '__main__':
    unittest.main()
