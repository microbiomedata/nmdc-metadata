# Schema
The [NMDC](https://microbiomedata.org/) schema specifies how metadata elements are related. The main elements are:
* [Study](https://microbiomedata.github.io/nmdc-metadata/docs/Study.html): Summarizes the overall goal of a research initiative and outlines the key objective of its underlying projects.
* [Biosample](https://microbiomedata.github.io/nmdc-metadata/docs/Biosample.html): A material sample. It may be environmental (encompassing many organisms) or isolate or tissue.  
An environmental sample containing genetic material from multiple individuals is commonly referred to as a biosample.
* [Characteristic](https://microbiomedata.github.io/nmdc-metadata/docs/Characteristic.html): A characteristic of a biosample.  
Examples: depth, habitat, material. For NMDC, characteristics SHOULD be mapped to terms within a MIxS template
* [Omics processing](https://microbiomedata.github.io/nmdc-metadata/docs/OmicsProcessing.html): The methods and processes used to generate omics data from a biosample or organism.
Examples of outputs include samples cultivated from another sample or data objects created by instruments runs.
* [Data object](https://microbiomedata.github.io/nmdc-metadata/docs/DataObject.html): An object that primarily consists of symbols that represent information.  
Files, records, and omics data are examples of data objects.  

During the [translation process](../metadata-translation/notebooks) [biosamples](https://microbiomedata.github.io/nmdc-metadata/docs/Biosample.html) are annotated with [characteristics](https://microbiomedata.github.io/nmdc-metadata/docs/Characteristic.html) that specify such things as where, when, or how the sample was collected.

![img](https://raw.githubusercontent.com/microbiomedata/nmdc-metadata/master/schema/nmdc_schema_uml.png)

## Schema management
The [NMDC](https://microbiomedata.org/) schema is developed using the [Biolink modeling language (BiolinkML)](https://github.com/biolink/biolinkml). [BiolinkML](https://github.com/biolink/biolinkml) is a general purpose modeling language following object-oriented and ontological principles. Models are authored in YAML, and a variety of artifacts can be generated from the model, such as ShEx, JSON-Schema, OWL, Python dataclasses, UML diagrams, and Markdown pages for deployment in a GitHub pages site.  

Using [BiolinkML](https://github.com/biolink/biolinkml), we define high-level entities to represent the data we are integrating. These entities include biosamples (specific portions of material collected from a site), biosample processing (e.g., sequencing performed on a biosample), data objects (e.g., a fastq file produced from a sequencing run), and annotations that specify characteristics of biosamples (e.g., the temperature and elevation of the site where the sample was collected). 

[nmdc.yaml](nmdc.yaml) is the source file for the [NMDC](https://microbiomedata.org/) schema.
 
## Documentation
BiolinkML generates a set of markdown files. These markdown files are then deployed as GitHub pages to:

 * https://microbiomedata.github.io/nmdc-metadata/
 
This workflow allows us to easily modify the the schema and deploy documentation as part of the build process.