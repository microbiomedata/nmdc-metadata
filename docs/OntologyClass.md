---
parent: Classes
title: nmdc:OntologyClass
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: OntologyClass




URI: [nmdc:OntologyClass](https://microbiomedata/meta/OntologyClass)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GenomeFeature]-%20type%200..1%3E[OntologyClass%7Cid(i):string;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20%2A],[ControlledTermValue]++-%20term%200..1%3E[OntologyClass],[OntologyClass]%5E-[FunctionalAnnotationTerm],[OntologyClass]%5E-[EnvironmentalMaterialTerm],[OntologyClass]%5E-[ChemicalEntity],[NamedThing]%5E-[OntologyClass],[NamedThing],[GenomeFeature],[FunctionalAnnotationTerm],[EnvironmentalMaterialTerm],[ControlledTermValue],[ChemicalEntity])

---


## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Children

 * [ChemicalEntity](ChemicalEntity.md) - An atom or molecule that can be represented with a chemical formula. Include lipids, glycans, natural products, drugs. There may be different terms for distinct acid-base forms, protonation states
 * [EnvironmentalMaterialTerm](EnvironmentalMaterialTerm.md)
 * [FunctionalAnnotationTerm](FunctionalAnnotationTerm.md) - Abstract grouping class for any term/descriptor that can be applied to a functional unit of a genome (protein, ncRNA, complex).

## Referenced by class

 *  **[GenomeFeature](GenomeFeature.md)** *[genome feature➞type](genome_feature_type.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
 *  **[ControlledTermValue](ControlledTermValue.md)** *[term](term.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**

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
