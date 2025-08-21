import os

def get_files_info(working_directory, directory="."):
    try:
        # Create the full path by joining working_directory and directory
        full_path = os.path.abspath(os.path.join(working_directory, directory))
        working_directory = os.path.abspath(working_directory)
        
        # Check if the full path is within the working directory
        if not full_path.startswith(working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        # Check if the path is a directory
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        
        # Get directory contents
        result = []
        for item in sorted(os.listdir(full_path)):
            item_path = os.path.join(full_path, item)
            try:
                # Get file size and directory status
                file_size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                # Format the output string
                result.append(f"- {item}: file_size={file_size} bytes, is_dir={is_dir}")
            except (OSError, PermissionError) as e:
                result.append(f"Error: Unable to access {item}: {str(e)}")
        
        # Join results with newlines
        return "\n".join(result) if result else "Error: Directory is empty"
    
    except (OSError, PermissionError) as e:
        return f"Error: {str(e)}"