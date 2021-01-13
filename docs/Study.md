---
parent: Classes
title: nmdc:Study
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: Study


A study summarizes the overall goal of a research initiative and outlines the key objective of its underlying projects.

URI: [nmdc:Study](https://microbiomedata/meta/Study)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[AttributeValue]%3Cdoi%200..1-++[Study%7Cid:string;name:string%20%3F;alternate_identifiers:string%20%2A;description(i):string%20%3F],[PersonValue]%3Cprincipal%20investigator%200..1-++[Study],[AttributeValue]%3Cspecific_ecosystem%200..1-++[Study],[AttributeValue]%3Cecosystem_subtype%200..1-++[Study],[AttributeValue]%3Cecosystem_type%200..1-++[Study],[AttributeValue]%3Cecosystem_category%200..1-++[Study],[AttributeValue]%3Cecosystem%200..1-++[Study],[OmicsProcessing]-%20part%20of%200..%2A%3E[Study],[Database]++-%20study%20set%200..%2A%3E[Study],[NamedThing]%5E-[Study],[PersonValue],[OmicsProcessing],[NamedThing],[Database],[AttributeValue])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[OmicsProcessing](OmicsProcessing.md)** *[omics processing➞part of](omics_processing_part_of.md)*  <sub>0..*</sub>  **[Study](Study.md)**
 *  **[Database](Database.md)** *[study set](study_set.md)*  <sub>0..*</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [doi](doi.md)  <sub>OPT</sub>
    * range: [AttributeValue](AttributeValue.md)
 * [ecosystem](ecosystem.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [ecosystem_category](ecosystem_category.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [ecosystem_subtype](ecosystem_subtype.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [ecosystem_type](ecosystem_type.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [principal investigator](principal_investigator.md)  <sub>OPT</sub>
    * Description: represents the PI
    * range: [PersonValue](PersonValue.md)
 * [specific_ecosystem](specific_ecosystem.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [AttributeValue](AttributeValue.md)
 * [study➞alternate identifiers](study_alternate_identifiers.md)  <sub>0..*</sub>
    * Description: The same study may have distinct identifiers in different databases (e.g. GOLD and EMSL)
    * range: [String](types/String.md)
 * [study➞id](study_id.md)  <sub>REQ</sub>
    * Description: The primary identifier for the study.
    * range: [String](types/String.md)
 * [study➞name](study_name.md)  <sub>OPT</sub>
    * Description: A human readable name or description of the study.
    * range: [String](types/String.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](types/String.md)
 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](types/String.md)

### Domain for slot:

 * [study➞alternate identifiers](study_alternate_identifiers.md)  <sub>0..*</sub>
    * Description: The same study may have distinct identifiers in different databases (e.g. GOLD and EMSL)
    * range: [String](types/String.md)
 * [study➞id](study_id.md)  <sub>REQ</sub>
    * Description: The primary identifier for the study.
    * range: [String](types/String.md)
 * [study➞name](study_name.md)  <sub>OPT</sub>
    * Description: A human readable name or description of the study.
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | proposal |
|  | | research proposal |
|  | | research study |
|  | | investigation |
| **In Subsets:** | | sample subset |

