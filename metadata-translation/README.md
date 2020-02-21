# Metadata translation
Translates [JGI](https://jgi.doe.gov/) and [EMSL](https://www.pnnl.gov/environmental-molecular-sciences-laboratory) metadata into JSON conformant with the [NMDC schema](https://github.com/microbiomedata/nmdc-metadata/tree/master/schema).

## Notebook setup
We use venv to create a virtural enironment.  
To create a virtual environment run the command `python3 -m venv <environment name>`  .  
I typically name my environment `.env`, and configure `.gitignore` to ignore `.env` files. This prevents the environment libraries from being uploaded to the repository.  

After the environment is created, run the command `source <environment name>/bin/activate` to enter the environment.  
Once in the environment, run the command `pip install -r requirements.txt` to install the necessary python libraries.

You exit the environment by executing the command `deactivate` in the terminal.
