from unittest import TestCase
import increment


class TestSimple(TestCase):
    def test_should_increment_by_1(self):
        x = 4
        actual = increment.inc1(x)

        # available assert:
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

        # expected, actual
        self.assertEqual(x + 1, actual, "what!")
