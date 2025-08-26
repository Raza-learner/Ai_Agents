import os
from google.genai.types import FunctionDeclaration, Schema, Type

schema_write_file = FunctionDeclaration(
    name="write_file",
    description="Writes or overwrites content to a specified file, constrained to the working directory.",
    parameters=Schema(
        type=Type.OBJECT,
        properties={
            "file_path": Schema(
                type=Type.STRING,
                description="The path to the file to write, relative to the working directory.",
            ),
            "content": Schema(
                type=Type.STRING,
                description="The content to write to the file.",
            ),
        },
        required=["file_path", "content"],
    ),
)
def write_file(working_directory, file_path, content):
    try:
        
        full_path = os.path.abspath(os.path.join(working_directory, file_path))
        working_directory = os.path.abspath(working_directory)
        
        if not full_path.startswith(working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        parent_dir = os.path.dirname(full_path)
        if parent_dir and not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except (OSError, PermissionError) as e:
        return f'Error: Unable to write to "{file_path}": {str(e)}'