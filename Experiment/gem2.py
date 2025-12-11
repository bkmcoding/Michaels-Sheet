import os
import time
from dotenv import load_dotenv
from google import genai

load_dotenv()

def convert_doc_to_latex(file_path):
    print(f"Processing: {file_path}...")

    #API takes PDF, JPEG, PNG.
    sample_file = genai.upload_file(path=file_path, display_name="UserContent")
    
    # Check if the file is processed (usually instant for images, fast for PDFs)
    while sample_file.state.name == "PROCESSING":
        print("Waiting for file processing...")
        time.sleep(2)
        sample_file = genai.get_file(sample_file.name)


    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="""
        You are a specialized LaTeX conversion engine.
        RULES:
        1. Output ONLY valid LaTeX code. No conversational text or markdown blocks (```latex).
        2. Use the 'article' class.
        3. Use the 'tikz' package for any diagrams found in the document.
        4. If a diagram is too complex, create a simplified block diagram in TikZ.
        5. Maintain the document hierarchy (sections, subsections).
        """
    )

    prompt = """
    Please convert the attached document into a single LaTeX file.
    - Summarize the text content.
    - Transform any charts, graphs, or flowcharts into TikZ figures.
    - Ensure all code compiles.
    """

    try:
        response = model.generate_content([sample_file, prompt])
        
        clean_latex = response.text.replace("```latex", "").replace("```", "")
        
        output_filename = "output.tex"
        with open(output_filename, "w") as f:
            f.write(clean_latex)
            
        print(f"Success! LaTeX saved to {output_filename}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

    genai.delete_file(sample_file.name)


if __name__ == "__main__":
    convert_doc_to_latex("hw2.pdf") 
    pass