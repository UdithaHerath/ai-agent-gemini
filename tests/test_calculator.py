import unittest
from tools.calculator_tool import CalculatorTool


class TestCalculatorTool(unittest.TestCase):

    def setUp(self):
        self.calculator = CalculatorTool()

    def test_addition(self):
        result = self.calculator.execute({"expression": "5 + 3"})
        self.assertIn("8", result)

    def test_subtraction(self):
        result = self.calculator.execute({"expression": "10 - 4"})
        self.assertIn("6", result)

    def test_multiplication(self):
        result = self.calculator.execute({"expression": "6 * 7"})
        self.assertIn("42", result)

    def test_division(self):
        result = self.calculator.execute({"expression": "8 / 2"})
        self.assertIn("4", result)

    def test_division_by_zero(self):
        result = self.calculator.execute({"expression": "5 / 0"})
        self.assertTrue("error" in result.lower() or "division" in result.lower())


if __name__ == "__main__":
    unittest.main()