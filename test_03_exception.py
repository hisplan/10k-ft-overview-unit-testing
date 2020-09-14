from unittest import TestCase
import increment


class TestCatchException(TestCase):
    def test_should_increment_by_n(self):
        x = 4
        n = 3
        actual = increment.inc2(x, n=3)
        self.assertEqual(x + n, actual, "what!")

    def test_should_raise_exception(self):
        with self.assertRaises(TypeError):
            x = 4
            increment.inc2(x, n="xyz")
