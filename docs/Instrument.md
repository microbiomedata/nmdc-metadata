---
parent: Classes
title: nmdc:Instrument
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: Instrument


A material entity that is designed to perform a function in a scientific investigation, but is not a reagent[OBI].

URI: [nmdc:Instrument](https://microbiomedata/meta/Instrument)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[MetaproteomicsAnalysisActivity],[MetabolomicsAnalysisActivity],[MetabolomicsAnalysisActivity]-%20used%200..1%3E[Instrument%7Cid(i):string;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20%2A],[MetaproteomicsAnalysisActivity]-%20used%200..1%3E[Instrument],[NamedThing]%5E-[Instrument])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[MetabolomicsAnalysisActivity](MetabolomicsAnalysisActivity.md)** *[metabolomics analysis activity➞used](metabolomics_analysis_activity_used.md)*  <sub>OPT</sub>  **[Instrument](Instrument.md)**
 *  **[MetaproteomicsAnalysisActivity](MetaproteomicsAnalysisActivity.md)** *[metaproteomics analysis activity➞used](metaproteomics_analysis_activity_used.md)*  <sub>OPT</sub>  **[Instrument](Instrument.md)**

## Attributes


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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | device |
| **Exact Mappings:** | | OBI:0000485 |

