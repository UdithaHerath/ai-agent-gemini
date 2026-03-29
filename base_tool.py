from abc import ABC, abstractmethod


class BaseTool(ABC):
    @abstractmethod
    def execute(self, args: dict):
        """Run the tool with structured arguments."""
        pass

    @abstractmethod
    def get_declaration(self):
        """Return Gemini function declaration schema."""
        pass