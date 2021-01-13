---
parent: Classes
title: nmdc:FunctionalAnnotationTerm
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: FunctionalAnnotationTerm


Abstract grouping class for any term/descriptor that can be applied to a functional unit of a genome (protein, ncRNA, complex).

URI: [nmdc:FunctionalAnnotationTerm](https://microbiomedata/meta/FunctionalAnnotationTerm)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Reaction],[Pathway],[OrthologyGroup],[OntologyClass],[FunctionalAnnotation]-%20has%20function%200..1%3E[FunctionalAnnotationTerm%7Cid(i):string;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20%2A],[FunctionalAnnotationTerm]%5E-[Reaction],[FunctionalAnnotationTerm]%5E-[Pathway],[FunctionalAnnotationTerm]%5E-[OrthologyGroup],[OntologyClass]%5E-[FunctionalAnnotationTerm],[FunctionalAnnotation])

---


## Parents

 *  is_a: [OntologyClass](OntologyClass.md)

## Children

 * [OrthologyGroup](OrthologyGroup.md) - A set of genes or gene products in which all members are orthologous
 * [Pathway](Pathway.md) - A pathway is a sequence of steps/reactions carried out by an organism or community of organisms
 * [Reaction](Reaction.md) - An individual biochemical transformation carried out by a functional unit of an organism, in which a collection of substrates are transformed into a collection of products. Can also represent transporters

## Referenced by class

 *  **[FunctionalAnnotation](FunctionalAnnotation.md)** *[functional annotation➞has function](functional_annotation_has_function.md)*  <sub>OPT</sub>  **[FunctionalAnnotationTerm](FunctionalAnnotationTerm.md)**
 *  **None** *[has function](has_function.md)*  <sub>OPT</sub>  **[FunctionalAnnotationTerm](FunctionalAnnotationTerm.md)**

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
| **Aliases:** | | function |
|  | | functional annotation |

