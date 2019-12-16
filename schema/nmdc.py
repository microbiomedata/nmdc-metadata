# Auto generated from nmdc.yaml by pythongen.py version: 0.2.0
# Generation date: 2019-12-13 16:15
# Schema: nmdc_schema
#
# id: https://microbiomedata/schema
# description: Schema for NMDC. Alpha. Currently focuses on samples
# license: https://creativecommons.org/publicdomain/zero/1.0/

from typing import Optional, List, Union, Dict, ClassVar
from dataclasses import dataclass
from biolinkml.utils.metamodelcore import empty_list, empty_dict
from biolinkml.utils.yamlutils import YAMLRoot
from includes.types import Double, Float, String

metamodel_version = "1.3.5"

# Types

# Class references
class NamedThingId(str):
    pass


class BiosampleId(NamedThingId):
    pass


class CharacteristicId(NamedThingId):
    pass


class OntologyClassId(NamedThingId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    # === named thing ===
    id: Union[str, NamedThingId]
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)


@dataclass
class Biosample(NamedThing):
    """
    A material sample. May be environmental (encompassing many organisms) or isolate or tissue
    """
    _inherited_slots: ClassVar[List[str]] = []

    # === named thing ===

    # === biosample ===
    id: Union[str, BiosampleId] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()
    annotations: List[Union[dict, "Annotation"]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, BiosampleId):
            self.id = BiosampleId(self.id)
        self.annotations = [v if isinstance(v, Annotation)
                            else Annotation(**v) for v in self.annotations]


@dataclass
class BiosampleProcessing(YAMLRoot):
    """
    A process that takes one or more biosamples as inputs and generates one or more as output
    """
    _inherited_slots: ClassVar[List[str]] = []

    # === biosample processing ===
    input: List[Union[str, BiosampleId]] = empty_list()
    output: List[Union[str, BiosampleId]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        self.input = [v if isinstance(v, BiosampleId)
                      else BiosampleId(v) for v in self.input]
        self.output = [v if isinstance(v, BiosampleId)
                       else BiosampleId(v) for v in self.output]


@dataclass
class Annotation(YAMLRoot):
    """
    An annotation on a sample. This is essentially a key value pair
    """
    _inherited_slots: ClassVar[List[str]] = []

    # === annotation ===
    has_raw_value: str
    has_characteristic: Optional[Union[str, CharacteristicId]] = None
    has_normalized_value: List[Union[dict, "NormalizedValue"]] = empty_list()

    def _fix_elements(self):
        super()._fix_elements()
        if self.has_characteristic is not None and not isinstance(self.has_characteristic, CharacteristicId):
            self.has_characteristic = CharacteristicId(self.has_characteristic)
        self.has_normalized_value = [v if isinstance(v, NormalizedValue)
                                     else NormalizedValue(**v) for v in self.has_normalized_value]


@dataclass
class Characteristic(NamedThing):
    """
    A characteristic of a biosample. Examples: depth, habitat, material, ... For NMDC, characteristics SHOULD be
    mapped to fields within a MIxS template
    """
    _inherited_slots: ClassVar[List[str]] = []

    # === named thing ===
    id: Union[str, CharacteristicId] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()

    # === characteristic ===
    description: Optional[str] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, CharacteristicId):
            self.id = CharacteristicId(self.id)


@dataclass
class NormalizedValue(YAMLRoot):
    """
    The value that was specified for an annotation in parsed/normalized form. This could be a range of different types
    """
    _inherited_slots: ClassVar[List[str]] = []
    pass


@dataclass
class QuantityValue(NormalizedValue):
    """
    A simple quantity, e.g. 2cm
    """
    _inherited_slots: ClassVar[List[str]] = []
    pass

    # === quantity value ===
    has_unit: List[Union[dict, "Unit"]] = empty_list()
    has_numeric_value: Optional[float] = None

    def _fix_elements(self):
        super()._fix_elements()
        self.has_unit = [v if isinstance(v, Unit)
                         else Unit(**v) for v in self.has_unit]


@dataclass
class ControlledTermValue(NormalizedValue):
    """
    A controlled term or class from an ontology
    """
    _inherited_slots: ClassVar[List[str]] = []
    pass

    # === controlled term value ===
    instance_of: Optional[Union[str, OntologyClassId]] = None

    def _fix_elements(self):
        super()._fix_elements()
        if self.instance_of is not None and not isinstance(self.instance_of, OntologyClassId):
            self.instance_of = OntologyClassId(self.instance_of)


@dataclass
class GeolocationValue(NormalizedValue):
    """
    A normalized value for a location on the earth's surface
    """
    _inherited_slots: ClassVar[List[str]] = []
    pass

    # === geolocation value ===
    latitude: Optional[float] = None
    longitude: Optional[float] = None


@dataclass
class Unit(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []
    pass


@dataclass
class OntologyClass(NamedThing):
    _inherited_slots: ClassVar[List[str]] = []

    # === named thing ===
    id: Union[str, OntologyClassId] = None
    name: Optional[str] = None
    alternate_identifiers: List[str] = empty_list()

    # === ontology class ===

    def _fix_elements(self):
        super()._fix_elements()
        if self.id is not None and not isinstance(self.id, OntologyClassId):
            self.id = OntologyClassId(self.id)

