# Metadata management for the [National Microbiome Data Collaborative](https://microbiomedata.org/)

[![Build Status](https://travis-ci.org/microbiomedata/nmdc-metadata.svg?branch=master)](https://travis-ci.org/microbiomedata/nmdc-metadata)

The purpose of this repository is to manage metadata for the [National Microbiome Data Collaborative (NMDC)](https://microbiomedata.org/). The [NMDC](https://microbiomedata.org/) is a multi-organizational effort to enable integrated microbiome data across diverse areas in medicine, agriculture, bioenergy, and the environment. This integrated platform facilitates comprehensive discovery of and access to multidisciplinary microbiome data in order to unlock new possibilities with microbiome data science. 

Current tasks managed by the repository are:
* Generating the [schema](https://github.com/microbiomedata/nmdc-metadata/tree/master/schema)
* Deploying the [documentation](https://microbiomedata.github.io/nmdc-metadata/) 
* Integrating metadata from multiple environmental data repositories

## Schema

The [NMDC](https://microbiomedata.org/) [schema](https://github.com/microbiomedata/nmdc-metadata/tree/master/schema) is developed using the [Biolink modeling language (BiolinkML)](https://github.com/biolink/biolinkml). [BiolinkML](https://github.com/biolink/biolinkml) is a general purpose modeling language following object-oriented and ontological principles. Models are authored in YAML, and a variety of artefacts can be generated from the model, such as ShEx, JSON-Schema, OWL, Python dataclasses, UML diagrams, and Markdown pages for deployment in a GitHub pages site. Using [BiolinkML](https://github.com/biolink/biolinkml), we define high-level entities to represent the data we are integrating. These entities include biosamples (specific portions of material collected from a site), biosample processing (e.g., sequencing performed on a biosample), data objects (e.g., a fastq file produced from a sequencing run), and annotations that specify characteristics of biosamples (e.g., the temperature and elevation of the site where the sample was collected). 

The schema is in the [schema](https://github.com/microbiomedata/nmdc-metadata/tree/master/schema) folder. The yaml file is the source.

Generated human-readable documentation:

 * https://microbiomedata.github.io/nmdc-metadata/
 
 ![img](https://raw.githubusercontent.com/microbiomedata/nmdc-metadata/master/schema/nmdc_schema_uml.png)

## Standardization of characteristics

See the [mixs-ng](https://github.com/GenomicsStandardsConsortium/mixs-ng) repository.

In the interim we are using the GOLD columns.

## Ingest from GOLD

Currently this is in [Jupyter notebooks](https://github.com/microbiomedata/nmdc-metadata/tree/master/GOLD-ontology-translation). We are developing a more comprehensive ETL pipeline.

## Ingest from EMSL

In progress.

For now see the [metadata files](https://drive.google.com/drive/u/1/folders/1frzGlz8EB8inpVokNTSwD6Ia94eVUlsZ) folder on the NMDC drive
