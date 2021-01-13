
# Type: gff_coordinate


A positive 1-based integer coordinate indicating start or end

URI: [nmdc:gff_coordinate](https://microbiomedata/meta/gff_coordinate)


## Domain and Range

None ->  <sub>OPT</sub> [Integer](types/Integer.md)

## Parents


## Children

 *  [end](end.md)
 *  [genome feature➞end](genome_feature_end.md)
 *  [genome feature➞start](genome_feature_start.md)
 *  [start](start.md)

## Used by


## Other properties

|  |  |  |
| --- | --- | --- |
| **Comments:** | | For features that cross the origin of a circular feature (e.g. most bacterial genomes, plasmids, and some viral genomes), the requirement for start to be less than or equal to end is satisfied by making end = the position of the end + the length of the landmark feature. |

