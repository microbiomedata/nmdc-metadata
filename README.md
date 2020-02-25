# Metadata management for the [National Microbiome Data Collaborative](https://microbiomedata.org/)
[![Build Status](https://travis-ci.org/microbiomedata/nmdc-metadata.svg?branch=master)](https://travis-ci.org/microbiomedata/nmdc-metadata)

The purpose of this repository is to manage metadata for the [National Microbiome Data Collaborative (NMDC)](https://microbiomedata.org/). The [NMDC](https://microbiomedata.org/) is a multi-organizational effort to enable integrated microbiome data across diverse areas in medicine, agriculture, bioenergy, and the environment. This integrated platform facilitates comprehensive discovery of and access to multidisciplinary microbiome data in order to unlock new possibilities with microbiome data science. 

Tasks managed by the repository are:
* Generating the [schema](https://github.com/microbiomedata/nmdc-metadata/tree/master/schema)
* Deploying the [documentation](https://microbiomedata.github.io/nmdc-metadata/) 
* Integrating metadata from multiple environmental data repositories

## Schema
The [NMDC](https://microbiomedata.org/) [schema](https://github.com/microbiomedata/nmdc-metadata/tree/master/schema) is developed using the [Biolink modeling language (BiolinkML)](https://github.com/biolink/biolinkml). [BiolinkML](https://github.com/biolink/biolinkml) is a general purpose modeling language following object-oriented and ontological principles. Models are authored in YAML, and a variety of artifacts can be generated from the model, such as ShEx, JSON-Schema, OWL, Python dataclasses, UML diagrams, and Markdown pages for deployment in a GitHub pages site. Using [BiolinkML](https://github.com/biolink/biolinkml), we define high-level entities to represent the data we are integrating. These entities include biosamples (specific portions of material collected from a site), biosample processing (e.g., sequencing performed on a biosample), data objects (e.g., a fastq file produced from a sequencing run), and annotations that specify characteristics of biosamples (e.g., the temperature and elevation of the site where the sample was collected). 

The schema is in the [schema](https://github.com/microbiomedata/nmdc-metadata/tree/master/schema) folder. The yaml file is the source.
  ![img](https://raw.githubusercontent.com/microbiomedata/nmdc-metadata/master/schema/nmdc_schema_uml.png)

## Documentation
Documentation for the [NMDC schema](./schema) can be browsed here:
* https://microbiomedata.github.io/nmdc-metadata/
 
## Standardization of characteristics
Entities in the schema are annotated with characteristics. When possible, we use standard terminologies and ontologies to define these characteristics. These standards include:
* [Minimum Information about any (x) Sequence (MIxS)](https://gensc.org/mixs/)
* The [Environment Ontology (ENVO)](https://github.com/EnvironmentOntology/envo)
 
We are actively involved in updating the [MIxS](https://gensc.org/mixs/) standards ([mixs-ng](https://github.com/GenomicsStandardsConsortium/mixs-ng)) and creating an RDF version of [MIxS](https://gensc.org/mixs/) ([mixs-rdf](https://github.com/GenomicsStandardsConsortium/mixs-rdf)).


## Metadata sources
At present, we ingest metadata from the [Joint Genome Institute (JGI)](https://jgi.doe.gov/) and the [Environmental Molecular Sciences Lab (EMSL)](https://www.pnnl.gov/environmental-molecular-sciences-laboratory).  

The [NMDC schema](./schema) and [translation process](./metadata-translation/notebooks) will be modified as more metadata sources become available.

## Metadata integration

We use [Jupyter notebooks](https://github.com/microbiomedata/nmdc-metadata/tree/master/metadata-translation/notebooks) to integrate the metadata sources. This allows us to iterate quickly in a transparent and interactive manner as new metadata sources become available. 

Development of more comprehensive ETL pipeline will progress as the metadata sources and schema become more concrete.

