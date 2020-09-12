from unittest import TestCase
import increment


class TestSimple(TestCase):
    def test_should_increment_by_1(self):
        x = 4
        actual = increment.inc1(x)
        # expected, actual
        self.assertEqual(x + 1, actual, "what!")

    # @unittest.skip("skip this test")
    # def test_add_correctly2(self):
    #     a = 3.3
    #     b = 44
    #     actual = hello.add(a, b)
    #     self.assertEqual(a + b, actual, "what!")
