# Auto File Sorter With Logging

A Python tool that automatically sorts files by extension, copies them into corresponding folders, and records all actions in `log.txt`.

## Features

- Automatically detects file extensions
- Creates folders if they do not exist
- Copies files into extension-based folders
- Records actions in `log.txt`
- Ignores files without extensions
- Skips `log.txt` to avoid recursive copying

## Technologies Used

- Python 3
- pathlib
- shutil

## Usage

Run the script in the target directory:

```bash
python auto_file_sorter_with_logging.py
