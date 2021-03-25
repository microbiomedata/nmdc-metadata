## author: Bill Duncan
## summary: Contians methods for transforming data in NMDC ETL pipeline.

## add ./lib and rooth directory to sys.path so that local modules can be found
import os, sys, git_root

sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./lib"))
sys.path.append(git_root.git_root("./schema"))
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


def has_raw_value(obj, attribute: str) -> bool:
    """
    Helper function that returns True/False if a an object attribute
    has a has_raw_value property.
    E.g.: "lat_lon": {"has_raw_value": "-33.460524 150.168149"}

    Args:
        obj (dict or object):
        attribute (string): the name of the attribute in obj to check.

    Returns:
        boolean: True if haw_raw_value property is present.
    """

    val = getattr(obj, attribute)  # get value of object

    if val is None:  # check that value exists
        return False

    ## if val is a dict, check that it has a has_raw_value key
    ## and that the value is not null
    if type(val) == type({}):
        if "has_raw_value" in val.keys():
            return pds.notnull(val["has_raw_value"])
        else:
            return False

    ## if val is not a dict, assume it is a class
    ## and check has_raw_value
    obj_vars = vars(val)
    if "has_raw_value" in obj_vars.keys():
        return pds.notnull(obj_vars["has_raw_value"])
    else:
        return False


def record_has_field(nmdc_record: namedtuple, attribute_field: str) -> bool:
    """
    Returns True/False if a field is in nmdc_record (a namedtuple).

     Args:
        nmdc_record (namedtuple): the nmdc record
        attribute_field (string): the name of the attribute

    Returns:
        bool: True if the record has the field.
    """
    if pds.isnull(nmdc_record):
        return None

    if "," in attribute_field:  # e.g., "file_size_bytes, int"
        field = attribute_field.split(",")[0].strip()
    else:  # default to string datatype
        field = attribute_field.strip()

    return field in nmdc_record._fields


def coerce_value(value, dtype: str):
    """
    Coerces value into the type specified by dtype and returns the coerced value.

    Args:
        value: the value to coerece
        dtype (str): the data type to coerce/cast value into

    Returns:
        the value cast into the data type specified by dtype
    """
    if value is None:
        return None

    if dtype != "str":  # only do the eval when it is not a string
        return eval(f"""{dtype}({value})""")  # convert value to specified datatype
    else:
        return f"""{value}"""


def get_dtype_from_attribute_field(attribute_field) -> str:
    """
    Return data type part of attribute_field (e.g. 'file_size, int').
    If no dtype is given, "str" is returned.

    Args:
        attribute_field: the attribute field to get the data type from

    Returns:
        str: the string representation of the attribute field's data type
    """
    if type(attribute_field) == type({}):
        if "$const" in attribute_field.keys():
            ## NB: RECURSIVE CALL
            dtype = get_dtype_from_attribute_field(attribute_field["$const"])
        else:
            dtype = "str"
    elif "," in attribute_field:  # e.g., "file_size_bytes, int"
        dtype = attribute_field.split(",")[1].strip()
    else:  # default to string datatype
        dtype = "str"

    return dtype


def get_field_and_dtype_from_attribute_field(attribute_field) -> tuple:
    """
    Returns both the field and data type parts of attribute_field (e.g. 'file_size, int').
    If no dtype is given, a dtype of "str" is returned.

     Args:
        attribute_field: the name of the attribute field

    Returns:
        tuple: contains the (field, data type)
    """
    if type(attribute_field) == type({}):
        if "$const" in attribute_field.keys():
            ## NB: RECURSIVE CALL
            field, dtype = get_field_and_dtype_from_attribute_field(
                attribute_field["$const"]
            )
        elif "$field" in attribute_field.keys():
            ## NB: RECURSIVE CALL
            field, dtype = get_field_and_dtype_from_attribute_field(
                attribute_field["$field"]
            )
        else:
            field, dtype = attribute_field, "str"
    elif "," in attribute_field:  # e.g., "file_size_bytes, int"
        field, dtype = attribute_field.split(",")
        field, dtype = field.strip(), dtype.strip()
    else:  # default to string datatype
        field, dtype = attribute_field.strip(), "str"

    return field, dtype


