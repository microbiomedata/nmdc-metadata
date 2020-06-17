
# Type: biosample


A material sample. It may be environmental (encompassing many organisms) or isolate or tissue.   An environmental sample containing genetic material from multiple individuals is commonly referred to as a biosample.

URI: [nmdc:Biosample](https://microbiomedata/meta/Biosample)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[QuantityValue]<elev%200..1-++\[Biosample&#124;id:string;name:string%20%3F;alternate_identifiers:string%20*;ecosystem:string%20%3F;ecosystem_category:string%20%3F;ecosystem_type:string%20%3F;ecosystem_subtype:string%20%3F;specific_ecosystem:string%20%3F;description(i):string%20%3F],%20\[QuantityValue]<alt%200..1-++\[Biosample],%20\[QuantityValue]<tot_org_carb%200..1-++\[Biosample],%20\[QuantityValue]<depth%200..1-++\[Biosample],%20\[ControlledTermValue]<env_medium%201..1-++\[Biosample],%20\[ControlledTermValue]<env_local_scale%201..1-++\[Biosample],%20\[ControlledTermValue]<env_broad_scale%201..1-++\[Biosample],%20\[TimestampValue]<collection_date%200..1-++\[Biosample],%20\[TextValue]<geo_loc_name%200..1-++\[Biosample],%20\[GeolocationValue]<lat_lon%201..1-++\[Biosample],%20\[TextValue]<env_package%200..1-++\[Biosample],%20\[BiosampleProcessing]-%20has%20input%200..*>\[Biosample],%20\[Database]++-%20biosample%20set%200..*>\[Biosample],%20\[NamedThing]^-\[Biosample])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - a databased entity or concept/class

## Referenced by class

 *  **[BiosampleProcessing](BiosampleProcessing.md)** *[biosample processing➞has input](biosample_processing_has_input.md)*  <sub>0..*</sub>  **[Biosample](Biosample.md)**
 *  **[Database](Database.md)** *[biosample set](biosample_set.md)*  <sub>0..*</sub>  **[Biosample](Biosample.md)**

## Attributes


### Own

 * [alt](alt.md)  <sub>OPT</sub>
    * Description: "Altitude is a term used to identify heights of objects such as airplanes, space shuttles, rockets, atmospheric balloons and heights of places such as atmospheric layers and clouds. It is used to measure the height of an object which is above the earthbs surface. In this context, the altitude measurement is the vertical distance between the earth's surface above sea level and the sampled position in the air"
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (environment)
 * [biosample➞alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [biosample➞depth](biosample_depth.md)  <sub>OPT</sub>
    * range: [QuantityValue](QuantityValue.md)
 * [biosample➞env_broad_scale](biosample_env_broad_scale.md)  <sub>REQ</sub>
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞env_local_scale](biosample_env_local_scale.md)  <sub>REQ</sub>
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞env_medium](biosample_env_medium.md)  <sub>REQ</sub>
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞id](biosample_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
 * [biosample➞lat_lon](biosample_lat_lon.md)  <sub>REQ</sub>
    * range: [GeolocationValue](GeolocationValue.md)
 * [biosample➞name](biosample_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
 * [collection_date](collection_date.md)  <sub>OPT</sub>
    * Description: "The time of sampling, either as an instance (single point in time) or interval. In case no exact time is available, the date/time can be right truncated i.e. all of these are valid times: 2008-01-23T19:23:10+00:00; 2008-01-23T19:23:10; 2008-01-23; 2008-01; 2008; Except: 2008-01; 2008 all are ISO8601 compliant"
    * range: [TimestampValue](TimestampValue.md)
    * in subsets: (environment)
 * [elev](elev.md)  <sub>OPT</sub>
    * Description: "Elevation of the sampling site is its height above a fixed reference point, most commonly the mean sea level. Elevation is mainly used when referring to points on the earth's surface, while altitude is used for points above the surface, such as an aircraft in flight or a spacecraft in orbit"
    * range: [QuantityValue](QuantityValue.md)
    * in subsets: (environment)
 * [env_package](env_package.md)  <sub>OPT</sub>
    * Description: "MIxS extension for reporting of measurements and observations obtained from one or more of the environments where the sample was obtained. All environmental packages listed here are further defined in separate subtables. By giving the name of the environmental package, a selection of fields can be made from the subtables and can be reported"
    * range: [TextValue](TextValue.md)
    * in subsets: (mixs extension)
 * [geo_loc_name](geo_loc_name.md)  <sub>OPT</sub>
    * Description: "The geographical origin of the sample as defined by the country or sea name followed by specific region name. Country or sea names should be chosen from the INSDC country list (http://insdc.org/country.html), or the GAZ ontology (v 1.512) (http://purl.bioontology.org/ontology/GAZ)"
    * range: [TextValue](TextValue.md)
    * in subsets: (environment)
 * [tot_org_carb](tot_org_carb.md)  <sub>OPT</sub>
    * Description: "Definition for soil: total organic carbon content of the soil, definition otherwise: total organic carbon content"
    * range: [QuantityValue](QuantityValue.md)

### Inherited from named thing:

 * [id](id.md)  <sub>REQ</sub>
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

### Inherited from study:

 * [study➞id](study_id.md)  <sub>REQ</sub>
    * range: [String](types/String.md)
    * inherited from: [Study](Study.md)
 * [study➞name](study_name.md)  <sub>OPT</sub>
    * range: [String](types/String.md)
    * inherited from: [Study](Study.md)
 * [study➞alternate identifiers](study_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
    * inherited from: [Study](Study.md)
 * [submitted_to_insdc](submitted_to_insdc.md)  <sub>OPT</sub>
    * Description: "Depending on the study (large-scale e.g. done with next generation sequencing technology, or small-scale) sequences have to be submitted to SRA (Sequence Read Archive), DRA (DDBJ Read Archive) or via the classical Webin/Sequin systems to Genbank, ENA and DDBJ. Although this field is mandatory, it is meant as a self-test field, therefore it is not necessary to include this field in contextual data submitted to databases"
    * range: [BooleanValue](BooleanValue.md)
    * inherited from: None
    * in subsets: (investigation)
 * [investigation_type](investigation_type.md)  <sub>OPT</sub>
    * Description: "Nucleic Acid Sequence Report is the root element of all MIGS/MIMS compliant reports as standardized by Genomic Standards Consortium. This field is either eukaryote,bacteria,virus,plasmid,organelle, metagenome,mimarks-survey, mimarks-specimen, metatranscriptome, single amplified genome, metagenome-assembled genome, or uncultivated viral genome"
    * range: [TextValue](TextValue.md)
    * inherited from: None
    * in subsets: (investigation)
 * [project_name](project_name.md)  <sub>OPT</sub>
    * Description: Name of the project within which the sequencing was organized
    * range: [TextValue](TextValue.md)
    * inherited from: None
    * in subsets: (investigation)
 * [experimental_factor](experimental_factor.md)  <sub>OPT</sub>
    * Description: "Experimental factors are essentially the variable aspects of an experiment design which can be used to describe an experiment, or set of experiments, in an increasingly detailed manner. This field accepts ontology terms from Experimental Factor Ontology (EFO) and/or Ontology for Biomedical Investigations (OBI). For a browser of EFO (v 2.95) terms, please see http://purl.bioontology.org/ontology/EFO; for a browser of OBI (v 2018-02-12) terms please see http://purl.bioontology.org/ontology/OBI"
    * range: [ControlledTermValue](ControlledTermValue.md)
    * inherited from: None
    * in subsets: (investigation)
 * [ecosystem](ecosystem.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [ecosystem_category](ecosystem_category.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [ecosystem_type](ecosystem_type.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [ecosystem_subtype](ecosystem_subtype.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [specific_ecosystem](specific_ecosystem.md)  <sub>OPT</sub>
    * Description: TODO
    * range: [String](types/String.md)
 * [principal investigator](principal_investigator.md)  <sub>OPT</sub>
    * Description: represents the PI
    * range: [PersonValue](PersonValue.md)
    * inherited from: None

### Domain for slot:

 * [biosample➞alternate identifiers](biosample_alternate_identifiers.md)  <sub>0..*</sub>
    * range: [String](types/String.md)
 * [biosample➞depth](biosample_depth.md)  <sub>OPT</sub>
    * range: [QuantityValue](QuantityValue.md)
 * [biosample➞env_broad_scale](biosample_env_broad_scale.md)  <sub>REQ</sub>
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞env_local_scale](biosample_env_local_scale.md)  <sub>REQ</sub>
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞env_medium](biosample_env_medium.md)  <sub>REQ</sub>
    * range: [ControlledTermValue](ControlledTermValue.md)
 * [biosample➞id](biosample_id.md)  <sub>REQ</sub>
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

