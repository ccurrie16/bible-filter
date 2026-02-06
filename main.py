import json
import ollama
import os
import shutil

# Dynamic File Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Check If Date Directory Exists
os.makedirs(DATA_DIR, exist_ok=True)

print("--- 📖 Universal Bible AI Rater (Auto-Importer) ---")
raw_input_path = input("Enter the path to your Bible JSON file: ").strip().strip('"')

# Validate Input File
filename = os.path.basename(raw_input_path)
final_input_path = os.path.join(DATA_DIR, filename)

# Move File If Not Already in Data Directory
if not os.path.exists(final_input_path):
    print(f"📦 Importing {filename} into project structure...")
    try:
        shutil.move(raw_input_path, final_input_path)
    except Exception as e:
        print(f"❌ Could not move file: {e}")
        final_input_path = raw_input_path

# User Inputs
out_filename = input("Enter name for output file (e.g., curated_kjv.json): ").strip()
FILE_OUT = os.path.join(DATA_DIR, out_filename)

keywords_raw = input("Enter boring keywords to skip (comma-separated): ")
BORING_KEYWORDS = [w.strip().lower() for w in keywords_raw.split(",") if w.strip()]

# Load Bible Data
with open(final_input_path, 'r', encoding='utf-8') as f:
    bible_data = json.load(f)

# Sum Of Verses Kept
total_verses = sum(len(c['verses']) for b in new_bible_data['books'] for c in b['chapters'])

print(f"\n✨ SUCCESS!")
print(f"📂 Output saved to: {FILE_OUT}")
print(f"💎 Total Masterpiece Verses kept: {total_verses}")