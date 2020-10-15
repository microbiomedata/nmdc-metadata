## author: Bill Duncan
## summary:

## add ./lib directory to sys.path so that local modules can be found
import os, sys

sys.path.append(os.path.abspath("."))
# print(sys.path)

## system level modules
import pandas as pds
import jq
import jsonasobj
import json
import zipfile
import yaml
from yaml import CLoader as Loader, CDumper as Dumper
from dotted_dict import DottedDict
from collections import namedtuple

## add all classes for local nmdc.py
## this is the file of python classes generated by biolinkml
import nmdc

def make_json_string_list (dictionary,
                           nmdc_class,
                           constructor_map={},
                           attribute_fields=[],
                           attribute_map={},
                           remove_key_attributes=True,
                           add_attribute=True):
    """
    Takes a dictionary in which each item is a record and returns a list of json strings build from each record.
    Args:
        dictionary: A python dictionary containing each record as an item.
        nmdc_class: The NMDC class (found in nmdc.py) that will be used to convert each record.
        id_key: The key in each record whose value is to be used as the id.
        name_key: The key in each record whose value is to be used as the name.
        description_key: The key in each record whose value is to be used as the description.
        part_of_key: The key in each record whose value is to be used as the part of value.
        has_input_key: The key in each record whose value is to be used as the has input value.
        has_output_key: The key in each record whose value is to be used as the has output value.
        characteristic_fields: A list that contains the names of fields whose values will transformed into characteristics.
        remove_key_attributes: Specifies whether to remove the named keys (e.g, id_key, part_of_key) from the attributes list.
    Returns:
        A list in which each item is a json string.
      
    """
    dict_list = \
        make_nmdc_dict_list(dictionary,
                            nmdc_class,
                            constructor_map=constructor_map,
                            attribute_fields=attribute_fields,
                            attribute_map=attribute_map,
                            remove_key_attributes=remove_key_attributes,
                            add_attribute=add_attribute)
    
    return convert_dict_list_to_json_list(dict_list)


def convert_dict_list_to_json_list (dict_list:list):
    """
    Takes a list of dictionaries, converts each dictionary into json, and returns a list the json strings.
    Args:
      dict_list: A list in which each item is a dictionary.
    Returns:
      A list in which each item is a json string.
    """
    json_list = []  # list to hold json
    
    ## iterate over dict list
    for d in dict_list:
        # print(d)
        # print(jsonasobj.as_json(d))
        # print(json.dumps(d))
        json_list.append(json.dumps(d))
    
    ## return final list
    return json_list


def config_nmdc_class(nmdc_class,
                      constructor_map={},
                      attribute_fields=[],
                      attribute_map={},
                      remove_key_attributes=True,
                      add_attribute=True):
    ## add a 'type' slot to the nmdc class
    ## this allows us to easily inspect the type of entity in the json
    # setattr(nmdc_class, 'type', None)
    
    ## by default, we don't want the constructors for the class
    ## to also be attributes of the object, these keys link objects other objects
    # for key in constructor_map.keys():
    #     if key in attribute_fields:
    #         attribute_fields.remove(key)

    # ## add attribute to the nmdc class if not present
    # if add_attribute:
    #     for af in attribute_fields:
    #         if type({}) == type(af): af = list(af.keys())[0] # needed for attributes given as a dict
    #         if not hasattr(nmdc_class, str(af)): setattr(nmdc_class, str(af), None)
    #         ### TODO ! throw a a warning ###

    #     if len(attribute_map) > 0:
    #         for af in attribute_map.values():
    #             if not hasattr(nmdc_class, af): setattr(nmdc_class, af, None)
                
    return nmdc_class



def make_constructor_args (constructor_map, nmdc_record):
    ## for every mapping between a key and data field create a dict
    ## of the parameters needed to instantiate the class
    constructor_dict = {}
    for key, field in constructor_map.items():
        ## if the fields is a dict, constructor param takes an object
        ## e.g., {'init': {'latitude': 'latitude', 'longitude': 'longitude', 'has_raw_value': 'lat_lon'}, 'class_type': 'GeolocationValue']
        if type({}) == type(field):
            constructor_dict[key] = make_object_from_dict(nmdc_record, field)
        else:
            # print(field)
            constructor_dict[key] = getattr(nmdc_record, field)
    
    return constructor_dict


