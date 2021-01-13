---
parent: Classes
title: nmdc:MetaboliteQuantification
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: MetaboliteQuantification


This is used to link a metabolomics analysis workflow to a specific metabolite

URI: [nmdc:MetaboliteQuantification](https://microbiomedata/meta/MetaboliteQuantification)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MetabolomicsAnalysisActivity],[ChemicalEntity]%3Cmetabolite%20quantified%200..1-%20[MetaboliteQuantification%7Chighest_similarity_score:float%20%3F],[MetabolomicsAnalysisActivity]++-%20has%20metabolite%20quantifications%200..%2A%3E[MetaboliteQuantification],[ChemicalEntity])

---


## Referenced by class

 *  **None** *[has metabolite quantifications](has_metabolite_quantifications.md)*  <sub>0..*</sub>  **[MetaboliteQuantification](MetaboliteQuantification.md)**
 *  **[MetabolomicsAnalysisActivity](MetabolomicsAnalysisActivity.md)** *[metabolomics analysis activity➞has metabolite quantifications](metabolomics_analysis_activity_has_metabolite_quantifications.md)*  <sub>0..*</sub>  **[MetaboliteQuantification](MetaboliteQuantification.md)**

## Attributes


### Own

 * [metabolite quantification➞highest similarity score](metabolite_quantification_highest_similarity_score.md)  <sub>OPT</sub>
    * Description: TODO: Yuri to fill in
    * range: [Float](types/Float.md)
 * [metabolite quantification➞metabolite quantified](metabolite_quantification_metabolite_quantified.md)  <sub>OPT</sub>
    * Description: the specific metabolite identifier
    * range: [ChemicalEntity](ChemicalEntity.md)

### Domain for slot:

 * [metabolite quantification➞highest similarity score](metabolite_quantification_highest_similarity_score.md)  <sub>OPT</sub>
    * Description: TODO: Yuri to fill in
    * range: [Float](types/Float.md)
 * [metabolite quantification➞metabolite quantified](metabolite_quantification_metabolite_quantified.md)  <sub>OPT</sub>
    * Description: the specific metabolite identifier
    * range: [ChemicalEntity](ChemicalEntity.md)
