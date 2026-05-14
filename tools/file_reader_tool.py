from base_tool import BaseTool


class FileReaderTool(BaseTool):
    def execute(self, params):
        try:
            filename = params.get("filename") or params.get("file_path")

            if not filename:
                return "Error: Missing filename"

            with open(filename, "r") as f:
                return f.read()

        except FileNotFoundError:
            return "Error: File not found"

        except Exception as e:
            return f"Error: {str(e)}"

    def get_declaration(self):
        return {
            "name": "read_file",
            "description": "Read the contents of a text file",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "Path to the file to read"
                    }
                },
                "required": ["filename"]
            }
        }