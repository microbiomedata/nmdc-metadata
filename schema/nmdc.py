# Auto generated from nmdc.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-06-02 21:53
# Schema: NMDC Schema
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
from biolinkml.utils.metamodelcore import Bool
from includes.types import Boolean, Double, Float, String

metamodel_version = "1.4.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
MIXS = CurieNamespace('MIxS', 'http://example.org/UNKNOWN/MIxS/')
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
class Database(YAMLRoot):
    """
    top level holder class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Database
    class_class_curie: ClassVar[str] = "nmdc:Database"
    class_name: ClassVar[str] = "database"
    class_model_uri: ClassVar[URIRef] = NMDC.Database

    biosample_set: Optional[Union[dict, "Biosample"]] = None
    data_object_set: Optional[Union[dict, "DataObject"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.biosample_set is not None and not isinstance(self.biosample_set, Biosample):
            self.biosample_set = Biosample(**self.biosample_set)
        if self.data_object_set is not None and not isinstance(self.data_object_set, DataObject):
            self.data_object_set = DataObject(**self.data_object_set)
        super().__post_init__(**kwargs)


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

@dataclass
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

    file_size: Optional[str] = None

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
    env_local_scale: Union[dict, "ControlledTermValue"] = None
    env_medium: Union[dict, "ControlledTermValue"] = None
    id: Optional[str] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()
    depth: Optional[Union[dict, "TextValue"]] = None
    alt: Optional[Union[dict, "QuantityValue"]] = None
    elev: Optional[Union[dict, "QuantityValue"]] = None
    geo_loc_name: Optional[Union[dict, "TextValue"]] = None
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_type: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    specific_ecosystem: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.depth is not None and not isinstance(self.depth, TextValue):
            self.depth = TextValue(**self.depth)
        if self.lat_lon is None:
            raise ValueError(f"lat_lon must be supplied")
        if not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**self.lat_lon)
        if self.alt is not None and not isinstance(self.alt, QuantityValue):
            self.alt = QuantityValue(**self.alt)
        if self.elev is not None and not isinstance(self.elev, QuantityValue):
            self.elev = QuantityValue(**self.elev)
        if self.geo_loc_name is not None and not isinstance(self.geo_loc_name, TextValue):
            self.geo_loc_name = TextValue(**self.geo_loc_name)
        if self.collection_date is not None and not isinstance(self.collection_date, TimestampValue):
            self.collection_date = TimestampValue(**self.collection_date)
        if self.env_broad_scale is None:
            raise ValueError(f"env_broad_scale must be supplied")
        if not isinstance(self.env_broad_scale, ControlledTermValue):
            self.env_broad_scale = ControlledTermValue(**self.env_broad_scale)
        if self.env_local_scale is None:
            raise ValueError(f"env_local_scale must be supplied")
        if not isinstance(self.env_local_scale, ControlledTermValue):
            self.env_local_scale = ControlledTermValue(**self.env_local_scale)
        if self.env_medium is None:
            raise ValueError(f"env_medium must be supplied")
        if not isinstance(self.env_medium, ControlledTermValue):
            self.env_medium = ControlledTermValue(**self.env_medium)
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
    submitted_to_insdc: Optional[Union[dict, "TextValue"]] = None
    investigation_type: Optional[Union[dict, "TextValue"]] = None
    project_name: Optional[Union[dict, "TextValue"]] = None
    experimental_factor: Optional[Union[dict, "ControlledTermValue"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.submitted_to_insdc is not None and not isinstance(self.submitted_to_insdc, TextValue):
            self.submitted_to_insdc = TextValue(**self.submitted_to_insdc)
        if self.investigation_type is not None and not isinstance(self.investigation_type, TextValue):
            self.investigation_type = TextValue(**self.investigation_type)
        if self.project_name is not None and not isinstance(self.project_name, TextValue):
            self.project_name = TextValue(**self.project_name)
        if self.experimental_factor is not None and not isinstance(self.experimental_factor, ControlledTermValue):
            self.experimental_factor = ControlledTermValue(**self.experimental_factor)
        super().__post_init__(**kwargs)


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

    has_raw_value: Optional[str] = None
    has_unit: List[Union[dict, "Unit"]] = empty_list()
    has_numeric_value: Optional[float] = None

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


@dataclass
class IntegerValue(AttributeValue):
    """
    A value that is an integer
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.IntegerValue
    class_class_curie: ClassVar[str] = "nmdc:IntegerValue"
    class_name: ClassVar[str] = "integer value"
    class_model_uri: ClassVar[URIRef] = NMDC.IntegerValue

    has_numeric_value: Optional[str] = None

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

    has_boolean_value: Optional[Bool] = None

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

