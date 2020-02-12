# Auto generated from nmdc.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-02-12 11:59
# Schema: nmdc_schema
#
# id: https://microbiomedata/schema
# description: Schema for NMDC. Alpha. Currently focuses on samples
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from includes.types import Double, Float, String

metamodel_version = "1.4.3"


# Namespaces
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
NMDC = CurieNamespace('nmdc', 'https://microbiomedata/meta/')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://example.org/UNKNOWN/rdf/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
SKOS = CurieNamespace('skos', 'http://example.org/UNKNOWN/skos/')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NMDC


# Types

# Class references



@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.NamedThing
    class_class_curie: ClassVar[str] = "nmdc:NamedThing"
    class_name: ClassVar[str] = "named thing"
    class_model_uri: ClassVar[URIRef] = NMDC.NamedThing

    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()
    annotations: List[Union[dict, "Annotation"]] = empty_list()

    def __post_init__(self):
        self.annotations = [v if isinstance(v, Annotation)
                            else Annotation(**v) for v in self.annotations]
        super().__post_init__()


class OntologyClass(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.OntologyClass
    class_class_curie: ClassVar[str] = "nmdc:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = NMDC.OntologyClass


@dataclass
class Biosample(NamedThing):
    """
    A material sample. It may be environmental (encompassing many organisms) or isolate or tissue. An environmental
    sample containing genetic material from multiple individuals is commonly referred to as a biosample. (see
    https://academic.oup.com/nar/article/47/D1/D649/5144132)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Biosample
    class_class_curie: ClassVar[str] = "nmdc:Biosample"
    class_name: ClassVar[str] = "biosample"
    class_model_uri: ClassVar[URIRef] = NMDC.Biosample

    id: Optional[str] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()

@dataclass
class Study(NamedThing):
    """
    A study summarizes the overall goal of a research initiative and outlines the key objective of its underlying
    projects. A study may have only one sequencing and analysis project, where sequencing a single organism fulfills a
    research objective. (see https://academic.oup.com/nar/article/47/D1/D649/5144132)
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Study
    class_class_curie: ClassVar[str] = "nmdc:Study"
    class_name: ClassVar[str] = "study"
    class_model_uri: ClassVar[URIRef] = NMDC.Study

    id: Optional[str] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()

@dataclass
class BiosampleProcessing(YAMLRoot):
    """
    A process that takes one or more biosamples as inputs and generates one or as outputs. Examples of outputs include
    samples cultivated from another sample or data objects created by instruments runs.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.BiosampleProcessing
    class_class_curie: ClassVar[str] = "nmdc:BiosampleProcessing"
    class_name: ClassVar[str] = "biosample processing"
    class_model_uri: ClassVar[URIRef] = NMDC.BiosampleProcessing

    has_input: List[Union[dict, Biosample]] = empty_list()
    has_output: List[Union[dict, NamedThing]] = empty_list()

    def __post_init__(self):
        self.has_input = [v if isinstance(v, Biosample)
                          else Biosample(**v) for v in self.has_input]
        self.has_output = [v if isinstance(v, NamedThing)
                           else NamedThing(**v) for v in self.has_output]
        super().__post_init__()


@dataclass
class SequencingProject(BiosampleProcessing):
    """
    The methods and processes used to generate sequencing output from a biosample or organism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.SequencingProject
    class_class_curie: ClassVar[str] = "nmdc:SequencingProject"
    class_name: ClassVar[str] = "sequencing project"
    class_model_uri: ClassVar[URIRef] = NMDC.SequencingProject

    part_of: List[Union[dict, Study]] = empty_list()
    annotations: List[Union[dict, "Annotation"]] = empty_list()

    def __post_init__(self):
        self.part_of = [v if isinstance(v, Study)
                        else Study(**v) for v in self.part_of]
        self.annotations = [v if isinstance(v, Annotation)
                            else Annotation(**v) for v in self.annotations]
        super().__post_init__()


class Characteristic(NamedThing):
    """
    A characteristic of a biosample. Examples: depth, habitat, material, ... For NMDC, characteristics SHOULD be
    mapped to fields within a MIxS template
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Characteristic
    class_class_curie: ClassVar[str] = "nmdc:Characteristic"
    class_name: ClassVar[str] = "characteristic"
    class_model_uri: ClassVar[URIRef] = NMDC.Characteristic


class NormalizedValue(YAMLRoot):
    """
    The value that was specified for an annotation in parsed/normalized form. This could be a range of different types
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.NormalizedValue
    class_class_curie: ClassVar[str] = "nmdc:NormalizedValue"
    class_name: ClassVar[str] = "normalized value"
    class_model_uri: ClassVar[URIRef] = NMDC.NormalizedValue


@dataclass
class QuantityValue(NormalizedValue):
    """
    A simple quantity, e.g. 2cm
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.QuantityValue
    class_class_curie: ClassVar[str] = "nmdc:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = NMDC.QuantityValue

    has_unit: List[Union[dict, "Unit"]] = empty_list()
    has_numeric_value: Optional[float] = None

    def __post_init__(self):
        self.has_unit = [v if isinstance(v, Unit)
                         else Unit(**v) for v in self.has_unit]
        super().__post_init__()


@dataclass
class ControlledTermValue(NormalizedValue):
    """
    A controlled term or class from an ontology
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.ControlledTermValue
    class_class_curie: ClassVar[str] = "nmdc:ControlledTermValue"
    class_name: ClassVar[str] = "controlled term value"
    class_model_uri: ClassVar[URIRef] = NMDC.ControlledTermValue

    instance_of: Optional[Union[dict, OntologyClass]] = None

    def __post_init__(self):
        if self.instance_of is not None and not isinstance(self.instance_of, OntologyClass):
            self.instance_of = OntologyClass(**self.instance_of)
        super().__post_init__()


@dataclass
class GeolocationValue(NormalizedValue):
    """
    A normalized value for a location on the earth's surface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.GeolocationValue
    class_class_curie: ClassVar[str] = "nmdc:GeolocationValue"
    class_name: ClassVar[str] = "geolocation value"
    class_model_uri: ClassVar[URIRef] = NMDC.GeolocationValue

    latitude: Optional[float] = None
    longitude: Optional[float] = None

class Unit(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Unit
    class_class_curie: ClassVar[str] = "nmdc:Unit"
    class_name: ClassVar[str] = "unit"
    class_model_uri: ClassVar[URIRef] = NMDC.Unit


class DataObject(NamedThing):
    """
    An object that primarily consists of symbols that represent information. Files, records, and sequencing data are
    examples of data objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.DataObject
    class_class_curie: ClassVar[str] = "nmdc:DataObject"
    class_name: ClassVar[str] = "data object"
    class_model_uri: ClassVar[URIRef] = NMDC.DataObject


@dataclass
class Annotation(YAMLRoot):
    """
    An annotation on a named thing. This is essentially a key value pair
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Annotation
    class_class_curie: ClassVar[str] = "nmdc:Annotation"
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = NMDC.Annotation

    has_characteristic: List[Union[dict, Characteristic]] = empty_list()
    has_raw_value: Optional[str] = None
    has_normalized_value: List[Union[dict, NormalizedValue]] = empty_list()

    def __post_init__(self):
        self.has_characteristic = [v if isinstance(v, Characteristic)
                                   else Characteristic(**v) for v in self.has_characteristic]
        self.has_normalized_value = [v if isinstance(v, NormalizedValue)
                                     else NormalizedValue(**v) for v in self.has_normalized_value]
        super().__post_init__()



# Slots
class slots:
    pass

slots.id = Slot(uri=NMDC.id, name="id", curie=NMDC.curie('id'),
                      model_uri=NMDC.id, domain=None, range=Optional[str])

slots.name = Slot(uri=NMDC.name, name="name", curie=NMDC.curie('name'),
                      model_uri=NMDC.name, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                      model_uri=NMDC.description, domain=None, range=Optional[str])

slots.has_characteristic = Slot(uri=NMDC.has_characteristic, name="has characteristic", curie=NMDC.curie('has_characteristic'),
                      model_uri=NMDC.has_characteristic, domain=Annotation, range=List[Union[dict, Characteristic]])

slots.instance_of = Slot(uri=NMDC.instance_of, name="instance of", curie=NMDC.curie('instance_of'),
                      model_uri=NMDC.instance_of, domain=None, range=Optional[Union[dict, OntologyClass]])

slots.has_raw_value = Slot(uri=NMDC.has_raw_value, name="has raw value", curie=NMDC.curie('has_raw_value'),
                      model_uri=NMDC.has_raw_value, domain=Annotation, range=Optional[str])

slots.has_normalized_value = Slot(uri=NMDC.has_normalized_value, name="has normalized value", curie=NMDC.curie('has_normalized_value'),
                      model_uri=NMDC.has_normalized_value, domain=Annotation, range=List[Union[dict, NormalizedValue]])

slots.has_unit = Slot(uri=NMDC.has_unit, name="has unit", curie=NMDC.curie('has_unit'),
                      model_uri=NMDC.has_unit, domain=None, range=List[Union[dict, Unit]], mappings = [QUD.unit])

slots.has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="has numeric value", curie=NMDC.curie('has_numeric_value'),
                      model_uri=NMDC.has_numeric_value, domain=None, range=Optional[float], mappings = [QUD.quantityValue])

slots.alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.alternate_identifiers, domain=None, range=List[str])

slots.annotations = Slot(uri=NMDC.annotations, name="annotations", curie=NMDC.curie('annotations'),
                      model_uri=NMDC.annotations, domain=NamedThing, range=List[Union[dict, "Annotation"]])

slots.latitude = Slot(uri=WGS.lat, name="latitude", curie=WGS.curie('lat'),
                      model_uri=NMDC.latitude, domain=None, range=Optional[float])

slots.longitude = Slot(uri=WGS.long, name="longitude", curie=WGS.curie('long'),
                      model_uri=NMDC.longitude, domain=None, range=Optional[float])

slots.has_input = Slot(uri=NMDC.has_input, name="has input", curie=NMDC.curie('has_input'),
                      model_uri=NMDC.has_input, domain=NamedThing, range=List[str])

slots.has_output = Slot(uri=NMDC.has_output, name="has output", curie=NMDC.curie('has_output'),
                      model_uri=NMDC.has_output, domain=NamedThing, range=List[str])

slots.part_of = Slot(uri=DCTERMS.isPartOf, name="part of", curie=DCTERMS.curie('isPartOf'),
                      model_uri=NMDC.part_of, domain=NamedThing, range=List[str])

slots.named_thing_annotations = Slot(uri=NMDC.annotations, name="named thing_annotations", curie=NMDC.curie('annotations'),
                      model_uri=NMDC.named_thing_annotations, domain=NamedThing, range=List[Union[dict, "Annotation"]])

slots.biosample_id = Slot(uri=NMDC.id, name="biosample_id", curie=NMDC.curie('id'),
                      model_uri=NMDC.biosample_id, domain=Biosample, range=Optional[str])

slots.biosample_name = Slot(uri=NMDC.name, name="biosample_name", curie=NMDC.curie('name'),
                      model_uri=NMDC.biosample_name, domain=Biosample, range=Optional[str])

slots.biosample_alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="biosample_alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.biosample_alternate_identifiers, domain=Biosample, range=List[str])

slots.study_id = Slot(uri=NMDC.id, name="study_id", curie=NMDC.curie('id'),
                      model_uri=NMDC.study_id, domain=Study, range=Optional[str])

slots.study_name = Slot(uri=NMDC.name, name="study_name", curie=NMDC.curie('name'),
                      model_uri=NMDC.study_name, domain=Study, range=Optional[str])

slots.study_alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="study_alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.study_alternate_identifiers, domain=Study, range=List[str])

slots.biosample_processing_has_input = Slot(uri=NMDC.has_input, name="biosample processing_has input", curie=NMDC.curie('has_input'),
                      model_uri=NMDC.biosample_processing_has_input, domain=BiosampleProcessing, range=List[Union[dict, Biosample]])

slots.biosample_processing_has_output = Slot(uri=NMDC.has_output, name="biosample processing_has output", curie=NMDC.curie('has_output'),
                      model_uri=NMDC.biosample_processing_has_output, domain=BiosampleProcessing, range=List[Union[dict, NamedThing]])

slots.sequencing_project_id = Slot(uri=NMDC.id, name="sequencing project_id", curie=NMDC.curie('id'),
                      model_uri=NMDC.sequencing_project_id, domain=SequencingProject, range=Optional[str])

slots.sequencing_project_name = Slot(uri=NMDC.name, name="sequencing project_name", curie=NMDC.curie('name'),
                      model_uri=NMDC.sequencing_project_name, domain=SequencingProject, range=Optional[str])

slots.sequencing_project_alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="sequencing project_alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.sequencing_project_alternate_identifiers, domain=SequencingProject, range=List[str])

slots.sequencing_project_part_of = Slot(uri=NMDC.part_of, name="sequencing project_part of", curie=NMDC.curie('part_of'),
                      model_uri=NMDC.sequencing_project_part_of, domain=SequencingProject, range=List[Union[dict, Study]])

slots.sequencing_project_has_output = Slot(uri=NMDC.has_output, name="sequencing project_has output", curie=NMDC.curie('has_output'),
                      model_uri=NMDC.sequencing_project_has_output, domain=SequencingProject, range=List[Union[dict, "DataObject"]])

slots.sequencing_project_annotations = Slot(uri=NMDC.annotations, name="sequencing project_annotations", curie=NMDC.curie('annotations'),
                      model_uri=NMDC.sequencing_project_annotations, domain=SequencingProject, range=List[Union[dict, "Annotation"]])
