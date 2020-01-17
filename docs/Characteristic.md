
# Type: characteristic


A characteristic of a biosample. Examples: depth, habitat, material, ... For NMDC, characteristics SHOULD be mapped to fields within a MIxS template

URI: [nmdc:Characteristic](https://microbiomedata/meta/Characteristic)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Annotation]++-%20has%20characteristic%200..*>\[Characteristic&#124;id(i):string%20%3F;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20*],%20\[NamedThing]^-\[Characteristic])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[Annotation](Annotation.md)** *[has characteristic](has_characteristic.md)*  <sub>0..*</sub>  **[Characteristic](Characteristic.md)**

## Attributes


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

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | field |
|  | | property |
|  | | template field |
|  | | key |