slots.biosample_set = Slot(uri=NMDC.biosample_set, name="biosample set", curie=NMDC.curie('biosample_set'),
                      model_uri=NMDC.biosample_set, domain=Database, range=Optional[Union[dict, "Biosample"]])

slots.data_object_set = Slot(uri=NMDC.data_object_set, name="data object set", curie=NMDC.curie('data_object_set'),
                      model_uri=NMDC.data_object_set, domain=Database, range=Optional[Union[dict, "DataObject"]])

slots.id = Slot(uri=NMDC.id, name="id", curie=NMDC.curie('id'),
                      model_uri=NMDC.id, domain=None, range=Optional[str])

slots.name = Slot(uri=NMDC.name, name="name", curie=NMDC.curie('name'),
                      model_uri=NMDC.name, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                      model_uri=NMDC.description, domain=None, range=Optional[str])

slots.annotations = Slot(uri=NMDC.annotations, name="annotations", curie=NMDC.curie('annotations'),
                      model_uri=NMDC.annotations, domain=None, range=List[str])

slots.attribute = Slot(uri=NMDC.attribute, name="attribute", curie=NMDC.curie('attribute'),
                      model_uri=NMDC.attribute, domain=None, range=Optional[str])

slots.has_raw_value = Slot(uri=NMDC.has_raw_value, name="has raw value", curie=NMDC.curie('has_raw_value'),
                      model_uri=NMDC.has_raw_value, domain=AttributeValue, range=Optional[str])

slots.has_unit = Slot(uri=NMDC.has_unit, name="has unit", curie=NMDC.curie('has_unit'),
                      model_uri=NMDC.has_unit, domain=None, range=List[Union[dict, Unit]], mappings = [QUD.unit])

slots.has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="has numeric value", curie=NMDC.curie('has_numeric_value'),
                      model_uri=NMDC.has_numeric_value, domain=None, range=Optional[str], mappings = [QUD.quantityValue])

slots.has_boolean_value = Slot(uri=NMDC.has_boolean_value, name="has boolean value", curie=NMDC.curie('has_boolean_value'),
                      model_uri=NMDC.has_boolean_value, domain=None, range=Optional[Bool])

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
                      model_uri=NMDC.file_size, domain=None, range=Optional[str])

slots.gold_path_field = Slot(uri=NMDC.gold_path_field, name="gold_path_field", curie=NMDC.curie('gold_path_field'),
                      model_uri=NMDC.gold_path_field, domain=None, range=Optional[str])

slots.ecosystem = Slot(uri=NMDC.ecosystem, name="ecosystem", curie=NMDC.curie('ecosystem'),
                      model_uri=NMDC.ecosystem, domain=None, range=Optional[str])

slots.ecosystem_category = Slot(uri=NMDC.ecosystem_category, name="ecosystem_category", curie=NMDC.curie('ecosystem_category'),
                      model_uri=NMDC.ecosystem_category, domain=None, range=Optional[str])

slots.ecosystem_type = Slot(uri=NMDC.ecosystem_type, name="ecosystem_type", curie=NMDC.curie('ecosystem_type'),
                      model_uri=NMDC.ecosystem_type, domain=None, range=Optional[str])

slots.ecosystem_subtype = Slot(uri=NMDC.ecosystem_subtype, name="ecosystem_subtype", curie=NMDC.curie('ecosystem_subtype'),
                      model_uri=NMDC.ecosystem_subtype, domain=None, range=Optional[str])

slots.specific_ecosystem = Slot(uri=NMDC.specific_ecosystem, name="specific_ecosystem", curie=NMDC.curie('specific_ecosystem'),
                      model_uri=NMDC.specific_ecosystem, domain=None, range=Optional[str])

slots.submitted_to_insdc = Slot(uri="str(uriorcurie)", name="submitted_to_insdc", curie=None,
                      model_uri=NMDC.submitted_to_insdc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.submitted_to_insdc])

slots.investigation_type = Slot(uri="str(uriorcurie)", name="investigation_type", curie=None,
                      model_uri=NMDC.investigation_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.investigation_type])

