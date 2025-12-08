import os
import shutil

# Folder you want to organize
folder = r"C:\Users\You\Downloads"   # Change this to any folder you want

# Loop through every item in the folder
for file_name in os.listdir(folder):
    file_path = os.path.join(folder, file_name)

    # Skip if it's already a folder
    if os.path.isdir(file_path):
        continue

    # Get the file extension (example: '.jpg' → 'jpg')
    extension = os.path.splitext(file_name)[1].lower()

    # If file has no extension, put it in "Others"
    if extension == "":
        extension_folder = os.path.join(folder, "Others")
    else:
        # Create a folder based on extension (example: jpg, pdf, mp3)
        extension_folder = os.path.join(folder, extension[1:])  # remove the dot

    # Create the folder if it doesn't exist
    os.makedirs(extension_folder, exist_ok=True)

    # Move the file into its new folder
    shutil.move(file_path, os.path.join(extension_folder, file_name))

print("All files organized successfully!")