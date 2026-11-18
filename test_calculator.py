import unittest

from calculator import calculate


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


if __name__ == "__main__":
    unittest.main()
