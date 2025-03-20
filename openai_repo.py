import openai

class OpenaiRepo:
    def __init__(self, api_key=None):
        self.api_key = api_key
        openai.api_key = self.api_key  # Set API key for authentication

    def send_completion_request(self, text_input, model="gpt-3.5-turbo", max_tokens=100):
        """
        Sends a completion request to OpenAI's API.

        :param text_input: The user prompt for the model.
        :param model: The model to use (default: "gpt-3.5-turbo").
        :param max_tokens: The maximum number of tokens to generate.
        :return: The generated text response.
        """
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": text_input}],
                max_tokens=max_tokens
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"Error communicating with OpenAI: {e}")
            return None

# Example usage:
if __name__ == "__main__":
    repo = OpenaiRepo(api_key="your-openai-api-key")  # Replace with your actual API key
    result = repo.send_completion_request("Tell me a fun fact about space.")
    print(result)
