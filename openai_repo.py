import requests
import os
class OpenaiRepo:
    def __init__(self, api_key=None):
        self.api_key = os.getenv("OPENAI_KEY")

    def send_completion_request(self, text_input, model="gpt-3.5-turbo", max_tokens=100):
# Load the API key from an environment variable (recommended for security)

        # Define the API URL
        url = "https://api.openai.com/v1/chat/completions"

        # Define headers
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        # Define the request payload
        data = {
            "model": "gpt-4o",
            "messages": [
                {"role": "developer", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello!"}
            ]
        }

        # Make the API request
        response = requests.post(url, headers=headers, json=data)

# Print the response
        return response.content


# Example usage:
if __name__ == "__main__":
    repo = OpenaiRepo(api_key="your-openai-api-key")  # Replace with your actual API key
    result = repo.send_completion_request("Tell me a fun fact about space.")
    print(result)
