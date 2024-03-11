# Create a Virtual Environment with Python
## System Settings
### Python

    Version:  Python 3.9.1
### PyCharm

    PyCharm 2023.3.3 (Community Edition)

---

Table of contents

- [Create a Virtual Environment with Python](#create-a-virtual-environment-with-python)
  - [Steps to creating a 'venv'](#steps-to-creating-a-venv)
  - [Configuring the email associated with GitHub](#configuring-the-email-associated-with-GitHub)

## Steps to creating a 'venv'

### Create a folder for the project

There are 2 options:

1. Create a repository on [GitHub.com](https://github.com "GitHub.com") BEFORE creating the project folder on the local machine.

    Once the repository is created, clone it onto the local machine. I have used GitHub Desktop for ease of use.

2. Create the project folder locally (see below gist)

   - First, open a **Terminal Prompt within VS Code**.

   - Then, go to the folder where the new project is to be created, *i.e.* go to the 'working folder'.

        For example, if the main folder is called ```python_projects```, go to

            C:\python_projects

        Hence, for the **relative path**, type:

            cd /python_projects

   - Create a folder for the project called ```project_name``` and check if it is present in the working folder

            mkdir project_name && dir

   - ```cd``` into this folder

            cd project_name

---

### Create a virtual environment for the project

1. Open the terminal through PyCharm, this will automatically open at the root for the current project.

2. Create a virtual environment called ```.venv```
    The `.` denotes a hidden folder.

    The command below will create a new folder called ```.venv```

        python3 -m venv .venv

    In my system the Python3 installation was not pointed to by the system `python` so I have used `python3` for the above command. Alternatively use the following:

        python -m venv venv

---

### Activate the new virtual environment ```.venv```

In the PyCharm terminal I type in the following command to activate the virtual environment ```.venv ```:

    source .venv/bin/activate

The active path should now be preceded by ```(.venv)``` or ```({name})``` if a specific venv name was chosen.

---

### Create 'default' folders and files

These will be needed for the project, *e.g.*:

    mkdir data, notebooks, src
    
    echo >> __init__.py
    echo >> main.py
	echo >> config.py
	echo >> setup.py
    echo >> requirements.txt

OPTION: if the project is to be hosted on GitHub, the following files can be created, or done automatically when creating a repository.

    echo >> README.md
    echo >> LICENSE
    echo >> .gitignore
    echo >> .gitkeep

NOTE 1: the 'LICENSE' and '.gitignore' files do NOT take a file extension. Only 'README.md' does.

NOTE 2: add a copy of .gitkeep into each folder in order to commit empty folders to GitHub.

---

### Record the dependencies for the project

- First, update the ```pip``` library

        python3 -m pip install --upgrade pip

- Then, create the dependencies file named ```requirements.txt```

        pip list > requirements.txt

---

### Install a Python Library

    python3 -m pip install package_name

If installing more than one package, type:

    python3 -m pip install package_name_1 package_name_2

If installing a specific version of a package, type:

    python3 -m pip install package_name=1.6

---

#### Install dependencies from a file

The ```requirements.txt``` file can be used within a **new environment** to install dependencies cleanly with the following command:

    python3 -m pip install -r requirements.txt

---

### Deactivate the virtual environment

    deactivate

---

## Configuring the email associated with GitHub
To configure the eail associated for the current repo (useful if working on multiple projects with different emails):

    git config user.email "your@email.com"

This can be verified with the command:

    git config user.email