def get_record_attr(record: namedtuple, attribute_field, return_field_if_none=True):
    """
    Returns the value specified by attribute_field in the record.
    E.g., get_record_attr(Record(id='gold:001', name='foo'), 'id') would return 'gold:001'.

    In some cases, the attribure_field may used for constant value (e.g., unit: meter).
    In these case the return_field_if_none (default True), specifies whether to return the
    constant value (e.g., return 'meter' instead of None)

    Args:
        record (namedtuple): the record containing the data
        attribute_field: the name of the field that contains the data
        return_field_if_none (bool, optional): Defaults to True.

    Returns:
        the value of record's field
    """
    ## check for constant
    if type({}) == type(attribute_field) and "$const" in attribute_field.keys():
        field, dtype = get_field_and_dtype_from_attribute_field(
            attribute_field["$const"]
        )
        return coerce_value(field, dtype)

    ## get field name and data type
    field, dtype = get_field_and_dtype_from_attribute_field(attribute_field)

    ## get value from record
    if record_has_field(record, field):  # check field
        val = getattr(record, field)
    else:  #### ********** Return value of field or None ******************* #######
        val = field if return_field_if_none else None

    if pds.notnull(val):
        return coerce_value(val, dtype)
    else:
        return None


def make_constructor_args_from_record(
    constructor_map: dict, nmdc_record: namedtuple
) -> dict:
    """
    Returns the constructor arguments as a dict that are needed to build an object.
    E.g., If the constructor map specifies that a Study object requires an id and name in
    the constructor, this function would return {id: gold:001, name: foo}.

    Args:
        constructor_map (dict): the arguments specified to build an object
        nmdc_record (namedtuple): holds the data that is used to build an object

    Returns:
        dict: the constructor arguments needed to build the object
    """
    ## for every mapping between a key and data field create a dict
    ## of the parameters needed to instantiate the class
    constructor_dict = {}
    for key, field in constructor_map.items():
        ## if the fields is a dict, constructor param takes an object
        ## e.g., {'latitude': 'latitude', 'longitude': 'longitude', 'has_raw_value': 'lat_lon', '$class_type': 'GeolocationValue'}
        if type({}) == type(field) and len(field) > 0:
            ## get values from the nmdc record for each field name
            record_dict = make_record_dict(nmdc_record, field)
            ## find constructors defined by the initialization key
            if "$class_type" in field.keys():
                class_type = make_nmdc_class(field["$class_type"])  # get class type

                ## update constructor dict
                constructor_dict[key] = class_type(**record_dict)
            else:
                constructor_dict[key] = record_dict
        else:
            constructor_dict[key] = get_record_attr(nmdc_record, field)

    return constructor_dict


