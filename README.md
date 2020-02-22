# Metadata management for the [National Microbiome Data Collaborative](https://microbiomedata.org/)

[![Build Status](https://travis-ci.org/microbiomedata/nmdc-metadata.svg?branch=master)](https://travis-ci.org/microbiomedata/nmdc-metadata)

The purpose of this repository is to manage metadata for the [National Microbiome Data Collaborative (NMDC)](https://microbiomedata.org/). The [NMDC](https://microbiomedata.org/) is a multi-organizational effort to enable integrated microbiome data across diverse areas in medicine, agriculture, bioenergy, and the environment. This integrated platform facilitates comprehensive discovery of and access to multidisciplinary microbiome data in order to unlock new possibilities with microbiome data science. 

Tasks managed by the repository are:
* Generating the [schema](https://github.com/microbiomedata/nmdc-metadata/tree/master/schema)
* Deploying the [documentation](https://microbiomedata.github.io/nmdc-metadata/) 
* Integrating metadata from multiple environmental data repositories

## Schema

The [NMDC](https://microbiomedata.org/) [schema](https://github.com/microbiomedata/nmdc-metadata/tree/master/schema) is developed using the [Biolink modeling language (BiolinkML)](https://github.com/biolink/biolinkml). [BiolinkML](https://github.com/biolink/biolinkml) is a general purpose modeling language following object-oriented and ontological principles. Models are authored in YAML, and a variety of artefacts can be generated from the model, such as ShEx, JSON-Schema, OWL, Python dataclasses, UML diagrams, and Markdown pages for deployment in a GitHub pages site. Using [BiolinkML](https://github.com/biolink/biolinkml), we define high-level entities to represent the data we are integrating. These entities include biosamples (specific portions of material collected from a site), biosample processing (e.g., sequencing performed on a biosample), data objects (e.g., a fastq file produced from a sequencing run), and annotations that specify characteristics of biosamples (e.g., the temperature and elevation of the site where the sample was collected). 

The schema is in the [schema](https://github.com/microbiomedata/nmdc-metadata/tree/master/schema) folder. The yaml file is the source.
  ![img](https://raw.githubusercontent.com/microbiomedata/nmdc-metadata/master/schema/nmdc_schema_uml.png)

## Documentation

To produce  human-readable documentation, BiolinkML generates a set of markdown files. These markdown files are then deployed as GitHub pages to:

 * https://microbiomedata.github.io/nmdc-metadata/
 
This workflow allows us to easily modify the the schema and deploy documentation as part of the build process.

## Standardization of characteristics

Entities in the schema are annotated with characteristics. When possible, we use standard terminologies and ontologies to define these characteristics. These standards include:
* [Minimum Information about any (x) Sequence (MIxS)](https://gensc.org/mixs/)
* The [Environment Ontology (ENVO)](https://github.com/EnvironmentOntology/envo)
 
We are actively involved in updating the [MIxS](https://gensc.org/mixs/) standards ([mixs-ng](https://github.com/GenomicsStandardsConsortium/mixs-ng)) and creating an RDF version of [MIxS](https://gensc.org/mixs/) ([mixs-rdf](https://github.com/GenomicsStandardsConsortium/mixs-rdf)).


## Metadata sources

At present, we ingest metadata from the [Joint Genome Institute (JGI)](https://jgi.doe.gov/) and the [Environmental Molecular Sciences Lab (EMSL)](https://www.pnnl.gov/environmental-molecular-sciences-laboratory).  

Metadata from [JGI](https://jgi.doe.gov/) is exported from the Institute's [Genomes Online Database (GOLD)](https://gold.jgi.doe.gov/) and [JGI Archive and Metadata Organizer (JAMO)](https://storageconference.us/2018/Presentations/Beecroft.pdf). These exports are available as downloads:
* [nmdc-version2.zip](https://drive.google.com/drive/u/1/folders/1Wohthyv23Wi6VjY2i_N3AkZuuKPL_P_Q): contains [GOLD's](https://gold.jgi.doe.gov/) metadata.
* [JAMO's](https://storageconference.us/2018/Presentations/Beecroft.pdf) metadata is contained in the files:
  - [ficus_project_fastq.tsv](https://drive.google.com/drive/u/1/folders/1frzGlz8EB8inpVokNTSwD6Ia94eVUlsZ) (sequencing metadata)
  - [ficus_project_fna.tsv](https://drive.google.com/drive/u/1/folders/1frzGlz8EB8inpVokNTSwD6Ia94eVUlsZ) (nucleotide assembly metadata)
  - [ficus_project_faa.tsv](https://drive.google.com/drive/u/1/folders/1frzGlz8EB8inpVokNTSwD6Ia94eVUlsZ) (amino acid assembly metadata)  
  
Metadata from [EMSL](https://www.pnnl.gov/environmental-molecular-sciences-laboratory) is contained in the files:
* [EMSL_FICUS_project_process_data_export.xlsx](https://drive.google.com/drive/u/1/folders/1frzGlz8EB8inpVokNTSwD6Ia94eVUlsZ)
* [FICUS - JGI-EMSL Proposal - Gold Study - ID mapping and PI.xlsx](https://drive.google.com/drive/u/1/folders/1frzGlz8EB8inpVokNTSwD6Ia94eVUlsZ)

## Metadata integration

Currently, we use [Jupyter notebooks](https://github.com/microbiomedata/nmdc-metadata/tree/master/metadata-translation/notebooks) to integrate the metadata sources. Due to early stage of the project, we need to be able to iterate quickly as new metadata sources become available and new schema changes are needed. The [Jupyter notebooks](https://github.com/microbiomedata/nmdc-metadata/tree/master/metadata-translation/notebooks) allow us to do this in a transparent and interactive manner.  

Development of more comprehensive ETL pipeline will progress as the metadata sources and schema become more concrete.

