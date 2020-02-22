
# Notebooks
We use [Jupyter notebooks](https://jupyter.org/) to integrate the metadata sources. Due to early stage of the project, we need to be able to iterate quickly as new metadata sources become available and new schema changes are needed. The [Jupyter notebooks](https://github.com/microbiomedata/nmdc-metadata/tree/master/metadata-translation/notebooks) allow us to do this in a transparent and interactive manner. 

## Notebook setup
We use [venv](https://docs.python.org/3/tutorial/venv.html) to create a virtual enironment.  

To create a virtual environment run the command `python3 -m venv <environment name>`  .  
I typically name my environment `.env`, and configure `.gitignore` to ignore `.env` files. This prevents the environment libraries from being uploaded to the repository.  

After the environment is created, run the command `source <environment name>/bin/activate` to enter the environment.  
Once in the environment, run the command `pip install -r requirements.txt` to install the necessary python libraries.

You exit the environment by executing the command `deactivate` in the terminal.

## Translation workflow

TODO