def make_object_from_dict(nmdc_record:namedtuple, object_dict:dict):
    ## using the data from an nmdc record, create an object from a dict with two keys:
    ## - init 
    ## - class_type
    ## the value of init is a dict represent the constructor(s) needed to instantiate the object
    ## the value of class_types is a string or class reference that is the class the object instantiates
    ## e.g., {'init': {latitude: 'latitude', longitude: 'longitude', has_raw_value: 'lat_lon'}, 'class_type': 'GeolocationValue'}
    
    ## create param name / param value pairs from init values
    constructor_args = \
        {
            # we don't want null/NaN to be a value in the constructor
            # param_name: "" if pds.isnull(getattr(nmdc_record, field)) else getattr(nmdc_record, field) 
            param_name: getattr(nmdc_record, field) for param_name, field in  object_dict['init'].items()
        }
    ## check if the class type is being passed as a string e.g., 'class_type': 'GeolocationValue'
    if type('') == type(object_dict['class_type']):
        class_type = getattr(nmdc, object_dict['class_type'])
    else:
        class_type = object_dict['class_type']

    obj = class_type(**constructor_args) # create object from type
    obj.uriorcurie = class_type.class_class_curie
    return obj


def make_attribute_value (nmdc_record:namedtuple, field):
    """
    Local function used to create attribute_value object linked the the raw value.
    """
    av = nmdc.AttributeValue()
    av.has_raw_value = getattr(nmdc_record, field)
    
    return \
        {k:v for k, v in av.__dict__.items() 
             if pds.notnull(v) and len(v) > 0 } # don't return null or empty values


def make_object_from_list(nmdc_record:namedtuple, nmdc_list:list):
    ## using the data from an nmdc record, create an object from a list in which
    ## - index 0 is a dict represent the constructor param name and nmdc_record field used as the value
    ## - index 1 is the class or class name (i.e., string)
    ## e.g., lat_lon': [{latitude: 'latitude', longitude: 'longitude', has_raw_value: 'lat_lon'}, 'GeolocationValue']
    
    ## create param name / param value pairs from first item in list
    constructor_args = \
        {
            # we don't want null/NaN to be a value in the constructor
            # param_name: "" if pds.isnull(getattr(nmdc_record, field)) else getattr(nmdc_record, field) 
            param_name: getattr(nmdc_record, field) for param_name, field in  nmdc_list[0].items()
        }
    ## check if nmdc class is being passed as a string e.g., lat_lon': ['lat_lon', 'GeolocationValue']
    if type('') == type(nmdc_list[1]):
        class_type = getattr(nmdc, nmdc_list[1])
    else:
        class_type = nmdc_list[1]

    obj = class_type(**constructor_args) # create object from type
    obj.type = class_type.class_class_curie
    return obj


def map_slot_to_entity (slot_map, record):
        """
        Connects a slot to an entity whose type is specified in a map/dict. 
        Example 1, the map: 
            {'part_of': project_gold_ids'}
        specifies that the part_of slot connects to the record's project_ids values.

        Example 2, the map:
           {'part_of': ({'id': 'project_gold_ids'}, nmdc.OmicsProcessing)}
        speficfies that the part_of slot (in this case) connects to an nmdc.OmicsProcessing entity.
        The enity (which I call the 'referenced entity') is identified by project_gold_ids field in the record.
        """
        slot_name = list(slot_map.keys())[0]
        slot_value = list(slot_map.values())[0]
        referenced_entity = None
        
        ## if the slot values is not a tuple, return record's values
        if type(()) != type(slot_value):
            ## if no value found in the record, simply return none
            if pds.isnull(record[slot_value]): return None

            if slot_name in ['part_of', 'has_input', 'has_output']:
                referenced_entity = record[slot_value].split(',')
            else:
                referenced_entity = record[slot_value]
        
        ## if the slot value is a tuple, then construct an object
        if type(()) == type(slot_value):
            param_dict = slot_value[0]
            nmdc_class = slot_value[1]
            id_field = param_dict['id']

            ## if no value found in the record, simply return none
            if pds.isnull(record[id_field]): return None

            if slot_name in ['part_of', 'has_input', 'has_output']:
                id_values = record[id_field].split(',')
                referenced_entity = [nmdc_class(**{'id': id_val}) for id_val in id_values]
                for r in referenced_entity:
                    setattr(r, 'type', nmdc_class.class_class_curie) # add type info
            else:
                referenced_entity = nmdc_class(**{'id':record[id_field]})
                setattr(referenced_entity, 'type', nmdc_class.class_class_curie)

        return referenced_entity


