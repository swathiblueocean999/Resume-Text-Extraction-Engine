import os
import json
import re

# Day 5: Resume Extraction Engine
class ResumeEngine:
    def get_pdf_text(self, file_path):
        # Task: Extract raw text from PDF or DOCX
        return "Raw Text from " + file_path

    def clean_data(self, text):
        # Task: Normalize text (Symbols, Capitalization, Bullet points)
        text = re.sub(r'\s+', ' ', text)  # Extra spaces 
        text = re.sub(r'[^\x00-\x7F]+', ' ', text) # Non-ASCII characters
        
        
        return text.strip().capitalize()

engine = ResumeEngine()
folder_path = "C:/Users/LENOVO/OneDrive/Desktop/Resume_Project"
output_list = []

# Automated Test Runs: 
files = [f for f in os.listdir(folder_path) if f.endswith(('.pdf', '.docx'))]

for filename in files:
    file_path = os.path.join(folder_path, filename)
    
    try:
        # 1 & 2. Extract and Normalize
        raw_text = engine.get_pdf_text(file_path)
        final_output = engine.clean_data(raw_text)
        
        # 3. Store in Structured Format
        output_list.append({
            "filename": filename,
            "cleaned_resume": final_output
        })
        
        # 5. Create Test Logs (Deliverable)
        with open("test_log.txt", "a") as log:
            log.write(f"Processed {filename} successfully.\n")
            
    except Exception as e:
        with open("test_log.txt", "a") as log:
            log.write(f"Error processing {filename}: {str(e)}\n")

# 4. Store in Structured File (Deliverable)
with open("cleaned_output.json", "w") as f:
    json.dump(output_list, f, indent=4)

print(f"Success! Processed {len(files)} files. Check cleaned_output.json and test_log.txt.")