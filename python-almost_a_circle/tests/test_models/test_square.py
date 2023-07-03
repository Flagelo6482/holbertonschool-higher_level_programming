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
        self.assertEqual("[Square] (37) 0/0 - 5", out)
        self.assertEqual(s1.width, s1.height)
        self.assertEqual(s1.x, s1.y)
        self.assertEqual(37, s1.id)
        s2 = Square(5, 4)
        out = s2.__str__()
        self.assertEqual("[Square] (38) 4/0 - 5", out)
        s3 = Square(5, 4, 10)
        out = s3.__str__()
        self.assertEqual("[Square] (39) 4/10 - 5", out)
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
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.readline(), '[]')
        r1 = Rectangle(3, 4)
        r2 = Rectangle(5, 4)
        Rectangle.save_to_file([r1, r2])
        file_1 = r1.to_dictionary()
        file_2 = r2.to_dictionary()
        file_ = [file_1, file_2]
        str_json = Rectangle.to_json_string(file_)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.readline(), str_json)
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.readline(), '[]')
        r3 = Rectangle(1, 2)
        r4 = Rectangle(3, 4)
        Rectangle.save_to_file([r3, r4])
        file_3 = r3.to_dictionary()
        file_4 = r4.to_dictionary()
        file_ = [file_3, file_4]
        str_json = Rectangle.to_json_string(file_)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.readline(), str_json)
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.readline(), '[]')
        s1 = Square(3)
        s2 = Square(5)
        Square.save_to_file([s1, s2])
        file_1 = s1.to_dictionary()
        file_2 = s2.to_dictionary()
        file_ = [file_1, file_2]
        str_json = Square.to_json_string(file_)
        with open("Square.json", "r") as f:
            self.assertEqual(f.readline(), str_json)
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.readline(), '[]')




if __name__ == '__main__':
    unittest.main()
