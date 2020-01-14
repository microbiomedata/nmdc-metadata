# Class: biosample processing


A process that takes one or more biosamples as inputs and generates one or more as output

URI: [nmdc:BiosampleProcessing](https://microbiomedata/meta/BiosampleProcessing)

![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[Biosample]<output%200..*-++\[BiosampleProcessing],%20\[Biosample]<input%200..*-++\[BiosampleProcessing])
## Inheritance

## Children

## Used by

## Fields

 * [input](input.md)  <sub>0..*</sub>
    * Description: An input biosample to a processing step
    * range: [Biosample](Biosample.md)
 * [output](output.md)  <sub>0..*</sub>
    * Description: An output biosample to a processing step
    * range: [Biosample](Biosample.md)
