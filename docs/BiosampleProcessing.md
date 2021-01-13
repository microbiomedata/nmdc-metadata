---
parent: Classes
title: nmdc:BiosampleProcessing
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: BiosampleProcessing


A process that takes one or more biosamples as inputs and generates one or as outputs. Examples of outputs include samples cultivated from another sample or data objects created by instruments runs.

URI: [nmdc:BiosampleProcessing](https://microbiomedata/meta/BiosampleProcessing)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OmicsProcessing],[NamedThing],[Biosample]%3Chas%20input%200..%2A-%20[BiosampleProcessing%7Cid(i):string;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20%2A],[BiosampleProcessing]%5E-[OmicsProcessing],[NamedThing]%5E-[BiosampleProcessing],[Biosample])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [OmicsProcessing](OmicsProcessing.md) - The methods and processes used to generate omics data from a biosample or organism.

## Referenced by class


## Attributes


### Own

 * [biosample processing➞has input](biosample_processing_has_input.md)  <sub>0..*</sub>
    * range: [Biosample](Biosample.md)

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

 * [biosample processing➞has input](biosample_processing_has_input.md)  <sub>0..*</sub>
    * range: [Biosample](Biosample.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | material processing |
| **Broad Mappings:** | | OBI:0000094 |

