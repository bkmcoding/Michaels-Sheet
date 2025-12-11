from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

sample_file = genai.upload_file(path="./hw2.pdf", display_name="hw2")

response = client.models.generate_content(
    model="gemma-3-12b-it",
    contents="You are a strict LaTeX converter. Output only raw LaTeX code.",
)
print(response.text)

