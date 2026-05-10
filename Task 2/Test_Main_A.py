import unittest
from Main_A import to_descending

class TestMainA(unittest.TestCase):

    def test_to_descending(self):
        # Проверка на валидных значениях
        self.assertEqual(to_descending('3', '5'), (5, 3))
        self.assertEqual(to_descending('5', '3'), (5, 3))
        self.assertEqual(to_descending('7', '7'), (7, 7))
        self.assertEqual(to_descending('-5', '-2'), (-2, -5))
        self.assertEqual(to_descending('-10', '0'), (0, -10))

        # Проверка исключений при невалидных значениях
        self.assertRaises(ValueError, to_descending, 'NumX', '0')
        self.assertRaises(ValueError, to_descending, '0', 'NumY')
        self.assertRaises(ValueError, to_descending, 'NumX', 'NumY')