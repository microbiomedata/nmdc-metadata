
# Type: data object


An object that primarily consists of symbols that represent information.   Files, records, and omics data are examples of data objects.

URI: [nmdc:DataObject](https://microbiomedata/meta/DataObject)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Database]++-%20data%20object%20set%200..*>\[DataObject&#124;file_size:integer%20%3F;id(i):string;name(i):string%20%3F;description(i):string%20%3F;alternate_identifiers(i):string%20*],%20\[OmicsProcessing]-%20has%20output%200..*>\[DataObject],%20\[NamedThing]^-\[DataObject])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[Database](Database.md)** *[data object set](data_object_set.md)*  <sub>0..*</sub>  **[DataObject](DataObject.md)**
 *  **[OmicsProcessing](OmicsProcessing.md)** *[omics processing➞has output](omics_processing_has_output.md)*  <sub>0..*</sub>  **[DataObject](DataObject.md)**

## Attributes


### Own

 * [file_size](file_size.md)  <sub>OPT</sub>
    * Description: units should be bytes
    * range: [Integer](types/Integer.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
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
