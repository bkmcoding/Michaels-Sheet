from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

print("--- Available Models ---")
for model in client.models.list():
    # Filter for models that support generating content
    if "generateContent" in model.supported_actions:
        print(f"Name: {model.name} | Display: {model.display_name}")