def dataframe_to_dict(nmdc_df:pds.DataFrame, 
                      nmdc_class,
                      constructor_map={},
                      attribute_fields=[],
                      attribute_map={},
                      remove_key_attributes=True,
                      add_attribute=True):

    
    def make_nmdc_object(nmdc_record:namedtuple, nmdc_class):
        ## check for constructor_map  containing the paramaters necessary to instantiate the class
        if len(constructor_map) > 0:
            constructor_args = make_constructor_args(constructor_map, nmdc_record)
            nmdc_obj = nmdc_class(**constructor_args)
        else:
            nmdc_obj = nmdc_class()

        # nmdc_obj.type = nmdc_class.class_class_curie  ## add info about the type of entity it is
        nmdc_obj.uriorcurie = nmdc_class.class_class_curie  ## add info about the type of entity it is
        
        ## get mappings for attribute fields
        for af in attribute_fields:
            ## check if attribute is a dict; e.g. part_of: gold_study_id
            if type({}) == type(af): 
                field, val = list(af.items())[0] # get the field and value parts from dict
                if type({}) == type(val):
                    av = make_object_from_dict(nmdc_record, val) # val is a dict
                else:
                    av = make_attribute_value(nmdc_record, val) # val names the field in the record
            else:
                field = af; av = make_attribute_value(nmdc_record, field) 

            ## check if attribute has been mapped in the sssom file
            if (len(attribute_map) > 0) and (field in attribute_map.keys()):
                setattr(nmdc_obj, attribute_map[field], av)
            else:
                setattr(nmdc_obj, field, av)

        return nmdc_obj

    nmdc_class = \
        config_nmdc_class(nmdc_class, constructor_map, attribute_fields, attribute_map, remove_key_attributes, add_attribute)
    
    ## transform each record into an nmdc object to type nmdc class
    ## and store in list
    nmdc_objs = []
    for record in nmdc_df.itertuples(index=False):
        nmdc_obj = make_nmdc_object(record, nmdc_class)
        nmdc_obj =\
            {k:v for k, v in nmdc_obj.__dict__.items() 
                 if pds.notnull(v) and len(v) > 0 } # don't return null or empty values
        nmdc_objs.append(nmdc_obj)
    return nmdc_objs

