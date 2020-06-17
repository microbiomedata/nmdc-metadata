
# Type: study


A study summarizes the overall goal of a research initiative and outlines the key objective of its underlying projects.

URI: [nmdc:Study](https://microbiomedata/meta/Study)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[PersonValue]<principal%20investigator%200..1-++\[Study&#124;id:string;name:string%20%3F;alternate_identifiers:string%20*;ecosystem:string%20%3F;ecosystem_category:string%20%3F;ecosystem_type:string%20%3F;ecosystem_subtype:string%20%3F;specific_ecosystem:string%20%3F;description(i):string%20%3F],%20\[ControlledTermValue]<experimental_factor%200..1-++\[Study],%20\[TextValue]<project_name%200..1-++\[Study],%20\[TextValue]<investigation_type%200..1-++\[Study],%20\[BooleanValue]<submitted_to_insdc%200..1-++\[Study],%20\[OmicsProcessing]-%20part%20of%200..*>\[Study],%20\[Database]++-%20study%20set%200..*>\[Study],%20\[NamedThing]^-\[Study])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[OmicsProcessing](OmicsProcessing.md)** *[omics processing➞part of](omics_processing_part_of.md)*  <sub>0..*</sub>  **[Study](Study.md)**
 *  **[Database](Database.md)** *[study set](study_set.md)*  <sub>0..*</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [ecosystem](ecosystem.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [ecosystem_category](ecosystem_category.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [ecosystem_subtype](ecosystem_subtype.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [ecosystem_type](ecosystem_type.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [experimental_factor](experimental_factor.md)  <sub>OPT</sub>
    * Description: "Experimental factors are essentially the variable aspects of an experiment design which can be used to describe an experiment, or set of experiments, in an increasingly detailed manner. This field accepts ontology terms from Experimental Factor Ontology (EFO) and/or Ontology for Biomedical Investigations (OBI). For a browser of EFO (v 2.95) terms, please see http://purl.bioontology.org/ontology/EFO; for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI"
    * range: [ControlledTermValue](ControlledTermValue.md)
    * in subsets: (investigation)
 * [investigation_type](investigation_type.md)  <sub>OPT</sub>
    * Description: "Nucleic Acid Sequence Report is the root element of all MIGS/MIMS compliant reports as standardized by Genomic Standards Consortium. This field is either eukaryote,bacteria,virus,plasmid,organelle, metagenome,mimarks-survey, mimarks-specimen, metatranscriptome, single amplified genome, metagenome-assembled genome, or uncultivated viral genome"
    * range: [TextValue](TextValue.md)
    * in subsets: (investigation)
 * [principal investigator](principal_investigator.md)  <sub>OPT</sub>
    * Description: represents the PI
    * range: [PersonValue](PersonValue.md)
 * [project_name](project_name.md)  <sub>OPT</sub>
    * Description: Name of the project within which the sequencing was organized
    * range: [TextValue](TextValue.md)
    * in subsets: (investigation)
 * [specific_ecosystem](specific_ecosystem.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [study➞alternate identifiers](study_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [study➞id](study_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [study➞name](study_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [submitted_to_insdc](submitted_to_insdc.md)  <sub>OPT</sub>
    * Description: "Depending on the study (large-scale e.g. done with next generation sequencing technology, or small-scale) sequences have to be submitted to SRA (Sequence Read Archive), DRA (DDBJ Read Archive) or via the classical Webin/Sequin systems to Genbank, ENA and DDBJ. Although this field is mandatory, it is meant as a self-test field, therefore it is not necessary to include this field in contextual data submitted to databases"
    * range: [BooleanValue](BooleanValue.md)
    * in subsets: (investigation)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * inherited from: None
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](types/String.md)
    * inherited from: None
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](types/String.md)
    * inherited from: None
 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](types/String.md)
    * inherited from: None

### Domain for slot:

 * [study➞alternate identifiers](study_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [study➞id](study_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [study➞name](study_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | proposal |
|  | | research proposal |
|  | | research study |
|  | | investigation |

