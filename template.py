import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')


project_name = "textsummarizer"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "research/trials.ipynb"
]

for filepath  in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # Split the path into directory and file name
    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # Create directory if it doesn't exist
        logging.info(f"Creating directory: {filedir} for the {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating file: {filename} in the directory: {filedir}")
    else:
        logging.info(f"File already exists: {filename} in the directory: {filedir}")