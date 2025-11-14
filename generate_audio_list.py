import os
import json

audio_folder = "audio_files"
json_path = "audio-list.json"

# List all audio files currently in the folder
audio_files = [f"audio_files/" + f for f in os.listdir(audio_folder)
               if f.lower().endswith(('.mp3', '.mpeg', '.mp4', '.wav', '.ogg', '.m4a'))]

# Sort alphabetically
audio_files.sort()

# Save to JSON (overwrites old JSON)
with open(json_path, "w") as f:
    json.dump(audio_files, f, indent=4)

print(f"Updated {json_path} with {len(audio_files)} total files.")
