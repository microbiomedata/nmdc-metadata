
# Type: named thing


a databased entity or concept/class

URI: [nmdc:NamedThing](https://microbiomedata/meta/NamedThing)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing&#124;id:string%20%3F;name:string%20%3F;description:string%20%3F;alternate_identifiers:string%20*]^-\[Study],%20\[NamedThing]^-\[Project],%20\[NamedThing]^-\[OntologyClass],%20\[NamedThing]^-\[Characteristic],%20\[NamedThing]^-\[Biosample])

## Children

 * [Biosample](Biosample.md) - A material sample. May be environmental (encompassing many organisms) or isolate or tissue
 * [Characteristic](Characteristic.md) - A characteristic of a biosample. Examples: depth, habitat, material, ... For NMDC, characteristics SHOULD be mapped to fields within a MIxS template
 * [OntologyClass](OntologyClass.md)
 * [Project](Project.md) - An individual or collaborative enterprise that is carefully planned and designed to achieve a particular aim.
 * [Study](Study.md) - A detailed investigation that  defines the overall goal of a research proposal.  It contains the list of sequencing projects that are part of the original proposal. (see https://gold.jgi.doe.gov/resources/project_help_doc.pdf)

## Referenced by class


## Attributes


### Own

 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](types/String.md)
 * [id](id.md)  <sub>OPT</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](types/String.md)
