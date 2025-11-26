import os
import json
import re

folder = "quran_audio"
os.makedirs(folder, exist_ok=True)

# Get all mp3 files
audio_files = [f for f in os.listdir(folder) if f.lower().endswith(".mp3")]

clean_files = []

for f in audio_files:
    # Extract number and title
    match = re.match(r'(\d+)[-_ ]*(.*)\.mp3', f, re.IGNORECASE)
    if match:
        num = match.group(1).zfill(3)
        title = match.group(2)

        # Replace special characters with underscores
        safe_title = re.sub(r'[^\w\d-]', '_', title)
        new_name = f"{num}_{safe_title}.mp3"

        old_path = os.path.join(folder, f)
        new_path = os.path.join(folder, new_name)

        if old_path != new_path:
            os.rename(old_path, new_path)

        clean_files.append(new_name)

# Sort files
clean_files.sort()

# Save JSON (overwrite existing)
with open("quran_list.json", "w", encoding="utf-8") as f:
    json.dump(clean_files, f, indent=4, ensure_ascii=False)

print("✅ All mp3 files renamed safely and JSON regenerated!")
