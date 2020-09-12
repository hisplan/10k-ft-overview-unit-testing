from unittest import TestCase
import increment


class TestMultiple(TestCase):
    def setUp(self):
        with open("data.txt", "rt") as fin:
            self.x = int(fin.read())

    def tearDown(self):
        pass

    def test_should_increment_by_1(self):
        actual = increment.inc1(self.x)
        self.assertEqual(self.x + 1, actual, "what!")

    def test_should_increment_by_n(self):
        n = 3
        actual = increment.inc2(self.x, n=3)
        self.assertEqual(self.x + n, actual, "what!")
