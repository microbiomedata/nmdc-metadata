pipenv run gen-py-classes schema/nmdc.yaml > schema/nmdc.py.tmp && mv schema/nmdc.py.tmp schema/nmdc.py
pipenv run gen-json-schema schema/nmdc.yaml > schema/nmdc.json.tmp && mv schema/nmdc.json.tmp schema/nmdc.json
pipenv run gen-markdown --dir docs schema/nmdc.yaml
# pipenv run python schema/generate_uml.py schema/nmdc.yaml schema/nmdc_schema_uml.png

## pipenv run throws error: ModuleNotFoundError: No module named 'yaml'
## running it w/o pipenv does not
python schema/generate_uml.py schema/nmdc.yaml schema/nmdc_schema_uml.png