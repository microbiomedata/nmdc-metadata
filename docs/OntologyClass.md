# Class: ontology class




URI: [nmdc:OntologyClass](https://microbiomedata/meta/OntologyClass)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ControlledTermValue]++-%20instance%20of%200..1>\[OntologyClass|id(i):string%20%3F;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20*],%20\[NamedThing]^-\[OntologyClass])
## Inheritance

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class
## Children

## Used by

 *  **[ControlledTermValue](ControlledTermValue.md)** *[instance of](instance_of.md)*  <sub>OPT</sub>  **[OntologyClass](OntologyClass.md)**
## Fields

 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](String.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](String.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [id](id.md)  <sub>OPT</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](String.md)
    * inherited from: [NamedThing](NamedThing.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](String.md)
    * inherited from: [NamedThing](NamedThing.md)
