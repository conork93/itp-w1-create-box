import unittest

from create_box import create_box
from create_box import hollow_box


first_box_expected = """
****
****
****
""".lstrip()

second_box_expected = """
@
""".lstrip()

third_box_expected = """
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
xxxxxxxxxxxxxxxxxxxxxxxx
""".lstrip()

first_hollowbox_expected = """
*****
*   *
*   *
*   *
*****
""".lstrip()

second_hollowbox_expected = """
*
""".lstrip()

third_hollowbox_expected = """
****
*  *
****
""".lstrip()

class TestCreateBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(create_box(3, 4, '*'), first_box_expected)

    def test_small_box(self):
        self.assertEqual(create_box(1, 1, '@'), second_box_expected)

    def test_big_box(self):
        self.assertEqual(create_box(3, 24, 'x'), third_box_expected)

#hollow block test        
class TestHollowBox(unittest.TestCase):
    def test_box(self):
        self.assertEqual(hollow_box(5, 5, '*'), first_hollowbox_expected)

    def test_small_box(self):
        self.assertEqual(hollow_box(1, 1, '*'), second_hollowbox_expected)

    def test_big_box(self):
        self.assertEqual(hollow_box(3, 4, '*'), third_hollowbox_expected)
