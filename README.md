Ai_Code_Assistant_Agent
A Python-based AI agent system integrated with the Google Gemini API, designed to perform file operations and execute Python scripts within a secure working directory.
About
The Ai_Agents project is an AI-powered coding assistant that leverages the Google Gemini API to process user prompts and perform tasks such as listing directory contents, reading files, writing files, and executing Python scripts. The agent operates within a constrained working directory (calculator/) to ensure security, using a set of predefined functions exposed to the LLM via function declarations. The system maintains a conversation history to handle multi-step tasks, with a system prompt guiding the LLM to plan and execute function calls appropriately.
Key features:

File Operations: List directory contents, read file contents (with truncation at 10,000 characters), and write/overwrite files.
Python Execution: Run Python scripts with optional arguments, capturing stdout/stderr with a 30-second timeout.
Gemini API Integration: Processes user prompts and triggers function calls based on a system prompt and tool declarations.
Security: All operations are restricted to the calculator/ directory to prevent unauthorized access.

Table of Contents

Project Structure
Installation
Usage
Available Functions
Contributing
License
Contact

Project Structure
Ai_Agents/
├── calculator/
│   ├── lorem.txt           # Sample text file (>20,000 characters)
│   ├── main.txt            # Test file from write_file
│   ├── test.txt            # Test file from write_file
│   ├── main.py             # Entry point for the AI agent
│   ├── tests.py            # Test script for function validation
│   └── pkg/
│       ├── calculator.py   # Calculator logic (assumed)
│       ├── render.py       # Rendering logic for calculator output
│       └── morelorem.txt   # Test file from write_file
├── functions/
│   ├── call_function.py    # Handles function call execution
│   ├── get_files_info.py   # Lists directory contents
│   ├── get_file_content.py # Reads file contents
│   ├── run_python_file.py  # Executes Python scripts
│   ├── write_file.py       # Writes/overwrites files
│   └── prompt.py           # Stores system prompt (early version)
├── config.py               # Defines MAX_CHARS for file reading
└── .env                    # Stores API keys (not committed)

Installation

Clone the repository:
git clone https://github.com/Raza-learner/Ai_Agents.git
cd Ai_Agents


Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:Install required packages:
pip install python-dotenv google-generativeai


Configure environment variables:Create a .env file with your Gemini API key:
echo "GEMINI_API_KEY=your_api_key_here" > .env

Obtain a key from https://x.ai/api.


Usage
Run the AI agent with a prompt to perform tasks or answer questions about the codebase:
uv run main.py "list the contents of the pkg directory" --verbose

Example Prompts and Expected Outputs:

List directory contents:
uv run main.py "list the contents of the pkg directory" --verbose

Output:
Calling function: get_files_info({'directory': 'pkg'})
-> {'result': '- calculator.py: file_size=[size] bytes, is_dir=False\n- morelorem.txt: file_size=26 bytes, is_dir=False\n- render.py: file_size=[size] bytes, is_dir=False'}


Read file contents:
uv run main.py "read the contents of main.py" --verbose

Output:
Calling function: get_file_content({'file_path': 'main.py'})
-> {'result': '[contents of main.py]'}


Write file contents:
uv run main.py "write 'hello' to test.txt" --verbose

Output:
Calling function: write_file({'file_path': 'test.txt', 'content': 'hello'})
-> {'result': 'Successfully wrote to "test.txt" (5 characters written)'}


Execute Python script:
uv run main.py "run tests.py" --verbose

Output:
Calling function: run_python_file({'file_path': 'tests.py'})
-> {'result': '[output from tests.py]'}


Explain code:
uv run main.py "explain how the calculator renders the result to the console" --verbose

Output:
Calling function: get_files_info({'directory': 'pkg'})
-> {'result': '- calculator.py: file_size=[size] bytes, is_dir=False\n- morelorem.txt: file_size=26 bytes, is_dir=False\n- render.py: file_size=[size] bytes, is_dir=False'}
Calling function: get_file_content({'file_path': 'pkg/render.py'})
-> {'result': '[contents of render.py]'}
Final response:
Okay, I've examined the `render` function in `pkg/render.py`. Here's how it works:
[Explanation of rendering logic, as described previously]



Use the --verbose flag for detailed function call output. Without it, function names are printed with a leading -.
Available Functions
The AI agent supports the following functions, constrained to the calculator/ working directory:

get_files_info(directory="."): Lists files and directories with their sizes and types.
get_file_content(file_path): Reads a file's contents, truncating at 10,000 characters.
run_python_file(file_path, args=[]): Executes a Python file with optional arguments, capturing output.
write_file(file_path, content): Writes or overwrites a file with the specified content.

These functions are exposed to the Gemini API via FunctionDeclaration schemas, allowing the LLM to call them based on user prompts.
Contributing
Contributions are welcome! To contribute:

Fork the repository.
Create a new branch:git checkout -b feature/your-feature-name


Make changes and commit:git commit -m "Add your feature description"


Push to your fork:git push origin feature/your-feature-name


Open a pull request on GitHub.

Please include tests in tests.py for new functionality and ensure code adheres to the project's style (e.g., PEP 8).
License
This project is licensed under the MIT License. See the LICENSE file for details. Note: If no LICENSE file exists, consider adding one.
Contact
For questions or suggestions:

GitHub Issues: Raza-learner/Ai_Agents Issues
Email: [Your contact email, if available]


© 2025 Raza-learner. Built with ❤️ for AI and coding enthusiasts.
