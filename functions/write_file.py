import os
from google.genai import types

def write_file(working_directory, file_path, content):    
     working_dir_abs = os.path.abspath(working_directory)
     target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
     valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
     if valid_target_dir:
        # Will be True or False
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
            
        else:
            os.makedirs(os.path.dirname(target_dir), exist_ok=True)
            try:
                with open(target_dir, "w") as f:
                        
                    f.write(content)
                    file_content_string = f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
                    return file_content_string
                

            except Exception as e:
                return(f"Error: {e}")
                
     else:
         return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes a file to a directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path where the new file should be created or overwritten.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The full text string to be written into the file.",
            )
        },
    ),
)
        

