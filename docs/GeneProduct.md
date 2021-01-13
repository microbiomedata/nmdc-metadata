---
parent: Classes
title: nmdc:GeneProduct
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: GeneProduct


A molecule encoded by a gene that has an evolved function

URI: [nmdc:GeneProduct](https://microbiomedata/meta/GeneProduct)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[ProteinQuantification],[PeptideQuantification],[GenomeFeature],[FunctionalAnnotation]++-%20subject%200..1%3E[GeneProduct],[GenomeFeature]++-%20encodes%200..1%3E[GeneProduct],[PeptideQuantification]++-%20all%20proteins%200..%2A%3E[GeneProduct],[PeptideQuantification]++-%20best%20protein%200..1%3E[GeneProduct],[ProteinQuantification]++-%20all%20proteins%200..%2A%3E[GeneProduct],[ProteinQuantification]++-%20best%20protein%200..1%3E[GeneProduct],[FunctionalAnnotation])

---


## Identifier prefixes

 * UniProtKB
 * gtpo
 * PR

## Referenced by class

 *  **None** *[all proteins](all_proteins.md)*  <sub>0..*</sub>  **[GeneProduct](GeneProduct.md)**
 *  **None** *[best protein](best_protein.md)*  <sub>OPT</sub>  **[GeneProduct](GeneProduct.md)**
 *  **None** *[encodes](encodes.md)*  <sub>OPT</sub>  **[GeneProduct](GeneProduct.md)**
 *  **[FunctionalAnnotation](FunctionalAnnotation.md)** *[functional annotation➞subject](functional_annotation_subject.md)*  <sub>OPT</sub>  **[GeneProduct](GeneProduct.md)**
 *  **[GenomeFeature](GenomeFeature.md)** *[genome feature➞encodes](genome_feature_encodes.md)*  <sub>OPT</sub>  **[GeneProduct](GeneProduct.md)**
 *  **[PeptideQuantification](PeptideQuantification.md)** *[peptide quantification➞all proteins](peptide_quantification_all_proteins.md)*  <sub>0..*</sub>  **[GeneProduct](GeneProduct.md)**
 *  **[PeptideQuantification](PeptideQuantification.md)** *[peptide quantification➞best protein](peptide_quantification_best_protein.md)*  <sub>OPT</sub>  **[GeneProduct](GeneProduct.md)**
 *  **[ProteinQuantification](ProteinQuantification.md)** *[protein quantification➞all proteins](protein_quantification_all_proteins.md)*  <sub>0..*</sub>  **[GeneProduct](GeneProduct.md)**
 *  **[ProteinQuantification](ProteinQuantification.md)** *[protein quantification➞best protein](protein_quantification_best_protein.md)*  <sub>OPT</sub>  **[GeneProduct](GeneProduct.md)**
 *  **None** *[subject](subject.md)*  <sub>OPT</sub>  **[GeneProduct](GeneProduct.md)**

## Attributes


## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | we may include a more general gene product class in future to allow for ncRNA annotation |
| **Exact Mappings:** | | biolink:GeneProduct |

