# Simple File organizer using python 
import os
import shutil 

# The folder to organize
folder_path = r"REMOVE THIS LINE AND PUT THE LOCATION"  # put your destination folder

# Types of folders
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Video": [".mp4", ".mov", ".avi"],
    "Document": [".pdf", ".docx", ".txt"],
}

# Loop through all files 
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file) # Goes through all the files 

    # Skip folders
    if os.path.isdir(file_path):
        print(f"Skipfolder: {file}")
        continue

    extension = os.path.splitext(file)[1].lower()
    print(f"Found file: {file} | Extension: {extension}")

    moved = False

    # Check the categories
    for category, extensions in file_types.items():
        if extension in extensions:
            category_folder = os.path.join(folder_path, category)
            os.makedirs(category_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(category_folder, file))
            print(f"Moved {file} to {category_folder}")
            moved = True
            break

    # If no match, move to Others
    if not moved:
        other_folder = os.path.join(folder_path, "Others")
        os.makedirs(other_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(other_folder, file))
        print(f"Moved {file} to {other_folder}")

print("Successfully ✅")
