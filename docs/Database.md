---
parent: Classes
title: nmdc:Database
grand_parent: Browse the NMDC Schema
layout: default
---

# Type: Database


An abstract holder for any set of metadata and data. It does not need to correspond to an actual managed databse top level holder class. When translated to JSON-Schema this is the 'root' object. It should contain pointers to other objects of interest

URI: [nmdc:Database](https://microbiomedata/meta/Database)


---

![img](http://yuml.me/diagram/nofunky;dir:TB/class/[Study],[OmicsProcessing],[OmicsProcessing]%3Comics%20processing%20set%200..%2A-++[Database],[Activity]%3Cactivity%20set%200..%2A-++[Database],[DataObject]%3Cdata%20object%20set%200..%2A-++[Database],[Study]%3Cstudy%20set%200..%2A-++[Database],[Biosample]%3Cbiosample%20set%200..%2A-++[Database],[DataObject],[Biosample],[Activity])

---


## Referenced by class


## Attributes


### Own

 * [activity set](activity_set.md)  <sub>0..*</sub>
    * Description: This property links a database object to the set of prov activities.
    * range: [Activity](Activity.md)
 * [biosample set](biosample_set.md)  <sub>0..*</sub>
    * Description: This property links a database object to the set of samples within it.
    * range: [Biosample](Biosample.md)
 * [data object set](data_object_set.md)  <sub>0..*</sub>
    * Description: This property links a database object to the set of data objects within it.
    * range: [DataObject](DataObject.md)
 * [omics processing set](omics_processing_set.md)  <sub>0..*</sub>
    * Description: This property links a database object to the set of omics processings within it.
    * range: [OmicsProcessing](OmicsProcessing.md)
 * [study set](study_set.md)  <sub>0..*</sub>
    * Description: This property links a database object to the set of studies within it.
    * range: [Study](Study.md)

### Domain for slot:

 * [activity set](activity_set.md)  <sub>0..*</sub>
    * Description: This property links a database object to the set of prov activities.
    * range: [Activity](Activity.md)
 * [biosample set](biosample_set.md)  <sub>0..*</sub>
    * Description: This property links a database object to the set of samples within it.
    * range: [Biosample](Biosample.md)
 * [data object set](data_object_set.md)  <sub>0..*</sub>
    * Description: This property links a database object to the set of data objects within it.
    * range: [DataObject](DataObject.md)
 * [omics processing set](omics_processing_set.md)  <sub>0..*</sub>
    * Description: This property links a database object to the set of omics processings within it.
    * range: [OmicsProcessing](OmicsProcessing.md)
 * [study set](study_set.md)  <sub>0..*</sub>
    * Description: This property links a database object to the set of studies within it.
    * range: [Study](Study.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | NMDC metadata object |

