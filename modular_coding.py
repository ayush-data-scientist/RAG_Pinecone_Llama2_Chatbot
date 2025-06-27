import os
from pathlib import Path
import logging
logging.basicConfig(level= logging.INFO, format='%(asctime)s: %(message)s:')

list_of_files= [
    # "requirements.txt"
    # ".env"
    "setup.py",
    "app.py",
    "experiments.ipynb",
    "store_index.py",
    "static",
    "templates/chat.html",
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py"

]
for file_path in list_of_files:
    file_path=Path(file_path)
    dir_name, file_name= os.path.split(file_path)

    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
        logging.info(f"{dir_name} directory created.")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, 'w') as file:
            logging.info(f"{file_name} created.")
            pass
    else:
            logging.info(f"{file_name} already exists")