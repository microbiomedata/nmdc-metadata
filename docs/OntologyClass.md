
# Class: ontology class




URI: [nmdc:OntologyClass](https://microbiomedata/meta/OntologyClass)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]^-\[OntologyClass|id(i):string%20%3F;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20*])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **None** *[instance of](instance_of.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**

## Attributes


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
