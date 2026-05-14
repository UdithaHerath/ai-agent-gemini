from base_tool import BaseTool


class CalculatorTool(BaseTool):
    def execute(self, params):
        try:
            expression = params.get("expression")
            if not expression:
                return "Error: Missing expression"

            result = eval(expression, {"__builtins__": {}}, {})
            return str(result)

        except ZeroDivisionError:
            return "Error: Division by zero"

        except Exception as e:
            return f"Error: {str(e)}"
    
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