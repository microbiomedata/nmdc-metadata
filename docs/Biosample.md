
# Type: biosample


A material sample. May be environmental (encompassing many organisms) or isolate or tissue

URI: [nmdc:Biosample](https://microbiomedata/meta/Biosample)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Project]<involved%20in%200..*-++\[Biosample&#124;id:string%20%3F;name:string%20%3F;alternate_identifiers:string%20*;description(i):string%20%3F],%20\[Annotation]<annotations%200..*-++\[Biosample],%20\[NamedThing]^-\[Biosample])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **None** *[input](input.md)*  <sub>0..*</sub>  **[Biosample](Biosample.md)**
 *  **None** *[output](output.md)*  <sub>0..*</sub>  **[Biosample](Biosample.md)**

## Attributes


### Own

 * [annotations](annotations.md)  <sub>0..*</sub>
    * Description: Zero to many annotations on a sample
    * range: [Annotation](Annotation.md)
 * [biosample➞alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [biosample➞id](biosample_id.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [biosample➞name](biosample_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [involved in](involved_in.md)  <sub>0..*</sub>
    * Description: Links a biosample to a project that makes use of it.
    * range: [Project](Project.md)

### Inherited from named thing:

 * [id](id.md)  <sub>OPT</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
    * inherited from: None
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](types/String.md)
    * inherited from: None
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](types/String.md)
    * inherited from: None
 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](types/String.md)
    * inherited from: None

### Domain for slot:

 * [annotations](annotations.md)  <sub>0..*</sub>
    * Description: Zero to many annotations on a sample
    * range: [Annotation](Annotation.md)
 * [biosample➞alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [biosample➞id](biosample_id.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [biosample➞name](biosample_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [involved in](involved_in.md)  <sub>0..*</sub>
    * Description: Links a biosample to a project that makes use of it.
    * range: [Project](Project.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | sample |
|  | | material sample |

