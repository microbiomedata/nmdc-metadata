
# Class: study


A detailed investigation that  defines the overall goal of a research proposal.  It contains the list of sequencing projects that are part of the original proposal. (see https://gold.jgi.doe.gov/resources/project_help_doc.pdf)

URI: [nmdc:Study](https://microbiomedata/meta/Study)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Project]++-%20part%20of%200..*>\[Study|id:string%20%3F;name:string%20%3F;alternate_identifiers:string%20*;description(i):string%20%3F],%20\[NamedThing]^-\[Study])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[Project](Project.md)** *[part of](part_of.md)*  <sub>0..*</sub>  **[Study](Study.md)**

## Attributes


### Own

 * [alternate identifiers](study_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](String.md)
 * [id](study_id.md)  <sub>OPT</sub>
    * range: [String](String.md)
 * [name](study_name.md)  <sub>OPT</sub>
    * range: [String](String.md)

### Inherited from named thing:

 * [id](id.md)  <sub>OPT</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](String.md)
    * inherited from: None
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](String.md)
    * inherited from: None
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](String.md)
    * inherited from: None
 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](String.md)
    * inherited from: None

### Domain for slot:

 * [alternate identifiers](study_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](String.md)
 * [id](study_id.md)  <sub>OPT</sub>
    * range: [String](String.md)
 * [name](study_name.md)  <sub>OPT</sub>
    * range: [String](String.md)
