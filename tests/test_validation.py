import unittest
from unittest.mock import patch

from utils.validation import get_positive_integer_input


class TestValidation(unittest.TestCase):

    @patch("builtins.input", side_effect=["0", "-5", "10"])
    def test_positive_integer_rejects_invalid_values(self, mock_input):
        result = get_positive_integer_input("Enter a positive number: ")

        self.assertEqual(result, 10)
        self.assertEqual(mock_input.call_count, 3)


if __name__ == "__main__":
    unittest.main()