
# Type: project


An individual or collaborative enterprise that is carefully planned and designed to achieve a particular aim.

URI: [nmdc:Project](https://microbiomedata/meta/Project)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Study]<part%20of%200..*-++\[Project&#124;id:string%20%3F;name:string%20%3F;alternate_identifiers:string%20*;description(i):string%20%3F],%20\[Biosample]++-%20involved%20in%200..*>\[Project],%20\[NamedThing]^-\[Project])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[Biosample](Biosample.md)** *[involved in](involved_in.md)*  <sub>0..*</sub>  **[Project](Project.md)**

## Attributes


### Own

 * [part of](part_of.md)  <sub>0..*</sub>
    * Description: Linds a resource to another resource that either logically or physically includes it.
    * range: [Study](Study.md)
 * [project➞alternate identifiers](project_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [project➞id](project_id.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [project➞name](project_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

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

 * [part of](part_of.md)  <sub>0..*</sub>
    * Description: Linds a resource to another resource that either logically or physically includes it.
    * range: [Study](Study.md)
 * [project➞alternate identifiers](project_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [project➞id](project_id.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [project➞name](project_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | research project |