def make_nmdc_dict_list (dictionary:dict,
                         nmdc_class,
                         constructor_map={},
                         attribute_fields=[],
                         attribute_map={},
                         remove_key_attributes=True,
                         add_attribute=True):
    """
    Takes a dictionary in which each item is a record and returns a list of dictionaries that conform to the nmdc schema.
    Args:
        dictionary: A python dictionary containing each record as an item.
        nmdc_class: The NMDC class (found in nmdc.py) that will be used to convert each record.
        id_key: The key in each record whose value is to be used as the id.
        name_key: The key in each record whose value is to be used as the name.
        description_key: The key in each record whose value is to be used as the description.
        part_of_key: The key in each record whose value is to be used as the part of value.
        has_input_key: The key in each record whose value is to be used as the has input value.
        has_output_key: The key in each record whose value is to be used as the has output value.
        attribute_fields: A list that contains the names of fields whose values will transformed into characteristics.
        remove_key_attributes: Specifies whether to remove the named keys (e.g, id_key, part_of_key) from the attributes list.
        add_attribute: Specifies whether an attributes in the attribute_fields list should be added to the nmdc class if not already present.
    Returns:
        A list in which each item is a dictionary that conforms to the nmdc schema
      
    """

    def map_slot_to_entity (slot_map, nmdc_record:namedtuple):
        """
        Connects a slot to an entity whose type is specified in a map/dict. 
        Example 1, the map: 
            {'part_of': project_gold_ids'}
        specifies that the part_of slot connects to the record's project_ids values.

        Example 2, the map:
           {'part_of': [{'id': 'project_gold_ids'}, nmdc.OmicsProcessing]}
        speficfies that the part_of slot (in this case) connects to an nmdc.OmicsProcessing entity.
        The enity (which I call the 'referenced entity') is identified by project_gold_ids field in the record.
        """
        slot_name = list(slot_map.keys())[0]
        slot_value = list(slot_map.values())[0]
        referenced_entity = None
        
        ## if the slot values is not a tuple, return record's values
        if type(()) != type(slot_value):
            ## if no value found in the record, simply return none
            if pds.isnull(record[slot_value]): return None

            if slot_name in ['part_of', 'has_input', 'has_output']:
                referenced_entity = record[slot_value].split(',')
            else:
                referenced_entity = record[slot_value]
        
        ## if the slot value is a tuple, then construct an object
        if type(()) == type(slot_value):
            param_dict = slot_value[0]
            nmdc_class = slot_value[1]
            id_field = param_dict['id']

            ## if no value found in the record, simply return none
            if pds.isnull(record[id_field]): return None

            if slot_name in ['part_of', 'has_input', 'has_output']:
                id_values = record[id_field].split(',')
                referenced_entity = [nmdc_class(**{'id': id_val}) for id_val in id_values]
                for r in referenced_entity:
                    setattr(r, 'type', nmdc_class.class_class_curie) # add type info
            else:
                referenced_entity = nmdc_class(**{'id':record[id_field]})
                setattr(referenced_entity, 'type', nmdc_class.class_class_curie)

        return referenced_entity


    def make_constructor_args (constructor_map, record):
        ## for every mapping between a key and data field create a dict
        ## of the parameters needed to instantiate the class
        constructor_dict = {}
        for key, field in constructor_map.items():
            ## if the fields is a list, index 0 is param dict, index 1 is the class
            ## e.g., lat_lon': ['lat_lon', 'GeolocationValue'], or lat_lon': ['lat_lon', nmdc.GeolocationValue]
            if type([]) == type(field):
                params = \
                    {
                        key: "" if pds.isnull(record[value]) else record[value] # we don't want null/NaN to be a value in the constructor
                        for key, value in  field[0].items()
                    }
                ## check if nmdc class is being passed as a string e.g., lat_lon': ['lat_lon', 'GeolocationValue']
                if type('') == type(field[1]):
                    constructor_type = getattr(nmdc, field[1])
                else:
                    constructor_type = field[1]

                constructor_obj = constructor_type(**params) # create object from type
                constructor_obj.type = constructor_type.class_class_curie
                constructor_dict[key] = constructor_obj
            else:
                # print(field)
                constructor_dict[key] = record[field]
        
        return constructor_dict
   
    
    def make_attribute_value (data_value):
        """
        Local function used to create attribute_value object linked the the raw value.
        """
        #print(obj, key, value)
        av = nmdc.AttributeValue()
        av.has_raw_value = data_value
        
        return av
    
    ## add a 'type' slot to the nmdc class
    ## this allows us to easily inspect the type of entity in the json
    setattr(nmdc_class, 'type', None)
    
    ## by default, we don't want the constructors for the class
    ## to also be attributes of the object, these keys link objects other objects
    for key in constructor_map.keys():
        if key in attribute_fields:
            attribute_fields.remove(key)

    ## add attribute to the nmdc class if not present
    if add_attribute:
        for af in attribute_fields:
            if type({}) == type(af): af = list(af.keys())[0] # needed for attributes given as a dict
            if not hasattr(nmdc_class, str(af)): setattr(nmdc_class, str(af), None)
            ### TODO ! throw a a warning ###

        if len(attribute_map) > 0:
            for af in attribute_map.values():
                if not hasattr(nmdc_class, af): setattr(nmdc_class, af, None)
    
    ## for each record in the dictionary, create an object of type nmdc_class and put the object into the list
    dict_list = []  # list to hold individual dictionary objects
    for record in dictionary:
        ## check for constructor_map  containing the paramaters necessary to instantiate the class
        if len(constructor_map) > 0:
            constructor_args = make_constructor_args(constructor_map, record)
            obj = nmdc_class(**constructor_args)
        else:
            obj = nmdc_class()

        obj.type = nmdc_class.class_class_curie  ## add info about the type of entity it is
        
        for key, item in record.items():
            if (not pds.isnull(item)) and ('' != item) and (not (item is None)) and (key in attribute_fields):
                av = make_attribute_value(item)

                ## check if attribute has been mapped to a mixs term
                if len(attribute_map) > 0:
                    if key in attribute_map.keys():
                        mapped_attr = attribute_map[key]
                        setattr(obj, mapped_attr, av)
                    else:
                        setattr(obj, key, av)
                else:
                    setattr(obj, key, av)
        
        ## go though the attribute list and link slots to entities specified in slot map/dict
        ## for example: {part_of: study_gold_id} ####{'part_of': ({'id': 'project_gold_ids'}, nmdc.OmicsProcessing)}
        for af in attribute_fields:
            if type({}) == type(af):
                slot_name = list(af.keys())[0]
                if 'part_of' == slot_name: obj.part_of = map_slot_to_entity (af, record)
                if 'has_input' == slot_name: obj.has_input = map_slot_to_entity(af, record)
                if 'has_output' == slot_name: obj.has_output = map_slot_to_entity(af, record)
                
        dict_obj = json.loads(jsonasobj.as_json(obj))  # in order to not save empty values you need to convert to json
        dict_list.append(dict_obj)  # and then loads json to get dict; this may be a bug
    
    ## return final list
    return dict_list

