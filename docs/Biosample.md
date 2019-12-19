
# Class: biosample


A material sample. May be environmental (encompassing many organisms) or isolate or tissue

URI: [nmdc:Biosample](https://microbiomedata/meta/Biosample)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Annotation]<annotations%200..*-++\[Biosample|id:string;name:string%20%3F;alternate_identifiers:string%20*],%20\[NamedThing]^-\[Biosample])

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
 * [alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](String.md)
 * [id](biosample_id.md)  <sub>REQ</sub>
    * range: [String](String.md)
 * [name](biosample_name.md)  <sub>OPT</sub>
    * range: [String](String.md)

### Domain for slot:

 * [annotations](annotations.md)  <sub>0..*</sub>
    * Description: Zero to many annotations on a sample
    * range: [Annotation](Annotation.md)
 * [alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](String.md)
 * [id](biosample_id.md)  <sub>REQ</sub>
    * range: [String](String.md)
 * [name](biosample_name.md)  <sub>OPT</sub>
    * range: [String](String.md)
