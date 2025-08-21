import os
import sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

# Check if a prompt was provided as a command line argument
if len(sys.argv) < 2:
    print("Error: Please provide a prompt as a command line argument")
    print("Example: uv run main.py \"Your prompt here\"")
    sys.exit(1)

# Get the prompt from command line argument
prompt = sys.argv[1]

client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model='gemini-2.0-flash-001', 
    contents=prompt
)
print(response.text)

# Print token usage
usage = response.usage_metadata
print("\nPrompt tokens:", usage.prompt_token_count)
print("Response tokens:", usage.candidates_token_count)