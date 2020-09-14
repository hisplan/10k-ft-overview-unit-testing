from unittest import TestCase
import increment


class TestMultiple(TestCase):
    def test_should_increment_by_1(self):
        x = 4
        actual = increment.inc1(x)
        self.assertEqual(x + 1, actual, "what!")

    def test_should_increment_by_n(self):
        x = 4
        n = 3
        actual = increment.inc2(x, n=3)
        self.assertEqual(x + n, actual, "what!")
