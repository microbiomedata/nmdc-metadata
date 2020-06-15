# Auto generated from nmdc.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-06-15 11:15
# Schema: NMDC Schema
#
# id: https://microbiomedata/schema
# description: Schema for National Microbiome Data Collaborative (NMDC). This schem is organized into 3 separate
#              modules: * a set of core types for representing data values * the mixs schema (auto-translated from
#              mixs excel) * the NMDC schema itself
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
from includes.types import Boolean, Double, Float, Integer, String

metamodel_version = "1.4.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GOLD = CurieNamespace('GOLD', 'https://identifiers.org/gold/')
MIXS = CurieNamespace('MIxS', 'http://example.org/UNKNOWN/MIxS/')
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
MIXS = CurieNamespace('mixs', 'https://w3id.org/gensc/')
NMDC = CurieNamespace('nmdc', 'https://microbiomedata/meta/')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDF = CurieNamespace('rdf', 'http://example.org/UNKNOWN/rdf/')
RDFS = CurieNamespace('rdfs', 'http://example.org/UNKNOWN/rdfs/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://example.org/UNKNOWN/skos/')
WGS = CurieNamespace('wgs', 'http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NMDC


# Types
class DecimalDegree(float):
    """ A decimal degree expresses latitude or longitude as decimal fractions. """
    type_class_uri = XSD.decimal
    type_class_curie = "xsd:decimal"
    type_name = "decimal degree"
    type_model_uri = NMDC.DecimalDegree


class LanguageCode(str):
    """ A language code conforming to ISO_639-1 """
    type_class_uri = XSD.language
    type_class_curie = "xsd:language"
    type_name = "language code"
    type_model_uri = NMDC.LanguageCode


class Unit(str):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "unit"
    type_model_uri = NMDC.Unit


# Class references
class NamedThingId(extended_str):
    pass


class DataObjectId(NamedThingId):
    pass


class BiosampleId(NamedThingId):
    pass


class StudyId(NamedThingId):
    pass


class BiosampleProcessingId(NamedThingId):
    pass


class OmicsProcessingId(BiosampleProcessingId):
    pass


class PersonId(NamedThingId):
    pass


class OntologyClassId(NamedThingId):
    pass


class EnvironmentalMaterialTermId(OntologyClassId):
    pass


class ActivityActivityId(extended_str):
    pass


@dataclass
class Database(YAMLRoot):
    """
    An abstract holder for any set of metadata and data. It does not need to correspond to an actual managed databse
    top level holder class. When translated to JSON-Schema this is the 'root' object. It should contain pointers to
    other objects of interest
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Database
    class_class_curie: ClassVar[str] = "nmdc:Database"
    class_name: ClassVar[str] = "database"
    class_model_uri: ClassVar[URIRef] = NMDC.Database

    biosample_set: Dict[Union[str, BiosampleId], Union[dict, "Biosample"]] = empty_dict()
    study_set: Dict[Union[str, StudyId], Union[dict, "Study"]] = empty_dict()
    data_object_set: Dict[Union[str, DataObjectId], Union[dict, "DataObject"]] = empty_dict()
    activity_set: Dict[Union[str, ActivityActivityId], Union[dict, "Activity"]] = empty_dict()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        for k, v in self.biosample_set.items():
            if not isinstance(v, Biosample):
                self.biosample_set[k] = Biosample(id=k, **({} if v is None else v))
        for k, v in self.study_set.items():
            if not isinstance(v, Study):
                self.study_set[k] = Study(id=k, **({} if v is None else v))
        for k, v in self.data_object_set.items():
            if not isinstance(v, DataObject):
                self.data_object_set[k] = DataObject(id=k, **({} if v is None else v))
        for k, v in self.activity_set.items():
            if not isinstance(v, Activity):
                self.activity_set[k] = Activity(activity_id=k, **({} if v is None else v))
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

    id: Union[str, NamedThingId]
    name: Optional[str] = None
    description: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[str, DataObjectId] = None
    file_size: Optional[int] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, DataObjectId):
            self.id = DataObjectId(self.id)
        super().__post_init__(**kwargs)


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

    id: Union[str, BiosampleId] = None
    lat_lon: Union[dict, "GeolocationValue"] = None
    env_broad_scale: Union[dict, "ControlledTermValue"] = None
    env_local_scale: Union[dict, "ControlledTermValue"] = None
    env_medium: Union[dict, "ControlledTermValue"] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()
    env_package: Optional[Union[dict, "TextValue"]] = None
    geo_loc_name: Optional[Union[dict, "TextValue"]] = None
    collection_date: Optional[Union[dict, "TimestampValue"]] = None
    depth: Optional[Union[dict, "QuantityValue"]] = None
    tot_org_carb: Optional[Union[dict, "QuantityValue"]] = None
    alt: Optional[Union[dict, "QuantityValue"]] = None
    elev: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)
        if self.env_package is not None and not isinstance(self.env_package, TextValue):
            self.env_package = TextValue(**self.env_package)
        if self.lat_lon is None:
            raise ValueError(f"lat_lon must be supplied")
        if not isinstance(self.lat_lon, GeolocationValue):
            self.lat_lon = GeolocationValue(**self.lat_lon)
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
        if self.depth is not None and not isinstance(self.depth, QuantityValue):
            self.depth = QuantityValue(**self.depth)
        if self.tot_org_carb is not None and not isinstance(self.tot_org_carb, QuantityValue):
            self.tot_org_carb = QuantityValue(**self.tot_org_carb)
        if self.alt is not None and not isinstance(self.alt, QuantityValue):
            self.alt = QuantityValue(**self.alt)
        if self.elev is not None and not isinstance(self.elev, QuantityValue):
            self.elev = QuantityValue(**self.elev)
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

    id: Union[str, StudyId] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()
    submitted_to_insdc: Optional[Union[dict, "BooleanValue"]] = None
    investigation_type: Optional[Union[dict, "TextValue"]] = None
    project_name: Optional[Union[dict, "TextValue"]] = None
    experimental_factor: Optional[Union[dict, "ControlledTermValue"]] = None
    ecosystem: Optional[str] = None
    ecosystem_category: Optional[str] = None
    ecosystem_type: Optional[str] = None
    ecosystem_subtype: Optional[str] = None
    specific_ecosystem: Optional[str] = None
    principal_investigator: Optional[Union[dict, "PersonValue"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)
        if self.submitted_to_insdc is not None and not isinstance(self.submitted_to_insdc, BooleanValue):
            self.submitted_to_insdc = BooleanValue(**self.submitted_to_insdc)
        if self.investigation_type is not None and not isinstance(self.investigation_type, TextValue):
            self.investigation_type = TextValue(**self.investigation_type)
        if self.project_name is not None and not isinstance(self.project_name, TextValue):
            self.project_name = TextValue(**self.project_name)
        if self.experimental_factor is not None and not isinstance(self.experimental_factor, ControlledTermValue):
            self.experimental_factor = ControlledTermValue(**self.experimental_factor)
        if self.principal_investigator is not None and not isinstance(self.principal_investigator, PersonValue):
            self.principal_investigator = PersonValue(**self.principal_investigator)
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

    id: Union[str, BiosampleProcessingId] = None
    has_input: List[Union[str, BiosampleId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, BiosampleProcessingId):
            self.id = BiosampleProcessingId(self.id)
        self.has_input = [v if isinstance(v, BiosampleId)
                          else BiosampleId(v) for v in self.has_input]
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

    id: Union[str, OmicsProcessingId] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()
    part_of: List[Union[str, StudyId]] = empty_list()
    has_output: List[Union[str, DataObjectId]] = empty_list()

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OmicsProcessingId):
            self.id = OmicsProcessingId(self.id)
        self.part_of = [v if isinstance(v, StudyId)
                        else StudyId(v) for v in self.part_of]
        self.has_output = [v if isinstance(v, DataObjectId)
                           else DataObjectId(v) for v in self.has_output]
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

    id: Union[str, PersonId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)
        super().__post_init__(**kwargs)


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
    was_generated_by: Optional[Union[str, ActivityActivityId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.was_generated_by is not None and not isinstance(self.was_generated_by, ActivityActivityId):
            self.was_generated_by = ActivityActivityId(self.was_generated_by)
        super().__post_init__(**kwargs)


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
    has_unit: Optional[str] = None
    has_numeric_value: Optional[float] = None

@dataclass
class PersonValue(AttributeValue):
    """
    An attribute value representing a person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.PersonValue
    class_class_curie: ClassVar[str] = "nmdc:PersonValue"
    class_name: ClassVar[str] = "person value"
    class_model_uri: ClassVar[URIRef] = NMDC.PersonValue

    has_raw_value: Optional[str] = None
    orcid: Optional[str] = None

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

    has_numeric_value: Optional[float] = None

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

@dataclass
class ControlledTermValue(AttributeValue):
    """
    A controlled term or class from an ontology
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.ControlledTermValue
    class_class_curie: ClassVar[str] = "nmdc:ControlledTermValue"
    class_name: ClassVar[str] = "controlled term value"
    class_model_uri: ClassVar[URIRef] = NMDC.ControlledTermValue

    term: Optional[Union[dict, "OntologyClass"]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.term is not None and not isinstance(self.term, OntologyClass):
            self.term = OntologyClass(self.term)
        super().__post_init__(**kwargs)


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

@dataclass
class OntologyClass(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.OntologyClass
    class_class_curie: ClassVar[str] = "nmdc:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = NMDC.OntologyClass

    id: Union[str, OntologyClassId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class EnvironmentalMaterialTerm(OntologyClass):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.EnvironmentalMaterialTerm
    class_class_curie: ClassVar[str] = "nmdc:EnvironmentalMaterialTerm"
    class_name: ClassVar[str] = "environmental material term"
    class_model_uri: ClassVar[URIRef] = NMDC.EnvironmentalMaterialTerm

    id: Union[str, EnvironmentalMaterialTermId] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.id is None:
            raise ValueError(f"id must be supplied")
        if not isinstance(self.id, EnvironmentalMaterialTermId):
            self.id = EnvironmentalMaterialTermId(self.id)
        super().__post_init__(**kwargs)


@dataclass
class Activity(YAMLRoot):
    """
    a provence-generating activity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Activity
    class_class_curie: ClassVar[str] = "nmdc:Activity"
    class_name: ClassVar[str] = "activity"
    class_model_uri: ClassVar[URIRef] = NMDC.Activity

    activity_id: Union[str, ActivityActivityId]
    started_at_time: Optional[str] = None
    ended_at_time: Optional[str] = None
    was_associated_with: Optional[Union[dict, "Agent"]] = None
    used: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.activity_id is None:
            raise ValueError(f"activity_id must be supplied")
        if not isinstance(self.activity_id, ActivityActivityId):
            self.activity_id = ActivityActivityId(self.activity_id)
        if self.was_associated_with is not None and not isinstance(self.was_associated_with, Agent):
            self.was_associated_with = Agent(**self.was_associated_with)
        super().__post_init__(**kwargs)


@dataclass
class Agent(YAMLRoot):
    """
    a provence-generating agent
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Agent
    class_class_curie: ClassVar[str] = "nmdc:Agent"
    class_name: ClassVar[str] = "agent"
    class_model_uri: ClassVar[URIRef] = NMDC.Agent

    acted_on_behalf_of: Optional[Union[dict, "Agent"]] = None
    was_informed_by: Optional[Union[str, ActivityActivityId]] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.acted_on_behalf_of is not None and not isinstance(self.acted_on_behalf_of, Agent):
            self.acted_on_behalf_of = Agent(**self.acted_on_behalf_of)
        if self.was_informed_by is not None and not isinstance(self.was_informed_by, ActivityActivityId):
            self.was_informed_by = ActivityActivityId(self.was_informed_by)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.biosample_set = Slot(uri=NMDC.biosample_set, name="biosample set", curie=NMDC.curie('biosample_set'),
                      model_uri=NMDC.biosample_set, domain=Database, range=Dict[Union[str, BiosampleId], Union[dict, "Biosample"]])

slots.study_set = Slot(uri=NMDC.study_set, name="study set", curie=NMDC.curie('study_set'),
                      model_uri=NMDC.study_set, domain=Database, range=Dict[Union[str, StudyId], Union[dict, "Study"]])

slots.data_object_set = Slot(uri=NMDC.data_object_set, name="data object set", curie=NMDC.curie('data_object_set'),
                      model_uri=NMDC.data_object_set, domain=Database, range=Dict[Union[str, DataObjectId], Union[dict, "DataObject"]])

slots.activity_set = Slot(uri=NMDC.activity_set, name="activity set", curie=NMDC.curie('activity_set'),
                      model_uri=NMDC.activity_set, domain=Database, range=Dict[Union[str, ActivityActivityId], Union[dict, "Activity"]])

slots.has_input = Slot(uri=NMDC.has_input, name="has input", curie=NMDC.curie('has_input'),
                      model_uri=NMDC.has_input, domain=None, range=List[str])

slots.has_output = Slot(uri=NMDC.has_output, name="has output", curie=NMDC.curie('has_output'),
                      model_uri=NMDC.has_output, domain=None, range=List[str])

slots.part_of = Slot(uri=DCTERMS.isPartOf, name="part of", curie=DCTERMS.curie('isPartOf'),
                      model_uri=NMDC.part_of, domain=NamedThing, range=List[str])

slots.file_size = Slot(uri=NMDC.file_size, name="file_size", curie=NMDC.curie('file_size'),
                      model_uri=NMDC.file_size, domain=None, range=Optional[int])

slots.principal_investigator = Slot(uri=NMDC.principal_investigator, name="principal investigator", curie=NMDC.curie('principal_investigator'),
                      model_uri=NMDC.principal_investigator, domain=None, range=Optional[Union[dict, PersonValue]])

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
                      model_uri=NMDC.submitted_to_insdc, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.submitted_to_insdc])

slots.investigation_type = Slot(uri="str(uriorcurie)", name="investigation_type", curie=None,
                      model_uri=NMDC.investigation_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.investigation_type])

slots.project_name = Slot(uri="str(uriorcurie)", name="project_name", curie=None,
                      model_uri=NMDC.project_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.project_name])

slots.experimental_factor = Slot(uri="str(uriorcurie)", name="experimental_factor", curie=None,
                      model_uri=NMDC.experimental_factor, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.experimental_factor])

slots.lat_lon = Slot(uri="str(uriorcurie)", name="lat_lon", curie=None,
                      model_uri=NMDC.lat_lon, domain=None, range=Optional[Union[dict, GeolocationValue]], mappings = [MIXS.lat_lon])

slots.depth = Slot(uri="str(uriorcurie)", name="depth", curie=None,
                      model_uri=NMDC.depth, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.depth])

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
                      model_uri=NMDC._16s_recover, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS._16s_recover])

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
                      model_uri=NMDC.reassembly_bin, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.reassembly_bin])

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

slots.barometric_press = Slot(uri="str(uriorcurie)", name="barometric_press", curie=None,
                      model_uri=NMDC.barometric_press, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.barometric_press])

slots.carb_dioxide = Slot(uri="str(uriorcurie)", name="carb_dioxide", curie=None,
                      model_uri=NMDC.carb_dioxide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.carb_dioxide])

slots.carb_monoxide = Slot(uri="str(uriorcurie)", name="carb_monoxide", curie=None,
                      model_uri=NMDC.carb_monoxide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.carb_monoxide])

slots.chem_administration = Slot(uri="str(uriorcurie)", name="chem_administration", curie=None,
                      model_uri=NMDC.chem_administration, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.chem_administration])

slots.humidity = Slot(uri="str(uriorcurie)", name="humidity", curie=None,
                      model_uri=NMDC.humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.humidity])

slots.methane = Slot(uri="str(uriorcurie)", name="methane", curie=None,
                      model_uri=NMDC.methane, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.methane])

slots.misc_param = Slot(uri="str(uriorcurie)", name="misc_param", curie=None,
                      model_uri=NMDC.misc_param, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.misc_param])

slots.organism_count = Slot(uri="str(uriorcurie)", name="organism_count", curie=None,
                      model_uri=NMDC.organism_count, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.organism_count])

slots.oxygen = Slot(uri="str(uriorcurie)", name="oxygen", curie=None,
                      model_uri=NMDC.oxygen, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.oxygen])

slots.oxy_stat_samp = Slot(uri="str(uriorcurie)", name="oxy_stat_samp", curie=None,
                      model_uri=NMDC.oxy_stat_samp, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.oxy_stat_samp])

slots.perturbation = Slot(uri="str(uriorcurie)", name="perturbation", curie=None,
                      model_uri=NMDC.perturbation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.perturbation])

slots.pollutants = Slot(uri="str(uriorcurie)", name="pollutants", curie=None,
                      model_uri=NMDC.pollutants, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.pollutants])

slots.resp_part_matter = Slot(uri="str(uriorcurie)", name="resp_part_matter", curie=None,
                      model_uri=NMDC.resp_part_matter, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.resp_part_matter])

slots.samp_salinity = Slot(uri="str(uriorcurie)", name="samp_salinity", curie=None,
                      model_uri=NMDC.samp_salinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_salinity])

slots.samp_store_dur = Slot(uri="str(uriorcurie)", name="samp_store_dur", curie=None,
                      model_uri=NMDC.samp_store_dur, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_store_dur])

slots.samp_store_loc = Slot(uri="str(uriorcurie)", name="samp_store_loc", curie=None,
                      model_uri=NMDC.samp_store_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_store_loc])

slots.samp_store_temp = Slot(uri="str(uriorcurie)", name="samp_store_temp", curie=None,
                      model_uri=NMDC.samp_store_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_store_temp])

slots.samp_vol_we_dna_ext = Slot(uri="str(uriorcurie)", name="samp_vol_we_dna_ext", curie=None,
                      model_uri=NMDC.samp_vol_we_dna_ext, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_vol_we_dna_ext])

slots.solar_irradiance = Slot(uri="str(uriorcurie)", name="solar_irradiance", curie=None,
                      model_uri=NMDC.solar_irradiance, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.solar_irradiance])

slots.temp = Slot(uri="str(uriorcurie)", name="temp", curie=None,
                      model_uri=NMDC.temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.temp])

slots.ventilation_rate = Slot(uri="str(uriorcurie)", name="ventilation_rate", curie=None,
                      model_uri=NMDC.ventilation_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ventilation_rate])

slots.ventilation_type = Slot(uri="str(uriorcurie)", name="ventilation_type", curie=None,
                      model_uri=NMDC.ventilation_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ventilation_type])

slots.volatile_org_comp = Slot(uri="str(uriorcurie)", name="volatile_org_comp", curie=None,
                      model_uri=NMDC.volatile_org_comp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.volatile_org_comp])

slots.wind_direction = Slot(uri="str(uriorcurie)", name="wind_direction", curie=None,
                      model_uri=NMDC.wind_direction, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wind_direction])

slots.wind_speed = Slot(uri="str(uriorcurie)", name="wind_speed", curie=None,
                      model_uri=NMDC.wind_speed, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.wind_speed])

slots.surf_material = Slot(uri="str(uriorcurie)", name="surf_material", curie=None,
                      model_uri=NMDC.surf_material, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.surf_material])

slots.surf_air_cont = Slot(uri="str(uriorcurie)", name="surf_air_cont", curie=None,
                      model_uri=NMDC.surf_air_cont, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.surf_air_cont])

slots.rel_air_humidity = Slot(uri="str(uriorcurie)", name="rel_air_humidity", curie=None,
                      model_uri=NMDC.rel_air_humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.rel_air_humidity])

slots.abs_air_humidity = Slot(uri="str(uriorcurie)", name="abs_air_humidity", curie=None,
                      model_uri=NMDC.abs_air_humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.abs_air_humidity])

slots.surf_humidity = Slot(uri="str(uriorcurie)", name="surf_humidity", curie=None,
                      model_uri=NMDC.surf_humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.surf_humidity])

slots.air_temp = Slot(uri="str(uriorcurie)", name="air_temp", curie=None,
                      model_uri=NMDC.air_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.air_temp])

slots.surf_temp = Slot(uri="str(uriorcurie)", name="surf_temp", curie=None,
                      model_uri=NMDC.surf_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.surf_temp])

slots.surf_moisture_ph = Slot(uri="str(uriorcurie)", name="surf_moisture_ph", curie=None,
                      model_uri=NMDC.surf_moisture_ph, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.surf_moisture_ph])

slots.build_occup_type = Slot(uri="str(uriorcurie)", name="build_occup_type", curie=None,
                      model_uri=NMDC.build_occup_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.build_occup_type])

slots.surf_moisture = Slot(uri="str(uriorcurie)", name="surf_moisture", curie=None,
                      model_uri=NMDC.surf_moisture, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.surf_moisture])

slots.dew_point = Slot(uri="str(uriorcurie)", name="dew_point", curie=None,
                      model_uri=NMDC.dew_point, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.dew_point])

slots.indoor_space = Slot(uri="str(uriorcurie)", name="indoor_space", curie=None,
                      model_uri=NMDC.indoor_space, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.indoor_space])

slots.indoor_surf = Slot(uri="str(uriorcurie)", name="indoor_surf", curie=None,
                      model_uri=NMDC.indoor_surf, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.indoor_surf])

slots.filter_type = Slot(uri="str(uriorcurie)", name="filter_type", curie=None,
                      model_uri=NMDC.filter_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.filter_type])

slots.heat_cool_type = Slot(uri="str(uriorcurie)", name="heat_cool_type", curie=None,
                      model_uri=NMDC.heat_cool_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heat_cool_type])

slots.substructure_type = Slot(uri="str(uriorcurie)", name="substructure_type", curie=None,
                      model_uri=NMDC.substructure_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.substructure_type])

slots.building_setting = Slot(uri="str(uriorcurie)", name="building_setting", curie=None,
                      model_uri=NMDC.building_setting, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.building_setting])

slots.light_type = Slot(uri="str(uriorcurie)", name="light_type", curie=None,
                      model_uri=NMDC.light_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.light_type])

slots.samp_sort_meth = Slot(uri="str(uriorcurie)", name="samp_sort_meth", curie=None,
                      model_uri=NMDC.samp_sort_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_sort_meth])

slots.space_typ_state = Slot(uri="str(uriorcurie)", name="space_typ_state", curie=None,
                      model_uri=NMDC.space_typ_state, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.space_typ_state])

slots.typ_occup_density = Slot(uri="str(uriorcurie)", name="typ_occup_density", curie=None,
                      model_uri=NMDC.typ_occup_density, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.typ_occup_density])

slots.occup_samp = Slot(uri="str(uriorcurie)", name="occup_samp", curie=None,
                      model_uri=NMDC.occup_samp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.occup_samp])

slots.occup_density_samp = Slot(uri="str(uriorcurie)", name="occup_density_samp", curie=None,
                      model_uri=NMDC.occup_density_samp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.occup_density_samp])

slots.address = Slot(uri="str(uriorcurie)", name="address", curie=None,
                      model_uri=NMDC.address, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.address])

slots.adj_room = Slot(uri="str(uriorcurie)", name="adj_room", curie=None,
                      model_uri=NMDC.adj_room, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.adj_room])

slots.aero_struc = Slot(uri="str(uriorcurie)", name="aero_struc", curie=None,
                      model_uri=NMDC.aero_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.aero_struc])

slots.amount_light = Slot(uri="str(uriorcurie)", name="amount_light", curie=None,
                      model_uri=NMDC.amount_light, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.amount_light])

slots.arch_struc = Slot(uri="str(uriorcurie)", name="arch_struc", curie=None,
                      model_uri=NMDC.arch_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.arch_struc])

slots.avg_occup = Slot(uri="str(uriorcurie)", name="avg_occup", curie=None,
                      model_uri=NMDC.avg_occup, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.avg_occup])

slots.avg_dew_point = Slot(uri="str(uriorcurie)", name="avg_dew_point", curie=None,
                      model_uri=NMDC.avg_dew_point, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.avg_dew_point])

slots.avg_temp = Slot(uri="str(uriorcurie)", name="avg_temp", curie=None,
                      model_uri=NMDC.avg_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.avg_temp])

slots.bathroom_count = Slot(uri="str(uriorcurie)", name="bathroom_count", curie=None,
                      model_uri=NMDC.bathroom_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.bathroom_count])

slots.bedroom_count = Slot(uri="str(uriorcurie)", name="bedroom_count", curie=None,
                      model_uri=NMDC.bedroom_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.bedroom_count])

slots.built_struc_age = Slot(uri="str(uriorcurie)", name="built_struc_age", curie=None,
                      model_uri=NMDC.built_struc_age, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.built_struc_age])

slots.built_struc_set = Slot(uri="str(uriorcurie)", name="built_struc_set", curie=None,
                      model_uri=NMDC.built_struc_set, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.built_struc_set])

slots.built_struc_type = Slot(uri="str(uriorcurie)", name="built_struc_type", curie=None,
                      model_uri=NMDC.built_struc_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.built_struc_type])

slots.ceil_area = Slot(uri="str(uriorcurie)", name="ceil_area", curie=None,
                      model_uri=NMDC.ceil_area, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ceil_area])

slots.ceil_cond = Slot(uri="str(uriorcurie)", name="ceil_cond", curie=None,
                      model_uri=NMDC.ceil_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_cond])

slots.ceil_finish_mat = Slot(uri="str(uriorcurie)", name="ceil_finish_mat", curie=None,
                      model_uri=NMDC.ceil_finish_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_finish_mat])

slots.ceil_water_mold = Slot(uri="str(uriorcurie)", name="ceil_water_mold", curie=None,
                      model_uri=NMDC.ceil_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_water_mold])

slots.ceil_struc = Slot(uri="str(uriorcurie)", name="ceil_struc", curie=None,
                      model_uri=NMDC.ceil_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_struc])

slots.ceil_texture = Slot(uri="str(uriorcurie)", name="ceil_texture", curie=None,
                      model_uri=NMDC.ceil_texture, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_texture])

slots.ceil_thermal_mass = Slot(uri="str(uriorcurie)", name="ceil_thermal_mass", curie=None,
                      model_uri=NMDC.ceil_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ceil_thermal_mass])

slots.ceil_type = Slot(uri="str(uriorcurie)", name="ceil_type", curie=None,
                      model_uri=NMDC.ceil_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ceil_type])

slots.cool_syst_id = Slot(uri="str(uriorcurie)", name="cool_syst_id", curie=None,
                      model_uri=NMDC.cool_syst_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cool_syst_id])

slots.date_last_rain = Slot(uri="str(uriorcurie)", name="date_last_rain", curie=None,
                      model_uri=NMDC.date_last_rain, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.date_last_rain])

slots.build_docs = Slot(uri="str(uriorcurie)", name="build_docs", curie=None,
                      model_uri=NMDC.build_docs, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.build_docs])

slots.door_size = Slot(uri="str(uriorcurie)", name="door_size", curie=None,
                      model_uri=NMDC.door_size, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.door_size])

slots.door_cond = Slot(uri="str(uriorcurie)", name="door_cond", curie=None,
                      model_uri=NMDC.door_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_cond])

slots.door_direct = Slot(uri="str(uriorcurie)", name="door_direct", curie=None,
                      model_uri=NMDC.door_direct, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_direct])

slots.door_loc = Slot(uri="str(uriorcurie)", name="door_loc", curie=None,
                      model_uri=NMDC.door_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_loc])

slots.door_mat = Slot(uri="str(uriorcurie)", name="door_mat", curie=None,
                      model_uri=NMDC.door_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_mat])

slots.door_move = Slot(uri="str(uriorcurie)", name="door_move", curie=None,
                      model_uri=NMDC.door_move, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_move])

slots.door_water_mold = Slot(uri="str(uriorcurie)", name="door_water_mold", curie=None,
                      model_uri=NMDC.door_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_water_mold])

slots.door_type = Slot(uri="str(uriorcurie)", name="door_type", curie=None,
                      model_uri=NMDC.door_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_type])

slots.door_comp_type = Slot(uri="str(uriorcurie)", name="door_comp_type", curie=None,
                      model_uri=NMDC.door_comp_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_comp_type])

slots.door_type_metal = Slot(uri="str(uriorcurie)", name="door_type_metal", curie=None,
                      model_uri=NMDC.door_type_metal, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_type_metal])

slots.door_type_wood = Slot(uri="str(uriorcurie)", name="door_type_wood", curie=None,
                      model_uri=NMDC.door_type_wood, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.door_type_wood])

slots.drawings = Slot(uri="str(uriorcurie)", name="drawings", curie=None,
                      model_uri=NMDC.drawings, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.drawings])

slots.elevator = Slot(uri="str(uriorcurie)", name="elevator", curie=None,
                      model_uri=NMDC.elevator, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.elevator])

slots.escalator = Slot(uri="str(uriorcurie)", name="escalator", curie=None,
                      model_uri=NMDC.escalator, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.escalator])

slots.exp_duct = Slot(uri="str(uriorcurie)", name="exp_duct", curie=None,
                      model_uri=NMDC.exp_duct, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.exp_duct])

slots.exp_pipe = Slot(uri="str(uriorcurie)", name="exp_pipe", curie=None,
                      model_uri=NMDC.exp_pipe, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.exp_pipe])

slots.ext_door = Slot(uri="str(uriorcurie)", name="ext_door", curie=None,
                      model_uri=NMDC.ext_door, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ext_door])

slots.fireplace_type = Slot(uri="str(uriorcurie)", name="fireplace_type", curie=None,
                      model_uri=NMDC.fireplace_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.fireplace_type])

slots.floor_age = Slot(uri="str(uriorcurie)", name="floor_age", curie=None,
                      model_uri=NMDC.floor_age, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.floor_age])

slots.floor_area = Slot(uri="str(uriorcurie)", name="floor_area", curie=None,
                      model_uri=NMDC.floor_area, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.floor_area])

slots.floor_cond = Slot(uri="str(uriorcurie)", name="floor_cond", curie=None,
                      model_uri=NMDC.floor_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_cond])

slots.floor_count = Slot(uri="str(uriorcurie)", name="floor_count", curie=None,
                      model_uri=NMDC.floor_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_count])

slots.floor_finish_mat = Slot(uri="str(uriorcurie)", name="floor_finish_mat", curie=None,
                      model_uri=NMDC.floor_finish_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_finish_mat])

slots.floor_water_mold = Slot(uri="str(uriorcurie)", name="floor_water_mold", curie=None,
                      model_uri=NMDC.floor_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_water_mold])

slots.floor_struc = Slot(uri="str(uriorcurie)", name="floor_struc", curie=None,
                      model_uri=NMDC.floor_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.floor_struc])

slots.floor_thermal_mass = Slot(uri="str(uriorcurie)", name="floor_thermal_mass", curie=None,
                      model_uri=NMDC.floor_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.floor_thermal_mass])

slots.freq_clean = Slot(uri="str(uriorcurie)", name="freq_clean", curie=None,
                      model_uri=NMDC.freq_clean, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.freq_clean])

slots.freq_cook = Slot(uri="str(uriorcurie)", name="freq_cook", curie=None,
                      model_uri=NMDC.freq_cook, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.freq_cook])

slots.furniture = Slot(uri="str(uriorcurie)", name="furniture", curie=None,
                      model_uri=NMDC.furniture, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.furniture])

slots.gender_restroom = Slot(uri="str(uriorcurie)", name="gender_restroom", curie=None,
                      model_uri=NMDC.gender_restroom, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gender_restroom])

slots.hall_count = Slot(uri="str(uriorcurie)", name="hall_count", curie=None,
                      model_uri=NMDC.hall_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.hall_count])

slots.handidness = Slot(uri="str(uriorcurie)", name="handidness", curie=None,
                      model_uri=NMDC.handidness, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.handidness])

slots.heat_deliv_loc = Slot(uri="str(uriorcurie)", name="heat_deliv_loc", curie=None,
                      model_uri=NMDC.heat_deliv_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heat_deliv_loc])

slots.heat_system_deliv_meth = Slot(uri="str(uriorcurie)", name="heat_system_deliv_meth", curie=None,
                      model_uri=NMDC.heat_system_deliv_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heat_system_deliv_meth])

slots.heat_system_id = Slot(uri="str(uriorcurie)", name="heat_system_id", curie=None,
                      model_uri=NMDC.heat_system_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heat_system_id])

slots.height_carper_fiber = Slot(uri="str(uriorcurie)", name="height_carper_fiber", curie=None,
                      model_uri=NMDC.height_carper_fiber, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.height_carper_fiber])

slots.inside_lux = Slot(uri="str(uriorcurie)", name="inside_lux", curie=None,
                      model_uri=NMDC.inside_lux, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.inside_lux])

slots.int_wall_cond = Slot(uri="str(uriorcurie)", name="int_wall_cond", curie=None,
                      model_uri=NMDC.int_wall_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.int_wall_cond])

slots.last_clean = Slot(uri="str(uriorcurie)", name="last_clean", curie=None,
                      model_uri=NMDC.last_clean, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.last_clean])

slots.max_occup = Slot(uri="str(uriorcurie)", name="max_occup", curie=None,
                      model_uri=NMDC.max_occup, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.max_occup])

slots.mech_struc = Slot(uri="str(uriorcurie)", name="mech_struc", curie=None,
                      model_uri=NMDC.mech_struc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mech_struc])

slots.number_plants = Slot(uri="str(uriorcurie)", name="number_plants", curie=None,
                      model_uri=NMDC.number_plants, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.number_plants])

slots.number_pets = Slot(uri="str(uriorcurie)", name="number_pets", curie=None,
                      model_uri=NMDC.number_pets, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.number_pets])

slots.number_resident = Slot(uri="str(uriorcurie)", name="number_resident", curie=None,
                      model_uri=NMDC.number_resident, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.number_resident])

slots.occup_document = Slot(uri="str(uriorcurie)", name="occup_document", curie=None,
                      model_uri=NMDC.occup_document, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.occup_document])

slots.ext_wall_orient = Slot(uri="str(uriorcurie)", name="ext_wall_orient", curie=None,
                      model_uri=NMDC.ext_wall_orient, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ext_wall_orient])

slots.ext_window_orient = Slot(uri="str(uriorcurie)", name="ext_window_orient", curie=None,
                      model_uri=NMDC.ext_window_orient, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ext_window_orient])

slots.rel_humidity_out = Slot(uri="str(uriorcurie)", name="rel_humidity_out", curie=None,
                      model_uri=NMDC.rel_humidity_out, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.rel_humidity_out])

slots.pres_animal = Slot(uri="str(uriorcurie)", name="pres_animal", curie=None,
                      model_uri=NMDC.pres_animal, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pres_animal])

slots.quad_pos = Slot(uri="str(uriorcurie)", name="quad_pos", curie=None,
                      model_uri=NMDC.quad_pos, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.quad_pos])

slots.rel_samp_loc = Slot(uri="str(uriorcurie)", name="rel_samp_loc", curie=None,
                      model_uri=NMDC.rel_samp_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.rel_samp_loc])

slots.room_air_exch_rate = Slot(uri="str(uriorcurie)", name="room_air_exch_rate", curie=None,
                      model_uri=NMDC.room_air_exch_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_air_exch_rate])

slots.room_architec_element = Slot(uri="str(uriorcurie)", name="room_architec_element", curie=None,
                      model_uri=NMDC.room_architec_element, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_architec_element])

slots.room_condt = Slot(uri="str(uriorcurie)", name="room_condt", curie=None,
                      model_uri=NMDC.room_condt, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_condt])

slots.room_count = Slot(uri="str(uriorcurie)", name="room_count", curie=None,
                      model_uri=NMDC.room_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_count])

slots.room_dim = Slot(uri="str(uriorcurie)", name="room_dim", curie=None,
                      model_uri=NMDC.room_dim, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_dim])

slots.room_door_dist = Slot(uri="str(uriorcurie)", name="room_door_dist", curie=None,
                      model_uri=NMDC.room_door_dist, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_door_dist])

slots.room_loc = Slot(uri="str(uriorcurie)", name="room_loc", curie=None,
                      model_uri=NMDC.room_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_loc])

slots.room_moist_damage_hist = Slot(uri="str(uriorcurie)", name="room_moist_damage_hist", curie=None,
                      model_uri=NMDC.room_moist_damage_hist, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_moist_damage_hist])

slots.room_net_area = Slot(uri="str(uriorcurie)", name="room_net_area", curie=None,
                      model_uri=NMDC.room_net_area, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_net_area])

slots.room_occup = Slot(uri="str(uriorcurie)", name="room_occup", curie=None,
                      model_uri=NMDC.room_occup, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_occup])

slots.room_samp_pos = Slot(uri="str(uriorcurie)", name="room_samp_pos", curie=None,
                      model_uri=NMDC.room_samp_pos, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_samp_pos])

slots.room_type = Slot(uri="str(uriorcurie)", name="room_type", curie=None,
                      model_uri=NMDC.room_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_type])

slots.room_vol = Slot(uri="str(uriorcurie)", name="room_vol", curie=None,
                      model_uri=NMDC.room_vol, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.room_vol])

slots.room_window_count = Slot(uri="str(uriorcurie)", name="room_window_count", curie=None,
                      model_uri=NMDC.room_window_count, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_window_count])

slots.room_connected = Slot(uri="str(uriorcurie)", name="room_connected", curie=None,
                      model_uri=NMDC.room_connected, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_connected])

slots.room_hallway = Slot(uri="str(uriorcurie)", name="room_hallway", curie=None,
                      model_uri=NMDC.room_hallway, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_hallway])

slots.room_door_share = Slot(uri="str(uriorcurie)", name="room_door_share", curie=None,
                      model_uri=NMDC.room_door_share, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_door_share])

slots.room_wall_share = Slot(uri="str(uriorcurie)", name="room_wall_share", curie=None,
                      model_uri=NMDC.room_wall_share, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.room_wall_share])

slots.samp_weather = Slot(uri="str(uriorcurie)", name="samp_weather", curie=None,
                      model_uri=NMDC.samp_weather, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_weather])

slots.samp_floor = Slot(uri="str(uriorcurie)", name="samp_floor", curie=None,
                      model_uri=NMDC.samp_floor, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_floor])

slots.samp_room_id = Slot(uri="str(uriorcurie)", name="samp_room_id", curie=None,
                      model_uri=NMDC.samp_room_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_room_id])

slots.samp_time_out = Slot(uri="str(uriorcurie)", name="samp_time_out", curie=None,
                      model_uri=NMDC.samp_time_out, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_time_out])

slots.season = Slot(uri="str(uriorcurie)", name="season", curie=None,
                      model_uri=NMDC.season, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.season])

slots.season_use = Slot(uri="str(uriorcurie)", name="season_use", curie=None,
                      model_uri=NMDC.season_use, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.season_use])

slots.shading_device_cond = Slot(uri="str(uriorcurie)", name="shading_device_cond", curie=None,
                      model_uri=NMDC.shading_device_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_cond])

slots.shading_device_loc = Slot(uri="str(uriorcurie)", name="shading_device_loc", curie=None,
                      model_uri=NMDC.shading_device_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_loc])

slots.shading_device_mat = Slot(uri="str(uriorcurie)", name="shading_device_mat", curie=None,
                      model_uri=NMDC.shading_device_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_mat])

slots.shading_device_water_mold = Slot(uri="str(uriorcurie)", name="shading_device_water_mold", curie=None,
                      model_uri=NMDC.shading_device_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_water_mold])

slots.shading_device_type = Slot(uri="str(uriorcurie)", name="shading_device_type", curie=None,
                      model_uri=NMDC.shading_device_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.shading_device_type])

slots.specific_humidity = Slot(uri="str(uriorcurie)", name="specific_humidity", curie=None,
                      model_uri=NMDC.specific_humidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.specific_humidity])

slots.specific = Slot(uri="str(uriorcurie)", name="specific", curie=None,
                      model_uri=NMDC.specific, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.specific])

slots.temp_out = Slot(uri="str(uriorcurie)", name="temp_out", curie=None,
                      model_uri=NMDC.temp_out, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.temp_out])

slots.train_line = Slot(uri="str(uriorcurie)", name="train_line", curie=None,
                      model_uri=NMDC.train_line, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.train_line])

slots.train_stat_loc = Slot(uri="str(uriorcurie)", name="train_stat_loc", curie=None,
                      model_uri=NMDC.train_stat_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.train_stat_loc])

slots.train_stop_loc = Slot(uri="str(uriorcurie)", name="train_stop_loc", curie=None,
                      model_uri=NMDC.train_stop_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.train_stop_loc])

slots.vis_media = Slot(uri="str(uriorcurie)", name="vis_media", curie=None,
                      model_uri=NMDC.vis_media, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.vis_media])

slots.wall_area = Slot(uri="str(uriorcurie)", name="wall_area", curie=None,
                      model_uri=NMDC.wall_area, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.wall_area])

slots.wall_const_type = Slot(uri="str(uriorcurie)", name="wall_const_type", curie=None,
                      model_uri=NMDC.wall_const_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_const_type])

slots.wall_finish_mat = Slot(uri="str(uriorcurie)", name="wall_finish_mat", curie=None,
                      model_uri=NMDC.wall_finish_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_finish_mat])

slots.wall_height = Slot(uri="str(uriorcurie)", name="wall_height", curie=None,
                      model_uri=NMDC.wall_height, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.wall_height])

slots.wall_loc = Slot(uri="str(uriorcurie)", name="wall_loc", curie=None,
                      model_uri=NMDC.wall_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_loc])

slots.wall_water_mold = Slot(uri="str(uriorcurie)", name="wall_water_mold", curie=None,
                      model_uri=NMDC.wall_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_water_mold])

slots.wall_surf_treatment = Slot(uri="str(uriorcurie)", name="wall_surf_treatment", curie=None,
                      model_uri=NMDC.wall_surf_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_surf_treatment])

slots.wall_texture = Slot(uri="str(uriorcurie)", name="wall_texture", curie=None,
                      model_uri=NMDC.wall_texture, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wall_texture])

slots.wall_thermal_mass = Slot(uri="str(uriorcurie)", name="wall_thermal_mass", curie=None,
                      model_uri=NMDC.wall_thermal_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.wall_thermal_mass])

slots.water_feat_size = Slot(uri="str(uriorcurie)", name="water_feat_size", curie=None,
                      model_uri=NMDC.water_feat_size, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_feat_size])

slots.water_feat_type = Slot(uri="str(uriorcurie)", name="water_feat_type", curie=None,
                      model_uri=NMDC.water_feat_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.water_feat_type])

slots.weekday = Slot(uri="str(uriorcurie)", name="weekday", curie=None,
                      model_uri=NMDC.weekday, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.weekday])

slots.window_size = Slot(uri="str(uriorcurie)", name="window_size", curie=None,
                      model_uri=NMDC.window_size, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.window_size])

slots.window_cond = Slot(uri="str(uriorcurie)", name="window_cond", curie=None,
                      model_uri=NMDC.window_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_cond])

slots.window_cover = Slot(uri="str(uriorcurie)", name="window_cover", curie=None,
                      model_uri=NMDC.window_cover, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_cover])

slots.window_horiz_pos = Slot(uri="str(uriorcurie)", name="window_horiz_pos", curie=None,
                      model_uri=NMDC.window_horiz_pos, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_horiz_pos])

slots.window_loc = Slot(uri="str(uriorcurie)", name="window_loc", curie=None,
                      model_uri=NMDC.window_loc, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_loc])

slots.window_mat = Slot(uri="str(uriorcurie)", name="window_mat", curie=None,
                      model_uri=NMDC.window_mat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_mat])

slots.window_open_freq = Slot(uri="str(uriorcurie)", name="window_open_freq", curie=None,
                      model_uri=NMDC.window_open_freq, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_open_freq])

slots.window_water_mold = Slot(uri="str(uriorcurie)", name="window_water_mold", curie=None,
                      model_uri=NMDC.window_water_mold, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_water_mold])

slots.window_status = Slot(uri="str(uriorcurie)", name="window_status", curie=None,
                      model_uri=NMDC.window_status, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_status])

slots.window_type = Slot(uri="str(uriorcurie)", name="window_type", curie=None,
                      model_uri=NMDC.window_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_type])

slots.window_vert_pos = Slot(uri="str(uriorcurie)", name="window_vert_pos", curie=None,
                      model_uri=NMDC.window_vert_pos, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.window_vert_pos])

slots.ances_data = Slot(uri="str(uriorcurie)", name="ances_data", curie=None,
                      model_uri=NMDC.ances_data, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ances_data])

slots.biol_stat = Slot(uri="str(uriorcurie)", name="biol_stat", curie=None,
                      model_uri=NMDC.biol_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.biol_stat])

slots.genetic_mod = Slot(uri="str(uriorcurie)", name="genetic_mod", curie=None,
                      model_uri=NMDC.genetic_mod, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.genetic_mod])

slots.host_common_name = Slot(uri="str(uriorcurie)", name="host_common_name", curie=None,
                      model_uri=NMDC.host_common_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_common_name])

slots.samp_capt_status = Slot(uri="str(uriorcurie)", name="samp_capt_status", curie=None,
                      model_uri=NMDC.samp_capt_status, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_capt_status])

slots.samp_dis_stage = Slot(uri="str(uriorcurie)", name="samp_dis_stage", curie=None,
                      model_uri=NMDC.samp_dis_stage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_dis_stage])

slots.host_taxid = Slot(uri="str(uriorcurie)", name="host_taxid", curie=None,
                      model_uri=NMDC.host_taxid, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_taxid])

slots.host_subject_id = Slot(uri="str(uriorcurie)", name="host_subject_id", curie=None,
                      model_uri=NMDC.host_subject_id, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_subject_id])

slots.host_age = Slot(uri="str(uriorcurie)", name="host_age", curie=None,
                      model_uri=NMDC.host_age, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_age])

slots.host_life_stage = Slot(uri="str(uriorcurie)", name="host_life_stage", curie=None,
                      model_uri=NMDC.host_life_stage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_life_stage])

slots.host_sex = Slot(uri="str(uriorcurie)", name="host_sex", curie=None,
                      model_uri=NMDC.host_sex, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_sex])

slots.host_disease_stat = Slot(uri="str(uriorcurie)", name="host_disease_stat", curie=None,
                      model_uri=NMDC.host_disease_stat, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.host_disease_stat])

slots.host_body_habitat = Slot(uri="str(uriorcurie)", name="host_body_habitat", curie=None,
                      model_uri=NMDC.host_body_habitat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_body_habitat])

slots.host_body_site = Slot(uri="str(uriorcurie)", name="host_body_site", curie=None,
                      model_uri=NMDC.host_body_site, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.host_body_site])

slots.host_body_product = Slot(uri="str(uriorcurie)", name="host_body_product", curie=None,
                      model_uri=NMDC.host_body_product, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.host_body_product])

slots.host_tot_mass = Slot(uri="str(uriorcurie)", name="host_tot_mass", curie=None,
                      model_uri=NMDC.host_tot_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_tot_mass])

slots.host_height = Slot(uri="str(uriorcurie)", name="host_height", curie=None,
                      model_uri=NMDC.host_height, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_height])

slots.host_length = Slot(uri="str(uriorcurie)", name="host_length", curie=None,
                      model_uri=NMDC.host_length, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_length])

slots.host_diet = Slot(uri="str(uriorcurie)", name="host_diet", curie=None,
                      model_uri=NMDC.host_diet, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_diet])

slots.host_last_meal = Slot(uri="str(uriorcurie)", name="host_last_meal", curie=None,
                      model_uri=NMDC.host_last_meal, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_last_meal])

slots.host_growth_cond = Slot(uri="str(uriorcurie)", name="host_growth_cond", curie=None,
                      model_uri=NMDC.host_growth_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_growth_cond])

slots.host_substrate = Slot(uri="str(uriorcurie)", name="host_substrate", curie=None,
                      model_uri=NMDC.host_substrate, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_substrate])

slots.host_family_relationship = Slot(uri="str(uriorcurie)", name="host_family_relationship", curie=None,
                      model_uri=NMDC.host_family_relationship, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_family_relationship])

slots.host_infra_specific_name = Slot(uri="str(uriorcurie)", name="host_infra_specific_name", curie=None,
                      model_uri=NMDC.host_infra_specific_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_infra_specific_name])

slots.host_infra_specific_rank = Slot(uri="str(uriorcurie)", name="host_infra_specific_rank", curie=None,
                      model_uri=NMDC.host_infra_specific_rank, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_infra_specific_rank])

slots.host_genotype = Slot(uri="str(uriorcurie)", name="host_genotype", curie=None,
                      model_uri=NMDC.host_genotype, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_genotype])

slots.host_phenotype = Slot(uri="str(uriorcurie)", name="host_phenotype", curie=None,
                      model_uri=NMDC.host_phenotype, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.host_phenotype])

slots.host_body_temp = Slot(uri="str(uriorcurie)", name="host_body_temp", curie=None,
                      model_uri=NMDC.host_body_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_body_temp])

slots.host_dry_mass = Slot(uri="str(uriorcurie)", name="host_dry_mass", curie=None,
                      model_uri=NMDC.host_dry_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_dry_mass])

slots.host_blood_press_diast = Slot(uri="str(uriorcurie)", name="host_blood_press_diast", curie=None,
                      model_uri=NMDC.host_blood_press_diast, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_blood_press_diast])

slots.host_blood_press_syst = Slot(uri="str(uriorcurie)", name="host_blood_press_syst", curie=None,
                      model_uri=NMDC.host_blood_press_syst, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_blood_press_syst])

slots.host_color = Slot(uri="str(uriorcurie)", name="host_color", curie=None,
                      model_uri=NMDC.host_color, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_color])

slots.host_shape = Slot(uri="str(uriorcurie)", name="host_shape", curie=None,
                      model_uri=NMDC.host_shape, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_shape])

slots.gravidity = Slot(uri="str(uriorcurie)", name="gravidity", curie=None,
                      model_uri=NMDC.gravidity, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gravidity])

slots.ihmc_medication_code = Slot(uri="str(uriorcurie)", name="ihmc_medication_code", curie=None,
                      model_uri=NMDC.ihmc_medication_code, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ihmc_medication_code])

slots.smoker = Slot(uri="str(uriorcurie)", name="smoker", curie=None,
                      model_uri=NMDC.smoker, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.smoker])

slots.host_hiv_stat = Slot(uri="str(uriorcurie)", name="host_hiv_stat", curie=None,
                      model_uri=NMDC.host_hiv_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_hiv_stat])

slots.drug_usage = Slot(uri="str(uriorcurie)", name="drug_usage", curie=None,
                      model_uri=NMDC.drug_usage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.drug_usage])

slots.host_body_mass_index = Slot(uri="str(uriorcurie)", name="host_body_mass_index", curie=None,
                      model_uri=NMDC.host_body_mass_index, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_body_mass_index])

slots.diet_last_six_month = Slot(uri="str(uriorcurie)", name="diet_last_six_month", curie=None,
                      model_uri=NMDC.diet_last_six_month, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.diet_last_six_month])

slots.weight_loss_3_month = Slot(uri="str(uriorcurie)", name="weight_loss_3_month", curie=None,
                      model_uri=NMDC.weight_loss_3_month, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.weight_loss_3_month])

slots.ihmc_ethnicity = Slot(uri="str(uriorcurie)", name="ihmc_ethnicity", curie=None,
                      model_uri=NMDC.ihmc_ethnicity, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ihmc_ethnicity])

slots.host_occupation = Slot(uri="str(uriorcurie)", name="host_occupation", curie=None,
                      model_uri=NMDC.host_occupation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.host_occupation])

slots.pet_farm_animal = Slot(uri="str(uriorcurie)", name="pet_farm_animal", curie=None,
                      model_uri=NMDC.pet_farm_animal, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pet_farm_animal])

slots.travel_out_six_month = Slot(uri="str(uriorcurie)", name="travel_out_six_month", curie=None,
                      model_uri=NMDC.travel_out_six_month, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.travel_out_six_month])

slots.twin_sibling = Slot(uri="str(uriorcurie)", name="twin_sibling", curie=None,
                      model_uri=NMDC.twin_sibling, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.twin_sibling])

slots.medic_hist_perform = Slot(uri="str(uriorcurie)", name="medic_hist_perform", curie=None,
                      model_uri=NMDC.medic_hist_perform, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.medic_hist_perform])

slots.study_complt_stat = Slot(uri="str(uriorcurie)", name="study_complt_stat", curie=None,
                      model_uri=NMDC.study_complt_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.study_complt_stat])

slots.pulmonary_disord = Slot(uri="str(uriorcurie)", name="pulmonary_disord", curie=None,
                      model_uri=NMDC.pulmonary_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pulmonary_disord])

slots.nose_throat_disord = Slot(uri="str(uriorcurie)", name="nose_throat_disord", curie=None,
                      model_uri=NMDC.nose_throat_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.nose_throat_disord])

slots.blood_blood_disord = Slot(uri="str(uriorcurie)", name="blood_blood_disord", curie=None,
                      model_uri=NMDC.blood_blood_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.blood_blood_disord])

slots.host_pulse = Slot(uri="str(uriorcurie)", name="host_pulse", curie=None,
                      model_uri=NMDC.host_pulse, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_pulse])

slots.gestation_state = Slot(uri="str(uriorcurie)", name="gestation_state", curie=None,
                      model_uri=NMDC.gestation_state, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gestation_state])

slots.maternal_health_stat = Slot(uri="str(uriorcurie)", name="maternal_health_stat", curie=None,
                      model_uri=NMDC.maternal_health_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.maternal_health_stat])

slots.foetal_health_stat = Slot(uri="str(uriorcurie)", name="foetal_health_stat", curie=None,
                      model_uri=NMDC.foetal_health_stat, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.foetal_health_stat])

slots.amniotic_fluid_color = Slot(uri="str(uriorcurie)", name="amniotic_fluid_color", curie=None,
                      model_uri=NMDC.amniotic_fluid_color, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.amniotic_fluid_color])

slots.kidney_disord = Slot(uri="str(uriorcurie)", name="kidney_disord", curie=None,
                      model_uri=NMDC.kidney_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.kidney_disord])

slots.urogenit_tract_disor = Slot(uri="str(uriorcurie)", name="urogenit_tract_disor", curie=None,
                      model_uri=NMDC.urogenit_tract_disor, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.urogenit_tract_disor])

slots.urine_collect_meth = Slot(uri="str(uriorcurie)", name="urine_collect_meth", curie=None,
                      model_uri=NMDC.urine_collect_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.urine_collect_meth])

slots.gastrointest_disord = Slot(uri="str(uriorcurie)", name="gastrointest_disord", curie=None,
                      model_uri=NMDC.gastrointest_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gastrointest_disord])

slots.liver_disord = Slot(uri="str(uriorcurie)", name="liver_disord", curie=None,
                      model_uri=NMDC.liver_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.liver_disord])

slots.special_diet = Slot(uri="str(uriorcurie)", name="special_diet", curie=None,
                      model_uri=NMDC.special_diet, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.special_diet])

slots.nose_mouth_teeth_throat_disord = Slot(uri="str(uriorcurie)", name="nose_mouth_teeth_throat_disord", curie=None,
                      model_uri=NMDC.nose_mouth_teeth_throat_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.nose_mouth_teeth_throat_disord])

slots.time_last_toothbrush = Slot(uri="str(uriorcurie)", name="time_last_toothbrush", curie=None,
                      model_uri=NMDC.time_last_toothbrush, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.time_last_toothbrush])

slots.dermatology_disord = Slot(uri="str(uriorcurie)", name="dermatology_disord", curie=None,
                      model_uri=NMDC.dermatology_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.dermatology_disord])

slots.time_since_last_wash = Slot(uri="str(uriorcurie)", name="time_since_last_wash", curie=None,
                      model_uri=NMDC.time_since_last_wash, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.time_since_last_wash])

slots.dominant_hand = Slot(uri="str(uriorcurie)", name="dominant_hand", curie=None,
                      model_uri=NMDC.dominant_hand, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.dominant_hand])

slots.menarche = Slot(uri="str(uriorcurie)", name="menarche", curie=None,
                      model_uri=NMDC.menarche, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.menarche])

slots.sexual_act = Slot(uri="str(uriorcurie)", name="sexual_act", curie=None,
                      model_uri=NMDC.sexual_act, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sexual_act])

slots.pregnancy = Slot(uri="str(uriorcurie)", name="pregnancy", curie=None,
                      model_uri=NMDC.pregnancy, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.pregnancy])

slots.douche = Slot(uri="str(uriorcurie)", name="douche", curie=None,
                      model_uri=NMDC.douche, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.douche])

slots.birth_control = Slot(uri="str(uriorcurie)", name="birth_control", curie=None,
                      model_uri=NMDC.birth_control, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.birth_control])

slots.menopause = Slot(uri="str(uriorcurie)", name="menopause", curie=None,
                      model_uri=NMDC.menopause, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.menopause])

slots.hrt = Slot(uri="str(uriorcurie)", name="hrt", curie=None,
                      model_uri=NMDC.hrt, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.hrt])

slots.hysterectomy = Slot(uri="str(uriorcurie)", name="hysterectomy", curie=None,
                      model_uri=NMDC.hysterectomy, domain=None, range=Optional[Union[dict, BooleanValue]], mappings = [MIXS.hysterectomy])

slots.gynecologic_disord = Slot(uri="str(uriorcurie)", name="gynecologic_disord", curie=None,
                      model_uri=NMDC.gynecologic_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.gynecologic_disord])

slots.urogenit_disord = Slot(uri="str(uriorcurie)", name="urogenit_disord", curie=None,
                      model_uri=NMDC.urogenit_disord, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.urogenit_disord])

slots.hcr = Slot(uri="str(uriorcurie)", name="hcr", curie=None,
                      model_uri=NMDC.hcr, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.hcr])

slots.hc_produced = Slot(uri="str(uriorcurie)", name="hc_produced", curie=None,
                      model_uri=NMDC.hc_produced, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.hc_produced])

slots.basin = Slot(uri="str(uriorcurie)", name="basin", curie=None,
                      model_uri=NMDC.basin, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.basin])

slots.field = Slot(uri="str(uriorcurie)", name="field", curie=None,
                      model_uri=NMDC.field, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.field])

slots.reservoir = Slot(uri="str(uriorcurie)", name="reservoir", curie=None,
                      model_uri=NMDC.reservoir, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.reservoir])

slots.hcr_temp = Slot(uri="str(uriorcurie)", name="hcr_temp", curie=None,
                      model_uri=NMDC.hcr_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.hcr_temp])

slots.tvdss_of_hcr_temp = Slot(uri="str(uriorcurie)", name="tvdss_of_hcr_temp", curie=None,
                      model_uri=NMDC.tvdss_of_hcr_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tvdss_of_hcr_temp])

slots.hcr_pressure = Slot(uri="str(uriorcurie)", name="hcr_pressure", curie=None,
                      model_uri=NMDC.hcr_pressure, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.hcr_pressure])

slots.tvdss_of_hcr_pressure = Slot(uri="str(uriorcurie)", name="tvdss_of_hcr_pressure", curie=None,
                      model_uri=NMDC.tvdss_of_hcr_pressure, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tvdss_of_hcr_pressure])

slots.permeability = Slot(uri="str(uriorcurie)", name="permeability", curie=None,
                      model_uri=NMDC.permeability, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.permeability])

slots.porosity = Slot(uri="str(uriorcurie)", name="porosity", curie=None,
                      model_uri=NMDC.porosity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.porosity])

slots.lithology = Slot(uri="str(uriorcurie)", name="lithology", curie=None,
                      model_uri=NMDC.lithology, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.lithology])

slots.depos_env = Slot(uri="str(uriorcurie)", name="depos_env", curie=None,
                      model_uri=NMDC.depos_env, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.depos_env])

slots.hcr_geol_age = Slot(uri="str(uriorcurie)", name="hcr_geol_age", curie=None,
                      model_uri=NMDC.hcr_geol_age, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.hcr_geol_age])

slots.owc_tvdss = Slot(uri="str(uriorcurie)", name="owc_tvdss", curie=None,
                      model_uri=NMDC.owc_tvdss, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.owc_tvdss])

slots.hcr_fw_salinity = Slot(uri="str(uriorcurie)", name="hcr_fw_salinity", curie=None,
                      model_uri=NMDC.hcr_fw_salinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.hcr_fw_salinity])

slots.sulfate_fw = Slot(uri="str(uriorcurie)", name="sulfate_fw", curie=None,
                      model_uri=NMDC.sulfate_fw, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sulfate_fw])

slots.vfa_fw = Slot(uri="str(uriorcurie)", name="vfa_fw", curie=None,
                      model_uri=NMDC.vfa_fw, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.vfa_fw])

slots.sr_kerog_type = Slot(uri="str(uriorcurie)", name="sr_kerog_type", curie=None,
                      model_uri=NMDC.sr_kerog_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sr_kerog_type])

slots.sr_lithology = Slot(uri="str(uriorcurie)", name="sr_lithology", curie=None,
                      model_uri=NMDC.sr_lithology, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sr_lithology])

slots.sr_dep_env = Slot(uri="str(uriorcurie)", name="sr_dep_env", curie=None,
                      model_uri=NMDC.sr_dep_env, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sr_dep_env])

slots.sr_geol_age = Slot(uri="str(uriorcurie)", name="sr_geol_age", curie=None,
                      model_uri=NMDC.sr_geol_age, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sr_geol_age])

slots.samp_well_name = Slot(uri="str(uriorcurie)", name="samp_well_name", curie=None,
                      model_uri=NMDC.samp_well_name, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_well_name])

slots.win = Slot(uri="str(uriorcurie)", name="win", curie=None,
                      model_uri=NMDC.win, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.win])

slots.samp_type = Slot(uri="str(uriorcurie)", name="samp_type", curie=None,
                      model_uri=NMDC.samp_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_type])

slots.samp_subtype = Slot(uri="str(uriorcurie)", name="samp_subtype", curie=None,
                      model_uri=NMDC.samp_subtype, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_subtype])

slots.pressure = Slot(uri="str(uriorcurie)", name="pressure", curie=None,
                      model_uri=NMDC.pressure, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.pressure])

slots.samp_tvdss = Slot(uri="str(uriorcurie)", name="samp_tvdss", curie=None,
                      model_uri=NMDC.samp_tvdss, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_tvdss])

slots.samp_md = Slot(uri="str(uriorcurie)", name="samp_md", curie=None,
                      model_uri=NMDC.samp_md, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_md])

slots.samp_transport_cond = Slot(uri="str(uriorcurie)", name="samp_transport_cond", curie=None,
                      model_uri=NMDC.samp_transport_cond, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_transport_cond])

slots.organism_count_qpcr_info = Slot(uri="str(uriorcurie)", name="organism_count_qpcr_info", curie=None,
                      model_uri=NMDC.organism_count_qpcr_info, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.organism_count_qpcr_info])

slots.ph = Slot(uri="str(uriorcurie)", name="ph", curie=None,
                      model_uri=NMDC.ph, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ph])

slots.alkalinity = Slot(uri="str(uriorcurie)", name="alkalinity", curie=None,
                      model_uri=NMDC.alkalinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.alkalinity])

slots.alkalinity_method = Slot(uri="str(uriorcurie)", name="alkalinity_method", curie=None,
                      model_uri=NMDC.alkalinity_method, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.alkalinity_method])

slots.sulfate = Slot(uri="str(uriorcurie)", name="sulfate", curie=None,
                      model_uri=NMDC.sulfate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sulfate])

slots.sulfide = Slot(uri="str(uriorcurie)", name="sulfide", curie=None,
                      model_uri=NMDC.sulfide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sulfide])

slots.tot_sulfur = Slot(uri="str(uriorcurie)", name="tot_sulfur", curie=None,
                      model_uri=NMDC.tot_sulfur, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_sulfur])

slots.nitrate = Slot(uri="str(uriorcurie)", name="nitrate", curie=None,
                      model_uri=NMDC.nitrate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.nitrate])

slots.nitrite = Slot(uri="str(uriorcurie)", name="nitrite", curie=None,
                      model_uri=NMDC.nitrite, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.nitrite])

slots.ammonium = Slot(uri="str(uriorcurie)", name="ammonium", curie=None,
                      model_uri=NMDC.ammonium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ammonium])

slots.tot_nitro = Slot(uri="str(uriorcurie)", name="tot_nitro", curie=None,
                      model_uri=NMDC.tot_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_nitro])

slots.diss_iron = Slot(uri="str(uriorcurie)", name="diss_iron", curie=None,
                      model_uri=NMDC.diss_iron, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_iron])

slots.sodium = Slot(uri="str(uriorcurie)", name="sodium", curie=None,
                      model_uri=NMDC.sodium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sodium])

slots.chloride = Slot(uri="str(uriorcurie)", name="chloride", curie=None,
                      model_uri=NMDC.chloride, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chloride])

slots.potassium = Slot(uri="str(uriorcurie)", name="potassium", curie=None,
                      model_uri=NMDC.potassium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.potassium])

slots.magnesium = Slot(uri="str(uriorcurie)", name="magnesium", curie=None,
                      model_uri=NMDC.magnesium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.magnesium])

slots.calcium = Slot(uri="str(uriorcurie)", name="calcium", curie=None,
                      model_uri=NMDC.calcium, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.calcium])

slots.tot_iron = Slot(uri="str(uriorcurie)", name="tot_iron", curie=None,
                      model_uri=NMDC.tot_iron, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_iron])

slots.diss_org_carb = Slot(uri="str(uriorcurie)", name="diss_org_carb", curie=None,
                      model_uri=NMDC.diss_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_org_carb])

slots.diss_inorg_carb = Slot(uri="str(uriorcurie)", name="diss_inorg_carb", curie=None,
                      model_uri=NMDC.diss_inorg_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_inorg_carb])

slots.diss_inorg_phosp = Slot(uri="str(uriorcurie)", name="diss_inorg_phosp", curie=None,
                      model_uri=NMDC.diss_inorg_phosp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_inorg_phosp])

slots.tot_phosp = Slot(uri="str(uriorcurie)", name="tot_phosp", curie=None,
                      model_uri=NMDC.tot_phosp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_phosp])

slots.suspend_solids = Slot(uri="str(uriorcurie)", name="suspend_solids", curie=None,
                      model_uri=NMDC.suspend_solids, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.suspend_solids])

slots.density = Slot(uri="str(uriorcurie)", name="density", curie=None,
                      model_uri=NMDC.density, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.density])

slots.diss_carb_dioxide = Slot(uri="str(uriorcurie)", name="diss_carb_dioxide", curie=None,
                      model_uri=NMDC.diss_carb_dioxide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_carb_dioxide])

slots.diss_oxygen_fluid = Slot(uri="str(uriorcurie)", name="diss_oxygen_fluid", curie=None,
                      model_uri=NMDC.diss_oxygen_fluid, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_oxygen_fluid])

slots.vfa = Slot(uri="str(uriorcurie)", name="vfa", curie=None,
                      model_uri=NMDC.vfa, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.vfa])

slots.benzene = Slot(uri="str(uriorcurie)", name="benzene", curie=None,
                      model_uri=NMDC.benzene, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.benzene])

slots.toluene = Slot(uri="str(uriorcurie)", name="toluene", curie=None,
                      model_uri=NMDC.toluene, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.toluene])

slots.ethylbenzene = Slot(uri="str(uriorcurie)", name="ethylbenzene", curie=None,
                      model_uri=NMDC.ethylbenzene, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.ethylbenzene])

slots.xylene = Slot(uri="str(uriorcurie)", name="xylene", curie=None,
                      model_uri=NMDC.xylene, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.xylene])

slots.api = Slot(uri="str(uriorcurie)", name="api", curie=None,
                      model_uri=NMDC.api, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.api])

slots.tan = Slot(uri="str(uriorcurie)", name="tan", curie=None,
                      model_uri=NMDC.tan, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tan])

slots.viscosity = Slot(uri="str(uriorcurie)", name="viscosity", curie=None,
                      model_uri=NMDC.viscosity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.viscosity])

slots.pour_point = Slot(uri="str(uriorcurie)", name="pour_point", curie=None,
                      model_uri=NMDC.pour_point, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.pour_point])

slots.saturates_pc = Slot(uri="str(uriorcurie)", name="saturates_pc", curie=None,
                      model_uri=NMDC.saturates_pc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.saturates_pc])

slots.aromatics_pc = Slot(uri="str(uriorcurie)", name="aromatics_pc", curie=None,
                      model_uri=NMDC.aromatics_pc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.aromatics_pc])

slots.resins_pc = Slot(uri="str(uriorcurie)", name="resins_pc", curie=None,
                      model_uri=NMDC.resins_pc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.resins_pc])

slots.asphaltenes_pc = Slot(uri="str(uriorcurie)", name="asphaltenes_pc", curie=None,
                      model_uri=NMDC.asphaltenes_pc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.asphaltenes_pc])

slots.additional_info = Slot(uri="str(uriorcurie)", name="additional_info", curie=None,
                      model_uri=NMDC.additional_info, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.additional_info])

slots.prod_start_date = Slot(uri="str(uriorcurie)", name="prod_start_date", curie=None,
                      model_uri=NMDC.prod_start_date, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.prod_start_date])

slots.prod_rate = Slot(uri="str(uriorcurie)", name="prod_rate", curie=None,
                      model_uri=NMDC.prod_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.prod_rate])

slots.water_production_rate = Slot(uri="str(uriorcurie)", name="water_production_rate", curie=None,
                      model_uri=NMDC.water_production_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_production_rate])

slots.water_cut = Slot(uri="str(uriorcurie)", name="water_cut", curie=None,
                      model_uri=NMDC.water_cut, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_cut])

slots.iwf = Slot(uri="str(uriorcurie)", name="iwf", curie=None,
                      model_uri=NMDC.iwf, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.iwf])

slots.add_recov_method = Slot(uri="str(uriorcurie)", name="add_recov_method", curie=None,
                      model_uri=NMDC.add_recov_method, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.add_recov_method])

slots.iw_bt_date_well = Slot(uri="str(uriorcurie)", name="iw_bt_date_well", curie=None,
                      model_uri=NMDC.iw_bt_date_well, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.iw_bt_date_well])

slots.biocide = Slot(uri="str(uriorcurie)", name="biocide", curie=None,
                      model_uri=NMDC.biocide, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.biocide])

slots.biocide_admin_method = Slot(uri="str(uriorcurie)", name="biocide_admin_method", curie=None,
                      model_uri=NMDC.biocide_admin_method, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.biocide_admin_method])

slots.chem_treatment = Slot(uri="str(uriorcurie)", name="chem_treatment", curie=None,
                      model_uri=NMDC.chem_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.chem_treatment])

slots.chem_treatment_method = Slot(uri="str(uriorcurie)", name="chem_treatment_method", curie=None,
                      model_uri=NMDC.chem_treatment_method, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chem_treatment_method])

slots.samp_loc_corr_rate = Slot(uri="str(uriorcurie)", name="samp_loc_corr_rate", curie=None,
                      model_uri=NMDC.samp_loc_corr_rate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_loc_corr_rate])

slots.samp_collection_point = Slot(uri="str(uriorcurie)", name="samp_collection_point", curie=None,
                      model_uri=NMDC.samp_collection_point, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.samp_collection_point])

slots.samp_preserv = Slot(uri="str(uriorcurie)", name="samp_preserv", curie=None,
                      model_uri=NMDC.samp_preserv, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.samp_preserv])

slots.alkyl_diethers = Slot(uri="str(uriorcurie)", name="alkyl_diethers", curie=None,
                      model_uri=NMDC.alkyl_diethers, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.alkyl_diethers])

slots.aminopept_act = Slot(uri="str(uriorcurie)", name="aminopept_act", curie=None,
                      model_uri=NMDC.aminopept_act, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.aminopept_act])

slots.bacteria_carb_prod = Slot(uri="str(uriorcurie)", name="bacteria_carb_prod", curie=None,
                      model_uri=NMDC.bacteria_carb_prod, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bacteria_carb_prod])

slots.biomass = Slot(uri="str(uriorcurie)", name="biomass", curie=None,
                      model_uri=NMDC.biomass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.biomass])

slots.bishomohopanol = Slot(uri="str(uriorcurie)", name="bishomohopanol", curie=None,
                      model_uri=NMDC.bishomohopanol, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bishomohopanol])

slots.bromide = Slot(uri="str(uriorcurie)", name="bromide", curie=None,
                      model_uri=NMDC.bromide, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bromide])

slots.carb_nitro_ratio = Slot(uri="str(uriorcurie)", name="carb_nitro_ratio", curie=None,
                      model_uri=NMDC.carb_nitro_ratio, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.carb_nitro_ratio])

slots.chlorophyll = Slot(uri="str(uriorcurie)", name="chlorophyll", curie=None,
                      model_uri=NMDC.chlorophyll, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chlorophyll])

slots.diether_lipids = Slot(uri="str(uriorcurie)", name="diether_lipids", curie=None,
                      model_uri=NMDC.diether_lipids, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diether_lipids])

slots.diss_hydrogen = Slot(uri="str(uriorcurie)", name="diss_hydrogen", curie=None,
                      model_uri=NMDC.diss_hydrogen, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_hydrogen])

slots.diss_org_nitro = Slot(uri="str(uriorcurie)", name="diss_org_nitro", curie=None,
                      model_uri=NMDC.diss_org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_org_nitro])

slots.diss_oxygen = Slot(uri="str(uriorcurie)", name="diss_oxygen", curie=None,
                      model_uri=NMDC.diss_oxygen, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_oxygen])

slots.glucosidase_act = Slot(uri="str(uriorcurie)", name="glucosidase_act", curie=None,
                      model_uri=NMDC.glucosidase_act, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.glucosidase_act])

slots.mean_frict_vel = Slot(uri="str(uriorcurie)", name="mean_frict_vel", curie=None,
                      model_uri=NMDC.mean_frict_vel, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.mean_frict_vel])

slots.mean_peak_frict_vel = Slot(uri="str(uriorcurie)", name="mean_peak_frict_vel", curie=None,
                      model_uri=NMDC.mean_peak_frict_vel, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.mean_peak_frict_vel])

slots.n_alkanes = Slot(uri="str(uriorcurie)", name="n_alkanes", curie=None,
                      model_uri=NMDC.n_alkanes, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.n_alkanes])

slots.nitro = Slot(uri="str(uriorcurie)", name="nitro", curie=None,
                      model_uri=NMDC.nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.nitro])

slots.org_carb = Slot(uri="str(uriorcurie)", name="org_carb", curie=None,
                      model_uri=NMDC.org_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.org_carb])

slots.org_matter = Slot(uri="str(uriorcurie)", name="org_matter", curie=None,
                      model_uri=NMDC.org_matter, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.org_matter])

slots.org_nitro = Slot(uri="str(uriorcurie)", name="org_nitro", curie=None,
                      model_uri=NMDC.org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.org_nitro])

slots.part_org_carb = Slot(uri="str(uriorcurie)", name="part_org_carb", curie=None,
                      model_uri=NMDC.part_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.part_org_carb])

slots.petroleum_hydrocarb = Slot(uri="str(uriorcurie)", name="petroleum_hydrocarb", curie=None,
                      model_uri=NMDC.petroleum_hydrocarb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.petroleum_hydrocarb])

slots.phaeopigments = Slot(uri="str(uriorcurie)", name="phaeopigments", curie=None,
                      model_uri=NMDC.phaeopigments, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.phaeopigments])

slots.phosphate = Slot(uri="str(uriorcurie)", name="phosphate", curie=None,
                      model_uri=NMDC.phosphate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.phosphate])

slots.phosplipid_fatt_acid = Slot(uri="str(uriorcurie)", name="phosplipid_fatt_acid", curie=None,
                      model_uri=NMDC.phosplipid_fatt_acid, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.phosplipid_fatt_acid])

slots.redox_potential = Slot(uri="str(uriorcurie)", name="redox_potential", curie=None,
                      model_uri=NMDC.redox_potential, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.redox_potential])

slots.salinity = Slot(uri="str(uriorcurie)", name="salinity", curie=None,
                      model_uri=NMDC.salinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.salinity])

slots.silicate = Slot(uri="str(uriorcurie)", name="silicate", curie=None,
                      model_uri=NMDC.silicate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.silicate])

slots.tot_carb = Slot(uri="str(uriorcurie)", name="tot_carb", curie=None,
                      model_uri=NMDC.tot_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_carb])

slots.tot_nitro_content = Slot(uri="str(uriorcurie)", name="tot_nitro_content", curie=None,
                      model_uri=NMDC.tot_nitro_content, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_nitro_content])

slots.tot_org_carb = Slot(uri="str(uriorcurie)", name="tot_org_carb", curie=None,
                      model_uri=NMDC.tot_org_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_org_carb])

slots.turbidity = Slot(uri="str(uriorcurie)", name="turbidity", curie=None,
                      model_uri=NMDC.turbidity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.turbidity])

slots.water_content = Slot(uri="str(uriorcurie)", name="water_content", curie=None,
                      model_uri=NMDC.water_content, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_content])

slots.water_current = Slot(uri="str(uriorcurie)", name="water_current", curie=None,
                      model_uri=NMDC.water_current, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_current])

slots.air_temp_regm = Slot(uri="str(uriorcurie)", name="air_temp_regm", curie=None,
                      model_uri=NMDC.air_temp_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.air_temp_regm])

slots.antibiotic_regm = Slot(uri="str(uriorcurie)", name="antibiotic_regm", curie=None,
                      model_uri=NMDC.antibiotic_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.antibiotic_regm])

slots.biotic_regm = Slot(uri="str(uriorcurie)", name="biotic_regm", curie=None,
                      model_uri=NMDC.biotic_regm, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.biotic_regm])

slots.chem_mutagen = Slot(uri="str(uriorcurie)", name="chem_mutagen", curie=None,
                      model_uri=NMDC.chem_mutagen, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chem_mutagen])

slots.climate_environment = Slot(uri="str(uriorcurie)", name="climate_environment", curie=None,
                      model_uri=NMDC.climate_environment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.climate_environment])

slots.cult_root_med = Slot(uri="str(uriorcurie)", name="cult_root_med", curie=None,
                      model_uri=NMDC.cult_root_med, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cult_root_med])

slots.fertilizer_regm = Slot(uri="str(uriorcurie)", name="fertilizer_regm", curie=None,
                      model_uri=NMDC.fertilizer_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.fertilizer_regm])

slots.fungicide_regm = Slot(uri="str(uriorcurie)", name="fungicide_regm", curie=None,
                      model_uri=NMDC.fungicide_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.fungicide_regm])

slots.gaseous_environment = Slot(uri="str(uriorcurie)", name="gaseous_environment", curie=None,
                      model_uri=NMDC.gaseous_environment, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.gaseous_environment])

slots.gravity = Slot(uri="str(uriorcurie)", name="gravity", curie=None,
                      model_uri=NMDC.gravity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.gravity])

slots.growth_facil = Slot(uri="str(uriorcurie)", name="growth_facil", curie=None,
                      model_uri=NMDC.growth_facil, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.growth_facil])

slots.growth_habit = Slot(uri="str(uriorcurie)", name="growth_habit", curie=None,
                      model_uri=NMDC.growth_habit, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.growth_habit])

slots.growth_hormone_regm = Slot(uri="str(uriorcurie)", name="growth_hormone_regm", curie=None,
                      model_uri=NMDC.growth_hormone_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.growth_hormone_regm])

slots.herbicide_regm = Slot(uri="str(uriorcurie)", name="herbicide_regm", curie=None,
                      model_uri=NMDC.herbicide_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.herbicide_regm])

slots.host_wet_mass = Slot(uri="str(uriorcurie)", name="host_wet_mass", curie=None,
                      model_uri=NMDC.host_wet_mass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.host_wet_mass])

slots.humidity_regm = Slot(uri="str(uriorcurie)", name="humidity_regm", curie=None,
                      model_uri=NMDC.humidity_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.humidity_regm])

slots.light_regm = Slot(uri="str(uriorcurie)", name="light_regm", curie=None,
                      model_uri=NMDC.light_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.light_regm])

slots.mechanical_damage = Slot(uri="str(uriorcurie)", name="mechanical_damage", curie=None,
                      model_uri=NMDC.mechanical_damage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.mechanical_damage])

slots.mineral_nutr_regm = Slot(uri="str(uriorcurie)", name="mineral_nutr_regm", curie=None,
                      model_uri=NMDC.mineral_nutr_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.mineral_nutr_regm])

slots.non_mineral_nutr_regm = Slot(uri="str(uriorcurie)", name="non_mineral_nutr_regm", curie=None,
                      model_uri=NMDC.non_mineral_nutr_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.non_mineral_nutr_regm])

slots.ph_regm = Slot(uri="str(uriorcurie)", name="ph_regm", curie=None,
                      model_uri=NMDC.ph_regm, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ph_regm])

slots.pesticide_regm = Slot(uri="str(uriorcurie)", name="pesticide_regm", curie=None,
                      model_uri=NMDC.pesticide_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.pesticide_regm])

slots.plant_growth_med = Slot(uri="str(uriorcurie)", name="plant_growth_med", curie=None,
                      model_uri=NMDC.plant_growth_med, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.plant_growth_med])

slots.plant_product = Slot(uri="str(uriorcurie)", name="plant_product", curie=None,
                      model_uri=NMDC.plant_product, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.plant_product])

slots.plant_sex = Slot(uri="str(uriorcurie)", name="plant_sex", curie=None,
                      model_uri=NMDC.plant_sex, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.plant_sex])

slots.plant_struc = Slot(uri="str(uriorcurie)", name="plant_struc", curie=None,
                      model_uri=NMDC.plant_struc, domain=None, range=Optional[Union[dict, ControlledTermValue]], mappings = [MIXS.plant_struc])

slots.radiation_regm = Slot(uri="str(uriorcurie)", name="radiation_regm", curie=None,
                      model_uri=NMDC.radiation_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.radiation_regm])

slots.rainfall_regm = Slot(uri="str(uriorcurie)", name="rainfall_regm", curie=None,
                      model_uri=NMDC.rainfall_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.rainfall_regm])

slots.root_cond = Slot(uri="str(uriorcurie)", name="root_cond", curie=None,
                      model_uri=NMDC.root_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.root_cond])

slots.root_med_carbon = Slot(uri="str(uriorcurie)", name="root_med_carbon", curie=None,
                      model_uri=NMDC.root_med_carbon, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_carbon])

slots.root_med_macronutr = Slot(uri="str(uriorcurie)", name="root_med_macronutr", curie=None,
                      model_uri=NMDC.root_med_macronutr, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_macronutr])

slots.root_med_micronutr = Slot(uri="str(uriorcurie)", name="root_med_micronutr", curie=None,
                      model_uri=NMDC.root_med_micronutr, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_micronutr])

slots.root_med_suppl = Slot(uri="str(uriorcurie)", name="root_med_suppl", curie=None,
                      model_uri=NMDC.root_med_suppl, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_suppl])

slots.root_med_ph = Slot(uri="str(uriorcurie)", name="root_med_ph", curie=None,
                      model_uri=NMDC.root_med_ph, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_ph])

slots.root_med_regl = Slot(uri="str(uriorcurie)", name="root_med_regl", curie=None,
                      model_uri=NMDC.root_med_regl, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.root_med_regl])

slots.root_med_solid = Slot(uri="str(uriorcurie)", name="root_med_solid", curie=None,
                      model_uri=NMDC.root_med_solid, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.root_med_solid])

slots.salt_regm = Slot(uri="str(uriorcurie)", name="salt_regm", curie=None,
                      model_uri=NMDC.salt_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.salt_regm])

slots.season_environment = Slot(uri="str(uriorcurie)", name="season_environment", curie=None,
                      model_uri=NMDC.season_environment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.season_environment])

slots.standing_water_regm = Slot(uri="str(uriorcurie)", name="standing_water_regm", curie=None,
                      model_uri=NMDC.standing_water_regm, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.standing_water_regm])

slots.tiss_cult_growth_med = Slot(uri="str(uriorcurie)", name="tiss_cult_growth_med", curie=None,
                      model_uri=NMDC.tiss_cult_growth_med, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tiss_cult_growth_med])

slots.water_temp_regm = Slot(uri="str(uriorcurie)", name="water_temp_regm", curie=None,
                      model_uri=NMDC.water_temp_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.water_temp_regm])

slots.watering_regm = Slot(uri="str(uriorcurie)", name="watering_regm", curie=None,
                      model_uri=NMDC.watering_regm, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.watering_regm])

slots.particle_class = Slot(uri="str(uriorcurie)", name="particle_class", curie=None,
                      model_uri=NMDC.particle_class, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.particle_class])

slots.sediment_type = Slot(uri="str(uriorcurie)", name="sediment_type", curie=None,
                      model_uri=NMDC.sediment_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sediment_type])

slots.tidal_stage = Slot(uri="str(uriorcurie)", name="tidal_stage", curie=None,
                      model_uri=NMDC.tidal_stage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tidal_stage])

slots.tot_depth_water_col = Slot(uri="str(uriorcurie)", name="tot_depth_water_col", curie=None,
                      model_uri=NMDC.tot_depth_water_col, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_depth_water_col])

slots.cur_land_use = Slot(uri="str(uriorcurie)", name="cur_land_use", curie=None,
                      model_uri=NMDC.cur_land_use, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cur_land_use])

slots.cur_vegetation = Slot(uri="str(uriorcurie)", name="cur_vegetation", curie=None,
                      model_uri=NMDC.cur_vegetation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cur_vegetation])

slots.cur_vegetation_meth = Slot(uri="str(uriorcurie)", name="cur_vegetation_meth", curie=None,
                      model_uri=NMDC.cur_vegetation_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.cur_vegetation_meth])

slots.previous_land_use = Slot(uri="str(uriorcurie)", name="previous_land_use", curie=None,
                      model_uri=NMDC.previous_land_use, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.previous_land_use])

slots.previous_land_use_meth = Slot(uri="str(uriorcurie)", name="previous_land_use_meth", curie=None,
                      model_uri=NMDC.previous_land_use_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.previous_land_use_meth])

slots.crop_rotation = Slot(uri="str(uriorcurie)", name="crop_rotation", curie=None,
                      model_uri=NMDC.crop_rotation, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.crop_rotation])

slots.agrochem_addition = Slot(uri="str(uriorcurie)", name="agrochem_addition", curie=None,
                      model_uri=NMDC.agrochem_addition, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.agrochem_addition])

slots.tillage = Slot(uri="str(uriorcurie)", name="tillage", curie=None,
                      model_uri=NMDC.tillage, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tillage])

slots.fire = Slot(uri="str(uriorcurie)", name="fire", curie=None,
                      model_uri=NMDC.fire, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.fire])

slots.flooding = Slot(uri="str(uriorcurie)", name="flooding", curie=None,
                      model_uri=NMDC.flooding, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.flooding])

slots.extreme_event = Slot(uri="str(uriorcurie)", name="extreme_event", curie=None,
                      model_uri=NMDC.extreme_event, domain=None, range=Optional[Union[dict, TimestampValue]], mappings = [MIXS.extreme_event])

slots.horizon = Slot(uri="str(uriorcurie)", name="horizon", curie=None,
                      model_uri=NMDC.horizon, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.horizon])

slots.horizon_meth = Slot(uri="str(uriorcurie)", name="horizon_meth", curie=None,
                      model_uri=NMDC.horizon_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.horizon_meth])

slots.sieving = Slot(uri="str(uriorcurie)", name="sieving", curie=None,
                      model_uri=NMDC.sieving, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sieving])

slots.water_content_soil_meth = Slot(uri="str(uriorcurie)", name="water_content_soil_meth", curie=None,
                      model_uri=NMDC.water_content_soil_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.water_content_soil_meth])

slots.pool_dna_extracts = Slot(uri="str(uriorcurie)", name="pool_dna_extracts", curie=None,
                      model_uri=NMDC.pool_dna_extracts, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pool_dna_extracts])

slots.store_cond = Slot(uri="str(uriorcurie)", name="store_cond", curie=None,
                      model_uri=NMDC.store_cond, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.store_cond])

slots.link_climate_info = Slot(uri="str(uriorcurie)", name="link_climate_info", curie=None,
                      model_uri=NMDC.link_climate_info, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.link_climate_info])

slots.annual_temp = Slot(uri="str(uriorcurie)", name="annual_temp", curie=None,
                      model_uri=NMDC.annual_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.annual_temp])

slots.season_temp = Slot(uri="str(uriorcurie)", name="season_temp", curie=None,
                      model_uri=NMDC.season_temp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.season_temp])

slots.annual_precpt = Slot(uri="str(uriorcurie)", name="annual_precpt", curie=None,
                      model_uri=NMDC.annual_precpt, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.annual_precpt])

slots.season_precpt = Slot(uri="str(uriorcurie)", name="season_precpt", curie=None,
                      model_uri=NMDC.season_precpt, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.season_precpt])

slots.link_class_info = Slot(uri="str(uriorcurie)", name="link_class_info", curie=None,
                      model_uri=NMDC.link_class_info, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.link_class_info])

slots.fao_class = Slot(uri="str(uriorcurie)", name="fao_class", curie=None,
                      model_uri=NMDC.fao_class, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.fao_class])

slots.local_class = Slot(uri="str(uriorcurie)", name="local_class", curie=None,
                      model_uri=NMDC.local_class, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.local_class])

slots.local_class_meth = Slot(uri="str(uriorcurie)", name="local_class_meth", curie=None,
                      model_uri=NMDC.local_class_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.local_class_meth])

slots.soil_type = Slot(uri="str(uriorcurie)", name="soil_type", curie=None,
                      model_uri=NMDC.soil_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.soil_type])

slots.soil_type_meth = Slot(uri="str(uriorcurie)", name="soil_type_meth", curie=None,
                      model_uri=NMDC.soil_type_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.soil_type_meth])

slots.slope_gradient = Slot(uri="str(uriorcurie)", name="slope_gradient", curie=None,
                      model_uri=NMDC.slope_gradient, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.slope_gradient])

slots.slope_aspect = Slot(uri="str(uriorcurie)", name="slope_aspect", curie=None,
                      model_uri=NMDC.slope_aspect, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.slope_aspect])

slots.profile_position = Slot(uri="str(uriorcurie)", name="profile_position", curie=None,
                      model_uri=NMDC.profile_position, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.profile_position])

slots.drainage_class = Slot(uri="str(uriorcurie)", name="drainage_class", curie=None,
                      model_uri=NMDC.drainage_class, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.drainage_class])

slots.texture = Slot(uri="str(uriorcurie)", name="texture", curie=None,
                      model_uri=NMDC.texture, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.texture])

slots.texture_meth = Slot(uri="str(uriorcurie)", name="texture_meth", curie=None,
                      model_uri=NMDC.texture_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.texture_meth])

slots.ph_meth = Slot(uri="str(uriorcurie)", name="ph_meth", curie=None,
                      model_uri=NMDC.ph_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.ph_meth])

slots.tot_org_c_meth = Slot(uri="str(uriorcurie)", name="tot_org_c_meth", curie=None,
                      model_uri=NMDC.tot_org_c_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tot_org_c_meth])

slots.tot_nitro_content_meth = Slot(uri="str(uriorcurie)", name="tot_nitro_content_meth", curie=None,
                      model_uri=NMDC.tot_nitro_content_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tot_nitro_content_meth])

slots.microbial_biomass = Slot(uri="str(uriorcurie)", name="microbial_biomass", curie=None,
                      model_uri=NMDC.microbial_biomass, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.microbial_biomass])

slots.microbial_biomass_meth = Slot(uri="str(uriorcurie)", name="microbial_biomass_meth", curie=None,
                      model_uri=NMDC.microbial_biomass_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.microbial_biomass_meth])

slots.link_addit_analys = Slot(uri="str(uriorcurie)", name="link_addit_analys", curie=None,
                      model_uri=NMDC.link_addit_analys, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.link_addit_analys])

slots.extreme_salinity = Slot(uri="str(uriorcurie)", name="extreme_salinity", curie=None,
                      model_uri=NMDC.extreme_salinity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.extreme_salinity])

slots.salinity_meth = Slot(uri="str(uriorcurie)", name="salinity_meth", curie=None,
                      model_uri=NMDC.salinity_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.salinity_meth])

slots.heavy_metals = Slot(uri="str(uriorcurie)", name="heavy_metals", curie=None,
                      model_uri=NMDC.heavy_metals, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.heavy_metals])

slots.heavy_metals_meth = Slot(uri="str(uriorcurie)", name="heavy_metals_meth", curie=None,
                      model_uri=NMDC.heavy_metals_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.heavy_metals_meth])

slots.al_sat = Slot(uri="str(uriorcurie)", name="al_sat", curie=None,
                      model_uri=NMDC.al_sat, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.al_sat])

slots.al_sat_meth = Slot(uri="str(uriorcurie)", name="al_sat_meth", curie=None,
                      model_uri=NMDC.al_sat_meth, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.al_sat_meth])

slots.biochem_oxygen_dem = Slot(uri="str(uriorcurie)", name="biochem_oxygen_dem", curie=None,
                      model_uri=NMDC.biochem_oxygen_dem, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.biochem_oxygen_dem])

slots.chem_oxygen_dem = Slot(uri="str(uriorcurie)", name="chem_oxygen_dem", curie=None,
                      model_uri=NMDC.chem_oxygen_dem, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.chem_oxygen_dem])

slots.efficiency_percent = Slot(uri="str(uriorcurie)", name="efficiency_percent", curie=None,
                      model_uri=NMDC.efficiency_percent, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.efficiency_percent])

slots.emulsions = Slot(uri="str(uriorcurie)", name="emulsions", curie=None,
                      model_uri=NMDC.emulsions, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.emulsions])

slots.gaseous_substances = Slot(uri="str(uriorcurie)", name="gaseous_substances", curie=None,
                      model_uri=NMDC.gaseous_substances, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.gaseous_substances])

slots.indust_eff_percent = Slot(uri="str(uriorcurie)", name="indust_eff_percent", curie=None,
                      model_uri=NMDC.indust_eff_percent, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.indust_eff_percent])

slots.inorg_particles = Slot(uri="str(uriorcurie)", name="inorg_particles", curie=None,
                      model_uri=NMDC.inorg_particles, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.inorg_particles])

slots.org_particles = Slot(uri="str(uriorcurie)", name="org_particles", curie=None,
                      model_uri=NMDC.org_particles, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.org_particles])

slots.pre_treatment = Slot(uri="str(uriorcurie)", name="pre_treatment", curie=None,
                      model_uri=NMDC.pre_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.pre_treatment])

slots.primary_treatment = Slot(uri="str(uriorcurie)", name="primary_treatment", curie=None,
                      model_uri=NMDC.primary_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.primary_treatment])

slots.reactor_type = Slot(uri="str(uriorcurie)", name="reactor_type", curie=None,
                      model_uri=NMDC.reactor_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.reactor_type])

slots.secondary_treatment = Slot(uri="str(uriorcurie)", name="secondary_treatment", curie=None,
                      model_uri=NMDC.secondary_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.secondary_treatment])

slots.sewage_type = Slot(uri="str(uriorcurie)", name="sewage_type", curie=None,
                      model_uri=NMDC.sewage_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.sewage_type])

slots.sludge_retent_time = Slot(uri="str(uriorcurie)", name="sludge_retent_time", curie=None,
                      model_uri=NMDC.sludge_retent_time, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.sludge_retent_time])

slots.soluble_inorg_mat = Slot(uri="str(uriorcurie)", name="soluble_inorg_mat", curie=None,
                      model_uri=NMDC.soluble_inorg_mat, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.soluble_inorg_mat])

slots.soluble_org_mat = Slot(uri="str(uriorcurie)", name="soluble_org_mat", curie=None,
                      model_uri=NMDC.soluble_org_mat, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.soluble_org_mat])

slots.tertiary_treatment = Slot(uri="str(uriorcurie)", name="tertiary_treatment", curie=None,
                      model_uri=NMDC.tertiary_treatment, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.tertiary_treatment])

slots.tot_phosphate = Slot(uri="str(uriorcurie)", name="tot_phosphate", curie=None,
                      model_uri=NMDC.tot_phosphate, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_phosphate])

slots.wastewater_type = Slot(uri="str(uriorcurie)", name="wastewater_type", curie=None,
                      model_uri=NMDC.wastewater_type, domain=None, range=Optional[Union[dict, TextValue]], mappings = [MIXS.wastewater_type])

slots.atmospheric_data = Slot(uri="str(uriorcurie)", name="atmospheric_data", curie=None,
                      model_uri=NMDC.atmospheric_data, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.atmospheric_data])

slots.bac_prod = Slot(uri="str(uriorcurie)", name="bac_prod", curie=None,
                      model_uri=NMDC.bac_prod, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bac_prod])

slots.bac_resp = Slot(uri="str(uriorcurie)", name="bac_resp", curie=None,
                      model_uri=NMDC.bac_resp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.bac_resp])

slots.conduc = Slot(uri="str(uriorcurie)", name="conduc", curie=None,
                      model_uri=NMDC.conduc, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.conduc])

slots.diss_inorg_nitro = Slot(uri="str(uriorcurie)", name="diss_inorg_nitro", curie=None,
                      model_uri=NMDC.diss_inorg_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.diss_inorg_nitro])

slots.down_par = Slot(uri="str(uriorcurie)", name="down_par", curie=None,
                      model_uri=NMDC.down_par, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.down_par])

slots.fluor = Slot(uri="str(uriorcurie)", name="fluor", curie=None,
                      model_uri=NMDC.fluor, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.fluor])

slots.light_intensity = Slot(uri="str(uriorcurie)", name="light_intensity", curie=None,
                      model_uri=NMDC.light_intensity, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.light_intensity])

slots.part_org_nitro = Slot(uri="str(uriorcurie)", name="part_org_nitro", curie=None,
                      model_uri=NMDC.part_org_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.part_org_nitro])

slots.photon_flux = Slot(uri="str(uriorcurie)", name="photon_flux", curie=None,
                      model_uri=NMDC.photon_flux, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.photon_flux])

slots.primary_prod = Slot(uri="str(uriorcurie)", name="primary_prod", curie=None,
                      model_uri=NMDC.primary_prod, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.primary_prod])

slots.size_frac_low = Slot(uri="str(uriorcurie)", name="size_frac_low", curie=None,
                      model_uri=NMDC.size_frac_low, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.size_frac_low])

slots.size_frac_up = Slot(uri="str(uriorcurie)", name="size_frac_up", curie=None,
                      model_uri=NMDC.size_frac_up, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.size_frac_up])

slots.soluble_react_phosp = Slot(uri="str(uriorcurie)", name="soluble_react_phosp", curie=None,
                      model_uri=NMDC.soluble_react_phosp, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.soluble_react_phosp])

slots.suspend_part_matter = Slot(uri="str(uriorcurie)", name="suspend_part_matter", curie=None,
                      model_uri=NMDC.suspend_part_matter, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.suspend_part_matter])

slots.tot_diss_nitro = Slot(uri="str(uriorcurie)", name="tot_diss_nitro", curie=None,
                      model_uri=NMDC.tot_diss_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_diss_nitro])

slots.tot_inorg_nitro = Slot(uri="str(uriorcurie)", name="tot_inorg_nitro", curie=None,
                      model_uri=NMDC.tot_inorg_nitro, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_inorg_nitro])

slots.tot_part_carb = Slot(uri="str(uriorcurie)", name="tot_part_carb", curie=None,
                      model_uri=NMDC.tot_part_carb, domain=None, range=Optional[Union[dict, QuantityValue]], mappings = [MIXS.tot_part_carb])

slots.id = Slot(uri=NMDC.id, name="id", curie=NMDC.curie('id'),
                      model_uri=NMDC.id, domain=None, range=URIRef)

slots.name = Slot(uri=NMDC.name, name="name", curie=NMDC.curie('name'),
                      model_uri=NMDC.name, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                      model_uri=NMDC.description, domain=None, range=Optional[str])

slots.alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.alternate_identifiers, domain=None, range=List[str])

slots.language = Slot(uri=NMDC.language, name="language", curie=NMDC.curie('language'),
                      model_uri=NMDC.language, domain=None, range=Optional[str])

slots.attribute = Slot(uri=NMDC.attribute, name="attribute", curie=NMDC.curie('attribute'),
                      model_uri=NMDC.attribute, domain=None, range=Optional[str])

slots.has_raw_value = Slot(uri=NMDC.has_raw_value, name="has raw value", curie=NMDC.curie('has_raw_value'),
                      model_uri=NMDC.has_raw_value, domain=AttributeValue, range=Optional[str])

slots.has_unit = Slot(uri=NMDC.has_unit, name="has unit", curie=NMDC.curie('has_unit'),
                      model_uri=NMDC.has_unit, domain=None, range=Optional[str], mappings = [QUD.unit, SCHEMA.unitCode])

slots.has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="has numeric value", curie=NMDC.curie('has_numeric_value'),
                      model_uri=NMDC.has_numeric_value, domain=None, range=Optional[float], mappings = [QUD.quantityValue, SCHEMA.value])

slots.has_boolean_value = Slot(uri=NMDC.has_boolean_value, name="has boolean value", curie=NMDC.curie('has_boolean_value'),
                      model_uri=NMDC.has_boolean_value, domain=None, range=Optional[Bool])

slots.latitude = Slot(uri=WGS.lat, name="latitude", curie=WGS.curie('lat'),
                      model_uri=NMDC.latitude, domain=GeolocationValue, range=Optional[float], mappings = [SCHEMA.latitude])

slots.longitude = Slot(uri=WGS.long, name="longitude", curie=WGS.curie('long'),
                      model_uri=NMDC.longitude, domain=GeolocationValue, range=Optional[float], mappings = [SCHEMA.longitude])

slots.term = Slot(uri=RDF.type, name="term", curie=RDF.curie('type'),
                      model_uri=NMDC.term, domain=ControlledTermValue, range=Optional[Union[dict, "OntologyClass"]])

slots.orcid = Slot(uri=NMDC.orcid, name="orcid", curie=NMDC.curie('orcid'),
                      model_uri=NMDC.orcid, domain=PersonValue, range=Optional[str])

slots.activity_id = Slot(uri=NMDC.activity_id, name="activity id", curie=NMDC.curie('activity_id'),
                      model_uri=NMDC.activity_id, domain=None, range=URIRef)

slots.started_at_time = Slot(uri=NMDC.started_at_time, name="started at time", curie=NMDC.curie('started_at_time'),
                      model_uri=NMDC.started_at_time, domain=None, range=Optional[str])

slots.ended_at_time = Slot(uri=NMDC.ended_at_time, name="ended at time", curie=NMDC.curie('ended_at_time'),
                      model_uri=NMDC.ended_at_time, domain=None, range=Optional[str])

slots.was_informed_by = Slot(uri=NMDC.was_informed_by, name="was informed by", curie=NMDC.curie('was_informed_by'),
                      model_uri=NMDC.was_informed_by, domain=None, range=Optional[Union[str, ActivityActivityId]])

slots.was_associated_with = Slot(uri=NMDC.was_associated_with, name="was associated with", curie=NMDC.curie('was_associated_with'),
                      model_uri=NMDC.was_associated_with, domain=None, range=Optional[Union[dict, Agent]])

slots.acted_on_behalf_of = Slot(uri=NMDC.acted_on_behalf_of, name="acted on behalf of", curie=NMDC.curie('acted_on_behalf_of'),
                      model_uri=NMDC.acted_on_behalf_of, domain=None, range=Optional[Union[dict, Agent]])

slots.was_generated_by = Slot(uri=NMDC.was_generated_by, name="was generated by", curie=NMDC.curie('was_generated_by'),
                      model_uri=NMDC.was_generated_by, domain=None, range=Optional[Union[str, ActivityActivityId]])

slots.used = Slot(uri=NMDC.used, name="used", curie=NMDC.curie('used'),
                      model_uri=NMDC.used, domain=Activity, range=Optional[str])

slots.biosample_id = Slot(uri=NMDC.id, name="biosample_id", curie=NMDC.curie('id'),
                      model_uri=NMDC.biosample_id, domain=Biosample, range=Union[str, BiosampleId])

slots.biosample_name = Slot(uri=NMDC.name, name="biosample_name", curie=NMDC.curie('name'),
                      model_uri=NMDC.biosample_name, domain=Biosample, range=Optional[str])

slots.biosample_alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="biosample_alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.biosample_alternate_identifiers, domain=Biosample, range=List[str])

slots.biosample_lat_lon = Slot(uri=NMDC.lat_lon, name="biosample_lat_lon", curie=NMDC.curie('lat_lon'),
                      model_uri=NMDC.biosample_lat_lon, domain=Biosample, range=Union[dict, "GeolocationValue"])

slots.biosample_depth = Slot(uri=NMDC.depth, name="biosample_depth", curie=NMDC.curie('depth'),
                      model_uri=NMDC.biosample_depth, domain=Biosample, range=Optional[Union[dict, "QuantityValue"]])

slots.biosample_env_broad_scale = Slot(uri=NMDC.env_broad_scale, name="biosample_env_broad_scale", curie=NMDC.curie('env_broad_scale'),
                      model_uri=NMDC.biosample_env_broad_scale, domain=Biosample, range=Union[dict, "ControlledTermValue"])

slots.biosample_env_local_scale = Slot(uri=NMDC.env_local_scale, name="biosample_env_local_scale", curie=NMDC.curie('env_local_scale'),
                      model_uri=NMDC.biosample_env_local_scale, domain=Biosample, range=Union[dict, "ControlledTermValue"])

slots.biosample_env_medium = Slot(uri=NMDC.env_medium, name="biosample_env_medium", curie=NMDC.curie('env_medium'),
                      model_uri=NMDC.biosample_env_medium, domain=Biosample, range=Union[dict, "ControlledTermValue"])

slots.study_id = Slot(uri=NMDC.id, name="study_id", curie=NMDC.curie('id'),
                      model_uri=NMDC.study_id, domain=Study, range=Union[str, StudyId])

slots.study_name = Slot(uri=NMDC.name, name="study_name", curie=NMDC.curie('name'),
                      model_uri=NMDC.study_name, domain=Study, range=Optional[str])

slots.study_alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="study_alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.study_alternate_identifiers, domain=Study, range=List[str])

slots.biosample_processing_has_input = Slot(uri=NMDC.has_input, name="biosample processing_has input", curie=NMDC.curie('has_input'),
                      model_uri=NMDC.biosample_processing_has_input, domain=BiosampleProcessing, range=List[Union[str, BiosampleId]])

slots.omics_processing_id = Slot(uri=NMDC.id, name="omics processing_id", curie=NMDC.curie('id'),
                      model_uri=NMDC.omics_processing_id, domain=OmicsProcessing, range=Union[str, OmicsProcessingId])

slots.omics_processing_name = Slot(uri=NMDC.name, name="omics processing_name", curie=NMDC.curie('name'),
                      model_uri=NMDC.omics_processing_name, domain=OmicsProcessing, range=Optional[str])

slots.omics_processing_alternate_identifiers = Slot(uri=NMDC.alternate_identifiers, name="omics processing_alternate identifiers", curie=NMDC.curie('alternate_identifiers'),
                      model_uri=NMDC.omics_processing_alternate_identifiers, domain=OmicsProcessing, range=List[str])

slots.omics_processing_part_of = Slot(uri=NMDC.part_of, name="omics processing_part of", curie=NMDC.curie('part_of'),
                      model_uri=NMDC.omics_processing_part_of, domain=OmicsProcessing, range=List[Union[str, StudyId]])

slots.omics_processing_has_output = Slot(uri=NMDC.has_output, name="omics processing_has output", curie=NMDC.curie('has_output'),
                      model_uri=NMDC.omics_processing_has_output, domain=OmicsProcessing, range=List[Union[str, DataObjectId]])

slots.person_id = Slot(uri=NMDC.id, name="person_id", curie=NMDC.curie('id'),
                      model_uri=NMDC.person_id, domain=Person, range=Union[str, PersonId])

slots.quantity_value_has_raw_value = Slot(uri=NMDC.has_raw_value, name="quantity value_has raw value", curie=NMDC.curie('has_raw_value'),
                      model_uri=NMDC.quantity_value_has_raw_value, domain=QuantityValue, range=Optional[str])

slots.quantity_value_has_unit = Slot(uri=NMDC.has_unit, name="quantity value_has unit", curie=NMDC.curie('has_unit'),
                      model_uri=NMDC.quantity_value_has_unit, domain=QuantityValue, range=Optional[str])

slots.quantity_value_has_numeric_value = Slot(uri=NMDC.has_numeric_value, name="quantity value_has numeric value", curie=NMDC.curie('has_numeric_value'),
                      model_uri=NMDC.quantity_value_has_numeric_value, domain=QuantityValue, range=Optional[float])

slots.person_value_has_raw_value = Slot(uri=NMDC.has_raw_value, name="person value_has raw value", curie=NMDC.curie('has_raw_value'),
                      model_uri=NMDC.person_value_has_raw_value, domain=PersonValue, range=Optional[str])

slots.geolocation_value_has_raw_value = Slot(uri=NMDC.has_raw_value, name="geolocation value_has raw value", curie=NMDC.curie('has_raw_value'),
                      model_uri=NMDC.geolocation_value_has_raw_value, domain=GeolocationValue, range=Optional[str])
