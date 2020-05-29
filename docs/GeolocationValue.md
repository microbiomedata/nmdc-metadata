
# Type: geolocation value


A normalized value for a location on the earth's surface

URI: [nmdc:GeolocationValue](https://microbiomedata/meta/GeolocationValue)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Biosample]++-%20lat_lon%201..1>\[GeolocationValue&#124;has_raw_value:string%20%3F;latitude:float%20%3F;longitude:float%20%3F],%20\[AttributeValue]^-\[GeolocationValue])

## Parents

 *  is_a: [AttributeValue](AttributeValue.md) - The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and the structured value

## Referenced by class

 *  **[Biosample](Biosample.md)** *[biosample➞lat_lon](biosample_lat_lon.md)*  <sub>REQ</sub>  **[GeolocationValue](GeolocationValue.md)**
 *  **[NamedThing](NamedThing.md)** *[lat_lon](lat_lon.md)*  <sub>OPT</sub>  **[GeolocationValue](GeolocationValue.md)**

## Attributes


### Own

 * [geolocation value➞has raw value](geolocation_value_has_raw_value.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [latitude](latitude.md)  <sub>OPT</sub>
    * Description: latitude
    * range: [Float](types/Float.md)
 * [longitude](longitude.md)  <sub>OPT</sub>
    * Description: longitude
    * range: [Float](types/Float.md)

### Domain for slot:

 * [geolocation value➞has raw value](geolocation_value_has_raw_value.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [latitude](latitude.md)  <sub>OPT</sub>
    * Description: latitude
    * range: [Float](types/Float.md)
 * [longitude](longitude.md)  <sub>OPT</sub>
    * Description: longitude
    * range: [Float](types/Float.md)