def make_dict_from_nmdc_obj(nmdc_obj) -> dict:
    """
    Returns a dict based on the nmdc_obj.

    Args:
        nmdc_obj: an object containing nmdc data

    Returns:
        dict: representation of the object
    """

    def is_value(variable):
        """
        Checks if variable has a value. Returns True if:
        - variable is not None and
        - has length > 0 if variable is a list and dict and
        - has an id and/or has raw value key if variable is a dict
        """
        ## check if variable is None
        if variable is None:
            return False

        ## check for zero len variable
        if (
            type([]) == type(variable)
            or type({}) == type(variable)
            or type("") == type(variable)
        ):
            if len(variable) == 0:
                return False
        else:
            if pds.isnull(variable):
                return False  ## check for null

        ## if variable is a dict, make sure it has an id or raw value
        if type({}) == type(variable):
            if "id" in variable.keys():
                return is_value(variable["id"])  # check if id has a value
            elif "has_raw_value" in variable.keys():
                return is_value(
                    variable["has_raw_value"]
                )  # check if has_raw_value has a value
            else:
                return False  # if it makes it here, there wasn't an id or has_raw_value

        return True  # if it makes it here, all good

    def make_dict(obj):
        """
        Transforms an nmdc object into a dict
        """
        if obj == None:
            return  # make sure the object has a value

        ## check if obj can convert to dict
        if not hasattr(obj, "_as_dict"):
            return obj

        # temp_dict = jsonasobj.as_dict(obj) # convert obj dict
        temp_dict = {}
        obj_dict = {}

        ## include only valid values in lists and dicts
        for key, val in jsonasobj.as_dict(obj).items():
            # print('key:', key, '\n', ' val:', val, '\n')
            if type({}) == type(val):  # check values in dict
                temp_dict[key] = {k: v for k, v in val.items() if is_value(v)}
            elif type([]) == type(val):  # check values in list
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

    def make_dict(obj):
        """
        transforms an nmdc object into a dict
        """
        if obj == None:
            return  # make sure the object has a value

        ## check if obj can convert to dict
        if not hasattr(obj, "_as_dict"):
            return obj

        # temp_dict = jsonasobj.as_dict(obj) # convert obj dict
        temp_dict = {}
        obj_dict = {}

        ## include only valid values in lists and dicts
        for key, val in jsonasobj.as_dict(obj).items():
            # print('key:', key, '\n', ' val:', val, '\n')
            if type({}) == type(val):  # check values in dict
                temp_dict[key] = {k: v for k, v in val.items() if is_value(v)}
            elif type([]) == type(val):  # check values in list
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


def set_nmdc_object(
    nmdc_obj, nmdc_record: namedtuple, attribute_map: dict, attribute_field
):
    ## by default property values are represented as dicts
    ## the exception is when an value is created using '$init'
    ## e.g. {'$init': {'latitude': 'latitude', 'longitude': 'longitude', 'has_raw_value': 'lat_lon'}, '$class_type': 'GeolocationValue'}
    ## when '$init' is used the represent as dict flag is changed
    represent_as_dict = True

    ## check if attribute is a dict; e.g. part_of: gold_study_id
    if type({}) == type(attribute_field):
        ## get the field and value parts from dict
        field, val = list(attribute_field.items())[0]
        if type([]) == type(val):
            av = make_object_from_list(nmdc_record, val)
        elif type({}) == type(val):
            av = make_object_from_dict(nmdc_record, val)  # val is a dict

            ## check if the av needs to be represented as an object
            if "$init" in val.keys():
                represent_as_dict = False

        elif type("") == type(val):  # e.g. has_output: "data_object_id, str"
            av = make_value_from_string(nmdc_record, val)
        else:
            ## val names the field in the record
            av = make_attribute_value_from_record(nmdc_record, val)
    elif type("") == type(attribute_field):
        if "," in attribute_field:
            ## e.g., "file_size_bytes, int"
            field = attribute_field.split(",")[0].strip()
        else:
            field = attribute_field.strip()

        av = make_value_from_string(nmdc_record, attribute_field)
    else:
        field = attribute_field
        av = make_attribute_value_from_record(nmdc_record, field)

    ## convert attribute value into a dict
    if represent_as_dict == True:
        av = make_dict_from_nmdc_obj(av)

    ## check if attribute has been mapped in the sssom file
    if (len(attribute_map) > 0) and (field in attribute_map.keys()):
        setattr(nmdc_obj, attribute_map[field], av)
    else:
        setattr(nmdc_obj, field, av)

    return nmdc_obj


def make_attribute_value_from_record(nmdc_record: namedtuple, field, object_type=""):
    """
    Creates an attribute value object linked the value in the nmdc record's field.
    """
    # val = getattr(nmdc_record, field)
    val = get_record_attr(nmdc_record, field)
    av = make_attribute_value(val, object_type)

    return av


