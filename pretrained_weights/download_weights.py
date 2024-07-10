import gdown
import os

folder_ids = ['1fuWf0L5vUs6rVZmw_besLF60QeailOGF', '1TQiugdYlNPIZ7gPuqeIxK9cUReMCGKw5']

for folder_id in folder_ids:
  url = f"https://drive.google.com/drive/folders/{folder_id}?usp=sharing"
  gdown.download_folder(url)