# Class: biosample


A material sample. May be environmental (encompassing many organisms) or isolate or tissue

URI: [nmdc:Biosample](https://microbiomedata/meta/Biosample)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Annotation]<annotations%200..*-++\[Biosample|id:string%20%3F;name:string%20%3F;alternate_identifiers:string%20*;description(i):string%20%3F],%20\[BiosampleProcessing]++-%20input%200..*>\[Biosample],%20\[BiosampleProcessing]++-%20output%200..*>\[Biosample],%20\[NamedThing]^-\[Biosample])
## Inheritance

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class
## Children

## Used by

 *  **[BiosampleProcessing](BiosampleProcessing.md)** *[input](input.md)*  <sub>0..*</sub>  **[Biosample](Biosample.md)**
 *  **[BiosampleProcessing](BiosampleProcessing.md)** *[output](output.md)*  <sub>0..*</sub>  **[Biosample](Biosample.md)**
## Fields

 * [annotations](annotations.md)  <sub>0..*</sub>
    * Description: Zero to many annotations on a sample
    * range: [Annotation](Annotation.md)
 * [biosample.alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](String.md)
 * [biosample.id](biosample_id.md)  <sub>OPT</sub>
    * range: [String](String.md)
 * [biosample.name](biosample_name.md)  <sub>OPT</sub>
    * range: [String](String.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](String.md)
    * inherited from: [NamedThing](NamedThing.md)