def make_attribute_map(sssom_map_file: str):
    attr_map = {}
    if len(sssom_map_file) > 0:
        ## load sssom mapping file and subset to skos:exactMatch
        mapping_df = nmdc_dataframes.make_dataframe(
            sssom_map_file, comment_str="#"
        ).query("predicate_id == 'skos:exactMatch'")
        attr_map = {
            subj: obj
            for idx, subj, obj in mapping_df[
                ["subject_label", "object_label"]
            ].itertuples()
        }  # build attribute dict

    return attr_map


def make_attribute_value(val, object_type=""):
    """
    Creates an attribute value object linked to value val.
    """
    av = nmdc.AttributeValue()
    if pds.notnull(val):
        av.has_raw_value = val

    return av


def make_nmdc_class(class_type):
    ## check if the class type is being passed as a string e.g., '$class_type': 'GeolocationValue'
    if type("") == type(class_type):
        class_type = getattr(nmdc, class_type)
    return class_type


def make_uriorcuri(object_dict={}, class_type=None, uriorcurie=""):
    ## return uriorcurie based on rules
    if "uriorcurie" in object_dict.keys():
        return object_dict["uriorcurie"]
    elif len(uriorcurie) > 0:
        return uriorcurie
    else:
        return class_type.class_class_curie


def make_object_type(object_dict={}, class_type=None, object_type=""):
    ## return object type based on rules
    if "$class_type" in object_dict.keys():
        return object_dict["$class_type"]
    elif type(class_type) == type(""):
        return class_type
    elif len(object_type) > 0:
        return object_type
    else:
        return class_type.class_class_curie


def make_object_from_dict(nmdc_record: namedtuple, object_dict: dict):
    ## using the data from an nmdc record, create an object
    ## There are two ways to do this:
    ##   1. using the keys $init and $class_type
    ##      the value of $init is a dict represent the constructor(s) needed to instantiate the object
    ##      the value of $class_typ is a string or class reference that is the class the object instantiates
    ##      e.g., {'$init': {latitude: 'latitude', longitude: 'longitude', has_raw_value: 'lat_lon'}, '$class_type': 'GeolocationValue'}
    ##   2. using dict to specify the properties of an attibute value object

    ## determine the type of class
    if "$class_type" in object_dict.keys():
        class_type = make_nmdc_class(object_dict["$class_type"])
    else:
        class_type = nmdc.AttributeValue

    if "$init" in object_dict.keys():
        ## get this intitialization dict and use it build constructor arguments
        constructor_map = object_dict["$init"]

        ## create constructor arguments from the intitialization dict
        constructor_args = make_constructor_dict_from_record(
            constructor_map, nmdc_record
        )
        obj = class_type(**constructor_args)  # create object from type
    else:
        obj = class_type()  # create AttributeValue object
        for obj_key, obj_val in object_dict.items():
            # if obj_key != "$class_type":  # ignore key specifying the class type
            if type({}) == type(obj_val):
                ## if the object value is a dict (e.g., {has_unit: {const: 'meter'}})
                ## then set the value to the dict's value
                record_value = list(obj_val.values())[0]
            elif record_has_field(nmdc_record, obj_val):
                ## get records value from nmdc record
                record_value = get_record_attr(nmdc_record, obj_val)
            else:
                ## catch all condition: simply add key/val to ojbect
                ## this is useful for adding extra informaton to the dict; e.g:
                ##   {has_raw_value: '10', type: QuantityValue}
                ## NB: the keys '$init' and '$class_type' has special meaning and will throw an error if used
                record_value = obj_val

            setattr(obj, obj_key, record_value)

    return obj


