
# Type: quantity value


A simple quantity, e.g. 2cm

URI: [nmdc:QuantityValue](https://microbiomedata/meta/QuantityValue)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Unit]<has%20unit%200..*-++\[QuantityValue&#124;has_numeric_value:double%20%3F;has_raw_value(i):string%20%3F],%20\[AttributeValue]^-\[QuantityValue])

## Parents

 *  is_a: [AttributeValue](AttributeValue.md) - The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and the structured value

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[alt](alt.md)*  <sub>OPT</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[NamedThing](NamedThing.md)** *[elev](elev.md)*  <sub>OPT</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[NamedThing](NamedThing.md)** *[samp_size](samp_size.md)*  <sub>OPT</sub>  **[QuantityValue](QuantityValue.md)**
 *  **[NamedThing](NamedThing.md)** *[size_frac](size_frac.md)*  <sub>OPT</sub>  **[QuantityValue](QuantityValue.md)**

## Attributes


### Own

 * [has unit](has_unit.md)  <sub>0..*</sub>
    * Description: Links a quantity value to a unit
    * range: [Unit](Unit.md)

### Inherited from attribute value:

 * [has raw value](has_raw_value.md)  <sub>OPT</sub>
    * Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
    * range: [String](types/String.md)
    * inherited from: [AttributeValue](AttributeValue.md)

### Inherited from boolean value:

 * [has numeric value](has_numeric_value.md)  <sub>OPT</sub>
    * Description: Links a quantity value to a number
    * range: [Double](types/Double.md)