slots.project_name = Slot(uri="str(uriorcurie)", name="project_name", curie=None,
                      model_uri=NMDC.project_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.project_name])

slots.experimental_factor = Slot(uri="str(uriorcurie)", name="experimental_factor", curie=None,
                      model_uri=NMDC.experimental_factor, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.experimental_factor])

slots.lat_lon = Slot(uri="str(uriorcurie)", name="lat_lon", curie=None,
                      model_uri=NMDC.lat_lon, domain=None, range=Optional[Union[dict, GeolocationValue]], mappings = [MIXS.lat_lon])

slots.depth = Slot(uri="str(uriorcurie)", name="depth", curie=None,
                      model_uri=NMDC.depth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.depth])

slots.alt = Slot(uri="str(uriorcurie)", name="alt", curie=None,
                      model_uri=NMDC.alt, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.alt])

slots.elev = Slot(uri="str(uriorcurie)", name="elev", curie=None,
                      model_uri=NMDC.elev, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.elev])

slots.geo_loc_name = Slot(uri="str(uriorcurie)", name="geo_loc_name", curie=None,
                      model_uri=NMDC.geo_loc_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.geo_loc_name])

slots.collection_date = Slot(uri="str(uriorcurie)", name="collection_date", curie=None,
                      model_uri=NMDC.collection_date, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.collection_date])

slots.env_broad_scale = Slot(uri="str(uriorcurie)", name="env_broad_scale", curie=None,
                      model_uri=NMDC.env_broad_scale, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.env_broad_scale])

slots.env_local_scale = Slot(uri="str(uriorcurie)", name="env_local_scale", curie=None,
                      model_uri=NMDC.env_local_scale, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.env_local_scale])

slots.env_medium = Slot(uri="str(uriorcurie)", name="env_medium", curie=None,
                      model_uri=NMDC.env_medium, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.env_medium])

slots.env_package = Slot(uri="str(uriorcurie)", name="env_package", curie=None,
                      model_uri=NMDC.env_package, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.env_package])

slots.subspecf_gen_lin = Slot(uri="str(uriorcurie)", name="subspecf_gen_lin", curie=None,
                      model_uri=NMDC.subspecf_gen_lin, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.subspecf_gen_lin])

slots.ploidy = Slot(uri="str(uriorcurie)", name="ploidy", curie=None,
                      model_uri=NMDC.ploidy, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.ploidy])

slots.num_replicons = Slot(uri="str(uriorcurie)", name="num_replicons", curie=None,
                      model_uri=NMDC.num_replicons, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.num_replicons])

slots.extrachrom_elements = Slot(uri="str(uriorcurie)", name="extrachrom_elements", curie=None,
                      model_uri=NMDC.extrachrom_elements, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.extrachrom_elements])

slots.estimated_size = Slot(uri="str(uriorcurie)", name="estimated_size", curie=None,
                      model_uri=NMDC.estimated_size, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.estimated_size])

slots.ref_biomaterial = Slot(uri="str(uriorcurie)", name="ref_biomaterial", curie=None,
                      model_uri=NMDC.ref_biomaterial, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ref_biomaterial])

slots.source_mat_id = Slot(uri="str(uriorcurie)", name="source_mat_id", curie=None,
                      model_uri=NMDC.source_mat_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.source_mat_id])

slots.pathogenicity = Slot(uri="str(uriorcurie)", name="pathogenicity", curie=None,
                      model_uri=NMDC.pathogenicity, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pathogenicity])

slots.biotic_relationship = Slot(uri="str(uriorcurie)", name="biotic_relationship", curie=None,
                      model_uri=NMDC.biotic_relationship, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.biotic_relationship])

slots.specific_host = Slot(uri="str(uriorcurie)", name="specific_host", curie=None,
                      model_uri=NMDC.specific_host, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.specific_host])

slots.host_spec_range = Slot(uri="str(uriorcurie)", name="host_spec_range", curie=None,
                      model_uri=NMDC.host_spec_range, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_spec_range])

slots.health_disease_stat = Slot(uri="str(uriorcurie)", name="health_disease_stat", curie=None,
                      model_uri=NMDC.health_disease_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.health_disease_stat])

slots.trophic_level = Slot(uri="str(uriorcurie)", name="trophic_level", curie=None,
                      model_uri=NMDC.trophic_level, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.trophic_level])

slots.propagation = Slot(uri="str(uriorcurie)", name="propagation", curie=None,
                      model_uri=NMDC.propagation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.propagation])

