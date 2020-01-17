
# Type: annotation


An annotation on a sample. This is essentially a key value pair

URI: [nmdc:Annotation](https://microbiomedata/meta/Annotation)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NormalizedValue]<has%20normalized%20value%200..*-++\[Annotation&#124;has_raw_value:string],%20\[Characteristic]<has%20characteristic%200..*-++\[Annotation],%20\[Biosample]++-%20annotations%200..*>\[Annotation])

## Referenced by class

 *  **[Biosample](Biosample.md)** *[annotations](annotations.md)*  <sub>0..*</sub>  **[Annotation](Annotation.md)**

## Attributes


### Own

 * [has characteristic](has_characteristic.md)  <sub>0..*</sub>
    * Description: Links an annotation to the field/characteristic
    * range: [Characteristic](Characteristic.md)
 * [has normalized value](has_normalized_value.md)  <sub>0..*</sub>
    * Description: Links an annotation to the normalized/parsed raw value
    * range: [NormalizedValue](NormalizedValue.md)
 * [has raw value](has_raw_value.md)  <sub>REQ</sub>
    * Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
    * range: [String](types/String.md)

### Domain for slot:

 * [has characteristic](has_characteristic.md)  <sub>0..*</sub>
    * Description: Links an annotation to the field/characteristic
    * range: [Characteristic](Characteristic.md)
 * [has normalized value](has_normalized_value.md)  <sub>0..*</sub>
    * Description: Links an annotation to the normalized/parsed raw value
    * range: [NormalizedValue](NormalizedValue.md)
 * [has raw value](has_raw_value.md)  <sub>REQ</sub>
    * Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
    * range: [String](types/String.md)
