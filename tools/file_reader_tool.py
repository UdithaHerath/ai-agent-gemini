from base_tool import BaseTool


class FileReaderTool(BaseTool):
    def execute(self, args):
        filename = args.get("filename", "").strip()

        if not filename:
            raise ValueError("Missing 'filename'.")

        try:
            with open(filename, "r", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            raise ValueError(f"File '{filename}' not found.")
        except Exception as e:
            raise ValueError(f"Could not read file: {e}")

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