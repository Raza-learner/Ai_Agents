# Ai_Coding_Agent

A Python-based AI agent system integrated with the Google Gemini API, designed to perform file operations and execute Python scripts within a secure working directory.

## About

The `Ai_Coding_Agent` project is an AI-powered coding assistant that leverages the Google Gemini API to process user prompts and perform tasks such as listing directory contents, reading files, writing files, and executing Python scripts. The agent operates within a constrained working directory (`calculator/`) to ensure security, using a set of predefined functions exposed to the LLM via function declarations. The system maintains a conversation history to handle multi-step tasks, with a system prompt guiding the LLM to plan and execute function calls appropriately.

Key features:
- **File Operations**: List directory contents, read file contents (with truncation at 10,000 characters), and write/overwrite files.
- **Python Execution**: Run Python scripts with optional arguments, capturing stdout/stderr with a 30-second timeout.
- **Gemini API Integration**: Processes user prompts and triggers function calls based on a system prompt and tool declarations.
- **Security**: All operations are restricted to the `calculator/` directory to prevent unauthorized access.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Available Functions](#available-functions)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Structure

```
Ai_Coding_Agent/
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
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Raza-learner/Ai_Coding_Agent.git
   cd Ai_Coding_Agent
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   Install required packages:
   ```bash
   pip install python-dotenv google-generativeai
   ```

4. **Configure environment variables**:
   Create a `.env` file with your Gemini API key:
   ```bash
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

## Usage

Run the AI agent with a prompt to perform tasks or answer questions about the codebase:

```bash
uv run main.py "list the contents of the pkg directory" --verbose
```

**Example Prompts and Expected Outputs**:

1. **List directory contents**:
   ```bash
   uv run main.py "list the contents of the pkg directory" --verbose
   ```
   Output:
   ```
   Calling function: get_files_info({'directory': 'pkg'})
   -> {'result': '- calculator.py: file_size=[size] bytes, is_dir=False\n- morelorem.txt: file_size=26 bytes, is_dir=False\n- render.py: file_size=[size] bytes, is_dir=False'}
   ```

2. **Read file contents**:
   ```bash
   uv run main.py "read the contents of main.py" --verbose
   ```
   Output:
   ```
   Calling function: get_file_content({'file_path': 'main.py'})
   -> {'result': '[contents of main.py]'}
   ```

3. **Write file contents**:
   ```bash
   uv run main.py "write 'hello' to test.txt" --verbose
   ```
   Output:
   ```
   Calling function: write_file({'file_path': 'test.txt', 'content': 'hello'})
   -> {'result': 'Successfully wrote to "test.txt" (5 characters written)'}
   ```

4. **Execute Python script**:
   ```bash
   uv run main.py "run tests.py" --verbose
   ```
   Output:
   ```
   Calling function: run_python_file({'file_path': 'tests.py'})
   -> {'result': '[output from tests.py]'}
   ```

5. **Explain code**:
   ```bash
   uv run main.py "explain how the calculator renders the result to the console" --verbose
   ```
   Output:
   ```
   Calling function: get_files_info({'directory': 'pkg'})
   -> {'result': '- calculator.py: file_size=[size] bytes, is_dir=False\n- morelorem.txt: file_size=26 bytes, is_dir=False\n- render.py: file_size=[size] bytes, is_dir=False'}
   Calling function: get_file_content({'file_path': 'pkg/render.py'})
   -> {'result': '[contents of render.py]'}
   Final response:
   Okay, I've examined the `render` function in `pkg/render.py`. Here's how it works:
   [Explanation of rendering logic, as described previously]
   ```

Use the `--verbose` flag for detailed function call output. Without it, function names are printed with a leading `-`.

## Available Functions

The AI agent supports the following functions, constrained to the `calculator/` working directory:

- **get_files_info(directory=".")**: Lists files and directories with their sizes and types.
- **get_file_content(file_path)**: Reads a file's contents, truncating at 10,000 characters.
- **run_python_file(file_path, args=[])**: Executes a Python file with optional arguments, capturing output.
- **write_file(file_path, content)**: Writes or overwrites a file with the specified content.

These functions are exposed to the Gemini API via `FunctionDeclaration` schemas, allowing the LLM to call them based on user prompts.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make changes and commit:
   ```bash
   git commit -m "Add your feature description"
   ```
4. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request on GitHub.

Please include tests in `tests.py` for new functionality and ensure code adheres to the project's style (e.g., PEP 8).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details. *Note*: If no LICENSE file exists, consider adding one.

## Contact

For questions or suggestions:
- GitHub Issues: [Raza-learner/Ai_Coding_Agent Issues](https://github.com/Raza-learner/Ai_Coding_Agent/issues)


---

© 2025 Raza-learner. Built with ❤️ for AI and coding enthusiasts.



