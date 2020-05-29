
# Type: timestamp value


A value that is a timestamp. The range should be ISO-8601

URI: [nmdc:TimestampValue](https://microbiomedata/meta/TimestampValue)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[AttributeValue]^-\[TimestampValue&#124;has_raw_value(i):string%20%3F])

## Parents

 *  is_a: [AttributeValue](AttributeValue.md) - The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and the structured value

## Referenced by class

 *  **[NamedThing](NamedThing.md)** *[collection_date](collection_date.md)*  <sub>OPT</sub>  **[TimestampValue](TimestampValue.md)**

## Attributes


### Inherited from attribute value:

 * [has raw value](has_raw_value.md)  <sub>OPT</sub>
    * Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
    * range: [String](types/String.md)
    * inherited from: [AttributeValue](AttributeValue.md)
