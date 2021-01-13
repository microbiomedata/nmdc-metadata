---
parent: Classes
title: nmdc:OrthologyGroup
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: OrthologyGroup


A set of genes or gene products in which all members are orthologous

URI: [nmdc:OrthologyGroup](https://microbiomedata/meta/OrthologyGroup)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[FunctionalAnnotationTerm]%5E-[OrthologyGroup%7Cid(i):string;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20%2A],[FunctionalAnnotationTerm])

---


## Identifier prefixes

 * KEGG.ORTHOLOGY
 * EGGNOG
 * PFAM
 * TIGRFAM
 * SUPFAM
 * CATH
 * PANTHER.FAMILY

## Parents

 *  is_a: [FunctionalAnnotationTerm](FunctionalAnnotationTerm.md) - Abstract grouping class for any term/descriptor that can be applied to a functional unit of a genome (protein, ncRNA, complex).

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
| **Exact Mappings:** | | biolink:GeneFamily |

