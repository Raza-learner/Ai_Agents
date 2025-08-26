import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig, Tool , Content
from functions.get_files_info import schema_get_files_info
from functions.get_files_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Define system prompt
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan to gather necessary information or perform actions. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.

For questions requiring analysis (e.g., explaining code), use the available functions to retrieve file contents or list directories as needed, then provide a clear, concise explanation based on the information gathered. Avoid speculative responses and focus on using the tools to obtain accurate data.
"""

# Define available functions
available_functions = Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

# Check if a prompt was provided as a command line argument
if len(sys.argv) < 2:
    print("Error: Please provide a prompt as a command line argument")
    print("Example: uv run main.py \"Your prompt here\"")
    sys.exit(1)

# Get the prompt and check for --verbose flag
prompt = sys.argv[1]
verbose = "--verbose" in sys.argv

client = genai.Client(api_key=api_key)
messages = [Content(role="user", parts=[{"text": prompt}])]

# Loop for up to 20 iterations
max_iterations = 20
for i in range(max_iterations):
    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=GenerateContentConfig(
                tools=[available_functions],
                system_instruction=system_prompt
            ),
        )

        # Append candidate content to messages
        for candidate in response.candidates:
            messages.append(candidate.content)

        # Check for function calls
        if response.function_calls:
            for function_call_part in response.function_calls:
                function_call_result = call_function(function_call_part, verbose=verbose)
                if not function_call_result.parts or not hasattr(function_call_result.parts[0], "function_response"):
                    raise Exception("Invalid function call response: No function_response found")
                if verbose:
                    print(f"-> {function_call_result.parts[0].function_response.response}")
                # Append function response as a user message
                messages.append(function_call_result)
        else:
            # If text response, print and break
            if response.text:
                print("Final response:")
                print(response.text)
                break
            else:
                raise Exception("No text or function call in response")

    except Exception as e:
        print(f"Error during iteration {i + 1}: {str(e)}")
        break

# Print token usage
usage = response.usage_metadata
print("\nPrompt tokens:", usage.prompt_token_count)
print("Response tokens:", usage.candidates_token_count)