
# Nmdc_Schema schema


Schema for NMDC. Alpha. Currently focuses on samples


### Classes

 * [Annotation](Annotation.md) - An annotation on a named thing. This is essentially a key value pair
 * [NamedThing](NamedThing.md) - a databased entity or concept/class
    * [Biosample](Biosample.md) - A material sample. It may be environmental (encompassing many organisms) or isolate or tissue.   An environmental sample containing genetic material from multiple individuals is commonly referred to as a biosample.  
    * [BiosampleProcessing](BiosampleProcessing.md) - A process that takes one or more biosamples as inputs and generates one or as outputs. Examples of outputs include samples cultivated from another sample or data objects created by instruments runs.
       * [OmicsProcessing](OmicsProcessing.md) - The methods and processes used to generate omics data from a biosample or organism.
    * [Characteristic](Characteristic.md) - A characteristic of a biosample. Examples: depth, habitat, material. For NMDC, characteristics SHOULD be mapped to terms within a MIxS template
    * [DataObject](DataObject.md) - An object that primarily consists of symbols that represent information.   Files, records, and omics data are examples of data objects. 
    * [Study](Study.md) - A study summarizes the overall goal of a research initiative and outlines the key objective of its underlying projects.  
 * [NormalizedValue](NormalizedValue.md) - The value that was specified for an annotation in parsed/normalized form. This could be a range of different types.
    * [ControlledTermValue](ControlledTermValue.md) - A controlled term or class from an ontology
    * [GeolocationValue](GeolocationValue.md) - A normalized value for a location on the earth's surface
    * [QuantityValue](QuantityValue.md) - A simple quantity, e.g. 2cm
 * [Unit](Unit.md)

### Mixins


### Slots

 * [alternate identifiers](alternate_identifiers.md) - Non-primary identifiers
    * [biosample➞alternate identifiers](biosample_alternate_identifiers.md)
    * [omics processing➞alternate identifiers](omics_processing_alternate_identifiers.md)
    * [study➞alternate identifiers](study_alternate_identifiers.md)
 * [annotations](annotations.md) - Zero to many annotations on an entity.
    * [biosample processing➞annotations](biosample_processing_annotations.md)
    * [biosample➞annotations](biosample_annotations.md)
    * [data object➞annotations](data_object_annotations.md)
    * [study➞annotations](study_annotations.md)
 * [description](description.md) - a human-readable description of a thing
 * [has characteristic](has_characteristic.md) - Links an annotation to the field/characteristic
 * [has input](has_input.md) - An input to a process.
    * [biosample processing➞has input](biosample_processing_has_input.md)
 * [has normalized value](has_normalized_value.md) - Links an annotation to the normalized/parsed raw value
 * [has numeric value](has_numeric_value.md) - Links a quantity value to a number
 * [has output](has_output.md) - An output biosample to a processing step
    * [omics processing➞has output](omics_processing_has_output.md)
 * [has raw value](has_raw_value.md) - The value that was specified for an annotation in raw form, i.e. a string. E.g. "2 cm" or "2-4 cm"
 * [has unit](has_unit.md) - Links a quantity value to a unit
 * [id](id.md) - A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * [biosample➞id](biosample_id.md)
    * [omics processing➞id](omics_processing_id.md)
    * [study➞id](study_id.md)
 * [latitude](latitude.md) - latitude
 * [longitude](longitude.md) - longitude
 * [name](name.md) - A human readable label for an entity
    * [biosample➞name](biosample_name.md)
    * [omics processing➞name](omics_processing_name.md)
    * [study➞name](study_name.md)
 * [part of](part_of.md) - Links a resource to another resource that either logically or physically includes it.
    * [omics processing➞part of](omics_processing_part_of.md)

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

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE
