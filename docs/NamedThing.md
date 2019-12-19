
# Class: named thing


a databased entity or concept/class

URI: [nmdc:NamedThing](https://microbiomedata/meta/NamedThing)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing|id:string;name:string%20%3F;alternate_identifiers:string%20*]^-\[OntologyClass],%20\[NamedThing]^-\[Characteristic],%20\[NamedThing]^-\[Biosample])

## Children

 * [Biosample](Biosample.md) - A material sample. May be environmental (encompassing many organisms) or isolate or tissue
 * [Characteristic](Characteristic.md) - A characteristic of a biosample. Examples: depth, habitat, material, ... For NMDC, characteristics SHOULD be mapped to fields within a MIxS template
 * [OntologyClass](OntologyClass.md)

## Referenced by class


## Attributes


### Own

 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](String.md)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](String.md)
