# import os
# import comtypes.client

# # Define your input/output names
# input_rel = "./conversion/examples/midtermreview.pptx" 
# output_rel = "../resultPDF/midtermreview.pdf"

# # --- THE FIX: Convert to Absolute Paths ---
# # This turns "presentation.pptx" into "C:\Users\orkar\...\presentation.pptx"
# input_path = os.path.abspath(input_rel)
# print(input_path)
# output_path = os.path.abspath(output_rel)

# def ppt_to_pdf(input_path, output_path):
#     powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
#     powerpoint.Visible = 1
    
#     # Now this will work because it has the full C:\ path
#     deck = powerpoint.Presentations.Open(input_path) 
    
#     deck.SaveAs(output_path, 32) # 32 = PDF format
#     deck.Close()
#     powerpoint.Quit()

# ppt_to_pdf(input_path, output_path)

import os
import comtypes.client

# 1. SETUP: Define filenames
input_filename = "./examples/finalreviewcyber.pptx"
output_filename = "../resultPDF/finalreviewcyber.pdf"

# 2. THE FIX: Convert filenames to ABSOLUTE Windows paths
# This fixes "Path not found" and "Unspecified error"
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, input_filename)
output_path = os.path.join(script_dir, output_filename)

def ppt_to_pdf(in_path, out_path):
    # Check if input exists to avoid crashing
    if not os.path.exists(in_path):
        print(f"Error: Input file not found at: {in_path}")
        return

    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1
    
    try:
        # Open Presentation
        deck = powerpoint.Presentations.Open(in_path)
        
        # Save as PDF (32 is the code for PDF)
        deck.SaveAs(out_path, 32)
        print(f"Success! Saved to: {out_path}")
        
        deck.Close()
    except Exception as e:
        print(f"PowerPoint Error: {e}")
        print("Tip: Close the PDF if it is open in Acrobat/Chrome.")
    finally:
        # Quit PowerPoint safely
        powerpoint.Quit()

if __name__ == "__main__":
    ppt_to_pdf(input_path, output_path)