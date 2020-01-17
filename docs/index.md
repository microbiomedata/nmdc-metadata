
# Nmdc_Schema schema


Schema for NMDC. Alpha. Currently focuses on samples


### Classes

 * [Annotation](Annotation.md) - An annotation on a sample. This is essentially a key value pair
 * [BiosampleProcessing](BiosampleProcessing.md) - A process that takes one or more biosamples as inputs and generates one or more as output
 * [NamedThing](NamedThing.md) - a databased entity or concept/class
    * [Biosample](Biosample.md) - A material sample. May be environmental (encompassing many organisms) or isolate or tissue
    * [Characteristic](Characteristic.md) - A characteristic of a biosample. Examples: depth, habitat, material, ... For NMDC, characteristics SHOULD be mapped to fields within a MIxS template
    * [OntologyClass](OntologyClass.md)
    * [Project](Project.md) - An individual or collaborative enterprise that is carefully planned and designed to achieve a particular aim.
    * [Study](Study.md) - A detailed investigation that  defines the overall goal of a research proposal.  It contains the list of sequencing projects that are part of the original proposal.
 * [NormalizedValue](NormalizedValue.md) - The value that was specified for an annotation in parsed/normalized form. This could be a range of different types
    * [ControlledTermValue](ControlledTermValue.md) - A controlled term or class from an ontology
    * [GeolocationValue](GeolocationValue.md) - A normalized value for a location on the earth's surface
    * [QuantityValue](QuantityValue.md) - A simple quantity, e.g. 2cm
 * [Unit](Unit.md)

### Mixins


### Slots

 * [alternate identifiers](alternate_identifiers.md) - Non-primary identifiers
    * [alternate identifiers](biosample_alternate_identifiers.md)
    * [alternate identifiers](project_alternate_identifiers.md)
    * [alternate identifiers](study_alternate_identifiers.md)
 * [annotations](annotations.md) - Zero to many annotations on a sample
 * [description](description.md) - a human-readable description of a thing
 * [has characteristic](has_characteristic.md) - Links an annotation to the field/characteristic
 * [has normalized value](has_normalized_value.md) - Links an annotation to the normalized/parsed raw value
 * [has numeric value](has_numeric_value.md) - Links a quantity value to a number
 * [has raw value](has_raw_value.md) - The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
 * [has unit](has_unit.md) - Links a quantity value to a unit
 * [id](id.md) - A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * [id](biosample_id.md)
    * [id](project_id.md)
    * [id](study_id.md)
 * [input](input.md) - An input biosample to a processing step
 * [instance of](instance_of.md)
 * [involved in](involved_in.md) - Links a biosample to a project that makes use of it.
 * [latitude](latitude.md) - latitude
 * [longitude](longitude.md) - longitude
 * [name](name.md) - A human readable label for an entity
    * [name](biosample_name.md)
    * [name](project_name.md)
    * [name](study_name.md)
 * [output](output.md) - An output biosample to a processing step
 * [part of](part_of.md) - Linds a resource to another resource that either logically or physically includes it.

### Types


#### Built in

 * **Bool**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Double](Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](Integer.md)  (**int**)  - An integer
 * [Ncname](Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](String.md)  (**str**)  - A character string
 * [Time](Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
