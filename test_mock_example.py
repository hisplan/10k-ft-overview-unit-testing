from unittest import TestCase, mock
import increment

# https://docs.python.org/3/library/unittest.mock.html#the-mock-class
class TestMockExample(TestCase):
    @mock.patch("increment.randint", return_value=3)
    def test_increment(self, mock_randint):
        actual = increment.inc3(4)
        self.assertEqual(7, actual)
        mock_randint.assert_called()
        mock_randint.assert_called_with(1, 100)
