import unittest
from tool_registry import ToolRegistry
from tools.calculator_tool import CalculatorTool


class TestToolRegistry(unittest.TestCase):

    def setUp(self):
        self.registry = ToolRegistry()
        self.calculator = CalculatorTool()
        self.registry.register_tool("calculator", self.calculator)

    def test_tool_registration(self):
        tool = self.registry.get_tool("calculator")
        self.assertIsNotNone(tool)

    def test_tool_execution(self):
        tool = self.registry.get_tool("calculator")
        result = tool.execute({"expression": "2 + 2"})
        self.assertIn("4", result)

    def test_invalid_tool(self):
        tool = self.registry.get_tool("unknown")
        self.assertIsNone(tool)


if __name__ == "__main__":
    unittest.main()