slots.encoded_traits = Slot(uri="str(uriorcurie)", name="encoded_traits", curie=None,
                      model_uri=NMDC.encoded_traits, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.encoded_traits])

slots.rel_to_oxygen = Slot(uri="str(uriorcurie)", name="rel_to_oxygen", curie=None,
                      model_uri=NMDC.rel_to_oxygen, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.rel_to_oxygen])

slots.isol_growth_condt = Slot(uri="str(uriorcurie)", name="isol_growth_condt", curie=None,
                      model_uri=NMDC.isol_growth_condt, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.isol_growth_condt])

slots.samp_collect_device = Slot(uri="str(uriorcurie)", name="samp_collect_device", curie=None,
                      model_uri=NMDC.samp_collect_device, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_collect_device])

slots.samp_mat_process = Slot(uri="str(uriorcurie)", name="samp_mat_process", curie=None,
                      model_uri=NMDC.samp_mat_process, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.samp_mat_process])

slots.size_frac = Slot(uri="str(uriorcurie)", name="size_frac", curie=None,
                      model_uri=NMDC.size_frac, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.size_frac])

slots.samp_size = Slot(uri="str(uriorcurie)", name="samp_size", curie=None,
                      model_uri=NMDC.samp_size, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_size])

slots.source_uvig = Slot(uri="str(uriorcurie)", name="source_uvig", curie=None,
                      model_uri=NMDC.source_uvig, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.source_uvig])

slots.virus_enrich_appr = Slot(uri="str(uriorcurie)", name="virus_enrich_appr", curie=None,
                      model_uri=NMDC.virus_enrich_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.virus_enrich_appr])

slots.nucl_acid_ext = Slot(uri="str(uriorcurie)", name="nucl_acid_ext", curie=None,
                      model_uri=NMDC.nucl_acid_ext, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.nucl_acid_ext])

slots.nucl_acid_amp = Slot(uri="str(uriorcurie)", name="nucl_acid_amp", curie=None,
                      model_uri=NMDC.nucl_acid_amp, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.nucl_acid_amp])

slots.lib_size = Slot(uri="str(uriorcurie)", name="lib_size", curie=None,
                      model_uri=NMDC.lib_size, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_size])

slots.lib_reads_seqd = Slot(uri="str(uriorcurie)", name="lib_reads_seqd", curie=None,
                      model_uri=NMDC.lib_reads_seqd, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_reads_seqd])

slots.lib_layout = Slot(uri="str(uriorcurie)", name="lib_layout", curie=None,
                      model_uri=NMDC.lib_layout, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_layout])

slots.lib_vector = Slot(uri="str(uriorcurie)", name="lib_vector", curie=None,
                      model_uri=NMDC.lib_vector, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_vector])

slots.lib_screen = Slot(uri="str(uriorcurie)", name="lib_screen", curie=None,
                      model_uri=NMDC.lib_screen, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lib_screen])

slots.target_gene = Slot(uri="str(uriorcurie)", name="target_gene", curie=None,
                      model_uri=NMDC.target_gene, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.target_gene])

slots.target_subfragment = Slot(uri="str(uriorcurie)", name="target_subfragment", curie=None,
                      model_uri=NMDC.target_subfragment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.target_subfragment])

slots.pcr_primers = Slot(uri="str(uriorcurie)", name="pcr_primers", curie=None,
                      model_uri=NMDC.pcr_primers, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pcr_primers])

slots.mid = Slot(uri="str(uriorcurie)", name="mid", curie=None,
                      model_uri=NMDC.mid, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mid])

slots.adapters = Slot(uri="str(uriorcurie)", name="adapters", curie=None,
                      model_uri=NMDC.adapters, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.adapters])

slots.pcr_cond = Slot(uri="str(uriorcurie)", name="pcr_cond", curie=None,
                      model_uri=NMDC.pcr_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pcr_cond])

slots.seq_meth = Slot(uri="str(uriorcurie)", name="seq_meth", curie=None,
                      model_uri=NMDC.seq_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.seq_meth])

slots.seq_quality_check = Slot(uri="str(uriorcurie)", name="seq_quality_check", curie=None,
                      model_uri=NMDC.seq_quality_check, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.seq_quality_check])

slots.chimera_check = Slot(uri="str(uriorcurie)", name="chimera_check", curie=None,
                      model_uri=NMDC.chimera_check, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.chimera_check])

