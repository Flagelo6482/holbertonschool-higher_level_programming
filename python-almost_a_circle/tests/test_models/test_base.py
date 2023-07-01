"""Comentario"""
import unittest
from models.base import Base


class To_json_string(unittest.TestCase):
    """Comentario"""

    def test_init(self):
        """Comentario"""
        obj = Base()
        self.assertEqual(1, obj.id)

    def test_to_json_string_empty(self):
        """Comentario"""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        """Comentario"""
        self.assertEqual("[]", Base.to_json_string(None))


if __name__ == '__main__':
    unittest.main()
