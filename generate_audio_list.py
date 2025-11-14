import os
import json

# Path to your audio folder
audio_folder = os.path.join("audio_files")  # your folder name

# Read existing JSON if it exists
json_path = "audio-list.json"
if os.path.exists(json_path):
    with open(json_path, "r") as f:
        existing_files = json.load(f)
else:
    existing_files = []

# List all audio files (.mp3, .mpeg, .mp4)
audio_files = [f"audio_files/{f}" for f in os.listdir(audio_folder)
               if f.lower().endswith(('.mp3', '.mpeg', '.mp4'))]

# Add only new files
for f in audio_files:
    if f not in existing_files:
        existing_files.append(f)

# Sort alphabetically (optional)
existing_files.sort()

# Save back to JSON
with open(json_path, "w") as f:
    json.dump(existing_files, f, indent=4)

print(f"Updated {json_path} with {len(existing_files)} total files.")
