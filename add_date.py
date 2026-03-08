import os
from datetime import datetime

def add_date_to_filenames(folder_path):
    # Get today's date in YYYY-MM-DD format
    today_date = datetime.now().strftime("%Y-%m-%d")
    
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' not found.")
        return

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        # Create the full old path
        old_path = os.path.join(folder_path, filename)
        
        # Ensure we are only renaming files (skip directories)
        if os.path.isfile(old_path):
            # Create the new filename with the date prefix
            new_filename = f"{today_date}_{filename}"
            new_path = os.path.join(folder_path, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    # Path to the current folder
    target_folder = "."
    
    # Get today's date in YYYY-MM-DD format
    today_date = datetime.now().strftime("%Y-%m-%d")
    
    # Iterate through all files in the folder
    for filename in os.listdir(target_folder):
        # Create the full old path
        old_path = os.path.join(target_folder, filename)
        
        # Ensure we are only renaming the target files (skip directories, script itself, and common files)
        if os.path.isfile(old_path) and filename.startswith("file") and filename.endswith(".md"):
            # Create the new filename with the date prefix
            new_filename = f"{today_date}_{filename}"
            new_path = os.path.join(target_folder, new_filename)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")