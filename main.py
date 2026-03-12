import os
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv
from config import system_prompt
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from call_function import call_function
import sys

#Above and Below is Outside of loop

#Calling on the AI client
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

#Giving the AI the tool box in order to use the functions
available_functions = types.Tool(
    function_declarations=[schema_get_files_info, schema_run_python_file, schema_get_file_content, schema_write_file]
)

#using argparse
parser = argparse.ArgumentParser(description="AI ChatBot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args() # Now we can access `args.user_prompt`

#Spliting things up for easy coding:
prompt = args.user_prompt

#place to store the messages
messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

#Above is outside of loop




#Below is inside the loop

for _ in range(5):

    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents= messages,
        config=types.GenerateContentConfig(tools=[available_functions],system_instruction=system_prompt,temperature=0)
    
    )


    #Checking if the AI prompt didt bomb:
    if response.usage_metadata == None:
        raise RuntimeError("Data not found, as it is responding with None")


    # Adding replys to messages to be saved and used later in conversation with AI
    for candidate in response.candidates:
        messages.append(candidate.content)



    # Checking if the function call the AI is requesting is available.
    final_function_call_results = []
    if response.function_calls:    
        for call in response.function_calls:
            function_call_result = call_function(call)
            if not function_call_result.parts:
                raise Exception ("function call is empty")

            if function_call_result.parts[0].function_response is None:
                raise Exception("Not a valid responce")
                
            
            if function_call_result.parts[0].function_response.response is None:
                raise Exception("Not a valid responce")
            
            final_function_call_results.append(function_call_result.parts[0])

            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

        
        # adding the calls to messages to the AI Remembers
        messages.append(types.Content(role="user", parts=final_function_call_results))
            


    else:
        #Labeling data for ease of use
        response_token_count = response.usage_metadata.candidates_token_count
        question_token_count = response.usage_metadata.prompt_token_count
        response_from_AI = response.text


        if args.verbose:
            print(f"User prompt: {prompt}")
            print(f"Prompt tokens: {question_token_count}")
            print(f"Response tokens: {response_token_count}")

        print(f"Response:")
        print(response_from_AI)
        break
    


    #Above is inside of the loop
else:
    # only runs if loop finished without break
    print("Max iterations reached...")
    sys.exit(1)