def make_object_from_list(nmdc_record: namedtuple, nmdc_list: list):
    obj_list = []
    for val in nmdc_list:
        if type({}) == type(val):
            if "field" in val.keys():
                ## e.g., [{field: data_object_id, dtype: str, multivalued: true}]
                ## get record value for the field
                # record_val = getattr(nmdc_record, val["field"])
                record_val = get_record_attr(nmdc_record, val["field"])

                ## check the record value is not None
                if record_val is not None:
                    ## set datatype for values
                    if "dtype" in val.keys():
                        dtype = val["dtype"]
                    else:
                        dtype = "str"

                    ## check if record needs to be split
                    if "split_val" in val.keys():
                        split_val = val["split_val"]
                        if type(record_val) != type(""):
                            record_val = str(
                                record_val
                            )  # make sure record_val is a string

                        for rv in record_val.split(split_val):
                            ## coerce into datatype
                            if dtype == "str":
                                obj_list.append(str(rv))
                            else:
                                obj_list.append(eval("""{dtype}({rv})"""))
                    else:
                        ## coerce into datatype
                        if dtype == "str":
                            obj_list.append(str(record_val))
                        else:
                            obj_list.append(eval("""{dtype}({record_val}"""))

            elif "$init" in val.keys():
                ## e.g., {part_of: {$init: {id: study_gold_id}, $class_type: Study}}
                init_dict = val["$init"]
                class_type = val["$class_type"]

                ## get each value from the nmdc record as specified
                ## by the key in the $init dictionary
                ## e.g., {'part_of': 'study_ids', 'name': 'study_names'}
                ##       -> {'part_of': [1, 2], 'name': ['foo', 'bar']}
                values_dict = {}
                for k, v in init_dict.items():
                    # record_vals = getattr(nmdc_record, v)
                    record_vals = get_record_attr(nmdc_record, v)
                    if pds.notnull(record_vals):  # check for null
                        values_dict[k] = record_vals.split(",")

                if len(values_dict) < 1:
                    continue  # make sure we have values

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
                    ith_vals = [v[i] for v in values]  # e.g., [1, 'foo'], [2, 'bar']]
                    temp_dict = dict(
                        zip(keys, ith_vals)
                    )  # e.g., {'id': '1', 'name': 'foo'}
                    class_type = getattr(nmdc, val["$class_type"])

                    ## create object and add to list
                    obj = class_type(**temp_dict)
                    obj.type = class_type.class_class_curie
                    obj_list.append(obj)
            else:
                ## e.g., {has_input [{id: biosample_gold_id, $class_type: nmdc:Biosample}]}
                obj = make_object_from_dict(nmdc_record, val)
                obj_list.append(obj)
        elif type("") == type(val):
            ## e.g., has_output: ["data_object_id, str"]
            record_val = make_value_from_string(nmdc_record, val)
            obj_list.append(record_val)
        else:
            ## this is default case: the record is turned into an attribute value
            # record_val = getattr(nmdc_record, val)
            record_val = get_record_attr(nmdc_record, val)

            ## check the record value is not None
            if record_val is not None:
                av = make_attribute_value(record_val)
                obj_list.append(av)

        return obj_list


def make_value_from_string(nmdc_record: namedtuple, attribute_string: str):
    val = get_record_attr(nmdc_record, attribute_string)

    if pds.notnull(val):
        return val
    else:
        return None


