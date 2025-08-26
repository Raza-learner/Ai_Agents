import os
from config import MAX_CHARS
from google.genai.types import  FunctionDeclaration, Schema, Type

schema_get_file_content = FunctionDeclaration(
    name="get_file_content",
    description="Reads the contents of a specified file, constrained to the working directory. Truncates content at 10000 characters if longer.",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(
                type=Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)

def get_file_content(working_directory, file_path):
    try:
        # Create the full path by joining working_directory and file_path
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory = os.path.abspath(working_directory)
        
        # Check if the full path is within the working directory
        if not full_path.startswith(working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        # Check if the path is a file
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        # Read and return the file contents
        with open(full_path, 'r', encoding='utf-8') as file:
            content = file.read(MAX_CHARS)
            # Check if file was truncated
            if os.path.getsize(full_path) > MAX_CHARS:
                return content + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
    
    except UnicodeDecodeError:
        return f'Error: Unable to read "{file_path}": File is not a valid text file'
    except (OSError, PermissionError) as e:
        return f'Error: Unable to read "{file_path}": {str(e)}'