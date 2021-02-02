## author: Bill Duncan
## summary: Contians methods for transforming data in NMDC ETL pipeline.

## add ./lib and rooth directory to sys.path so that local modules can be found
import os, sys, git_root
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./lib"))
sys.path.append(git_root.git_root('./schema'))
# print(sys.path)

## system level modules
import pandas as pds
import jq
import jsonasobj
import json
import jq
import zipfile
import yaml
from yaml import CLoader as Loader, CDumper as Dumper
from dotted_dict import DottedDict
from collections import namedtuple
import nmdc_dataframes

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


def make_constructor_dict_from_record(constructor_map:dict, nmdc_record:namedtuple):
    ## for every mapping between a key and data field create a dict
    ## of the parameters needed to instantiate the class
    constructor_dict = {}
    for key, field in constructor_map.items():
        ## if the fields is a dict, constructor param takes an object
        ## e.g., {'init': {'latitude': 'latitude', 'longitude': 'longitude', 'has_raw_value': 'lat_lon'}, 'class_type': 'GeolocationValue']
        if type({}) == type(field):
            ## create param name / param value pairs from init values
            constructor_dict = \
                {
                    param_name: getattr(nmdc_record, field) for param_name, field in  constructor_map.items()
                }
        else:
            constructor_dict[key] = getattr(nmdc_record, field)
    
    return constructor_dict


def make_constructor_args_from_record(constructor_map:dict, nmdc_record:namedtuple):
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


def make_dict_from_nmdc_obj(nmdc_obj):
        def is_value(variable):
            ## check if variable is None
            if (not variable): return False 
            
            ## check for zero len variable
            if (type([]) == type(variable) 
                or type({}) == type(variable)
                or type('') == type(variable)):
                if len(variable) == 0:
                    return False
            else:
                if pds.isnull(variable): return False  ## check for null
            
            ## if variable is a dict, make sure it has an id or raw value
            if type({}) == type(variable):
                if 'id' in variable.keys():
                    return is_value(variable['id']) # check if id has a value
                elif 'has_raw_value' in variable.keys():
                    return is_value(variable['has_raw_value']) # check if has_raw_value has a value
                else:
                    return False # if it makes it here, there wasn't an id or has_raw_value
            
            return True # if it makes it here, all good
                            
        def make_dict(obj):
            """
            transforms an nmdc object into a dict
            """
            if obj == None: return # make sure the object has a value
            
            ## check if obj can convert to dict
            if not hasattr(obj, '_as_dict'): return obj
            
            # temp_dict = jsonasobj.as_dict(obj) # convert obj dict
            temp_dict = {}
            obj_dict = {} 
            
            ## include only valid values in lists and dicts
            for key, val in jsonasobj.as_dict(obj).items():
                # print('key:', key, '\n', ' val:', val, '\n')
                if type({}) == type(val): # check values in dict
                    temp_dict[key] = {k:v for k,v in val.items() if is_value(v)}
                elif type([]) == type(val): # check values in list
                    temp_dict[key] = [element for element in val if is_value(element)]
                else:
                    temp_dict[key] = val
            
            ## check for {} or [] that may resulted from prevous loop
            for key, val in temp_dict.items():
                if is_value(val):
                    obj_dict[key] = val
                    
            return obj_dict
        
        if type([]) == type(nmdc_obj):
            # print('nndc_obj:', nmdc_obj)
            nmdc_dict = [make_dict(o) for o in nmdc_obj if is_value(o)]
            # print('nmdc_dict:', nmdc_dict)
        else:
            nmdc_dict = make_dict(nmdc_obj)

        return nmdc_dict


def set_nmdc_object(nmdc_obj, 
                    nmdc_record:namedtuple,
                    attribute_map:dict,
                    attribute_field):
    
    ## check if attribute is a dict; e.g. part_of: gold_study_id
    if type({}) == type(attribute_field): 
        field, val = list(attribute_field.items())[0] # get the field and value parts from dict
        if type([]) == type(val):
            av = make_object_from_list(nmdc_record, val)
        elif type({}) == type(val):  
            av = make_object_from_dict(nmdc_record, val) # val is a dict
        else:
            av = make_attribute_value_from_record(nmdc_record, val) # val names the field in the record
    elif type("") == type(attribute_field) and "," in attribute_field:
        field = attribute_field.split(",")[0].strip() # e.g., "file_size_bytes, int"
        av = make_value_from_string(nmdc_record, attribute_field)
    else:
        field = attribute_field 
        av = make_attribute_value_from_record(nmdc_record, field)

    ## convert attribute value into a dict
    av = make_dict_from_nmdc_obj(av)

    ## check if attribute has been mapped in the sssom file
    if (len(attribute_map) > 0) and (field in attribute_map.keys()):
        setattr(nmdc_obj, attribute_map[field], av)
    else:
        setattr(nmdc_obj, field, av)

    return nmdc_obj