slots.tax_ident = Slot(uri="str(uriorcurie)", name="tax_ident", curie=None,
                      model_uri=NMDC.tax_ident, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tax_ident])

slots.assembly_qual = Slot(uri="str(uriorcurie)", name="assembly_qual", curie=None,
                      model_uri=NMDC.assembly_qual, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.assembly_qual])

slots.assembly_name = Slot(uri="str(uriorcurie)", name="assembly_name", curie=None,
                      model_uri=NMDC.assembly_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.assembly_name])

slots.assembly_software = Slot(uri="str(uriorcurie)", name="assembly_software", curie=None,
                      model_uri=NMDC.assembly_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.assembly_software])

slots.annot = Slot(uri="str(uriorcurie)", name="annot", curie=None,
                      model_uri=NMDC.annot, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.annot])

slots.number_contig = Slot(uri="str(uriorcurie)", name="number_contig", curie=None,
                      model_uri=NMDC.number_contig, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.number_contig])

slots.feat_pred = Slot(uri="str(uriorcurie)", name="feat_pred", curie=None,
                      model_uri=NMDC.feat_pred, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.feat_pred])

slots.ref_db = Slot(uri="str(uriorcurie)", name="ref_db", curie=None,
                      model_uri=NMDC.ref_db, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ref_db])

slots.sim_search_meth = Slot(uri="str(uriorcurie)", name="sim_search_meth", curie=None,
                      model_uri=NMDC.sim_search_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sim_search_meth])

slots.tax_class = Slot(uri="str(uriorcurie)", name="tax_class", curie=None,
                      model_uri=NMDC.tax_class, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tax_class])

slots._16s_recover = Slot(uri="str(uriorcurie)", name="_16s_recover", curie=None,
                      model_uri=NMDC._16s_recover, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS._16s_recover])

slots._16s_recover_software = Slot(uri="str(uriorcurie)", name="_16s_recover_software", curie=None,
                      model_uri=NMDC._16s_recover_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS._16s_recover_software])

slots.trnas = Slot(uri="str(uriorcurie)", name="trnas", curie=None,
                      model_uri=NMDC.trnas, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.trnas])

slots.trna_ext_software = Slot(uri="str(uriorcurie)", name="trna_ext_software", curie=None,
                      model_uri=NMDC.trna_ext_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.trna_ext_software])

slots.compl_score = Slot(uri="str(uriorcurie)", name="compl_score", curie=None,
                      model_uri=NMDC.compl_score, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.compl_score])

slots.compl_software = Slot(uri="str(uriorcurie)", name="compl_software", curie=None,
                      model_uri=NMDC.compl_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.compl_software])

slots.compl_appr = Slot(uri="str(uriorcurie)", name="compl_appr", curie=None,
                      model_uri=NMDC.compl_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.compl_appr])

slots.contam_score = Slot(uri="str(uriorcurie)", name="contam_score", curie=None,
                      model_uri=NMDC.contam_score, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.contam_score])

slots.contam_screen_input = Slot(uri="str(uriorcurie)", name="contam_screen_input", curie=None,
                      model_uri=NMDC.contam_screen_input, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.contam_screen_input])

slots.contam_screen_param = Slot(uri="str(uriorcurie)", name="contam_screen_param", curie=None,
                      model_uri=NMDC.contam_screen_param, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.contam_screen_param])

slots.decontam_software = Slot(uri="str(uriorcurie)", name="decontam_software", curie=None,
                      model_uri=NMDC.decontam_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.decontam_software])

slots.sort_tech = Slot(uri="str(uriorcurie)", name="sort_tech", curie=None,
                      model_uri=NMDC.sort_tech, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sort_tech])

slots.single_cell_lysis_appr = Slot(uri="str(uriorcurie)", name="single_cell_lysis_appr", curie=None,
                      model_uri=NMDC.single_cell_lysis_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.single_cell_lysis_appr])

slots.single_cell_lysis_prot = Slot(uri="str(uriorcurie)", name="single_cell_lysis_prot", curie=None,
                      model_uri=NMDC.single_cell_lysis_prot, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.single_cell_lysis_prot])

slots.wga_amp_appr = Slot(uri="str(uriorcurie)", name="wga_amp_appr", curie=None,
                      model_uri=NMDC.wga_amp_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wga_amp_appr])

