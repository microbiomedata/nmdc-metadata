.SECONDARY:

all: install build

python_dataclasses: schema/nmdc.py
json_schema: schema/nmdc.json

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