def make_attribute_value_from_record(nmdc_record:namedtuple, field, uriorcurie=''):
    """
    Creates an attribute value object linked the value in the nmdc record's field.
    """
    val = getattr(nmdc_record, field)
    av = make_attribute_value(val, uriorcurie)
    
    return av


def make_attribute_map(sssom_map_file:str):
    attr_map = {}
    if len(sssom_map_file) > 0:
        ## load sssom mapping file and subset to skos:exactMatch
        mapping_df = nmdc_dataframes.make_dataframe(sssom_map_file, comment_str='#').query("predicate_id == 'skos:exactMatch'")
        attr_map = {subj:obj for idx, subj, obj in mapping_df[['subject_label', 'object_label']].itertuples()} # build attribute dict
    
    return attr_map


def make_attribute_value(val, uriorcurie=''):
    """
    Creates an attribute value object linked to value val.
    """
    av = nmdc.AttributeValue()
    if pds.notnull(val):
        av.has_raw_value = val
        av.uriorcurie = \
            uriorcurie if len(uriorcurie) > 0 else nmdc.AttributeValue.class_class_curie
    
    return av


def make_nmdc_class_type(class_type):
    ## check if the class type is being passed as a string e.g., 'class_type': 'GeolocationValue'
    if type('') == type(class_type):
        class_type = getattr(nmdc, class_type)
    return class_type


def make_uriorcuri(object_dict={}, class_type=None, uriorcurie=''):
    ## return uriorcurie based on rules
    if 'uriorcurie' in object_dict.keys():
        return object_dict['uriorcurie']
    elif len(uriorcurie) > 0:
        return uriorcurie
    else:
        return class_type.class_class_curie


def make_object_from_dict(nmdc_record:namedtuple, object_dict:dict, uriorcurie=''):
    ## using the data from an nmdc record, create an object 
    ## There are two ways to do this:
    ##   1. using the keys init and class_type
    ##      the value of init is a dict represent the constructor(s) needed to instantiate the object
    ##      the value of class_types is a string or class reference that is the class the object instantiates
    ##      e.g., {'init': {latitude: 'latitude', longitude: 'longitude', has_raw_value: 'lat_lon'}, 'class_type': 'GeolocationValue'}
    ##   2. using the id and uriorcurie keys
    ##      This acts as a kind of foreign key to another object.
    ##      The id key specifice the id of ojbect and the uriorcurie specifies the type of object referenced
    
    if 'init' in object_dict.keys():
        ## create param name / param value pairs from init values
        constructor_map = object_dict['init']
        constructor_args = make_constructor_dict_from_record(constructor_map, nmdc_record)

        class_type = make_nmdc_class_type(object_dict['class_type']) # get class type
        obj = class_type(**constructor_args) # create object from type
    elif 'id' in object_dict.keys():
        class_type = nmdc.AttributeValue; obj = class_type() # create AttributeValue object
        obj.id = getattr(nmdc_record, object_dict['id'])
    else:
        class_type = nmdc.AttributeValue; obj = class_type() # create AttributeValue object
    
    # check if a raw value has been assigned
    if 'has_raw_value' in object_dict.keys(): 
        obj.has_raw_value = getattr(nmdc_record, object_dict['has_raw_value'])

    ## set the uriorcurie of object
    obj.uriorcurie = make_uriorcuri(object_dict, class_type, uriorcurie)

    return obj


