
# Type: url value


A value that is a string that conforms to URL syntax

URI: [nmdc:UrlValue](https://microbiomedata/meta/UrlValue)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[AttributeValue]^-\[UrlValue&#124;has_raw_value(i):string%20%3F])

## Parents

 *  is_a: [AttributeValue](AttributeValue.md) - The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and the structured value

## Attributes


### Inherited from attribute value:

 * [has raw value](has_raw_value.md)  <sub>OPT</sub>
    * Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
    * range: [String](types/String.md)
    * inherited from: [AttributeValue](AttributeValue.md)
