---
parent: Classes
title: nmdc:ProteinQuantification
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: ProteinQuantification


This is used to link a metaproteomics analysis workflow to a specific protein

URI: [nmdc:ProteinQuantification](https://microbiomedata/meta/ProteinQuantification)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GeneProduct]%3Call%20proteins%200..%2A-++[ProteinQuantification%7Cpeptide_sequence_count:integer%20%3F;protein_spectral_count:integer%20%3F;protein_sum_masic_abundance:integer%20%3F],[GeneProduct]%3Cbest%20protein%200..1-++[ProteinQuantification],[GeneProduct])

---


## Referenced by class


## Attributes


### Own

 * [protein quantification➞all proteins](protein_quantification_all_proteins.md)  <sub>0..*</sub>
    * Description: the grouped list of protein identifiers associated with the peptide sequences that were grouped to a best protein
    * range: [GeneProduct](GeneProduct.md)
 * [protein quantification➞best protein](protein_quantification_best_protein.md)  <sub>OPT</sub>
    * Description: the specific protein identifier most correctly grouped to its associated peptide sequences
    * range: [GeneProduct](GeneProduct.md)
 * [protein quantification➞peptide_sequence_count](protein_quantification_peptide_sequence_count.md)  <sub>OPT</sub>
    * Description: count of peptide sequences grouped to the best_protein
    * range: [Integer](types/Integer.md)
 * [protein quantification➞protein_spectral_count](protein_quantification_protein_spectral_count.md)  <sub>OPT</sub>
    * Description: sum of filter passing MS2 spectra associated with the best protein within a given LC-MS/MS data file
    * range: [Integer](types/Integer.md)
 * [protein quantification➞protein_sum_masic_abundance](protein_quantification_protein_sum_masic_abundance.md)  <sub>OPT</sub>
    * Description: combined MS1 extracted ion chromatograms derived from MS2 spectra associated with the best protein from a given LC-MS/MS data file using the MASIC tool
    * range: [Integer](types/Integer.md)

### Domain for slot:

 * [protein quantification➞all proteins](protein_quantification_all_proteins.md)  <sub>0..*</sub>
    * Description: the grouped list of protein identifiers associated with the peptide sequences that were grouped to a best protein
    * range: [GeneProduct](GeneProduct.md)
 * [protein quantification➞best protein](protein_quantification_best_protein.md)  <sub>OPT</sub>
    * Description: the specific protein identifier most correctly grouped to its associated peptide sequences
    * range: [GeneProduct](GeneProduct.md)
 * [protein quantification➞peptide_sequence_count](protein_quantification_peptide_sequence_count.md)  <sub>OPT</sub>
    * Description: count of peptide sequences grouped to the best_protein
    * range: [Integer](types/Integer.md)
 * [protein quantification➞protein_spectral_count](protein_quantification_protein_spectral_count.md)  <sub>OPT</sub>
    * Description: sum of filter passing MS2 spectra associated with the best protein within a given LC-MS/MS data file
    * range: [Integer](types/Integer.md)
 * [protein quantification➞protein_sum_masic_abundance](protein_quantification_protein_sum_masic_abundance.md)  <sub>OPT</sub>
    * Description: combined MS1 extracted ion chromatograms derived from MS2 spectra associated with the best protein from a given LC-MS/MS data file using the MASIC tool
    * range: [Integer](types/Integer.md)
