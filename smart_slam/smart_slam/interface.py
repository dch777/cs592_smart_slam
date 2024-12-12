import openai

openai.api_key = "your_openai_api_key"

class GPTAgent:
    def __init__(self, navigator):
        self.navigator = navigator

    def query_gpt(self, query):
        """Send a natural language query to GPT and get a structured response."""
        prompt = f"""
        You are a robot navigation assistant. Interpret the following user query and map it to one of the following commands:
        1. Navigate to a location: "Navigate to location X".
        2. Get status of all locations: "Check all statuses".
        3. Get status of a specific location: "Check status of location X".
        
        Query: {query}

        Respond with a structured JSON object, such as:
        {{
            "command": "navigate_to",
            "target": X
        }}
        OR
        {{
            "command": "get_status",
            "target": "all" or X
        }}
        """
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0
        )
        return response.choices[0].text.strip()

    def process_query(self, query):
        """Process the user's query, execute the corresponding command, and return the result."""
        gpt_response = self.query_gpt(query)
        try:
            command_data = eval(gpt_response)
            command = command_data.get("command")
            target = command_data.get("target")

            if command == "navigate_to":
                return self.navigator.navigate_to(target)
            elif command == "get_status":
                if target == "all":
                    return self.navigator.get_status()
                else:
                    return self.navigator.get_status(target)
            else:
                return "Unknown command."
        except Exception as e:
            return f"Error processing query: {e}"
