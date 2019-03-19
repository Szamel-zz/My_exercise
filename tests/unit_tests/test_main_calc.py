from unittest import TestCase
from unittest.mock import patch

from MockTraining.main_calc import Calculator


class TestCalculator(TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_my_sum(self):
        answer = self.calc.my_sum(2, 4)
        self.assertEqual(answer, 6)


class TestCalculator2(TestCase):
    @patch('MockTraining.main_calc.Calculator.my_sum', return_value=9)
    def test_my_sum(self, my_sum):
        self.assertEqual(my_sum(5,4), 9)


