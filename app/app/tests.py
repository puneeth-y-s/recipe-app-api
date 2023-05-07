"""
sample tests
"""
from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module. """
    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(10, 15)
        self.assertEqual(res, 25)

    def test_subtract_numbers(self):
        """Test subtracting numbers"""
        res = calc.subtract(10, 7)
        self.assertEqual(res, 3)
