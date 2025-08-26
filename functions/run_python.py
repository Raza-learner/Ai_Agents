import os
import subprocess
from google.genai.types import FunctionDeclaration, Schema, Type

schema_run_python_file = FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file with optional arguments, constrained to the working directory, with a 30-second timeout.",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(
                type=Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
            "args": Schema(
                type=Type.ARRAY,
                items=Schema(type=Type.STRING),
                description="Optional command-line arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory = os.path.abspath(working_directory)
        
        if not full_path.startswith(working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(full_path):
            return f'Error: File "{file_path}" not found.'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        
        completed_process = subprocess.run(
            ["python",full_path] + args,
            capture_output=True,
            text=True,
            cwd=working_directory,
            timeout=30
        )
        output = []
        if completed_process.stdout:
            output.append("STDOUT:\n" + completed_process.stdout)
        if completed_process.stderr:
            output.append("STDERR:\n" + completed_process.stderr)
        if completed_process.returncode != 0:
            output.append(f"Process exited with code {completed_process.returncode}")
        
        # Return formatted output or "No output produced."
        return "\n".join(output) if output else "No output produced."
    
    except subprocess.TimeoutExpired as e:
        return f"Error: executing Python file: Process timed out after 30 seconds"
    except (OSError, subprocess.SubprocessError) as e:
        return f"Error: executing Python file: {str(e)}"