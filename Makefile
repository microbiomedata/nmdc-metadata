.PHONY: all

all: install build

clean:
	rm env.lock

python_dataclasses: schema/nmdc.py
json_schema: schema/nmdc.json
schema_uml: schema/nmdc_schema_uml.png

install: env.lock

env.lock:
	pipenv install pyyaml biolinkml requests
	cp /dev/null env.lock

build: python_dataclasses json_schema

# Python dataclasses

schema/nmdc.py: schema/nmdc.yaml env.lock
	pipenv run gen-py-classes $< > $@.tmp && mv $@.tmp $@

# JSON Schema

# TODO rename
schema/nmdc.json: schema/nmdc.yaml env.lock
	pipenv run gen-json-schema $< > $@.tmp && mv $@.tmp $@


docs: schema/nmdc.yaml env.lock
	pipenv run gen-markdown --dir docs $<

schema/nmdc_schema_uml.png: schema/nmdc.yaml
	pipenv run python schema/generate_uml.py $< $@


schema/mixs.yaml: mixs5/mixs_v5.txt scripts/mixs-to-blml.pl
	scripts/mixs-to-blml.pl $< > $@


docs/%-slides.pdf: docs/%-slides.md
	pandoc $< -t beamer -o $@
docs/%-slides.pptx: docs/%-slides.md
	pandoc $< -o $@
docs/%-slides.html: docs/%-slides.md
	pandoc $< -s -t slidy -o $@
