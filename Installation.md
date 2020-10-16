# Installation

There are two ways of going about setting up a virtual environment, installing dependencies, and building the artifacts from [schema/nmdc.yaml](schema/nmdc.yaml).

1. Python venv
2. Pipenv

The exact steps for each approach are listed below.


## 1. Python venv

Python `venv` is a lightweight module for setting up virtual environments. You can create a virtual environment like so,

```
python -m venv my-env
```

Then to activate your virtual environment,

```
source my-env/bin/activate
```

### Install dependencies for the repository

To install all the core packages,

```
pip install -r requirements.txt
```

To install all the core and dev packages (required for running notebooks that are bundled as part of this repository),

```
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Building artifacts

You can individually generate each artiact or let the [Makefile](Makefile) do it for you.

### Running Jupyter notebooks

If you haven't already, make sure you install all the dev packages from the [requirements-dev.txt](requirements-dev.txt),

```
pip install -r requirements-dev.txt
```

Then start Jupyter,

```
jupyter notebook
```

and navigate to your desired notebook for running the analyses.

---

## 2. pipenv

[Pipenv](https://pipenv.pypa.io/en/latest/) is an alternative to Python's `venv` module and is the library we use in our build process and in our [Makefile](Makefile).
Using Pipenv is slightly nuanced and can be different from Python's `venv` module.


### Install pipenv

```
pip install pipenv
```

### Install dependencies for the repository

```
pipenv install
```

This tells pipenv to install all core packages listed [Pipfile](Pipfile), via the `[packages]` directive.

If you would like to install both the core packages and dev packages (required for running notebooks that are bundled as part of this repository) then, 

```
pipenv install --dev
```

### Building artifacts

You can individually generate each artifact or let the Makefile do it for you.

**Note:** The Makefile takes care of installing `pipenv` and all the required core packages necessary for building the artifacts. 


### Running Jupyter notebooks

> If you haven't already, make sure you install all the dev packages from the Pipfile,
> 
> ```
> pip install --dev
> ```


Start Jupyter via pipenv,

```
pipenv run jupyter notebook
```

and navigate to your desired notebook for running the analyses.


### Note for maintainers

The main source of truth for dependencies in this repository is the [Pipfile](Pipfile).
Each time you change the Pipfile, be sure to update the [requirements.txt](requirements.txt) and [requirements-dev.txt](requirements-dev.txt) 
to ensure that they are in sync.

This can be done by running the following command,

```
pipenv_to_requirements
```

The above command will parse the [Pipfile](Pipfile) and autogenerate [requirements.txt](requirements.txt) and [requirements-dev.txt](requirements-dev.txt)

