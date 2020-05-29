
# Type: integer value


A value that is an integer

URI: [nmdc:IntegerValue](https://microbiomedata/meta/IntegerValue)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[AttributeValue]^-\[IntegerValue&#124;has_numeric_value:double%20%3F;has_raw_value(i):string%20%3F])

## Parents

 *  is_a: [AttributeValue](AttributeValue.md) - The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and the structured value

## Attributes


### Inherited from attribute value:

 * [has raw value](has_raw_value.md)  <sub>OPT</sub>
    * Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
    * range: [String](types/String.md)
    * inherited from: [AttributeValue](AttributeValue.md)

### Inherited from boolean value:

 * [has numeric value](has_numeric_value.md)  <sub>OPT</sub>
    * Description: Links a quantity value to a number
    * range: [Double](types/Double.md)
