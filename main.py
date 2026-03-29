import os
from agent import Agent
from tool_registry import ToolRegistry

from tools.calculator_tool import CalculatorTool
from tools.time_tool import TimeTool
from tools.translator_tool import TranslatorTool
from tools.file_reader_tool import FileReaderTool


def build_registry():
    registry = ToolRegistry()
    registry.register("calculator", CalculatorTool())
    registry.register("time", TimeTool())
    registry.register("translate", TranslatorTool())
    registry.register("read_file", FileReaderTool())
    return registry


if __name__ == "__main__":
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

    registry = build_registry()
    agent = Agent( api key, registry)
    agent.run()