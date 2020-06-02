.PHONY: all

all: install build

clean:
	rm env.lock


install: env.lock

env.lock:
	pipenv install pyyaml biolinkml requests
	cp /dev/null env.lock

build: python_dataclasses json_schema

# The mixs subschema is not hand-authored; it is compiled
# from a tsv saved from the mixs excel file
schema/mixs.yaml: mixs5/mixs_v5.txt scripts/mixs-to-blml.pl
	scripts/mixs-to-blml.pl $< > $@


# -- Generated Artefacts --
#
# the biolinkml framework provides the ability to compile
# the schema to: json-schema, python dataclasses, graphql, ...

all_schema_artefacts: python_dataclasses json_schema graphql schema_uml

python_dataclasses: schema/nmdc.py
json_schema: schema/nmdc.schema.json
graphql: schema/nmdc.graphql
owl: schema/nmdc.owl
schema_uml: schema/nmdc_schema_uml.png

# Python dataclasses
schema/nmdc.py: schema/nmdc.yaml env.lock
	pipenv run gen-py-classes $< > $@.tmp && mv $@.tmp $@

# JSON Schema
schema/nmdc.schema.json: schema/nmdc.yaml env.lock
	pipenv run gen-json-schema -t database $<  > $@.tmp && mv $@.tmp $@

# OWL
schema/nmdc.owl: schema/nmdc.yaml env.lock
	pipenv run gen-owl $< > $@.tmp && mv $@.tmp $@

# GraphQL
schema/nmdc.graphql: schema/nmdc.yaml env.lock
	pipenv run gen-graphql $< > $@.tmp && mv $@.tmp $@

# ProtoBuf
schema/nmdc.proto: schema/nmdc.yaml env.lock
	pipenv run gen-proto $< > $@.tmp && mv $@.tmp $@

#schema/nmdc.rdf: schema/nmdc.yaml env.lock
#	pipenv run gen-rdf $< > $@.tmp && mv $@.tmp $@

docs: schema/nmdc.yaml env.lock
	pipenv run gen-markdown --dir docs $<

schema/nmdc_schema_uml.png: schema/nmdc.yaml
	pipenv run python schema/generate_uml.py $< $@

# -- Slides --
docs/%-slides.pdf: docs/%-slides.md
	pandoc $< -t beamer -o $@
docs/%-slides.pptx: docs/%-slides.md
	pandoc $< -o $@
docs/%-slides.html: docs/%-slides.md
	pandoc $< -s -t slidy -o $@
