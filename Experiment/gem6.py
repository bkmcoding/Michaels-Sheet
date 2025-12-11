import os, time
from pypdf import PdfReader, PdfWriter
from dotenv import load_dotenv
from google import genai
from google.genai import types

# --- CONFIGURATION ---
INPUT_PDF = "./resultPDF/finalreviewcyber.pdf"
PAGES_PER_CHUNK = 10
MODEL_ID = "gemma-3-27b-it"

load_dotenv()

client = genai.Client()


LATEX_PREAMBLE = r"""
\documentclass{article}
\usepackage{geometry} \geometry{margin=1in}
\usepackage{parskip}
\usepackage{ragged2e}
\usepackage{float}       % Required for [H]
\usepackage{tcolorbox}
\usepackage{amsmath, amssymb}
\usepackage{hyperref}     % Fixes "URL" errors
\usepackage{adjustbox}    % CRITICAL: Allows us to shrink huge diagrams
\usepackage{listings}     % For code blocks

% EXTENDED TIKZ LIBRARIES (Fixes "unknown library" errors)
\usepackage{tikz} 
\usetikzlibrary{shapes, arrows.meta, positioning, shadows, calc, fit, backgrounds, decorations.pathreplacing}

% GLOBAL STYLES
\tikzset{
    block/.style={rectangle, draw, thick, rounded corners, fill=blue!5, align=center, minimum height=2em},
    arrow/.style={thick, ->, >=stealth},
    decision/.style={diamond, draw, fill=green!10, align=center, aspect=2},
    cloud/.style={draw, ellipse, fill=red!10, node distance=3cm, minimum height=2em}
}
\raggedbottom

\begin{document}
"""


CHUNK_PROMPT = r"""
[ROLE]
You are an Elite Academic Professor. You are currently writing **ONE CHAPTER** of a larger "Student Companion Guide."
The preamble (packages, styles, title) has already been written. Your job is to output the **BODY CONTENT ONLY** for these specific slides.

[CONTENT RULES - "THE PROFESSOR"]
1.  **Fluid Prose:** Do NOT simply transcribe bullets. Convert slide points into clear, textbook-style paragraphs.
2.  **Gap Filling:** If a concept is brief, EXPAND on it using your academic knowledge. Explain *why* it matters.
3.  **No Meta-Talk:** Do not say "In these slides..." or "The presentation covers...". Jump immediately into the first topic header.
4.  **Tone:** Authoritative but accessible. Use bolding (`\textbf{}`) for key terms.
5.  **Code:** Use `\begin{lstlisting}[breaklines=true]` for code snippets.

[VISUALS - TIKZ (STRICT COMPLIANCE)]
1.  **Assumed Styles:** The main document has already defined these TikZ styles. YOU MUST USE THEM:
    - `block` (for standard steps)
    - `decision` (diamond shape)
    - `arrow` (thick arrow)
2.  **Mandatory TikZ:** If you see a diagram, recreate it using `\begin{tikzpicture}`.
3.  **Crash Prevention:**
    - If a node has multiple lines of text, you **MUST** add `[align=center]` (e.g., `\node[block, align=center] {Line 1\\Line 2};`).
    - Use relative positioning (e.g., `below=of node1`). Do not use absolute coordinates.
4.  **Placement (CRITICAL):** You MUST wrap every `tikzpicture` environment inside an `adjustbox` to prevent it from going off-screen. Use exactly this pattern:
    
    \begin{figure}[H]
        \centering
        \begin{adjustbox}{max width=\textwidth} % Forces diagram to fit page
            \begin{tikzpicture}[node distance=1.5cm, auto]
                % ... your tikz code here ...
            \end{tikzpicture}
        \end{adjustbox}
        \caption{Diagram Description}
    \end{figure}
5.  **Positioning:** Use `below=of prev_node`. NEVER use absolute coordinates like `(5,2)`.
6.  **Text Width:** If a node has long text, add `text width=3cm` to the node options to force text wrapping inside the shape.

[FORMATTING RULES]
1.  **Output Format:** Output **ONLY** raw LaTeX body content.
    - NO `\documentclass`
    - NO `\begin{document}`
    - NO `\end{document}`
    - NO Markdown fences (```).
2.  **Hierarchy:** Start the chunk with a `\section{...}` titled after the first major slide topic. Use `\subsection{}` for details.
3.  **Callouts:** Use `\begin{tcolorbox}[title=Definition]` for important definitions.

[INPUT]
Convert these attached slides into the LaTeX chapter body.
"""

def split_and_process(pdf_path):
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    
    full_latex_body = ""
    
    print(f"--- Processing {total_pages} pages in chunks of {PAGES_PER_CHUNK} ---")

    for i in range(0, total_pages, PAGES_PER_CHUNK):
        chunk_num = (i // PAGES_PER_CHUNK) + 1
        end_page = min(i + PAGES_PER_CHUNK, total_pages)
        
        print(f"Processing Chunk {chunk_num}: Pages {i+1} to {end_page}...")

        writer = PdfWriter()
        for p in range(i, end_page):
            writer.add_page(reader.pages[p])
        
        temp_pdf_name = f"temp_chunk_{chunk_num}.pdf"
        with open(temp_pdf_name, "wb") as f:
            writer.write(f)

        file_ref = client.files.upload(file=temp_pdf_name)

        while file_ref.state.name == "PROCESSING":
            time.sleep(2)
            file_ref = client.files.get(name=file_ref.name)

        try:
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=[
                    types.Content(
                        role="user",
                        parts=[
                            types.Part.from_uri(file_uri=file_ref.uri, mime_type=file_ref.mime_type),
                            types.Part(text=CHUNK_PROMPT)
                        ]
                    )
                ]
            )


            chunk_text = response.text
            chunk_text = chunk_text.replace("```latex", "").replace("```", "")

            full_latex_body += f"\n% --- START OF CHUNK {chunk_num} ---\n"
            full_latex_body += chunk_text + "\n"

            print(f"Chunk {chunk_num} complete.")

        except Exception as e:
            print(f"Error on Chunk {chunk_num}: {e}")

        os.remove(temp_pdf_name)


    print("--- Assembling Final Document ---")
    final_latex = LATEX_PREAMBLE + full_latex_body + "\n\\end{document}"

    with open("final_study_guide.tex", "w", encoding="utf-8") as f:
        f.write(final_latex)

    print("Done! Saved to 'final_study_guide.tex'")

# Run it
if __name__ == "__main__":
    split_and_process(INPUT_PDF)