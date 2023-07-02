"""Comentario"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle


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


if __name__ == '__main__':
    unittest.main()
