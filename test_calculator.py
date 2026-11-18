import unittest
from unittest.mock import patch

from calculator import calculate, main, read_number


class CalculatorTests(unittest.TestCase):
    def test_supported_operations(self):
        self.assertEqual(calculate("+", 8, 3), 11)
        self.assertEqual(calculate("-", 8, 3), 5)
        self.assertEqual(calculate("*", 8, 3), 24)
        self.assertEqual(calculate("/", 8, 4), 2)

    def test_division_by_zero_raises_clear_error(self):
        with self.assertRaisesRegex(ZeroDivisionError, "Cannot divide by zero"):
            calculate("/", 8, 0)

    def test_unsupported_operation_raises_clear_error(self):
        with self.assertRaisesRegex(ValueError, "Unsupported operation"):
            calculate("%", 8, 3)

    @patch("builtins.input", return_value="not a number")
    def test_read_number_reports_invalid_input(self, _input):
        with self.assertRaisesRegex(ValueError, "Please enter a valid number"):
            read_number("Number: ")

    @patch("builtins.input", side_effect=["%", "8", "3", "q"])
    def test_main_reports_invalid_operation_and_continues(self, _input):
        with patch("builtins.print") as print_mock:
            main()

        print_mock.assert_any_call("Error: Unsupported operation: %")
        print_mock.assert_any_call("Goodbye!")


if __name__ == "__main__":
    unittest.main()