import os
from pathlib  import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s],%(message)s')

project_name = "mlopsproject"

list_of_file=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configurationpy",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",#YAML files to store various parameters or configuration settings for an application or model.
    "params.yaml",#customize how your program works without diving into the code itself.
    "schema.yaml",#how data should be structured and what kind of information it can hold.
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",#how the project should be installed
    "research/trials.ipynb",
    "template/index.html",
]

for filepath in list_of_file:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory;{filedir} for the file:{filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):#creates an empty file with the specified path 
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating empty file;{filepath}")

    else:
        logging.info(f"File already exists;{filepath}")