def dataframe_to_dict(
    nmdc_df: pds.DataFrame,
    nmdc_class,
    constructor_map={},
    attribute_fields=[],
    attribute_map={},
    transform_map={},
):
    def make_nmdc_object(nmdc_record: namedtuple, nmdc_class):
        ## check for constructor_map  containing the paramaters necessary to instantiate the class
        if len(constructor_map) > 0:
            constructor_args = make_constructor_args_from_record(
                constructor_map, nmdc_record
            )
            nmdc_obj = nmdc_class(**constructor_args)
        else:
            nmdc_obj = nmdc_class()

        nmdc_obj.type = (
            nmdc_class.class_class_curie
        )  ## add info about the type of entity it is

        ## get mappings for attribute fields
        for af in attribute_fields:
            nmdc_obj = set_nmdc_object(nmdc_obj, nmdc_record, attribute_map, af)

        return nmdc_obj

    ## create transform kwargs and pre and post transform lists
    tx_kwargs = {
        "nmdc_class": nmdc_class,
        "constructor_map": constructor_map,
        "attribute_fields": attribute_fields,
        "attribute_map": attribute_map,
    }
    pre_transforms = transform_map["pre"] if "pre" in transform_map.keys() else []
    post_transforms = transform_map["post"] if "post" in transform_map.keys() else []

    ## execute specified pre transformations; note: this transforms the dataframe
    for transform in pre_transforms:
        tx_function = eval(transform["function"])  # dynamically load function
        tx_attributes = transform["attributes"]  # get list of attibutes

        ## apply transform funciton
        nmdc_df = tx_function(nmdc_df, tx_attributes)

    ## transform each record into an nmdc object and store in list
    ## NB: SSSOM mapping is performed during this step
    nmdc_objs = [
        make_nmdc_object(record, nmdc_class)
        for record in nmdc_df.itertuples(index=False)
    ]

    ## set value to None for fields that have dicts as values
    ## but not an id or has_raw_value key
    ## this needed in case conversions resulted in junk values
    for obj in nmdc_objs:
        for key, val in obj.__dict__.items():
            if type(val) == type({}):
                if (not "id" in val.keys()) and (not "has_raw_value" in val.keys()):
                    obj.__dict__[key] = None

    ## execute specified post transformations; note: this transforms the nmdc objects
    for transform in post_transforms:
        tx_function = eval(transform["function"])  # dynamically load function
        tx_attributes = transform["attributes"]  # get list of attibutes

        ## apply transform funciton
        nmdc_objs = tx_function(nmdc_objs, tx_attributes, **tx_kwargs)

    ## transform each nmdc object in a dict and store in list
    nmdc_dicts = [make_dict_from_nmdc_obj(obj) for obj in nmdc_objs]

    ## return list of dicts
    return nmdc_dicts


def test_pre_transform(nmdc_df, tx_attributes, **kwargs):
    print("*** test pre-transform ******")
    return nmdc_df


def make_quantity_value(nmdc_objs, tx_attributes, **kwargs):
    """
    Takes each nmdc object (either a dict or class instance) and
    and adds has_numeric_value and has_unit information.
    """
    print(f"*** executing make_quantity_value for attributes {tx_attributes}")
    for attribute in tx_attributes:
        for obj in nmdc_objs:
            if has_raw_value(obj, attribute):

                val = getattr(obj, attribute)
                # print("*** pre ***", val)

                ## split raw value after first space
                if type(val) == type({}):
                    value_list = str(val["has_raw_value"]).split(" ", 1)
                else:
                    value_list = str(getattr(val, "has_raw_value")).split(" ", 1)

                ## assign numeric quantity value
                if type(val) == type({}):
                    try:
                        val["has_numeric_value"] = float(value_list[0].strip())
                    except Exception as ex:
                        pass
                else:
                    try:
                        val.has_numeric_value = float(value_list[0].strip())
                    except Exception as ex:
                        pass

                ## assign unit if present
                if len(value_list) > 1:
                    if type(val) == type({}):
                        val["has_unit"] = value_list[1].strip()
                    else:
                        val.has_unit = value_list[1].strip()

                # print("*** post ***", val)

    return nmdc_objs


def get_json(file_path, replace_single_quote=False):
    ## load json
    with open(file_path, "r") as in_file:
        if replace_single_quote:  # json
            text = in_file.read()
            json_data = json.loads(text.replace("'", '"'))
        else:
            json_data = json.load(in_file)
    return json_data


def save_json(json_data, file_path):
    ## if json data is a string, it will need to be
    ## loaded into a variable to for "\" escape characters
    if type(json_data) == type(""):
        json_data = json.loads(json_data)

    ## save json with changed data types
    with open(file_path, "w") as out_file:
        json.dump(json_data, out_file, indent=2)
    return json_data


def collapse_json_file(
    file_path, json_property, collapse_property="id", replace_single_quote=False
):
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
    file_path = "../output/nmdc_etl/test.json"
    # test_json = collapse_json_file(file_path, 'part_of')
    # test_json = collapse_json_file(file_path, 'has_input')
    test_json = collapse_json_file(file_path, "has_output")
    print(test_json)