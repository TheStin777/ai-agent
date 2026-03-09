import os

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
        

