
# Class: quantity value


A simple quantity, e.g. 2cm

URI: [nmdc:QuantityValue](https://microbiomedata/meta/QuantityValue)

![img](QuantityValue
Unit
NormalizedValue
QuantityValue
http://yuml.me/diagram/nofunky;dir:TB/class/\[Unit]<has%20unit%200..*-++\[QuantityValue%7Chas_numeric_value:double%20%3F],%20\[NormalizedValue]^-\[QuantityValue])

## Parents

 *  is_a: [NormalizedValue](NormalizedValue.md) - The value that was specified for an annotation in parsed/normalized form. This could be a range of different types

## Referenced by class


## Attributes


### Own

 * [has numeric value](has_numeric_value.md)  <sub>OPT</sub>
    * Description: connects a quantity value to a number
    * range: [Double](Double.md)
 * [has unit](has_unit.md)  <sub>0..*</sub>
    * Description: connects a quantity value to a unit
    * range: [Unit](Unit.md)

### Domain for slot:

 * [has numeric value](has_numeric_value.md)  <sub>OPT</sub>
    * Description: connects a quantity value to a number
    * range: [Double](Double.md)
 * [has unit](has_unit.md)  <sub>0..*</sub>
    * Description: connects a quantity value to a unit
    * range: [Unit](Unit.md)
