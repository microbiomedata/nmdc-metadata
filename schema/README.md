# Schema



## Schema management
The [NMDC](https://microbiomedata.org/) schema is developed using the [Biolink modeling language (BiolinkML)](https://github.com/biolink/biolinkml). [BiolinkML](https://github.com/biolink/biolinkml) is a general purpose modeling language following object-oriented and ontological principles. Models are authored in YAML, and a variety of artifacts can be generated from the model, such as ShEx, JSON-Schema, OWL, Python dataclasses, UML diagrams, and Markdown pages for deployment in a GitHub pages site. Using [BiolinkML](https://github.com/biolink/biolinkml), we define high-level entities to represent the data we are integrating. These entities include biosamples (specific portions of material collected from a site), biosample processing (e.g., sequencing performed on a biosample), data objects (e.g., a fastq file produced from a sequencing run), and annotations that specify characteristics of biosamples (e.g., the temperature and elevation of the site where the sample was collected). 

[nmdc.yaml](nmdc.yml) is the source file for the [NMDC](https://microbiomedata.org/) schema. ![img](https://raw.githubusercontent.com/microbiomedata/nmdc-metadata/master/schema/nmdc_schema_uml.png)

## Documentation
To produce human-readable documentation, BiolinkML generates a set of markdown files. These markdown files are then deployed as GitHub pages to:

 * https://microbiomedata.github.io/nmdc-metadata/
 
This workflow allows us to easily modify the the schema and deploy documentation as part of the build process.