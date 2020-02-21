
# Type: named thing


a databased entity or concept/class

URI: [nmdc:NamedThing](https://microbiomedata/meta/NamedThing)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing&#124;id:string%20%3F;name:string%20%3F;description:string%20%3F;alternate_identifiers:string%20*]^-\[Study],%20\[NamedThing]^-\[DataObject],%20\[NamedThing]^-\[Characteristic],%20\[NamedThing]^-\[BiosampleProcessing],%20\[NamedThing]^-\[Biosample])

## Children

 * [Biosample](Biosample.md) - A material sample. It may be environmental (encompassing many organisms) or isolate or tissue.   An environmental sample containing genetic material from multiple individuals is commonly referred to as a biosample.  
 * [BiosampleProcessing](BiosampleProcessing.md) - A process that takes one or more biosamples as inputs and generates one or as outputs. Examples of outputs include samples cultivated from another sample or data objects created by instruments runs.
 * [Characteristic](Characteristic.md) - A characteristic of a biosample. Examples: depth, habitat, material. For NMDC, characteristics SHOULD be mapped to terms within a MIxS template
 * [DataObject](DataObject.md) - An object that primarily consists of symbols that represent information.   Files, records, and omics data are examples of data objects. 
 * [Study](Study.md) - A study summarizes the overall goal of a research initiative and outlines the key objective of its underlying projects.  

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

### Domain for slot:

 * [annotations](annotations.md)  <sub>0..*</sub>
    * Description: Zero to many annotations on an entity.
    * range: [Annotation](Annotation.md)
 * [has input](has_input.md)  <sub>0..*</sub>
    * Description: An input to a process.
    * range: [String](types/String.md)
 * [part of](part_of.md)  <sub>0..*</sub>
    * Description: Links a resource to another resource that either logically or physically includes it.
    * range: [String](types/String.md)
