from base_tool import BaseTool


class CalculatorTool(BaseTool):
    def execute(self, args):
        expression = args.get("expression", "").strip()

        if not expression:
            raise ValueError("Missing 'expression'.")

        # Simple protection for assignment use
        allowed_chars = "0123456789+-*/(). %"
        if any(ch not in allowed_chars for ch in expression):
            raise ValueError("Expression contains unsupported characters.")

        return str(eval(expression, {"__builtins__": {}}, {}))

    def get_declaration(self):
        return {
            "name": "calculator",
            "description": "Evaluate mathematical expressions like 2+2 or (5*4)/2",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Math expression to evaluate"
                    }
                },
                "required": ["expression"]
            }
        }