def make_object_from_list(nmdc_record:namedtuple, nmdc_list:list):
    obj_list = []
    for val in nmdc_list:
        if type({}) == type(val):
            ## e.g., {part_of: {init: {id: study_gold_id}, class_type: Study}}
            if 'init' in val.keys():
                init_dict = val['init']
                class_type = val['class_type']
            
                ## get each value from the nmdc record as specified 
                ## by the key in the init dictionary
                ## e.g., {'part_of': 'study_ids', 'name': 'study_names'} 
                ##       -> {'part_of': [1, 2], 'name': ['foo', 'bar']}
                values_dict = {}
                for k, v in init_dict.items():
                    record_vals = getattr(nmdc_record, v)
                    if pds.notnull(record_vals): # check for null
                        values_dict[k] = record_vals.split(',')

                if len(values_dict) < 1: continue # make sure we have values

                ## set variables for easy access
                keys = list(values_dict.keys())
                values = list(values_dict.values())
                value_len = len(values_dict[keys[0]])

                ## grab the ith value for each value and create a
                ## new dictionary based on this pairing with the keys
                ## e.g., {'part_of': [1, 2], 'name': ['foo', 'bar']}
                ##       -> [[1, 'foo'], [2, 'bar']]
                ##       -> dict(zip(['part_of', 'name'], [1, 'foo']))
                ##       -> {'id': '1', 'name': 'foo'}
                ##       -> dict(zip(['part_of', 'name'], [2, 'bar']))
                ##       -> {'id': '2', 'name': 'bar'}
                ## each dict is used to create the object
                for i in range(value_len):
                    ith_vals = [v[i] for v in values] # e.g., [1, 'foo'], [2, 'bar']]
                    temp_dict = dict(zip(keys, ith_vals)) # e.g., {'id': '1', 'name': 'foo'}
                    class_type = getattr(nmdc, val['class_type'])

                    ## create object and add to list
                    obj = class_type(**temp_dict)
                    obj.uriorcurie = class_type.class_class_curie
                    obj_list.append(obj)
            else:
                ## e.g., {has_input [{id: biosample_gold_id, uriorcurie: nmdc:Biosample}]}
                obj = make_object_from_dict(nmdc_record, val, val['uriorcurie'])
                obj_list.append(obj)

        else:
            record_vals = getattr(nmdc_record, val)
            if pds.notnull(record_vals): # check for null
                ## e.g. {has_output: output_file_ids}
                for rv in record_vals.split(','):
                    av = make_attribute_value(rv)
                    obj_list.append(av)

        return obj_list


def make_value_from_string(nmdc_record:namedtuple, attribute_string: str):

    ## e.g., "file_size_bytes, int"
    ## get field and datatype from attribute string and strip spaces
    field, dtype = attribute_string.split(",")
    field, dtype = field.strip(), dtype.strip()
    
    ## get value from record
    val = getattr(nmdc_record, field)
    
    if pds.notnull(val):
        return eval(f"""{dtype}("{val}")""") # convert value to specified datatype
    else:
        return None


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
            constructor_args = make_constructor_args_from_record(constructor_map, nmdc_record)
            nmdc_obj = nmdc_class(**constructor_args)
        else:
            nmdc_obj = nmdc_class()

        nmdc_obj.uriorcurie = nmdc_class.class_class_curie  ## add info about the type of entity it is
        
        ## get mappings for attribute fields
        for af in attribute_fields:
            nmdc_obj = set_nmdc_object(nmdc_obj, nmdc_record, attribute_map, af)
            
        return nmdc_obj

    nmdc_class = \
        config_nmdc_class(nmdc_class, constructor_map, attribute_fields, attribute_map, remove_key_attributes, add_attribute)
    
    ## transform each record into an nmdc dict and store in list
    nmdc_objs = []
    for record in nmdc_df.itertuples(index=False):
        nmdc_obj = make_nmdc_object(record, nmdc_class) # create individual object
        nmdc_dict = make_dict_from_nmdc_obj(nmdc_obj) # transform object into a dict
        nmdc_objs.append(nmdc_dict) # add object to list
    return nmdc_objs


def get_json(file_path, replace_single_quote=False):
    ## load json
    with open(file_path, 'r') as in_file:
        if replace_single_quote: # json
            text = in_file.read()
            json_data = json.loads(text.replace("'", '"'))
        else:
            json_data =  json.load(in_file)
    return json_data


def save_json(json_data, file_path):
    ## if json data is a string, it will need to be
    ## loaded into a variable to for "\" escape characters
    if type(json_data) == type(""):
        json_data = json.loads(json_data)
        
    ## save json with changed data types
    with open(file_path, 'w') as out_file:
        json.dump(json_data, out_file, indent=2)
    return json_data


def collapse_json_file(file_path, json_property, collapse_property="id", replace_single_quote=False):
    jdata = get_json(file_path, replace_single_quote)
    return collapse_json_data(jdata, json_property, collapse_property)


def collapse_json_data(json_data, json_property, collapse_property="id"):
    if type(json_data) == type(""):
        jdata = json.loads(json_data)
    else:
        jdata = json_data.copy()
    
    print(jdata)
    
    for data in jdata:
        if type(data) == type({}) and json_property in data.keys():
            values = data[json_property]
            if type(values) == type([]):
                data[json_property] = [val[collapse_property] for val in values]
            else:
                data[json_property] = values[collapse_property]

    if type(json_data == type("")):
        return json.dumps(jdata)
    else:
        return jdata

    
if __name__ == "__main__":
    ## code for testing
    file_path = '../output/nmdc_etl/test.json'
    # test_json = collapse_json_file(file_path, 'part_of')
    # test_json = collapse_json_file(file_path, 'has_input')
    test_json = collapse_json_file(file_path, 'has_output')
    print(test_json)
    

