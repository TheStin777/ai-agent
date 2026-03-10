import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None): 
    try:   
            working_dir_abs = os.path.abspath(working_directory)
            target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
            valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
            if valid_target_dir:
                # Will be True or False
                if os.path.isfile(target_dir):
                    ext = os.path.splitext(file_path)
                    if ext[1].lower() == ".py":
                        command = ["python", target_dir]
                        if args != None:
                            command.extend(args)
                        
                        result = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)
                        output = []
                        if result.returncode != 0:
                            output.append(f"Process exited with code {result.returncode}")
                            
                        if not result.stdout and not result.stderr:
                            output.append(f"No output produced")
                        
                        else:
                            if result.stdout: 
                             output.append(f"STDOUT: {result.stdout}")

                            if result.stderr:
                             output.append(f"STDERR:{result.stderr}")
                        
                        return "\n".join(output)
                    
                    else:
                        return f'Error: "{file_path}" is not a Python file'
                    
                    
                else:
                            
                    return f'Error: "{file_path}" does not exist or is not a regular file'


                
                        
            else:
                return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the Python script that should be executed.",
            ),
        },
    ),
)

