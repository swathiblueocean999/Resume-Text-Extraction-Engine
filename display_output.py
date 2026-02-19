from tabulate import tabulate
import json
import sqlite3

# JSON file
with open('cleaned_output.json', 'r') as f:
    data = json.load(f)
    conn = sqlite3.connect('resumes.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS cleaned_resumes (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT, content TEXT)''')
    cursor.execute("DELETE FROM cleaned_resumes")  


    for entry in data:
        cursor.execute("INSERT INTO cleaned_resumes (filename, content) VALUES (?, ?)", (entry['filename'], entry['cleaned_content']))

    conn.commit()
    print("Data inserted into SQLite database successfully.")

print("\n--- Reading from SQL Table ---")
cursor.execute("SELECT filename, content FROM cleaned_resumes")
rows = cursor.fetchall()

from tabulate import tabulate 

cursor.execute("SELECT id, filename, content FROM cleaned_resumes")
rows = cursor.fetchall()

# printing the results in a tabular format using tabulate
headers = ["ID", "File Name", "Extracted Content Summary"]

# 50 characters summary for display
table_data = [[row[0], row[1], row[2][:70] + "..."] for row in rows]

print("\n" + "="*80)
print("RESUME EXTRACTION RESULTS")
print("="*80)
print(tabulate(table_data, headers=headers, tablefmt="grid"))

# save the report to a text file
with open('extraction_report.txt', 'w', encoding='utf-8') as f:
    f.write("RESUME EXTRACTION REPORT\n")
    f.write("="*80 + "\n")
    f.write(tabulate(table_data, headers=headers, tablefmt="grid"))
    f.write("\n" + "="*80)

print("\n report 'extraction_report.txt' file saved successfully!")

conn.close()

    
