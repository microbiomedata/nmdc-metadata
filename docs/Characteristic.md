
# Class: characteristic


A characteristic of a biosample. Examples: depth, habitat, material, ... For NMDC, characteristics SHOULD be mapped to fields within a MIxS template

URI: [nmdc:Characteristic](https://microbiomedata/meta/Characteristic)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Annotation]++-%20has%20characteristic%200..1>\[Characteristic|description:string%20%3F;id(i):string;name(i):string%20%3F;alternate_identifiers(i):string%20*],%20\[NamedThing]^-\[Characteristic])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[Annotation](Annotation.md)** *[has characteristic](has_characteristic.md)*  <sub>OPT</sub>  **[Characteristic](Characteristic.md)**

## Attributes


### Own

 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](String.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](String.md)
    * inherited from: None
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](String.md)
    * inherited from: None
 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](String.md)
    * inherited from: None
