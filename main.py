import os
import argparse
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

#using argparse
parser = argparse.ArgumentParser(description="AI ChatBot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args() # Now we can access `args.user_prompt`

#Spliting things up for easy coding:
prompt = args.user_prompt

#place to store the messages
messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]


response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents= messages,
   
)
#Checking if the AI prompt didt bomb:
if response.usage_metadata == None:
    raise RuntimeError("Data not found, as it is responding with None")

#Labeling data for ease of use
response_token_count = response.usage_metadata.candidates_token_count
question_token_count = response.usage_metadata.prompt_token_count
response_from_AI = response.text




print(f"User prompt: {prompt}")
print(f"Prompt tokens: {question_token_count}")
print(f"Response tokens: {response_token_count}")
print(f"Response:")
print(response_from_AI)