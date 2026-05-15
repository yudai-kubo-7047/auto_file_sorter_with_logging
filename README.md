📁 Auto File Sorter with Logging
A Python script that automatically organizes files by extension into subfolders — with a full activity log saved to log.txt.

🚀 What It Does
This tool scans a folder, sorts each file into a subfolder based on its extension, and records every action to a log file. Perfect for keeping track of what was moved and when.
Example:
Before:

📂 my_folder/
├── report.pdf
├── photo.jpg
├── data.csv


After running the script:

📂 my_folder/
├── 📂 pdf_folder/
│   └── report.pdf
├── 📂 jpg_folder/
│   └── photo.jpg
├── 📂 csv_folder/
│   └── data.csv
└── log.txt  ← activity log created automatically

log.txt output:
report.pdf copied to pdf_folder
photo.jpg copied to jpg_folder
data.csv copied to csv_folder

✨ Features

Automatically detects file extensions
Creates subfolders dynamically
Copies files into the correct subfolder
Logs every file operation to log.txt
Skips log.txt itself to avoid conflicts
Prints a confirmation message for each file processed


🛠️ Technologies Used

Python 3.x
pathlib — for file path handling
shutil — for file copying
Built-in file I/O (open, write) — for logging


📦 How to Use

Clone this repository:

bashgit clone https://github.com/yudai-kubo-7047/auto_file_sorter_with_logging.git
cd auto_file_sorter_with_logging

Place the files you want to sort in the same folder as the script
Run the script:

bashpython auto_file_sorter_with_logging.py

Check the subfolders and open log.txt to review the activity log!


💡 Why I Built This
This is an improved version of my auto-file-sorter project. I added logging functionality to make the tool more practical for real-world use — so users can always review what happened after the script runs.

🔄 Difference from auto-file-sorter
Featureauto-file-sorterauto-file-sorter-with-loggingSorts files by extension✅✅Creates subfolders✅✅Activity log (log.txt)❌✅Skips log file automatically❌✅

📝 Notes

This script copies files (does not delete originals)
log.txt is appended each time the script runs (history is preserved)
Files without an extension are skipped


👤 Author
yudai-kubo-7047
GitHub: @yudai-kubo-7047
