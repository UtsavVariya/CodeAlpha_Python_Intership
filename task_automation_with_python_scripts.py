import os
import shutil

# Set your source and destination folder paths here
source_folder = "source"
destination_folder = "destination"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# List all files in the source folder
files = os.listdir(source_folder)

# Counter for how many files moved
moved_count = 0

# Loop through the files
for file in files:
    if file.lower().endswith(".jpg"):
        src_path = os.path.join(source_folder, file)
        dst_path = os.path.join(destination_folder, file)
        
        # Move the file
        shutil.move(src_path, dst_path)
        print(f"Moved: {file}")
        moved_count += 1

if moved_count == 0:
    print("No .jpg files found in the source folder.")
else:
    print(f"\nTotal .jpg files moved: {moved_count}")
