# Auto generated from mixs_meta.yaml by pythongen.py version: 0.4.0
# Generation date: 2020-06-05 23:00
# Schema: MIxS Meta-Schema
#
# id: https://microbiomedata/schema/mixs_meta
# description: Definitions of fields used in MIxS
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
from includes.types import Integer, String

metamodel_version = "1.4.3"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINKML = CurieNamespace('biolinkml', 'https://w3id.org/biolink/biolinkml/')
MIXS = CurieNamespace('mixs', 'https://w3id.org/gensc/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = MIXS


# Types
class NarrativeTextType(String):
    """ A string that provides a human-readable description of something """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "narrative text type"
    type_model_uri = MIXS.NarrativeTextType


class UnitType(String):
    """ E.g. cm """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "unit type"
    type_model_uri = MIXS.UnitType


class MandatorinessCode(String):
    """ M/C/R/X/E """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "mandatoriness code"
    type_model_uri = MIXS.MandatorinessCode


class OccurrenceCode(String):
    """ One of 1: once; m: multiple, 0: none """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "occurrence code"
    type_model_uri = MIXS.OccurrenceCode


class LabelType(String):
    """ A string that provides a human-readable name for a thing """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "label type"
    type_model_uri = MIXS.LabelType


# Class references



@dataclass
class Template(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MIXS.Template
    class_class_curie: ClassVar[str] = "mixs:Template"
    class_name: ClassVar[str] = "template"
    class_model_uri: ClassVar[URIRef] = MIXS.Template

    Structured_comment_name: str
    Item: str
    Definition: str
    Value_syntax: str
    Section: str
    Expected_value: Optional[str] = None
    Example: Optional[str] = None
    migs_eu: Optional[Union[str, MandatorinessCode]] = None
    migs_ba: Optional[Union[str, MandatorinessCode]] = None
    migs_pl: Optional[Union[str, MandatorinessCode]] = None
    migs_vi: Optional[Union[str, MandatorinessCode]] = None
    migs_org: Optional[Union[str, MandatorinessCode]] = None
    me: Optional[Union[str, MandatorinessCode]] = None
    mimarks_s: Optional[Union[str, MandatorinessCode]] = None
    mimarks_c: Optional[Union[str, MandatorinessCode]] = None
    misag: Optional[Union[str, MandatorinessCode]] = None
    mimag: Optional[Union[str, MandatorinessCode]] = None
    miuvig: Optional[Union[str, MandatorinessCode]] = None
    Preferred_unit: Optional[Union[str, UnitType]] = None
    Occurence: Optional[Union[str, OccurrenceCode]] = None
    Position: Optional[int] = None
    MIXS_ID: Optional[str] = None

    def __post_init__(self, **kwargs: Dict[str, Any]):
        if self.Structured_comment_name is None:
            raise ValueError(f"Structured_comment_name must be supplied")
        if self.Item is None:
            raise ValueError(f"Item must be supplied")
        if self.Definition is None:
            raise ValueError(f"Definition must be supplied")
        if self.Value_syntax is None:
            raise ValueError(f"Value_syntax must be supplied")
        if self.Section is None:
            raise ValueError(f"Section must be supplied")
        if self.migs_eu is not None and not isinstance(self.migs_eu, MandatorinessCode):
            self.migs_eu = MandatorinessCode(self.migs_eu)
        if self.migs_ba is not None and not isinstance(self.migs_ba, MandatorinessCode):
            self.migs_ba = MandatorinessCode(self.migs_ba)
        if self.migs_pl is not None and not isinstance(self.migs_pl, MandatorinessCode):
            self.migs_pl = MandatorinessCode(self.migs_pl)
        if self.migs_vi is not None and not isinstance(self.migs_vi, MandatorinessCode):
            self.migs_vi = MandatorinessCode(self.migs_vi)
        if self.migs_org is not None and not isinstance(self.migs_org, MandatorinessCode):
            self.migs_org = MandatorinessCode(self.migs_org)
        if self.me is not None and not isinstance(self.me, MandatorinessCode):
            self.me = MandatorinessCode(self.me)
        if self.mimarks_s is not None and not isinstance(self.mimarks_s, MandatorinessCode):
            self.mimarks_s = MandatorinessCode(self.mimarks_s)
        if self.mimarks_c is not None and not isinstance(self.mimarks_c, MandatorinessCode):
            self.mimarks_c = MandatorinessCode(self.mimarks_c)
        if self.misag is not None and not isinstance(self.misag, MandatorinessCode):
            self.misag = MandatorinessCode(self.misag)
        if self.mimag is not None and not isinstance(self.mimag, MandatorinessCode):
            self.mimag = MandatorinessCode(self.mimag)
        if self.miuvig is not None and not isinstance(self.miuvig, MandatorinessCode):
            self.miuvig = MandatorinessCode(self.miuvig)
        if self.Preferred_unit is not None and not isinstance(self.Preferred_unit, UnitType):
            self.Preferred_unit = UnitType(self.Preferred_unit)
        if self.Occurence is not None and not isinstance(self.Occurence, OccurrenceCode):
            self.Occurence = OccurrenceCode(self.Occurence)
        super().__post_init__(**kwargs)



# Slots
class slots:
    pass

slots.Structured_comment_name = Slot(uri=MIXS.Structured_comment_name, name="Structured comment name", curie=MIXS.curie('Structured_comment_name'),
                      model_uri=MIXS.Structured_comment_name, domain=None, range=str)

slots.Item = Slot(uri=MIXS.Item, name="Item", curie=MIXS.curie('Item'),
                      model_uri=MIXS.Item, domain=None, range=str, mappings = [RDFS.label])

slots.Definition = Slot(uri=MIXS.Definition, name="Definition", curie=MIXS.curie('Definition'),
                      model_uri=MIXS.Definition, domain=None, range=str, mappings = [SKOS.definition])

slots.Expected_value = Slot(uri=MIXS.Expected_value, name="Expected value", curie=MIXS.curie('Expected_value'),
                      model_uri=MIXS.Expected_value, domain=None, range=Optional[str])

slots.Value_syntax = Slot(uri=MIXS.Value_syntax, name="Value syntax", curie=MIXS.curie('Value_syntax'),
                      model_uri=MIXS.Value_syntax, domain=None, range=str)

slots.Example = Slot(uri=MIXS.Example, name="Example", curie=MIXS.curie('Example'),
                      model_uri=MIXS.Example, domain=None, range=Optional[str])

slots.Section = Slot(uri=MIXS.Section, name="Section", curie=MIXS.curie('Section'),
                      model_uri=MIXS.Section, domain=None, range=str, mappings = [SKOS.inSubset])

slots.migs_eu = Slot(uri=MIXS.migs_eu, name="migs_eu", curie=MIXS.curie('migs_eu'),
                      model_uri=MIXS.migs_eu, domain=None, range=Optional[Union[str, MandatorinessCode]])

slots.migs_ba = Slot(uri=MIXS.migs_ba, name="migs_ba", curie=MIXS.curie('migs_ba'),
                      model_uri=MIXS.migs_ba, domain=None, range=Optional[Union[str, MandatorinessCode]])

slots.migs_pl = Slot(uri=MIXS.migs_pl, name="migs_pl", curie=MIXS.curie('migs_pl'),
                      model_uri=MIXS.migs_pl, domain=None, range=Optional[Union[str, MandatorinessCode]])

slots.migs_vi = Slot(uri=MIXS.migs_vi, name="migs_vi", curie=MIXS.curie('migs_vi'),
                      model_uri=MIXS.migs_vi, domain=None, range=Optional[Union[str, MandatorinessCode]])

slots.migs_org = Slot(uri=MIXS.migs_org, name="migs_org", curie=MIXS.curie('migs_org'),
                      model_uri=MIXS.migs_org, domain=None, range=Optional[Union[str, MandatorinessCode]])

slots.me = Slot(uri=MIXS.me, name="me", curie=MIXS.curie('me'),
                      model_uri=MIXS.me, domain=None, range=Optional[Union[str, MandatorinessCode]])

slots.mimarks_s = Slot(uri=MIXS.mimarks_s, name="mimarks_s", curie=MIXS.curie('mimarks_s'),
                      model_uri=MIXS.mimarks_s, domain=None, range=Optional[Union[str, MandatorinessCode]])

slots.mimarks_c = Slot(uri=MIXS.mimarks_c, name="mimarks_c", curie=MIXS.curie('mimarks_c'),
                      model_uri=MIXS.mimarks_c, domain=None, range=Optional[Union[str, MandatorinessCode]])

slots.misag = Slot(uri=MIXS.misag, name="misag", curie=MIXS.curie('misag'),
                      model_uri=MIXS.misag, domain=None, range=Optional[Union[str, MandatorinessCode]])

slots.mimag = Slot(uri=MIXS.mimag, name="mimag", curie=MIXS.curie('mimag'),
                      model_uri=MIXS.mimag, domain=None, range=Optional[Union[str, MandatorinessCode]])

slots.miuvig = Slot(uri=MIXS.miuvig, name="miuvig", curie=MIXS.curie('miuvig'),
                      model_uri=MIXS.miuvig, domain=None, range=Optional[Union[str, MandatorinessCode]])

slots.Preferred_unit = Slot(uri=MIXS.Preferred_unit, name="Preferred unit", curie=MIXS.curie('Preferred_unit'),
                      model_uri=MIXS.Preferred_unit, domain=None, range=Optional[Union[str, UnitType]])

slots.Occurence = Slot(uri=MIXS.Occurence, name="Occurence", curie=MIXS.curie('Occurence'),
                      model_uri=MIXS.Occurence, domain=None, range=Optional[Union[str, OccurrenceCode]])

slots.Position = Slot(uri=MIXS.Position, name="Position", curie=MIXS.curie('Position'),
                      model_uri=MIXS.Position, domain=None, range=Optional[int])

slots.MIXS_ID = Slot(uri=MIXS.MIXS_ID, name="MIXS ID", curie=MIXS.curie('MIXS_ID'),
                      model_uri=MIXS.MIXS_ID, domain=None, range=Optional[str])
