
# Type: database


An abstract holder for any set of metadata and data. It does not need to correspond to an actual managed databse top level holder class. When translated to JSON-Schema this is the 'root' object. It should contain pointers to other objects of interest

URI: [nmdc:Database](https://microbiomedata/meta/Database)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Activity]<activity%20set%200..*-++\[Database],%20\[DataObject]<data%20object%20set%200..*-++\[Database],%20\[Study]<study%20set%200..*-++\[Database],%20\[Biosample]<biosample%20set%200..*-++\[Database])

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
 * [study set](study_set.md)  <sub>0..*</sub>
    * Description: This property links a database object to the set of studies within it.
    * range: [Study](Study.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Aliases:** | | NMDC metadata object |

