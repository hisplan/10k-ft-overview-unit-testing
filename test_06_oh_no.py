from unittest import TestCase, skip
import increment


class TestCatchException(TestCase):
    @skip("skip this test")
    def test_should_catch_exception(self):
        increment.inc2(3, n="xyz")
