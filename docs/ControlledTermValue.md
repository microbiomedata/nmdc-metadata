
# Type: controlled term value


A controlled term or class from an ontology

URI: [nmdc:ControlledTermValue](https://microbiomedata/meta/ControlledTermValue)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Biosample]++-%20env_broad_scale%201..1>\[ControlledTermValue&#124;has_raw_value(i):string%20%3F],%20\[Biosample]++-%20env_local_scale%201..1>\[ControlledTermValue],%20\[Biosample]++-%20env_medium%201..1>\[ControlledTermValue],%20\[AttributeValue]^-\[ControlledTermValue])

## Parents

 *  is_a: [AttributeValue](AttributeValue.md) - The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and the structured value

## Referenced by class

 *  **[Biosample](Biosample.md)** *[biosample➞env_broad_scale](biosample_env_broad_scale.md)*  <sub>REQ</sub>  **[ControlledTermValue](ControlledTermValue.md)**
 *  **[Biosample](Biosample.md)** *[biosample➞env_local_scale](biosample_env_local_scale.md)*  <sub>REQ</sub>  **[ControlledTermValue](ControlledTermValue.md)**
 *  **[Biosample](Biosample.md)** *[biosample➞env_medium](biosample_env_medium.md)*  <sub>REQ</sub>  **[ControlledTermValue](ControlledTermValue.md)**
 *  **[NamedThing](NamedThing.md)** *[env_broad_scale](env_broad_scale.md)*  <sub>OPT</sub>  **[ControlledTermValue](ControlledTermValue.md)**
 *  **[NamedThing](NamedThing.md)** *[env_local_scale](env_local_scale.md)*  <sub>OPT</sub>  **[ControlledTermValue](ControlledTermValue.md)**
 *  **[NamedThing](NamedThing.md)** *[env_medium](env_medium.md)*  <sub>OPT</sub>  **[ControlledTermValue](ControlledTermValue.md)**
 *  **[NamedThing](NamedThing.md)** *[experimental_factor](experimental_factor.md)*  <sub>OPT</sub>  **[ControlledTermValue](ControlledTermValue.md)**
 *  **[NamedThing](NamedThing.md)** *[ploidy](ploidy.md)*  <sub>OPT</sub>  **[ControlledTermValue](ControlledTermValue.md)**
 *  **[NamedThing](NamedThing.md)** *[samp_mat_process](samp_mat_process.md)*  <sub>OPT</sub>  **[ControlledTermValue](ControlledTermValue.md)**

## Attributes


### Inherited from attribute value:

 * [has raw value](has_raw_value.md)  <sub>OPT</sub>
    * Description: The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
    * range: [String](types/String.md)
    * inherited from: [AttributeValue](AttributeValue.md)
