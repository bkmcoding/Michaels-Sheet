import time
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

client = genai.Client()

def process_massive_presentation(pdf_path):
    print(f"1. Uploading massive file: {pdf_path}...")
    
    #stores the file on Google's servers temporarily
    file_ref = client.files.upload(file=pdf_path)

    while file_ref.state.name == "PROCESSING":
        print("   Processing on server...")
        time.sleep(5)
        file_ref = client.files.get(name=file_ref.name)

    if file_ref.state.name == "FAILED":
        raise ValueError("File processing failed.")

    print("2. File ready. Sending to Gemini Flash Latest...")

    full_prompt = r"""
[ROLE]
You are an Elite Academic Professor and Expert LaTeX Typesetter. 
Your task is to convert the provided lecture slides into a comprehensive, self-contained Student Companion Guide.

[CONTENT - THE "PROFESSOR" MODE]
1.  **Anti-Robot Rule:** Do NOT just transcribe the slides. Slides are bullet points; your output must be full sentences and fluid prose.
2.  **Gap Filling:** If a slide mentions a concept briefly (e.g., "Mitochondria -> Powerhouse"), you must EXPAND on it using your general academic knowledge (e.g., "The mitochondria generates ATP through oxidative phosphorylation...").
3.  **Tone:** Write like a helpful, engaging teacher. Use phrases like "It is crucial to note that..." or "Intuitively, this means..."
4.  **Examples:** If the slide presents a formula or abstract concept without an example, briefly provide a concrete example or analogy to clarify it.

[VISUALS - TIKZ & DIAGRAMS]
1.  **Mandatory TikZ:** Recreate ALL diagrams/flowcharts using TikZ.
2.  **Strict Positioning:** Use `\node (b) [below=of a]`. NO absolute coordinates.
3.  **Style Definitions:** You MUST define every style used. Add this to your preamble:
    `\tikzset{
        block/.style={rectangle, draw, thick, rounded corners, minimum height=3em, align=center},
        process/.style={rectangle, draw, fill=blue!10, align=center},
        decision/.style={diamond, draw, fill=green!10, align=center, aspect=2},
        arrow/.style={thick, ->, >=stealth}
    }`
4.  **Line Break Rule:** If a node contains text with line breaks (`\\`), you MUST include `align=center` or `text width=3cm` in the node options, otherwise LaTeX will crash.
5.  **Sanitize:** Escape all special characters inside nodes (e.g., use `\_` instead of `_`, `\&` instead of `&`).

[FORMATTING - THE "TYPESETTER" MODE]
1.  **Preamble:** Start EXACTLY with:
    \documentclass{article}
    \usepackage{geometry} \geometry{margin=1in}
    \usepackage{parskip}  % Fixes paragraph spacing
    \usepackage{ragged2e}
    \usepackage{float}    % Fixes "floating" figures
    \usepackage{tcolorbox}
    \usepackage{amsmath, amssymb}
    \usepackage{tikz} \usetikzlibrary{shapes, arrows.meta, positioning, shadows}
    \usepackage{hyperref}
    
    % MANDATORY STYLE DEFINITIONS
    \tikzset{
        block/.style={rectangle, draw, thick, rounded corners, fill=blue!5, align=center, minimum height=2em},
        arrow/.style={thick, ->, >=stealth},
        decision/.style={diamond, draw, fill=green!10, align=center, aspect=2}
    }
    \raggedbottom % CRITICAL: Prevents huge vertical whitespace gaps

2.  **Figure Placement:** strictly use `\begin{figure}[H]` (capital H) for all diagrams. This forces them to stay exactly where they are in the text, preventing empty spaces.
3.  **Code:** Use `\begin{verbatim}` or `lstlisting` for code.

[OUTPUT CONSTRAINTS]
1.  Output **ONLY** the raw LaTeX code.
2.  Start directly with `\documentclass{article}`.
3.  End with `\end{document}`.
4.  Do not include markdown code fences (```).

[INPUT]
Convert the attached image into this high-quality study guide.
"""

    #gemini-latest has 1M context window
    response = client.models.generate_content(
        model='gemini-flash-latest',
        contents=[types.Content(
            parts=[
                types.Part.from_uri(
                    file_uri=file_ref.uri,
                    mime_type="application/pdf"
                ),
                types.Part(text=full_prompt)
            ]
        )],
        config=types.GenerateContentConfig(
            system_instruction="Output only valid LaTeX code."
        )
    )

    print("3. Saving output...")
    with open("presentation_converted.tex", "w", encoding="utf-8") as f:
        f.write(response.text)
    
    print("Done.")

if __name__ == "__main__":
    process_massive_presentation("./resultPDF/finalreviewcyber.pdf")