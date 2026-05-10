import unittest
from Main_B import get_mode_text

class TestMainB(unittest.TestCase):

    def test_get_mode_text(self):
        # Проверка правильности типа возвращаемого значения
        self.assertIsInstance(get_mode_text('1'), str)
        self.assertIsInstance(get_mode_text('2'), str)
        self.assertIsInstance(get_mode_text('3'), str)
        self.assertIsInstance(get_mode_text('4'), str)
        self.assertIsInstance(get_mode_text('5'), str)

        # Проверка на пустоту возвращаемого значения
        self.assertNotEqual(get_mode_text('1'), '')
        self.assertNotEqual(get_mode_text('2'), '')
        self.assertNotEqual(get_mode_text('3'), '')
        self.assertNotEqual(get_mode_text('4'), '')
        self.assertNotEqual(get_mode_text('5'), '')

        # Проверка исключений при невалидных значениях
        self.assertRaises(ValueError, get_mode_text, 'Mode1')