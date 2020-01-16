
# Class: biosample


A material sample. May be environmental (encompassing many organisms) or isolate or tissue

URI: [nmdc:Biosample](https://microbiomedata/meta/Biosample)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing]^-\[Biosample|id:string%20%3F;name:string%20%3F;alternate_identifiers:string%20*;description(i):string%20%3F])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **None** *[input](input.md)*  <sub>0..*</sub>  **[Biosample](Biosample.md)**
 *  **None** *[output](output.md)*  <sub>0..*</sub>  **[Biosample](Biosample.md)**

## Attributes


### Own

 * [alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](String.md)
 * [id](biosample_id.md)  <sub>OPT</sub>
    * range: [String](String.md)
 * [name](biosample_name.md)  <sub>OPT</sub>
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

 * [alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](String.md)
 * [id](biosample_id.md)  <sub>OPT</sub>
    * range: [String](String.md)
 * [name](biosample_name.md)  <sub>OPT</sub>
    * range: [String](String.md)
