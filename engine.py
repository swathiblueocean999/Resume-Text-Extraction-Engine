import os
import json
import re
import datetime
from PyPDF2 import PdfReader
from docx import Document

class ResumeEngine:
    def get_text(self, file_path):
        text = ""
        if file_path.endswith('.pdf'):
            reader = PdfReader(file_path)
            for page in reader.pages:
                text += page.extract_text()
        elif file_path.endswith('.docx'):
            doc = Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])
        return text

    def clean_data(self, text):
        text = re.sub(r'\s+', ' ', text)  # Extra spaces
        text = re.sub(r'[^\x00-\x7F]+', ' ', text) # Non-ASCII
        return text.strip().lower() # Normalizing to lowercase for AI consistency

# --- Main Execution ---
engine = ResumeEngine()
folder_path = "C:/Users/LENOVO/OneDrive/Desktop/Resume_Project" 
output_list = []
logs = [] # to store our test results

files = [f for f in os.listdir(folder_path) if f.endswith(('.pdf', '.docx'))]

for filename in files:
    file_path = os.path.join(folder_path, filename)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    try:
        raw_text = engine.get_text(file_path)
        cleaned = engine.clean_data(raw_text)
    
        output_list.append({
        "filename": filename,
        "cleaned_content": cleaned})
        logs.append(f"[{timestamp}] Processed {filename} successfully")
    except Exception as e:
        logs.append(f"[{timestamp}] Error processing {filename}: {str(e)}")
    

# --- Save to cleaned data ---
with open("cleaned_output.json", "w") as f:
    json.dump(output_list, f, indent=4)

    # --- Save logs ---
with open("test_log.txt", "w") as log_file:
    log_file.write("\n".join(logs))


print("Done! check 'cleaned_output.json' for cleaned data and 'test_log.txt' for processing logs.")

