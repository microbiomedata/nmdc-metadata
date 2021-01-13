---
parent: Classes
title: nmdc:Pathway
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: Pathway


A pathway is a sequence of steps/reactions carried out by an organism or community of organisms

URI: [nmdc:Pathway](https://microbiomedata/meta/Pathway)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Reaction],[Reaction]%3Chas_part%200..%2A-%20[Pathway%7Cid(i):string;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20%2A],[FunctionalAnnotationTerm]%5E-[Pathway],[FunctionalAnnotationTerm])

---


## Identifier prefixes

 * KEGG.PATHWAY
 * COG

## Parents

 *  is_a: [FunctionalAnnotationTerm](FunctionalAnnotationTerm.md) - Abstract grouping class for any term/descriptor that can be applied to a functional unit of a genome (protein, ncRNA, complex).

## Referenced by class


## Attributes


### Own

 * [pathway➞has_part](pathway_has_part.md)  <sub>0..*</sub>
    * Description: A pathway can be broken down to a series of reaction step
    * range: [Reaction](Reaction.md)

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

 * [pathway➞has_part](pathway_has_part.md)  <sub>0..*</sub>
    * Description: A pathway can be broken down to a series of reaction step
    * range: [Reaction](Reaction.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | biological process |
|  | | metabolic pathway |
|  | | signaling pathway |
| **Exact Mappings:** | | biolink:Pathway |

