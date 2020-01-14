# Auto generated from nmdc.yaml by pythongen.py version: 0.2.1
# Generation date: 2019-12-18 21:33
# Schema: nmdc_schema
#
# id: https://microbiomedata/schema
# description: Schema for NMDC. Alpha. Currently focuses on samples
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict, bnode
from biolinkml.utils.yamlutils import YAMLRoot
from biolinkml.utils.formatutils import camelcase, underscore, sfx
from rdflib import Namespace, URIRef
from includes.types import Double, Float, String

metamodel_version = "1.4.1"


# Namespaces
UO = Namespace('http://purl.obolibrary.org/obo/UO_')
DCTERMS = Namespace('http://example.org/UNKNOWN/dcterms/')
NMDC = Namespace('https://microbiomedata/meta/')
QUD = Namespace('http://qudt.org/1.1/schema/qudt#')
RDF = Namespace('http://example.org/UNKNOWN/rdf/')
RDFS = Namespace('http://example.org/UNKNOWN/rdfs/')
SHEX = Namespace('http://www.w3.org/ns/shex#')
SKOS = Namespace('http://example.org/UNKNOWN/skos/')
WGS = Namespace('http://www.w3.org/2003/01/geo/wgs84_pos')
XSD = Namespace('http://www.w3.org/2001/XMLSchema#')
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

@dataclass
class Biosample(NamedThing):
    """
    A material sample. May be environmental (encompassing many organisms) or isolate or tissue
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Biosample
    class_class_curie: ClassVar[str] = "nmdc:Biosample"
    class_name: ClassVar[str] = "biosample"
    class_model_uri: ClassVar[URIRef] = NMDC.Biosample

    id: Optional[str] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()
    annotations: List[Union[dict, "Annotation"]] = empty_list()

    def __post_init__(self):
        self.annotations = [v if isinstance(v, Annotation)
                            else Annotation(**v) for v in self.annotations]
        super().__post_init__()


@dataclass
class BiosampleProcessing(YAMLRoot):
    """
    A process that takes one or more biosamples as inputs and generates one or more as output
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.BiosampleProcessing
    class_class_curie: ClassVar[str] = "nmdc:BiosampleProcessing"
    class_name: ClassVar[str] = "biosample processing"
    class_model_uri: ClassVar[URIRef] = NMDC.BiosampleProcessing

    input: List[Union[dict, Biosample]] = empty_list()
    output: List[Union[dict, Biosample]] = empty_list()

    def __post_init__(self):
        self.input = [v if isinstance(v, Biosample)
                      else Biosample(**v) for v in self.input]
        self.output = [v if isinstance(v, Biosample)
                       else Biosample(**v) for v in self.output]
        super().__post_init__()


@dataclass
class Annotation(YAMLRoot):
    """
    An annotation on a sample. This is essentially a key value pair
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.Annotation
    class_class_curie: ClassVar[str] = "nmdc:Annotation"
    class_name: ClassVar[str] = "annotation"
    class_model_uri: ClassVar[URIRef] = NMDC.Annotation

    has_raw_value: str
    has_characteristic: Optional[Union[dict, "Characteristic"]] = None
    has_normalized_value: List[Union[dict, "NormalizedValue"]] = empty_list()

    def __post_init__(self):
        if self.has_characteristic is not None and not isinstance(self.has_characteristic, Characteristic):
            self.has_characteristic = Characteristic(**self.has_characteristic)
        if self.has_raw_value is None:
            raise ValueError(f"has_raw_value must be supplied")
        self.has_normalized_value = [v if isinstance(v, NormalizedValue)
                                     else NormalizedValue(**v) for v in self.has_normalized_value]
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

    instance_of: Optional[Union[dict, "OntologyClass"]] = None

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


class OntologyClass(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC.OntologyClass
    class_class_curie: ClassVar[str] = "nmdc:OntologyClass"
    class_name: ClassVar[str] = "ontology class"
    class_model_uri: ClassVar[URIRef] = NMDC.OntologyClass

