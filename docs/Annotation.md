
# Type: annotation


An annotation on a named thing. This is essentially a key value pair

URI: [nmdc:Annotation](https://microbiomedata/meta/Annotation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NormalizedValue]<has%20normalized%20value%200..*-++\[Annotation&#124;has_raw_value:string%20%3F],%20\[Characteristic]<has%20characteristic%200..*-++\[Annotation],%20\[BiosampleProcessing]++-%20annotations%200..*>\[Annotation],%20\[Biosample]++-%20annotations%200..*>\[Annotation],%20\[DataObject]++-%20annotations%200..*>\[Annotation],%20\[Study]++-%20annotations%200..*>\[Annotation])

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[annotations](annotations.md)*  <sub>0..*</sub>  **[Annotation](Annotation.md)**
 *  **[BiosampleProcessing](BiosampleProcessing.md)** *[biosample processing➞annotations](biosample_processing_annotations.md)*  <sub>0..*</sub>  **[Annotation](Annotation.md)**
 *  **[Biosample](Biosample.md)** *[biosample➞annotations](biosample_annotations.md)*  <sub>0..*</sub>  **[Annotation](Annotation.md)**
 *  **[DataObject](DataObject.md)** *[data object➞annotations](data_object_annotations.md)*  <sub>0..*</sub>  **[Annotation](Annotation.md)**
 *  **[Study](Study.md)** *[study➞annotations](study_annotations.md)*  <sub>0..*</sub>  **[Annotation](Annotation.md)**

## Attributes


### Own

 * [has characteristic](has_characteristic.md)  <sub>0..*</sub>
    * Description: Links an annotation to the field/characteristic
    * range: [Characteristic](Characteristic.md)
 * [has normalized value](has_normalized_value.md)  <sub>0..*</sub>
    * Description: Links an annotation to the normalized/parsed raw value
    * range: [NormalizedValue](NormalizedValue.md)
 * [has raw value](has_raw_value.md)  <sub>OPT</sub>
    * Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
    * range: [String](types/String.md)

### Domain for slot:

 * [has characteristic](has_characteristic.md)  <sub>0..*</sub>
    * Description: Links an annotation to the field/characteristic
    * range: [Characteristic](Characteristic.md)
 * [has normalized value](has_normalized_value.md)  <sub>0..*</sub>
    * Description: Links an annotation to the normalized/parsed raw value
    * range: [NormalizedValue](NormalizedValue.md)
 * [has raw value](has_raw_value.md)  <sub>OPT</sub>
    * Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
    * range: [String](types/String.md)
