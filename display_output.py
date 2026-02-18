
import json
import sqlite3

# JSON file
with open('cleaned_output.json', 'r') as f:
    data = json.load(f)
    conn = sqlite3.connect('resumes.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS cleaned_resumes (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT, content TEXT)''')


    for entry in data:
        cursor.execute("INSERT INTO cleaned_resumes (filename, content) VALUES (?, ?)", (entry['filename'], entry['cleaned_content']))

    conn.commit()
    print("Data inserted into SQLite database successfully.")

print("\n--- Reading from SQL Table ---")
cursor.execute("SELECT filename, content FROM cleaned_resumes")
rows = cursor.fetchall()

for row in rows:
    print(f"File: {row[0]} File: {row[1][:100]}...")  # Print first 50 chars of content Print first 100 chars of cleaned content

    conn.close()