import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv
# from google import genai

load_dotenv()

genai.configure()


def convert_slide_to_latex(image_path):
    model = genai.GenerativeModel('gemma-3-27b-it')

    img = Image.open(image_path)

    full_prompt = r"""
    [ROLE]
    You are an advanced LaTeX Code Generator and Academic Tutor. 
    Your goal is to transform an image of a document into a high-quality, compile-ready LaTeX study guide.

    [CONTENT INSTRUCTIONS]
    1. **Concept Synthesis:** Do not simply transcribe text. Analyze the academic concepts visible in the image and synthesize them into clear, study-guide style notes.
    2. **Key Terms:** Wrap all key definitions or important terms in `\textbf{}`.
    3. **Math Mode:** Detect mathematical expressions and strictly use LaTeX math mode (e.g., $E=mc^2$).
    4. **Hierarchy:** Use `\section{}`, `\subsection{}`, and `\itemize` to structure the notes logically.

    [VISUAL INSTRUCTIONS - TIKZ]
    1. **Diagram Detection:** If a diagram, flowchart, or graph is present, you MUST recreate it using TikZ.
    2. **Relative Positioning:** Do NOT use absolute coordinates (e.g., `\node at (3,4)`). Use the `positioning` library (e.g., `\node (b) [below=of a]`). This prevents shapes from overlapping.
    3. **Styling:** Use `\tikzset` to define common styles (e.g., `basic/.style={draw, rectangle, rounded corners}`) at the start of the environment.

    [FORMATTING CONSTRAINTS]
    1. **Output Format:** Your output must be RAW text. Do NOT wrap the code in markdown blocks (like ```latex ... ```).
    2. **Preamble:** You must start with `\documentclass{article}` and include `\usepackage{tikz}`, `\usetikzlibrary{shapes, arrows.meta, positioning}`, and `\usepackage{geometry}`.
    3. **Completeness:** The output must end with `\end{document}`.

    [USER REQUEST]
    Convert the attached image into a LaTeX study guide following the rules above.
    """



    print("Sending to Gemma 3 27B...")


    try:
        response = model.generate_content([full_prompt, img])
        
        print("\n--- GEMMA 3 OUTPUT ---\n")
        print(response.text)
        
        with open("./tex/output.tex", "w") as f:
            f.write(response.text)

    except Exception as e:
        print(f"Error: {e}")
        print("Tip: Ensure your API key has access to Gemma models in Google AI Studio.")


# needs to be jpg
if __name__ == "__main__":
    convert_slide_to_latex("./images/page_1.jpg")
    pass