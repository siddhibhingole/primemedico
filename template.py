import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

list_of_files = [   #name of the files to be created
    "src/__init__.py",
    "src/helper.py",
    "src/prompts.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_of_files:
    file_path = Path(filepath)
    file_dir, file_name = os.path.split(file_path)
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir} for file: {file_name}  ")

    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):    
     with open(file_path, 'w') as f:
        pass
        logging.info(f"Created file: {filepath}")


    else:
       logging.info(f"{file_name} is already exists")