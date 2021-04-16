.PHONY: all

all: install build

clean:
	rm env.lock


install: env.lock

env.lock:
	pip install pipenv
	pipenv install
	cp /dev/null env.lock

# TODO: nmdc-02
schema_test_examples = nmdc_example_database study_test biosample_test gold_project_test emsl_project_test emsl_data_object_test mg_assembly_activities_test mg_assembly_data_objects_test readQC_activities_test readQC_data_objects_test functional-annotation img_mg_annotation_data_objects img_mg_annotation_objects MAGs_activity read_based_analysis_activity metagenome_annotation_activity Froze_Core_2015_S2_0_10_7_Metab gcms_metabolomics_data_products ftms_nom_data_products nom_analysis_activity

test_jsonschema: $(patsubst %, schema/test-%.valid, $(schema_test_examples))
test: test_jsonschema pytest

pytest: schema/nmdc.py
	pipenv run python $<

build: python_dataclasses json_schema shex

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

#.PHONY: force_schema_build
#force_schema_build: schema/nmdc.yaml schema/prov.yaml schema/core.yaml  schema/annotation.yaml

# JSON Schema
schema/nmdc.schema.json: schema/nmdc.yaml env.lock
	pipenv run gen-json-schema -t database $<  > $@.tmp && jsonschema $@.tmp && mv $@.tmp $@

# This is temporary fix to apply additionalProperties: false gloabally
# see: https://github.com/biolink/biolinkml/issues/349
	jq '. += {"additionalProperties": false}' $@ > $@.tmp && mv $@.tmp $@

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

# JSONLD Context
schema/%.context.jsonld: schema/%.yaml env.lock
	pipenv run gen-jsonld-context $< > $@.tmp && mv $@.tmp $@

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

jekyll-docs: schema/nmdc.yaml env.lock
	pipenv run python scripts/jekyllmarkdowngen.py --yaml $< --dir docs

schema/nmdc_schema_uml.png: schema/nmdc.yaml
#	pipenv run python schema/generate_uml.py $< $@
# temporary hack to address issue of generate_uml.py not finding the correct directory
	cd schema/ &&	pipenv run python generate_uml.py $(notdir $<) $(notdir $@) && cd ..

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

# -- requirments --
.PHONY: requirements-file
requirements-file:
# calls pipenv to generate the requirements.txt and requirements-dev.txt files
	pipenv run pipenv_to_requirements

# -- ETL commands --
.PHONY: run-etl build-test-datasets build-example-db build-merged-db

# directories for output and data
etl_build_dir := metadata-translation/src/bin/output
etl_data_dir := metadata-translation/src/data
etl_example_dir := examples

# files produced by etl
etl_db := $(etl_build_dir)/nmdc_database.json
etl_db_zip := $(etl_build_dir)/nmdc_database.json.zip
etl_example_db := $(etl_build_dir)/nmdc_example_database.json
etl_test_sets := study_test.json gold_project_test.json biosample_test.json readQC_data_objects_test.json readQC_activities_test.json mg_assembly_data_objects_test.json mg_assembly_activities_test.json emsl_data_object_test.json emsl_project_test.json

# add directories to test set files
etl_test_set_files := $(foreach set, $(etl_test_sets), $(etl_build_dir)/$(set))

test-etl-vars:
	@echo $(etl_db)
	@echo $(etl_db_zip)
	@echo $(etl_example_db)
	@echo $(etl_test_sets)
	@echo $(etl_test_set_files)

run-etl:
# runs the ETL script, creates the nmdc datbase and test/example files
# create needed dirs
	mkdir -p metadata-translation/src/bin/output/nmdc_etl

# navigate to directory and execute pipeline script
	cd metadata-translation/src/bin/ && python execute_etl_pipeline.py

# zip output and move to data directory
	rm -f $(etl_db_zip) # remove old copy of zipped db
	zip $(etl_db_zip) $(etl_db) # zip new copy
	cp $(etl_db_zip) $(etl_data_dir) # cp new db to data directory

# copy example database to examples directory
	cp $(etl_example_db) $(etl_example_dir)

# copy test datasets to examples
	cp $(etl_test_set_files) $(etl_example_dir)

build-test-datasets:
# runs the ETL scipt, but ONLY creates the test dataset
# create needed dirs
	mkdir -p metadata-translation/src/bin/output/nmdc_etl

# navigate to directory and execute pipeline script
	cd metadata-translation/src/bin/ && python execute_etl_pipeline.py --testdata --no-etl --no-exdb --no-mergedb

# copy test datasets to examples
	cp $(etl_test_set_files) $(etl_example_dir)

build-example-db:
# runs the ETL scipt, but ONLY creates the example database
# create needed dirs
	mkdir -p metadata-translation/src/bin/output/nmdc_etl

# navigate to directory and execute pipeline script
	cd metadata-translation/src/bin/ && python execute_etl_pipeline.py --exdb --no-testdata --no-etl --no-mergedb

# copy example database to examples directory
	cp $(etl_example_db) $(etl_example_dir)

build-merged-db:
# runs the ETL scipt, but ONLY creates the merged data source used as input for the ETL pipeline
# create needed dirs
	mkdir -p metadata-translation/src/bin/output/nmdc_etl

# navigate to directory and execute pipeline script
	cd metadata-translation/src/bin/ && python execute_etl_pipeline.py --only-mergedb
