from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from google.genai import types



#Function call Map
function_map = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file
         
    # etc.
}

def call_function(function_call, verbose=False):

    

    #Checking for verbose
    if verbose:
        print(f"Calling function: {function_call.name}({function_call.args})")
    
    else:
        print(f" - Calling function: {function_call.name}")
    
    #Making sure function_name is a string or ""
    function_name = function_call.name or ""

    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    function_args_copy = dict(function_call.args) if function_call.args else {}
    function_args_copy["working_directory"] = "./calculator"
    function_result = function_map[function_name](**function_args_copy) 

    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
                )
            ],
        )
    