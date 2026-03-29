from base_tool import BaseTool
import datetime


class TimeTool(BaseTool):
    def execute(self, args):
        return str(datetime.datetime.now())

    def get_declaration(self):
        return {
            "name": "time",
            "description": "Get the current system date and time",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }