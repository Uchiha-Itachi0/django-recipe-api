"""
TEST FOR CALC

"""

from django.test import SimpleTestCase
from . import calc


class CalcTest(SimpleTestCase):
    """Test the calc module"""

    def test_add_number(self):
        """Test add two number"""

        res = calc.add_two_numbers(6, 5)

        self.assertEquals(res, 11)
