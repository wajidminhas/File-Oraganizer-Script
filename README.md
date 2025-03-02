# File Organizer Script

A Python script to organize files in a folder by moving them into subfolders based on their file extensions.

---

## Features
- Organizes files into subfolders based on their extensions.
- Handles files without extensions by moving them to a `misc_files` folder.
- Skips the script file itself to avoid moving it into a subfolder.
- Provides error handling for file operations.

---

## How It Works
1. The script lists all files in the specified folder.
2. It creates subfolders named after the file extensions (e.g., `txt_files`, `jpg_files`).
3. Files are moved into their respective subfolders.
4. Files without extensions are moved to a `misc_files` folder.

---

## Usage
1. Save the script as `file_organizer.py` in the folder you want to organize.
2. Open a terminal or command prompt.
3. Navigate to the folder where the script is saved:
   ```bash

   cd path/to/your/folder

  run:   python file_organizer.py

Author
WAJID SHABBIR MINHAS

