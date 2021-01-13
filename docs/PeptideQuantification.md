---
parent: Classes
title: nmdc:PeptideQuantification
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: PeptideQuantification


This is used to link a metaproteomics analysis workflow to a specific peptide sequence and related information

URI: [nmdc:PeptideQuantification](https://microbiomedata/meta/PeptideQuantification)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[GeneProduct]%3Call%20proteins%200..%2A-++[PeptideQuantification%7Cpeptide_sequence:string%20%3F;min_q_value:float%20%3F;peptide_spectral_count:integer%20%3F;peptide_sum_masic_abundance:integer%20%3F],[GeneProduct]%3Cbest%20protein%200..1-++[PeptideQuantification],[MetaproteomicsAnalysisActivity]++-%20has%20peptide%20quantifications%200..%2A%3E[PeptideQuantification],[MetaproteomicsAnalysisActivity],[GeneProduct])

---


## Referenced by class

 *  **None** *[has peptide quantifications](has_peptide_quantifications.md)*  <sub>0..*</sub>  **[PeptideQuantification](PeptideQuantification.md)**
 *  **[MetaproteomicsAnalysisActivity](MetaproteomicsAnalysisActivity.md)** *[metaproteomics analysis activity➞has peptide quantifications](metaproteomics_analysis_activity_has_peptide_quantifications.md)*  <sub>0..*</sub>  **[PeptideQuantification](PeptideQuantification.md)**

## Attributes


### Own

 * [peptide quantification➞all proteins](peptide_quantification_all_proteins.md)  <sub>0..*</sub>
    * Description: the list of protein identifiers that are associated with the peptide sequence
    * range: [GeneProduct](GeneProduct.md)
 * [peptide quantification➞best protein](peptide_quantification_best_protein.md)  <sub>OPT</sub>
    * Description: the specific protein identifier most correctly associated with the peptide sequence
    * range: [GeneProduct](GeneProduct.md)
 * [peptide quantification➞min_q_value](peptide_quantification_min_q_value.md)  <sub>OPT</sub>
    * Description: smallest Q-Value associated with the peptide sequence as provided by MSGFPlus tool
    * range: [Float](types/Float.md)
 * [peptide quantification➞peptide sequence](peptide_quantification_peptide_sequence.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [peptide quantification➞peptide_spectral_count](peptide_quantification_peptide_spectral_count.md)  <sub>OPT</sub>
    * Description: sum of filter passing MS2 spectra associated with the peptide sequence within a given LC-MS/MS data file
    * range: [Integer](types/Integer.md)
 * [peptide quantification➞peptide_sum_masic_abundance](peptide_quantification_peptide_sum_masic_abundance.md)  <sub>OPT</sub>
    * Description: combined MS1 extracted ion chromatograms derived from MS2 spectra associated with the peptide sequence from a given LC-MS/MS data file using the MASIC tool
    * range: [Integer](types/Integer.md)

### Domain for slot:

 * [peptide quantification➞all proteins](peptide_quantification_all_proteins.md)  <sub>0..*</sub>
    * Description: the list of protein identifiers that are associated with the peptide sequence
    * range: [GeneProduct](GeneProduct.md)
 * [peptide quantification➞best protein](peptide_quantification_best_protein.md)  <sub>OPT</sub>
    * Description: the specific protein identifier most correctly associated with the peptide sequence
    * range: [GeneProduct](GeneProduct.md)
 * [peptide quantification➞min_q_value](peptide_quantification_min_q_value.md)  <sub>OPT</sub>
    * Description: smallest Q-Value associated with the peptide sequence as provided by MSGFPlus tool
    * range: [Float](types/Float.md)
 * [peptide quantification➞peptide sequence](peptide_quantification_peptide_sequence.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [peptide quantification➞peptide_spectral_count](peptide_quantification_peptide_spectral_count.md)  <sub>OPT</sub>
    * Description: sum of filter passing MS2 spectra associated with the peptide sequence within a given LC-MS/MS data file
    * range: [Integer](types/Integer.md)
 * [peptide quantification➞peptide_sum_masic_abundance](peptide_quantification_peptide_sum_masic_abundance.md)  <sub>OPT</sub>
    * Description: combined MS1 extracted ion chromatograms derived from MS2 spectra associated with the peptide sequence from a given LC-MS/MS data file using the MASIC tool
    * range: [Integer](types/Integer.md)
