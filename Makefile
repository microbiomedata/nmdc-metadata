.PHONY: all

all: install build

clean:
	rm env.lock


install: env.lock

env.lock:
	pipenv install pyyaml biolinkml requests
	cp /dev/null env.lock

test: schema/test-nmdc-01.valid pytest

pytest: schema/nmdc.py
	pipenv run python $<

build: python_dataclasses json_schema

# The mixs subschema is not hand-authored; it is compiled
# from a tsv saved from the mixs excel file
schema/mixs.yaml: mixs5/mixs_v5.txt mixs5/mixs_v5e.txt
	scripts/mixs-to-blml.pl $^ > $@

schema/mixs_meta.schema.json: schema/mixs_meta.yaml
	pipenv run gen-json-schema -t template $<  > $@.tmp && mv $@.tmp $@

schema/mixs_meta.py: schema/mixs_meta.yaml
	pipenv run gen-py-classes $<  > $@.tmp && mv $@.tmp $@

# -- Generated Artefacts --
#
# the biolinkml framework provides the ability to compile
# the schema to: json-schema, python dataclasses, graphql, ...

all_schema_artefacts: python_dataclasses json_schema graphql schema_uml shex

python_dataclasses: schema/nmdc.py
json_schema: schema/nmdc.schema.json
graphql: schema/nmdc.graphql
owl: schema/nmdc.owl
shex: schema/nmdc.shex
schema_uml: schema/nmdc_schema_uml.png

# Python dataclasses
schema/%.py: schema/%.yaml env.lock
	pipenv run gen-py-classes $< > $@.tmp && pipenv run python $@.tmp && mv $@.tmp $@

# JSON Schema
schema/nmdc.schema.json: schema/nmdc.yaml env.lock
	pipenv run gen-json-schema -t database $<  > $@.tmp && jsonschema $@.tmp && mv $@.tmp $@

schema/kbase.schema.json: schema/kbase.yaml env.lock
	pipenv run gen-json-schema -t SESAR $<  > $@.tmp && jsonschema $@.tmp && mv $@.tmp $@

# OWL
schema/%.owl: schema/%.yaml env.lock
	pipenv run gen-owl $< > $@.tmp && mv $@.tmp $@ && perl -pi -ne 's@prefix meta: <https://w3id.org/biolink/biolinkml/meta/>@prefix meta: <https://w3id.org/$*/>@' $@

# GraphQL
schema/%.graphql: schema/%.yaml env.lock
	pipenv run gen-graphql $< > $@.tmp && mv $@.tmp $@

# ShEx
schema/%.shex: schema/%.yaml env.lock
	pipenv run gen-shex $< > $@.tmp && mv $@.tmp $@

schema/%.csv: schema/%.yaml env.lock
	pipenv run gen-csv $< > $@.tmp && mv $@.tmp $@

# ProtoBuf
schema/%.proto: schema/%.yaml env.lock
	pipenv run gen-proto $< > $@.tmp && mv $@.tmp $@

#schema/%.rdf: schema/%.yaml env.lock
#	pipenv run gen-rdf $< > $@.tmp && mv $@.tmp $@

schema/test-%.valid: examples/%.json schema/nmdc.schema.json 
	jsonschema -i $^

docs: schema/nmdc.yaml env.lock
	pipenv run gen-markdown --dir docs $<

schema/nmdc_schema_uml.png: schema/nmdc.yaml
	pipenv run python schema/generate_uml.py $< $@

# -- Mappings --

all_mappings: mappings/nmdc-to-kbase.tsv
mappings/nmdc-to-%.tsv: schema/%.ttl
	rdfmatch -p nmdc -i mappings/prefixes.ttl -i schema/nmdc.ttl -i $< match > $@

# -- Slides --
docs/%-slides.pdf: docs/%-slides.md
	pandoc $< -t beamer -o $@
docs/%-slides.pptx: docs/%-slides.md
	pandoc $< -o $@
docs/%-slides.html: docs/%-slides.md
	pandoc $< -s -t slidy -o $@

