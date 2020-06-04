# Auto generated from nmdc.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-05-28 12:57
# Schema: nmdc_schema
#
# id: https://microbiomedata/schema
# description: Schema for National Microbiome Data Collaborative (NMDC)
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from biolinkml.utils.slot import Slot
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
if sys.version_info < (3, 7, 6):
    from biolinkml.utils.dataclass_extensions_375 import dataclasses_init_fn_with_kwargs
else:
    from biolinkml.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from biolinkml.utils.curienamespace import CurieNamespace
from includes.types import Depth, Double, EnvBroadScale, Float, LatLon, String

metamodel_version = "1.4.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
MIXS = CurieNamespace('mixs', 'https://w3id.org/gensc/')
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

class DataObject(NamedThing):
    """
    An object that primarily consists of symbols that represent information. Files, records, and omics data are
    examples of data objects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.DataObject
    class_class_curie: ClassVar[str] = "nmdc:DataObject"
    class_name: ClassVar[str] = "data object"
    class_model_uri: ClassVar[URIRef] = NMDC.DataObject


@dataclass
class Biosample(NamedThing):
    """
    A material sample. It may be environmental (encompassing many organisms) or isolate or tissue. An environmental
    sample containing genetic material from multiple individuals is commonly referred to as a biosample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Biosample
    class_class_curie: ClassVar[str] = "nmdc:Biosample"
    class_name: ClassVar[str] = "biosample"
    class_model_uri: ClassVar[URIRef] = NMDC.Biosample

    lat_lon: Union[dict, "GeolocationValue"] = None
    env_broad_scale: Union[dict, "ControlledTermValue"] = None
    id: Optional[str] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()
    depth: Optional[Union[dict, "TextValue"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.lat_lon is None:
            raise ValueError(f"lat_lon must be supplied")
        if not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**self.lat_lon)
        if self.depth is not None and not isinstance(self.depth, TextValue):
            self.depth = TextValue(**self.depth)
        if self.env_broad_scale is None:
            raise ValueError(f"env_broad_scale must be supplied")
        if not isinstance(self.env_broad_scale, ControlledTermValue):
            self.env_broad_scale = ControlledTermValue(**self.env_broad_scale)
        super().__post_init__(**kwargs)


@dataclass
class Study(NamedThing):
    """
    A study summarizes the overall goal of a research initiative and outlines the key objective of its underlying
    projects.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Study
    class_class_curie: ClassVar[str] = "nmdc:Study"
    class_name: ClassVar[str] = "study"
    class_model_uri: ClassVar[URIRef] = NMDC.Study

    id: Optional[str] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()
    annotations: List[str] = empty_list()

@dataclass
class BiosampleProcessing(NamedThing):
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

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.has_input = [v if isinstance(v, Biosample)
                          else Biosample(**v) for v in self.has_input]
        super().__post_init__(**kwargs)


@dataclass
class OmicsProcessing(BiosampleProcessing):
    """
    The methods and processes used to generate omics data from a biosample or organism.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.OmicsProcessing
    class_class_curie: ClassVar[str] = "nmdc:OmicsProcessing"
    class_name: ClassVar[str] = "omics processing"
    class_model_uri: ClassVar[URIRef] = NMDC.OmicsProcessing

    id: Optional[str] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()
    part_of: List[Union[dict, Study]] = empty_list()
    has_output: List[Union[dict, DataObject]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.part_of = [v if isinstance(v, Study)
                        else Study(**v) for v in self.part_of]
        self.has_output = [v if isinstance(v, DataObject)
                           else DataObject(**v) for v in self.has_output]
        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    represents a person, such as a researcher
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Person
    class_class_curie: ClassVar[str] = "nmdc:Person"
    class_name: ClassVar[str] = "person"
    class_model_uri: ClassVar[URIRef] = NMDC.Person

    id: Optional[str] = None

@dataclass
class AttributeValue(YAMLRoot):
    """
    The value for any value of a attribute for a sample. This object can hold both the un-normalized atomic value and
    the structured value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.AttributeValue
    class_class_curie: ClassVar[str] = "nmdc:AttributeValue"
    class_name: ClassVar[str] = "attribute value"
    class_model_uri: ClassVar[URIRef] = NMDC.AttributeValue

    has_raw_value: Optional[str] = None

@dataclass
class QuantityValue(AttributeValue):
    """
    A simple quantity, e.g. 2cm
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.QuantityValue
    class_class_curie: ClassVar[str] = "nmdc:QuantityValue"
    class_name: ClassVar[str] = "quantity value"
    class_model_uri: ClassVar[URIRef] = NMDC.QuantityValue

    has_unit: List[Union[dict, "Unit"]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        self.has_unit = [v if isinstance(v, Unit)
                         else Unit(**v) for v in self.has_unit]
        super().__post_init__(**kwargs)


@dataclass
class TextValue(AttributeValue):
    """
    A basic string value
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.TextValue
    class_class_curie: ClassVar[str] = "nmdc:TextValue"
    class_name: ClassVar[str] = "text value"
    class_model_uri: ClassVar[URIRef] = NMDC.TextValue

    language: Optional[str] = None

class UrlValue(AttributeValue):
    """
    A value that is a string that conforms to URL syntax
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.UrlValue
    class_class_curie: ClassVar[str] = "nmdc:UrlValue"
    class_name: ClassVar[str] = "url value"
    class_model_uri: ClassVar[URIRef] = NMDC.UrlValue


class TimestampValue(AttributeValue):
    """
    A value that is a timestamp. The range should be ISO-8601
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.TimestampValue
    class_class_curie: ClassVar[str] = "nmdc:TimestampValue"
    class_name: ClassVar[str] = "timestamp value"
    class_model_uri: ClassVar[URIRef] = NMDC.TimestampValue


class IntegerValue(AttributeValue):
    """
    A value that is an integer
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.IntegerValue
    class_class_curie: ClassVar[str] = "nmdc:IntegerValue"
    class_name: ClassVar[str] = "integer value"
    class_model_uri: ClassVar[URIRef] = NMDC.IntegerValue


@dataclass
class BooleanValue(AttributeValue):
    """
    A value that is a boolean
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.BooleanValue
    class_class_curie: ClassVar[str] = "nmdc:BooleanValue"
    class_name: ClassVar[str] = "boolean value"
    class_model_uri: ClassVar[URIRef] = NMDC.BooleanValue

    has_numeric_value: Optional[float] = None

class ControlledTermValue(AttributeValue):
    """
    A controlled term or class from an ontology
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.ControlledTermValue
    class_class_curie: ClassVar[str] = "nmdc:ControlledTermValue"
    class_name: ClassVar[str] = "controlled term value"
    class_model_uri: ClassVar[URIRef] = NMDC.ControlledTermValue


@dataclass
class GeolocationValue(AttributeValue):
    """
    A normalized value for a location on the earth's surface
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.GeolocationValue
    class_class_curie: ClassVar[str] = "nmdc:GeolocationValue"
    class_name: ClassVar[str] = "geolocation value"
    class_model_uri: ClassVar[URIRef] = NMDC.GeolocationValue

    has_raw_value: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class Unit(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Unit
    class_class_curie: ClassVar[str] = "nmdc:Unit"
    class_name: ClassVar[str] = "unit"
    class_model_uri: ClassVar[URIRef] = NMDC.Unit


class OntologyClass(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.OntologyClass
    class_class_curie: ClassVar[str] = "nmdc:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = NMDC.OntologyClass


class EnvironmentalMaterialTerm(OntologyClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.EnvironmentalMaterialTerm
    class_class_curie: ClassVar[str] = "nmdc:EnvironmentalMaterialTerm"
    class_name: ClassVar[str] = "environmental material term"
    class_model_uri: ClassVar[URIRef] = NMDC.EnvironmentalMaterialTerm



# Slots
class slots:
    pass

slots.id = Slot(uri=NMDC.id, name="id", curie=NMDC.curie('id'),
                      model_uri=NMDC.id, domain=None, range=Optional[str])

slots.name = Slot(uri=NMDC.name, name="name", curie=NMDC.curie('name'),
                      model_uri=NMDC.name, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                      model_uri=NMDC.description, domain=None, range=Optional[str])

slots.annotations = Slot(uri=NMDC.annotations, name="annotations", curie=NMDC.curie('annotations'),
                      model_uri=NMDC.annotations, domain=None, range=List[str])

slots.attribute = Slot(uri=NMDC.attribute, name="attribute", curie=NMDC.curie('attribute'),
                      model_uri=NMDC.attribute, domain=NamedThing, range=Optional[str])

slots.has_raw_value = Slot(uri=NMDC.has_raw_value, name="has raw value", curie=NMDC.curie('has_raw_value'),
                      model_uri=NMDC.has_raw_value, domain=AttributeValue, range=Optional[str])

slots.has_unit = Slot(uri=NMDC.has_unit, name="has unit", curie=NMDC.curie('has_unit'),
                      model_uri=NMDC.has_unit, domain=None, range=List[Union[dict, Unit]], mappings = [QUD.unit])

slots.has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="has numeric value", curie=NMDC.curie('has_numeric_value'),
                      model_uri=NMDC.has_numeric_value, domain=None, range=Optional[float], mappings = [QUD.quantityValue])

slots.alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.alternate_identifiers, domain=None, range=List[str])

slots.latitude = Slot(uri=WGS.lat, name="latitude", curie=WGS.curie('lat'),
                      model_uri=NMDC.latitude, domain=GeolocationValue, range=Optional[float])

slots.longitude = Slot(uri=WGS.long, name="longitude", curie=WGS.curie('long'),
                      model_uri=NMDC.longitude, domain=GeolocationValue, range=Optional[float])

slots.has_input = Slot(uri=NMDC.has_input, name="has input", curie=NMDC.curie('has_input'),
                      model_uri=NMDC.has_input, domain=NamedThing, range=List[str])

slots.has_output = Slot(uri=NMDC.has_output, name="has output", curie=NMDC.curie('has_output'),
                      model_uri=NMDC.has_output, domain=None, range=List[str])

slots.part_of = Slot(uri=DCTERMS.isPartOf, name="part of", curie=DCTERMS.curie('isPartOf'),
                      model_uri=NMDC.part_of, domain=NamedThing, range=List[str])

slots.language = Slot(uri=NMDC.language, name="language", curie=NMDC.curie('language'),
                      model_uri=NMDC.language, domain=None, range=Optional[str])

slots.file_size = Slot(uri=NMDC.file_size, name="file_size", curie=NMDC.curie('file_size'),
                      model_uri=NMDC.file_size, domain=NamedThing, range=Optional[str])

slots.gold_path_field = Slot(uri=NMDC.gold_path_field, name="gold_path_field", curie=NMDC.curie('gold_path_field'),
                      model_uri=NMDC.gold_path_field, domain=NamedThing, range=Optional[str])

slots.ecosystem = Slot(uri=NMDC.ecosystem, name="ecosystem", curie=NMDC.curie('ecosystem'),
                      model_uri=NMDC.ecosystem, domain=NamedThing, range=Optional[str])

slots.ecosystem_category = Slot(uri=NMDC.ecosystem_category, name="ecosystem_category", curie=NMDC.curie('ecosystem_category'),
                      model_uri=NMDC.ecosystem_category, domain=NamedThing, range=Optional[str])

slots.ecosystem_type = Slot(uri=NMDC.ecosystem_type, name="ecosystem_type", curie=NMDC.curie('ecosystem_type'),
                      model_uri=NMDC.ecosystem_type, domain=NamedThing, range=Optional[str])

slots.ecosystem_subtype = Slot(uri=NMDC.ecosystem_subtype, name="ecosystem_subtype", curie=NMDC.curie('ecosystem_subtype'),
                      model_uri=NMDC.ecosystem_subtype, domain=NamedThing, range=Optional[str])

slots.specific_ecosystem = Slot(uri=NMDC.specific_ecosystem, name="specific_ecosystem", curie=NMDC.curie('specific_ecosystem'),
                      model_uri=NMDC.specific_ecosystem, domain=NamedThing, range=Optional[str])

slots.biosample_id = Slot(uri=NMDC.id, name="biosample_id", curie=NMDC.curie('id'),
                      model_uri=NMDC.biosample_id, domain=Biosample, range=Optional[str])

slots.biosample_name = Slot(uri=NMDC.name, name="biosample_name", curie=NMDC.curie('name'),
                      model_uri=NMDC.biosample_name, domain=Biosample, range=Optional[str])

slots.biosample_alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="biosample_alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.biosample_alternate_identifiers, domain=Biosample, range=List[str])

slots.biosample_lat_lon = Slot(uri=NMDC.lat_lon, name="biosample_lat_lon", curie=NMDC.curie('lat_lon'),
                      model_uri=NMDC.biosample_lat_lon, domain=Biosample, range=Union[dict, "GeolocationValue"])

slots.biosample_depth = Slot(uri=NMDC.depth, name="biosample_depth", curie=NMDC.curie('depth'),
                      model_uri=NMDC.biosample_depth, domain=Biosample, range=Optional[Union[dict, "TextValue"]])

slots.biosample_env_broad_scale = Slot(uri=NMDC.env_broad_scale, name="biosample_env_broad_scale", curie=NMDC.curie('env_broad_scale'),
                      model_uri=NMDC.biosample_env_broad_scale, domain=Biosample, range=Union[dict, "ControlledTermValue"])

slots.study_id = Slot(uri=NMDC.id, name="study_id", curie=NMDC.curie('id'),
                      model_uri=NMDC.study_id, domain=Study, range=Optional[str])

slots.study_name = Slot(uri=NMDC.name, name="study_name", curie=NMDC.curie('name'),
                      model_uri=NMDC.study_name, domain=Study, range=Optional[str])

slots.study_alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="study_alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.study_alternate_identifiers, domain=Study, range=List[str])

slots.biosample_processing_has_input = Slot(uri=NMDC.has_input, name="biosample processing_has input", curie=NMDC.curie('has_input'),
                      model_uri=NMDC.biosample_processing_has_input, domain=BiosampleProcessing, range=List[Union[dict, Biosample]])

slots.omics_processing_id = Slot(uri=NMDC.id, name="omics processing_id", curie=NMDC.curie('id'),
                      model_uri=NMDC.omics_processing_id, domain=OmicsProcessing, range=Optional[str])

slots.omics_processing_name = Slot(uri=NMDC.name, name="omics processing_name", curie=NMDC.curie('name'),
                      model_uri=NMDC.omics_processing_name, domain=OmicsProcessing, range=Optional[str])

slots.omics_processing_alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="omics processing_alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.omics_processing_alternate_identifiers, domain=OmicsProcessing, range=List[str])

slots.omics_processing_part_of = Slot(uri=NMDC.part_of, name="omics processing_part of", curie=NMDC.curie('part_of'),
                      model_uri=NMDC.omics_processing_part_of, domain=OmicsProcessing, range=List[Union[dict, Study]])

slots.omics_processing_has_output = Slot(uri=NMDC.has_output, name="omics processing_has output", curie=NMDC.curie('has_output'),
                      model_uri=NMDC.omics_processing_has_output, domain=OmicsProcessing, range=List[Union[dict, DataObject]])

slots.person_id = Slot(uri=NMDC.id, name="person_id", curie=NMDC.curie('id'),
                      model_uri=NMDC.person_id, domain=Person, range=Optional[str])

slots.geolocation_value_has_raw_value = Slot(uri=NMDC.has_raw_value, name="geolocation value_has raw value", curie=NMDC.curie('has_raw_value'),
                      model_uri=NMDC.geolocation_value_has_raw_value, domain=GeolocationValue, range=Optional[str])
