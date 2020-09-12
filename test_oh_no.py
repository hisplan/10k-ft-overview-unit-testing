from unittest import TestCase, skip
import increment


class TestCatchException(TestCase):
    def test_should_catch_exception(self):
        increment.inc2(3, n="xyz")
