---
parent: Classes
title: nmdc:MetaproteomicsAnalysisActivity
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: MetaproteomicsAnalysisActivity




URI: [nmdc:MetaproteomicsAnalysisActivity](https://microbiomedata/meta/MetaproteomicsAnalysisActivity)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowExecutionActivity],[PeptideQuantification],[PeptideQuantification]%3Chas%20peptide%20quantifications%200..%2A-++[MetaproteomicsAnalysisActivity%7Cexecution_resource(i):string%20%3F;git_url(i):string%20%3F;has_input(i):string%20%2A;has_output(i):string%20%2A;activity_id(i):string;started_at_time(i):string%20%3F;ended_at_time(i):string%20%3F],[Instrument]%3Cused%200..1-%20[MetaproteomicsAnalysisActivity],[WorkflowExecutionActivity]%5E-[MetaproteomicsAnalysisActivity],[Instrument],[Agent],[Activity])

---


## Parents

 *  is_a: [WorkflowExecutionActivity](WorkflowExecutionActivity.md) - Represents an instance of an execution of a particular workflow

## Referenced by class


## Attributes


### Own

 * [metaproteomics analysis activity➞has peptide quantifications](metaproteomics_analysis_activity_has_peptide_quantifications.md)  <sub>0..*</sub>
    * range: [PeptideQuantification](PeptideQuantification.md)
 * [metaproteomics analysis activity➞used](metaproteomics_analysis_activity_used.md)  <sub>OPT</sub>
    * Description: The instrument used to collect the data used in the analysis
    * range: [Instrument](Instrument.md)

### Inherited from activity:

 * [activity id](activity_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [started at time](started_at_time.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [ended at time](ended_at_time.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [was associated with](was_associated_with.md)  <sub>OPT</sub>
    * range: [Agent](Agent.md)
 * [used](used.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from agent:

 * [acted on behalf of](acted_on_behalf_of.md)  <sub>OPT</sub>
    * range: [Agent](Agent.md)
 * [was informed by](was_informed_by.md)  <sub>OPT</sub>
    * range: [Activity](Activity.md)

### Inherited from biosample processing:

 * [biosample processing➞has input](biosample_processing_has_input.md)  <sub>0..*</sub>
    * range: [Biosample](Biosample.md)

### Inherited from omics processing:

 * [omics processing➞part of](omics_processing_part_of.md)  <sub>0..*</sub>
    * range: [Study](Study.md)
 * [omics processing➞has output](omics_processing_has_output.md)  <sub>0..*</sub>
    * range: [DataObject](DataObject.md)
 * [omics type](omics_type.md)  <sub>OPT</sub>
    * Description: The type of omics data
    * range: [ControlledTermValue](ControlledTermValue.md)
    * Example: metatranscriptome None
    * Example: metagenome None
 * [omics processing➞id](omics_processing_id.md)  <sub>REQ</sub>
    * Description: The primary identifier for the omics processing. E.g. GOLD:GpNNNN
    * range: [String](types/String.md)
 * [omics processing➞name](omics_processing_name.md)  <sub>OPT</sub>
    * Description: A human readable name or description of the omics processing.
    * range: [String](types/String.md)
 * [omics processing➞alternate identifiers](omics_processing_alternate_identifiers.md)  <sub>0..*</sub>
    * Description: The same omics processing may have distinct identifiers in different databases (e.g. GOLD and EMSL, as well as NCBI)
    * range: [String](types/String.md)

### Inherited from workflow execution activity:

 * [execution resource](execution_resource.md)  <sub>OPT</sub>
    * Description: Example: NERSC-Cori
    * range: [String](types/String.md)
 * [git url](git_url.md)  <sub>OPT</sub>
    * Description: Example: https://github.com/microbiomedata/mg_annotation/releases/tag/0.1
    * range: [String](types/String.md)

### Domain for slot:

 * [metaproteomics analysis activity➞has peptide quantifications](metaproteomics_analysis_activity_has_peptide_quantifications.md)  <sub>0..*</sub>
    * range: [PeptideQuantification](PeptideQuantification.md)
 * [metaproteomics analysis activity➞used](metaproteomics_analysis_activity_used.md)  <sub>OPT</sub>
    * Description: The instrument used to collect the data used in the analysis
    * range: [Instrument](Instrument.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | workflow subset |

