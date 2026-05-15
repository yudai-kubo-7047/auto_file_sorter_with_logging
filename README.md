📁 Auto File Sorter
A Python script that automatically organizes files in a folder by sorting them into subfolders based on their file extension.

🚀 What It Does
Have a messy folder full of mixed file types? This tool scans the directory and automatically moves each file into a dedicated subfolder named after its extension.
Example:
Before:
📂 my_folder/
├── report.pdf
├── photo.jpg
├── data.csv
├── notes.txt

After running the script:
📂 my_folder/
├── 📂 pdf_folder/
│   └── report.pdf
├── 📂 jpg_folder/
│   └── photo.jpg
├── 📂 csv_folder/
│   └── data.csv
├── 📂 txt_folder/
│   └── notes.txt

✨ Features

Detects file extensions automatically
Creates subfolders on the fly (no manual setup needed)
Copies files safely into corresponding folders
Skips folders and files without extensions
Prints a confirmation message for each file processed


🛠️ Technologies Used

Python 3.x
pathlib — for file path handling
shutil — for file copying


📦 How to Use

Clone this repository:

bashgit clone https://github.com/yudai-kubo-7047/auto-file-sorter.git
cd auto-file-sorter

Place the files you want to sort in the same folder as auto_file_sorter.py
Run the script:

bashpython auto_file_sorter.py

Check the newly created subfolders!


💡 Why I Built This
Managing downloaded files manually is time-consuming and error-prone. I built this tool to automate the process and practice working with Python's file system libraries (pathlib and shutil).

📝 Notes

This script copies files (does not delete originals)
Files without an extension are skipped
Already existing folders are reused safely (exist_ok=True)


👤 Author
yudai-kubo-7047
GitHub: @yudai-kubo-7047
