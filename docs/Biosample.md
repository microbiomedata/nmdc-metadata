
# Type: biosample


A material sample. It may be environmental (encompassing many organisms) or isolate or tissue.   An environmental sample containing genetic material from multiple individuals is commonly referred to as a biosample.

URI: [nmdc:Biosample](https://microbiomedata/meta/Biosample)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[ControlledTermValue]<env_medium%201..1-++\[Biosample&#124;id:string%20%3F;name:string%20%3F;alternate_identifiers:string%20*;description(i):string%20%3F],%20\[ControlledTermValue]<env_local_scale%201..1-++\[Biosample],%20\[ControlledTermValue]<env_broad_scale%201..1-++\[Biosample],%20\[TextValue]<depth%200..1-++\[Biosample],%20\[GeolocationValue]<lat_lon%201..1-++\[Biosample],%20\[BiosampleProcessing]++-%20has%20input%200..*>\[Biosample],%20\[NamedThing]^-\[Biosample])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[BiosampleProcessing](BiosampleProcessing.md)** *[biosample processing➞has input](biosample_processing_has_input.md)*  <sub>0..*</sub>  **[Biosample](Biosample.md)**

## Attributes


### Own

 * [biosample➞alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [biosample➞depth](biosample_depth.md)  <sub>OPT</sub>
    * range: [TextValue](TextValue.md)
 * [biosample➞env_broad_scale](biosample_env_broad_scale.md)  <sub>REQ</sub>
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞env_local_scale](biosample_env_local_scale.md)  <sub>REQ</sub>
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞env_medium](biosample_env_medium.md)  <sub>REQ</sub>
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞id](biosample_id.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [biosample➞lat_lon](biosample_lat_lon.md)  <sub>REQ</sub>
    * range: [GeolocationValue](GeolocationValue.md)
 * [biosample➞name](biosample_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

### Inherited from named thing:

 * [id](id.md)  <sub>OPT</sub>
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

### Domain for slot:

 * [biosample➞alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [biosample➞depth](biosample_depth.md)  <sub>OPT</sub>
    * range: [TextValue](TextValue.md)
 * [biosample➞env_broad_scale](biosample_env_broad_scale.md)  <sub>REQ</sub>
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞env_local_scale](biosample_env_local_scale.md)  <sub>REQ</sub>
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞env_medium](biosample_env_medium.md)  <sub>REQ</sub>
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞id](biosample_id.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [biosample➞lat_lon](biosample_lat_lon.md)  <sub>REQ</sub>
    * range: [GeolocationValue](GeolocationValue.md)
 * [biosample➞name](biosample_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | sample |
|  | | material sample |

