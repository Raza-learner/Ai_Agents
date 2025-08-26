import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai.types import Tool,GenerateContentConfig
from functions.get_files_info import schema_get_files_info

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Define system prompt
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

# Define available functions
available_functions = Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

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
    contents=prompt,
    config=GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
    ),
)

# Check for function calls
if response.function_calls:
    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
else:
    print(response.text)

# Print token usage
usage = response.usage_metadata
print("\nPrompt tokens:", usage.prompt_token_count)
print("Response tokens:", usage.candidates_token_count)