"""
ファイルを拡張子ごとに自動分類し、
対応フォルダへコピーするツール。

処理内容は log.txt に記録される。
"""
from pathlib import Path
import shutil

folder = Path("./")

for item in folder.iterdir():
    if item.name == "log.txt":
        continue
    if item.is_file() and item.suffix:
        extension = item.suffix.replace(".", "")
        folder_name = f"{extension}_folder"
        target_folder = Path(folder_name)
        target_folder.mkdir(exist_ok=True)
        shutil.copy(item, target_folder / item.name)
        log_message = f"{item.name} copied to {folder_name}\n"
        with open("log.txt", "a") as f:
            f.write(log_message)
        print(f"{item.name} copied")
