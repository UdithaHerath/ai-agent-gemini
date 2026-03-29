from google import genai
from google.genai import types
from memory import MemoryManager


class Agent:
    def __init__(self, api_key, tool_registry):
        self.client = genai.Client(api_key=api_key) if api_key else genai.Client()
        self.memory = MemoryManager()
        self.registry = tool_registry
        self.model_name = "gemini-2.5-flash"

    def run(self):
        print("AI Agent started. Type 'exit' to quit.\n")

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() in {"exit", "quit"}:
                print("AI: Goodbye!")
                break

            self.memory.add("user", user_input)

            reply = self._handle_user_message(user_input)

            self.memory.add("assistant", reply)
            print("AI:", reply)

    def _handle_user_message(self, user_input):
        try:
            contents = self._build_contents_with_history(user_input)

            tool_config = types.ToolConfig(
                function_calling_config=types.FunctionCallingConfig(mode="AUTO")
            )

            config = types.GenerateContentConfig(
                tools=[types.Tool(function_declarations=self.registry.get_declarations())],
                tool_config=tool_config,
                system_instruction=(
                    "You are a CLI AI agent. "
                    "Use tools when needed. "
                    "If a tool is called, your final answer must be based only on the tool result. "
                    "Do not invent, improve, or replace tool outputs with your own knowledge. "
                    "If the tool returns a demo result, present that demo result clearly. "
                    "After receiving tool results, produce a clear final answer."
                ),
            )

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=contents,
                config=config,
            )

            if response.function_calls:
                return self._run_react_loop(user_input, response, config)

            return response.text if response.text else "No response generated."

        except Exception as e:
            return f"Error: {e}"

    def _run_react_loop(self, user_input, first_response, config, max_steps=5):
        """
        ReAct-style loop:
        Reason -> Act -> Observe -> Final answer
        """
        conversation = self._build_contents_with_history(user_input)
        response = first_response

        for _ in range(max_steps):
            if not response.function_calls:
                return response.text if response.text else "No response generated."

            # Keep the model's function call content in the conversation
            conversation.append(response.candidates[0].content)

            tool_response_parts = []

            for function_call_part in response.function_calls:
                tool_name = function_call_part.name
                tool_args = dict(function_call_part.args) if function_call_part.args else {}

                print(f"[Act] Calling tool: {tool_name} with args: {tool_args}")

                try:
                    if not self.registry.has_tool(tool_name):
                        tool_result = {"error": f"Tool '{tool_name}' is not registered."}
                    else:
                        result = self.registry.execute(tool_name, tool_args)
                        tool_result = {"result": result}

                    print(f"[Observe] {tool_result}")

                except Exception as e:
                    tool_result = {"error": str(e)}
                    print(f"[Observe] {tool_result}")

                tool_response_parts.append(
                    types.Part.from_function_response(
                        name=tool_name,
                        response=tool_result,
                    )
                )

            conversation.append(
                types.Content(role="tool", parts=tool_response_parts)
            )

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=conversation,
                config=config,
            )

        return "Error: Maximum tool steps reached."

    def _build_contents_with_history(self, current_user_input):
        """
        Convert memory into Gemini content format.
        """
        contents = []

        history = self.memory.get_history()

        # Include a small amount of prior conversation for context
        for item in history[-6:]:
            role = item["role"]
            text = item["content"]

            gemini_role = "model" if role == "assistant" else "user"

            contents.append(
                types.Content(
                    role=gemini_role,
                    parts=[types.Part.from_text(text=text)]
                )
            )

        # Current user turn
        if not history or history[-1]["content"] != current_user_input:
            contents.append(
                types.Content(
                    role="user",
                    parts=[types.Part.from_text(text=current_user_input)]
                )
            )

        return contents