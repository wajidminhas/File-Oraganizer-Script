import os
import shutil

file_path = "/home/minhas/Desktop/Code/Panaverse/script/documents"

def organize_files(folder_path):
    # Step 1: List all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    # Step 2: Loop through each file
    for file in files:
        # Skip the script file itself
        if file == "file_organizer.py":
            continue
        
        # Get the file extension
        if "." in file:
            file_extension = file.split(".")[-1].lower()  # Convert to lowercase for consistency
        else:
            file_extension = "misc"  # Handle files without extensions
        
        # Create a subfolder name based on the file extension
        subfolder_name = os.path.join(folder_path, file_extension + "_files")
        
        # Step 3: Create the subfolder if it doesn't exist
        if not os.path.exists(subfolder_name):
            os.mkdir(subfolder_name)
            print(f"Created folder: {subfolder_name}")
        
        # Step 4: Move the file to the subfolder
        try:
            shutil.move(os.path.join(folder_path, file), os.path.join(subfolder_name, file))
            print(f"Moved {file} to {subfolder_name}")
        except Exception as e:
            print(f"Error moving {file}: {e}")

    print("File organization complete!")

# Step 5: Get the folder path from the user
folder_path = input("Enter the path of the folder to organize: ")

# Step 6: Call the function to organize files
organize_files(file_path)