slots.wga_amp_kit = Slot(uri="str(uriorcurie)", name="wga_amp_kit", curie=None,
                      model_uri=NMDC.wga_amp_kit, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wga_amp_kit])

slots.bin_param = Slot(uri="str(uriorcurie)", name="bin_param", curie=None,
                      model_uri=NMDC.bin_param, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.bin_param])

slots.bin_software = Slot(uri="str(uriorcurie)", name="bin_software", curie=None,
                      model_uri=NMDC.bin_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.bin_software])

slots.reassembly_bin = Slot(uri="str(uriorcurie)", name="reassembly_bin", curie=None,
                      model_uri=NMDC.reassembly_bin, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.reassembly_bin])

slots.mag_cov_software = Slot(uri="str(uriorcurie)", name="mag_cov_software", curie=None,
                      model_uri=NMDC.mag_cov_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mag_cov_software])

slots.vir_ident_software = Slot(uri="str(uriorcurie)", name="vir_ident_software", curie=None,
                      model_uri=NMDC.vir_ident_software, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.vir_ident_software])

slots.pred_genome_type = Slot(uri="str(uriorcurie)", name="pred_genome_type", curie=None,
                      model_uri=NMDC.pred_genome_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pred_genome_type])

slots.pred_genome_struc = Slot(uri="str(uriorcurie)", name="pred_genome_struc", curie=None,
                      model_uri=NMDC.pred_genome_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pred_genome_struc])

slots.detec_type = Slot(uri="str(uriorcurie)", name="detec_type", curie=None,
                      model_uri=NMDC.detec_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.detec_type])

slots.votu_class_appr = Slot(uri="str(uriorcurie)", name="votu_class_appr", curie=None,
                      model_uri=NMDC.votu_class_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.votu_class_appr])

slots.votu_seq_comp_appr = Slot(uri="str(uriorcurie)", name="votu_seq_comp_appr", curie=None,
                      model_uri=NMDC.votu_seq_comp_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.votu_seq_comp_appr])

slots.votu_db = Slot(uri="str(uriorcurie)", name="votu_db", curie=None,
                      model_uri=NMDC.votu_db, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.votu_db])

slots.host_pred_appr = Slot(uri="str(uriorcurie)", name="host_pred_appr", curie=None,
                      model_uri=NMDC.host_pred_appr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_pred_appr])

slots.host_pred_est_acc = Slot(uri="str(uriorcurie)", name="host_pred_est_acc", curie=None,
                      model_uri=NMDC.host_pred_est_acc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_pred_est_acc])

slots.url = Slot(uri="str(uriorcurie)", name="url", curie=None,
                      model_uri=NMDC.url, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.url])

slots.sop = Slot(uri="str(uriorcurie)", name="sop", curie=None,
                      model_uri=NMDC.sop, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sop])

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

slots.biosample_env_local_scale = Slot(uri=NMDC.env_local_scale, name="biosample_env_local_scale", curie=NMDC.curie('env_local_scale'),
                      model_uri=NMDC.biosample_env_local_scale, domain=Biosample, range=Union[dict, "ControlledTermValue"])

slots.biosample_env_medium = Slot(uri=NMDC.env_medium, name="biosample_env_medium", curie=NMDC.curie('env_medium'),
                      model_uri=NMDC.biosample_env_medium, domain=Biosample, range=Union[dict, "ControlledTermValue"])

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

slots.quantity_value_has_raw_value = Slot(uri=NMDC.has_raw_value, name="quantity value_has raw value", curie=NMDC.curie('has_raw_value'),
                      model_uri=NMDC.quantity_value_has_raw_value, domain=QuantityValue, range=Optional[str])

slots.quantity_value_has_unit = Slot(uri=NMDC.has_unit, name="quantity value_has unit", curie=NMDC.curie('has_unit'),
                      model_uri=NMDC.quantity_value_has_unit, domain=QuantityValue, range=List[Union[dict, "Unit"]])

slots.quantity_value_has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="quantity value_has numeric value", curie=NMDC.curie('has_numeric_value'),
                      model_uri=NMDC.quantity_value_has_numeric_value, domain=QuantityValue, range=Optional[float])

slots.geolocation_value_has_raw_value = Slot(uri=NMDC.has_raw_value, name="geolocation value_has raw value", curie=NMDC.curie('has_raw_value'),
                      model_uri=NMDC.geolocation_value_has_raw_value, domain=GeolocationValue, range=Optional[str])
