"""Comentario"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class To_json_string(unittest.TestCase):
    """Comentario"""

    def test_init(self):
        """Comentario"""
        obj_1 = Base()
        obj_2 = Base(99)
        self.assertEqual(1, obj_1.id)
        self.assertEqual(99, obj_2.id)

    def test_to_json_string(self):
        """Comentario"""
        self.assertEqual("[]", Base.to_json_string(None))
        self.assertEqual("[]", Base.to_json_string([]))
        js = json.dumps([{'width': 4, 'height': 5}])
        self.assertEqual(js, Base.to_json_string([{'width': 4, 'height': 5}]))
        self.assertEqual(str, type(js))

    def test_from_json_string(self):
        """Comentario"""
        str_json = '[{"width": 4, "height": 5}]'
        self.assertEqual([], Base.from_json_string(None))
        j_s = json.loads(str_json)
        self.assertEqual(j_s, Base.from_json_string(str_json))
        self.assertEqual(list, type(j_s))

    def test_save_to_file(self):
        """Comentario"""
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

    def test_from_json_string(self):
        """Comentario"""
        list_output_1 = Rectangle.from_json_string('[]')
        self.assertEqual([], list_output_1)
        list_output_2 = Rectangle.from_json_string(None)
        self.assertEqual([], list_output_2)


if __name__ == '__main__':
    unittest.main()
