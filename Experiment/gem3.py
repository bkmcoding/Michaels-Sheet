import os
import google.generativeai as genai
from PIL import Image

os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

def convert_with_gemma_27b(image_path):
    # need to use -it for it to work
    model = genai.GenerativeModel('gemma-3-12b-it')
    
    img = Image.open(image_path)
    
    prompt = """
    [SYSTEM]
    You are an expert LaTeX developer. Convert this image into a standalone LaTeX file.
    - Use the TikZ package for diagrams.
    - Use \node [below of=NodeA] for relative positioning to ensure the diagram is clean.
    
    [USER]
    Convert this slide into LaTeX code.
    """
    
    print("Sending to Gemma 3 12B...")
    try:
        response = model.generate_content([prompt, img])
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")

# Note: The 27B model is heavier. It might take 2-3x longer to generate a response than the 12B model.