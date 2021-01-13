---
parent: Slots
title: nmdc:genome_feature_end
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: genome_feature_end


The end of the feature in positive 1-based integer coordinates

URI: [nmdc:genome_feature_end](https://microbiomedata/meta/genome_feature_end)

## Domain and Range

[GenomeFeature](GenomeFeature.md) ->  <sub>REQ</sub> [Integer](types/Integer.md)

## Parents

 *  is_a: [gff coordinate](gff_coordinate.md)

## Children


## Used by

 * [GenomeFeature](GenomeFeature.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | - "constraint: end > start" - "For features that cross the origin of a circular feature,  end = the position of the end + the length of the landmark feature." |
| **Close Mappings:** | | biolink:end_interbase_coordinate |

