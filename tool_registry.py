class ToolRegistry:
    def __init__(self):
        self.tools = {}

    def register_tool(self, name, tool):
        self.tools[name] = tool

    def execute(self, name, args):
        if name not in self.tools:
            raise ValueError(f"Tool '{name}' not found.")
        return self.tools[name].execute(args)

    def get_declarations(self):
        return [tool.get_declaration() for tool in self.tools.values()]

    def has_tool(self, name):
        return name in self.tools
    def get_tool(self, name):
        return self.tools.get(name)