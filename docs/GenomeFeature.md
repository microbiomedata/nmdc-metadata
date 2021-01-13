---
parent: Classes
title: nmdc:GenomeFeature
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: GenomeFeature


A feature localized to an interval along a genome

URI: [nmdc:GenomeFeature](https://microbiomedata/meta/GenomeFeature)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[OntologyClass],[GeneProduct]%3Cencodes%200..1-++[GenomeFeature%7Cseqid:string;start:integer;end:integer;strand:string%20%3F;phase:integer%20%3F],[OntologyClass]%3Ctype%200..1-%20[GenomeFeature],[GeneProduct])

---


## Referenced by class


## Attributes


### Own

 * [genome feature➞encodes](genome_feature_encodes.md)  <sub>OPT</sub>
    * Description: The gene product encoded by this feature. Typically this is used for a CDS feature or gene feature which will encode a protein. It can also be used by a nc transcript ot gene feature that encoded a ncRNA
    * range: [GeneProduct](GeneProduct.md)
 * [genome feature➞end](genome_feature_end.md)  <sub>REQ</sub>
    * Description: The end of the feature in positive 1-based integer coordinates
    * range: [Integer](types/Integer.md)
 * [genome feature➞phase](genome_feature_phase.md)  <sub>OPT</sub>
    * Description: The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2.
    * range: [Integer](types/Integer.md)
 * [genome feature➞seqid](genome_feature_seqid.md)  <sub>REQ</sub>
    * Description: The ID of the landmark used to establish the coordinate system for the current feature.
    * range: [String](types/String.md)
 * [genome feature➞start](genome_feature_start.md)  <sub>REQ</sub>
    * Description: The start of the feature in positive 1-based integer coordinates
    * range: [Integer](types/Integer.md)
 * [genome feature➞strand](genome_feature_strand.md)  <sub>OPT</sub>
    * Description: The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).
    * range: [String](types/String.md)
 * [genome feature➞type](genome_feature_type.md)  <sub>OPT</sub>
    * Description: A type from the sequence ontology
    * range: [OntologyClass](OntologyClass.md)

### Domain for slot:

 * [genome feature➞encodes](genome_feature_encodes.md)  <sub>OPT</sub>
    * Description: The gene product encoded by this feature. Typically this is used for a CDS feature or gene feature which will encode a protein. It can also be used by a nc transcript ot gene feature that encoded a ncRNA
    * range: [GeneProduct](GeneProduct.md)
 * [genome feature➞end](genome_feature_end.md)  <sub>REQ</sub>
    * Description: The end of the feature in positive 1-based integer coordinates
    * range: [Integer](types/Integer.md)
 * [genome feature➞phase](genome_feature_phase.md)  <sub>OPT</sub>
    * Description: The phase for a coding sequence entity. For example, phase of a CDS as represented in a GFF3 with a value of 0, 1 or 2.
    * range: [Integer](types/Integer.md)
 * [genome feature➞seqid](genome_feature_seqid.md)  <sub>REQ</sub>
    * Description: The ID of the landmark used to establish the coordinate system for the current feature.
    * range: [String](types/String.md)
 * [genome feature➞start](genome_feature_start.md)  <sub>REQ</sub>
    * Description: The start of the feature in positive 1-based integer coordinates
    * range: [Integer](types/Integer.md)
 * [genome feature➞strand](genome_feature_strand.md)  <sub>OPT</sub>
    * Description: The strand on which a feature is located. Has a value of '+' (sense strand or forward strand) or '-' (anti-sense strand or reverse strand).
    * range: [String](types/String.md)
 * [genome feature➞type](genome_feature_type.md)  <sub>OPT</sub>
    * Description: A type from the sequence ontology
    * range: [OntologyClass](OntologyClass.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | corresponds to an entry in GFF3 |
| **See also:** | | https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md |

