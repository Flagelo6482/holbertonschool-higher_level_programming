"""Comentario"""
import unittest
import json
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Comentario"""

    def test_init(self):
        """Comentario"""
        obj_1 = Base()
        obj_2 = Base(99)
        self.assertEqual(2, obj_1.id)
        self.assertEqual(99, obj_2.id)
        self.assertEqual(Base("3").id, "3")

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
        list_output_1 = Rectangle.from_json_string('[]')
        self.assertEqual([], list_output_1)
        list_output_2 = Rectangle.from_json_string(None)
        self.assertEqual([], list_output_2)

    def test_save_to_file(self):
        """Comentario"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.readline(), '[]')
        Rectangle.save_to_file([])
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

    def test_create(self):
        """Test for this method"""
        r1 = Rectangle(3, 5, 1)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertAlmostEqual(r1.id, 1)
        self.assertAlmostEqual(r2.id, 1)
        self.assertAlmostEqual(r2, r2)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)

    def test_load_from_file(self):
        """Test for this method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_input = [r1, r2]
        Rectangle.save_to_file(list_input)
        list_output = Rectangle.load_from_file()
        self.assertAlmostEqual(list_output[0].id, 3)
        self.assertAlmostEqual(list_output[0].x, 2)
        self.assertAlmostEqual(list_output[0].width, 10)
        self.assertAlmostEqual(list_output[0].height, 7)
        self.assertAlmostEqual(list_output[0].y, 8)
        self.assertAlmostEqual(list_output[1].id, 4)
        self.assertAlmostEqual(list_output[1].x, 0)
        self.assertAlmostEqual(list_output[1].width, 2)
        self.assertAlmostEqual(list_output[1].height, 4)
        self.assertAlmostEqual(list_output[1].y, 0)
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        sinput = [s1, s2]
        Square.save_to_file(sinput)
        soutput = Square.load_from_file()
        self.assertAlmostEqual(soutput[0].id, 5)
        self.assertAlmostEqual(soutput[0].width, 5)
        self.assertAlmostEqual(soutput[0].height, 5)
        self.assertAlmostEqual(soutput[0].x, 0)
        self.assertAlmostEqual(soutput[0].y, 0)
        self.assertAlmostEqual(soutput[1].id, 6)
        self.assertAlmostEqual(soutput[1].width, 7)
        self.assertAlmostEqual(soutput[1].height, 7)
        self.assertAlmostEqual(soutput[1].x, 9)
        self.assertAlmostEqual(soutput[1].y, 1)

    def test_pycodestyle_conformance(self):
        """Test that we conform to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py',
                                    'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")


if __name__ == '__main__':
    unittest.main()
