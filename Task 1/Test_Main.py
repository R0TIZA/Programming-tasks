import unittest
from Main import calculate_a, calculate_b


class TestMain(unittest.TestCase):

    def test_a(self):
        # Тест-кейс из задачника
        self.assertEqual(calculate_a('-1', '-1'), 0.2366935)

        # Дополнительные тест-кейсы
        self.assertEqual(calculate_a('0', '0'), 1.0)
        self.assertEqual(calculate_a('1', '0'), 0.0)
        self.assertEqual(calculate_a('4', '-8'), -0.0107180)
        self.assertEqual(calculate_a('-3', '8'), 0.0)
        self.assertEqual(calculate_a('0.5', '-27'), -0.0125038)

        # Проверка исключений при невалидных значениях
        self.assertRaises(ValueError, calculate_a, 'NumX', '-1')
        self.assertRaises(ValueError, calculate_a, '-1', 'NumY')
        self.assertRaises(ValueError, calculate_a, 'NumX', 'NumY')
        self.assertRaises(ValueError, calculate_a, '', '-1')
        self.assertRaises(ValueError, calculate_a, '-1', '')

    def test_b(self):
        # Тест-кейс из задачника
        self.assertEqual(calculate_b('-1', '3'), -1.384381)

        # Дополнительные тест-кейсы
        self.assertEqual(calculate_b('0', '0'), 0.0)
        self.assertEqual(calculate_b('1', '1'), 0.803714)
        self.assertEqual(calculate_b('4', '2'), 4.432242)
        self.assertEqual(calculate_b('-3', '-1'), -0.643806)
        self.assertEqual(calculate_b('0.5', '5'), 0.701799)

        # Проверка исключений при невалидных значениях
        self.assertRaises(ValueError, calculate_b, 'NumX', '3')
        self.assertRaises(ValueError, calculate_b, '-1', 'NumZ')
        self.assertRaises(ValueError, calculate_b, 'NumX', 'NumZ')
        self.assertRaises(ValueError, calculate_b, '', '3')
        self.assertRaises(ValueError, calculate_b, '-1', '')