from base_tool import BaseTool


class TranslatorTool(BaseTool):
    def execute(self, args):
        text = args.get("text", "").strip()
        target_language = args.get("target_language", "").strip().lower()

        if not text:
            raise ValueError("Missing 'text'.")
        if not target_language:
            raise ValueError("Missing 'target_language'.")

        demo_dict = {
            ("hello", "french"): "bonjour",
            ("hello", "german"): "hallo",
            ("hello", "spanish"): "hola",
            ("thank you", "french"): "merci",
        }

        translated = demo_dict.get((text.lower(), target_language))
        if translated:
            return translated

        return f"No demo translation available for '{text}' to {target_language}."

    def get_declaration(self):
        return {
            "name": "translate",
            "description": "Translate text into a target language",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"},
                    "target_language": {"type": "string"}
                },
                "required": ["text", "target_language"]
            }
        }