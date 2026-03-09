import os

def get_files_info(working_directory, directory="."):
     working_dir_abs = os.path.abspath(working_directory)
     target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
     valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
     if valid_target_dir:
        # Will be True or False
        if os.path.isdir(target_dir):
            try:
                files_names = os.listdir(target_dir)
                file_info = [] 
                for file_name in files_names:
                    file_info.append(f"  - {file_name}: file_size={os.path.getsize(os.path.join(target_dir,file_name))} bytes, is_dir={os.path.isdir(os.path.join(target_dir,file_name))}")

                return "\n".join(file_info)

            except Exception as e:
                return(f"Error: {e}")
        else:
            return f'Error: "{directory}" is not a directory'
        
     else:
         return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
     

