.SECONDARY:

all: install build

python_dataclasses: schema/nmdc.py
json_schema: schema/nmdc.json
schema_uml: schema/nmdc_schema_uml.png

install: env.lock

env.lock:
	pipenv install --dev
	cp /dev/null env.lock

build: python_dataclasses json_schema

# Python dataclasses

schema/nmdc.py: schema/nmdc.yaml env.lock
	pipenv run gen-py-classes $< > $@.tmp && mv $@.tmp $@

# JSON Schema

schema/nmdc.json: schema/nmdc.yaml env.lock
	pipenv run gen-json-schema $< > $@.tmp && mv $@.tmp $@

docs: schema/nmdc.yaml env.lock
	pipenv run gen-markdown --dir docs $<

schema/nmdc_schema_uml.png: schema/nmdc.yaml
	pipenv run python schema/generate_uml.py $< $@
