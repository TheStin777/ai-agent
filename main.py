import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

#Spliting things up for easy coding:
prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents= prompt,
   
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