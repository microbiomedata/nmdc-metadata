---
parent: Classes
title: nmdc:MetagenomeAssembly
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: MetagenomeAssembly




URI: [nmdc:MetagenomeAssembly](https://microbiomedata/meta/MetagenomeAssembly)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WorkflowExecutionActivity],[WorkflowExecutionActivity]%5E-[MetagenomeAssembly%7Casm_score:float%20%3F;scaffolds:float%20%3F;scaf_logsum:float%20%3F;scaf_powsum:float%20%3F;scaf_max:float%20%3F;scaf_bp:float%20%3F;scaf_N50:float%20%3F;scaf_N90:float%20%3F;scaf_L50:float%20%3F;scaf_L90:float%20%3F;scaf_n_gt50K:float%20%3F;scaf_l_gt50K:float%20%3F;scaf_pct_gt50K:float%20%3F;contigs:float%20%3F;contig_bp:float%20%3F;ctg_N50:float%20%3F;ctg_L50:float%20%3F;ctg_N90:float%20%3F;ctg_L90:float%20%3F;ctg_logsum:float%20%3F;ctg_powsum:float%20%3F;ctg_max:float%20%3F;gap_pct:float%20%3F;gc_std:float%20%3F;gc_avg:float%20%3F;num_input_reads:float%20%3F;num_aligned_reads:float%20%3F;execution_resource(i):string%20%3F;git_url(i):string%20%3F;has_input(i):string%20%2A;has_output(i):string%20%2A;activity_id(i):string;started_at_time(i):string%20%3F;ended_at_time(i):string%20%3F;used(i):string%20%3F],[Agent],[Activity])

---


## Parents

 *  is_a: [WorkflowExecutionActivity](WorkflowExecutionActivity.md) - Represents an instance of an execution of a particular workflow

## Attributes


### Own

 * [asm_score](asm_score.md)  <sub>OPT</sub>
    * Description: A score for comparing metagenomic assembly quality from same sample.
    * range: [Float](types/Float.md)
 * [contig_bp](contig_bp.md)  <sub>OPT</sub>
    * Description: Total size in bp of all contigs.
    * range: [Float](types/Float.md)
 * [contigs](contigs.md)  <sub>OPT</sub>
    * Description: The sum of the (length*log(length)) of all contigs, times some constant.  Increase the contiguity, the score will increase
    * range: [Float](types/Float.md)
 * [ctg_L50](ctg_L50.md)  <sub>OPT</sub>
    * Description: Given a set of contigs, the N50 is defined as the sequence length of the shortest contig at 50% of the total genome length.
    * range: [Float](types/Float.md)
 * [ctg_L90](ctg_L90.md)  <sub>OPT</sub>
    * Description: The L90 statistic is less than or equal to the L50 statistic; it is the length for which the collection of all contigs of that length or longer contains at least 90% of the sum of the lengths of all contigs.
    * range: [Float](types/Float.md)
 * [ctg_N50](ctg_N50.md)  <sub>OPT</sub>
    * Description: Given a set of contigs, each with its own length, the L50 count is defined as the smallest number of contigs whose length sum makes up half of genome size.
    * range: [Float](types/Float.md)
 * [ctg_N90](ctg_N90.md)  <sub>OPT</sub>
    * Description: Given a set of contigs, each with its own length, the L90 count is defined as the smallest number of contigs whose length sum makes up 90% of genome size.
    * range: [Float](types/Float.md)
 * [ctg_logsum](ctg_logsum.md)  <sub>OPT</sub>
    * Description: Maximum contig length.
    * range: [Float](types/Float.md)
 * [ctg_max](ctg_max.md)  <sub>OPT</sub>
    * Description: Maximum contig length.
    * range: [Float](types/Float.md)
 * [ctg_powsum](ctg_powsum.md)  <sub>OPT</sub>
    * Description: Powersum of all contigs is the same as logsum except that it uses the sum of (length*(length^P)) for some power P (default P=0.25).
    * range: [Float](types/Float.md)
 * [gap_pct](gap_pct.md)  <sub>OPT</sub>
    * Description: The gap size percentage of all scaffolds.
    * range: [Float](types/Float.md)
 * [gc_avg](gc_avg.md)  <sub>OPT</sub>
    * Description: Average of GC content of all contigs.
    * range: [Float](types/Float.md)
 * [gc_std](gc_std.md)  <sub>OPT</sub>
    * Description: Standard deviation of GC content of all contigs.
    * range: [Float](types/Float.md)
 * [num_aligned_reads](num_aligned_reads.md)  <sub>OPT</sub>
    * Description: The sequence count number of input reads aligned to assembled contigs.
    * range: [Float](types/Float.md)
 * [num_input_reads](num_input_reads.md)  <sub>OPT</sub>
    * Description: The sequence count number of input reads for assembly.
    * range: [Float](types/Float.md)
 * [scaf_L50](scaf_L50.md)  <sub>OPT</sub>
    * Description: Given a set of scaffolds, the N50 is defined as the sequence length of the shortest scaffold at 50% of the total genome length.
    * range: [Float](types/Float.md)
 * [scaf_L90](scaf_L90.md)  <sub>OPT</sub>
    * Description: The L90 statistic is less than or equal to the L50 statistic; it is the length for which the collection of all scaffolds of that length or longer contains at least 90% of the sum of the lengths of all scaffolds.
    * range: [Float](types/Float.md)
 * [scaf_N50](scaf_N50.md)  <sub>OPT</sub>
    * Description: Given a set of scaffolds, each with its own length, the L50 count is defined as the smallest number of scaffolds whose length sum makes up half of genome size.
    * range: [Float](types/Float.md)
 * [scaf_N90](scaf_N90.md)  <sub>OPT</sub>
    * Description: Given a set of scaffolds, each with its own length, the L90 count is defined as the smallest number of scaffolds whose length sum makes up 90% of genome size.
    * range: [Float](types/Float.md)
 * [scaf_bp](scaf_bp.md)  <sub>OPT</sub>
    * Description: Total size in bp of all scaffolds.
    * range: [Float](types/Float.md)
 * [scaf_l_gt50K](scaf_l_gt50K.md)  <sub>OPT</sub>
    * Description: Total size in bp of all scaffolds greater than 50 KB.
    * range: [Float](types/Float.md)
 * [scaf_logsum](scaf_logsum.md)  <sub>OPT</sub>
    * Description: The sum of the (length*log(length)) of all scaffolds, times some constant.  Increase the contiguity, the score will increase
    * range: [Float](types/Float.md)
 * [scaf_max](scaf_max.md)  <sub>OPT</sub>
    * Description: Maximum scaffold length.
    * range: [Float](types/Float.md)
 * [scaf_n_gt50K](scaf_n_gt50K.md)  <sub>OPT</sub>
    * Description: Total sequence count of scaffolds greater than 50 KB.
    * range: [Float](types/Float.md)
 * [scaf_pct_gt50K](scaf_pct_gt50K.md)  <sub>OPT</sub>
    * Description: Total sequence size percentage of scaffolds greater than 50 KB.
    * range: [Float](types/Float.md)
 * [scaf_powsum](scaf_powsum.md)  <sub>OPT</sub>
    * Description: Powersum of all scaffolds is the same as logsum except that it uses the sum of (length*(length^P)) for some power P (default P=0.25).
    * range: [Float](types/Float.md)
 * [scaffolds](scaffolds.md)  <sub>OPT</sub>
    * Description: Total sequence count of all scaffolds.
    * range: [Float](types/Float.md)

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

## Other properties

|  |  |  |
| --- | --- | --- |
| **In Subsets:** | | workflow subset |

