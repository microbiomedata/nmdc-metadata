## add ./lib directory to sys.path so that local modules can be found
import os, sys;

sys.path.append(os.path.abspath("."))
# print(sys.path)

## system level modules
import pandas as pds
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


def make_dataframe (file_name, subset_cols=[], exclude_cols=[], nrows=None, lowercase_col_names=True,
                    replace_spaces=True, file_type="tsv", delimiter="\t", sheet_name=0, file_archive_name=""):
    """
    Builds a pandas dataframe from the designated file.
    
    Args:
        file_name: The name of the file containing the data for the dataframe. If the file is not in the same directory, then specify the path as part of the file name.
        subset_cols: Specifies a specific of subset of columns to be included in the dataframe.
        exclude_cols: Specifies a specific of subset of columns to be excluded from the dataframe.
        nrows: Specifies the number of rows to be returned in the dataframe (useful for testing).
        lowercase_col_names: If true, the column names are converted to lower case.
        replace_spaces: If true, spaces in column names are replaced with spaces.
        file_type: Speicfies the type of file. Current acceptable file types are tsv, csv, and excel. Note that when using excel, you may need to specify a sheet name.
        delimiter: Specifies the delimiter character used between fields.
        sheet_name: If the files is an Excel spreadsheet, this parameter specifies a particular sheet.
        archive_name: If the file_name is contained in an zip or file, this is the name of archive file.
    Returns:
        Pandas dataframe
    """
    ## normalize paramaters for use with pandas
    if len(subset_cols) < 1: subset_cols = None
    if len(exclude_cols) < 1: exclude_cols = None
    
    ## check if file is contained in an archive
    file_archive = None
    if len(file_archive_name) > 1:
        file_archive = zipfile.ZipFile(file_archive_name, "r")
    
    ## load data from file
    if "tsv" == file_type.lower() or "csv" == file_type.lower():
        if None != file_archive:
            df = pds.read_csv(file_archive.open(file_name), sep=delimiter, nrows=nrows)
        else:
            df = pds.read_csv(file_name, sep=delimiter, nrows=nrows)
    elif "excel" == file_type.lower():
        if None != file_archive:
            df = pds.read_excel(file_archive.open(file_name), sheet_name=sheet_name, nrows=nrows)
        else:
            df = pds.read_excel(file_name, sheet_name=sheet_name, nrows=nrows)
    elif "multi-sheet-excel" == file_type.lower():
        if None != file_archive:
            df = pds.concat(
                pds.read_excel(file_archive.open(file_name), sheet_name=None, ignore_index=True, nrows=nrows))
        else:
            df = pds.concat(pds.read_excel(file_name, sheet_name=None, ignore_index=True, nrows=nrows))
    
    ## clean column names
    df = clean_dataframe_column_names(df, lowercase_col_names, replace_spaces)
    
    ## create subset of columns
    ## note: since column names are case sensitive, this needs to happen after cleaning column names
    if subset_cols:
        df = df[subset_cols]
    
    ## return dataframe
    return df


def clean_dataframe_column_names (df, lowercase_col_names=True, replace_spaces=True):
    """
    Changes the column names of a dataframe into a standard format. The default settings change the column names to:
      - lower case
      - replaces spaces with underscores
    Args:
        df: The dataframe whose columns will be cleaned.
        lowercase_col_names: If true, the column names are converted to lower case.
        replace_spaces: If true, spaces in column names are replaced with spaces.
    Returns:
      Pandas dataframe
    """
    
    ## clean column names
    if lowercase_col_names:
        df.columns = [c.strip().lower() for c in df.columns]
    
    if replace_spaces:
        df.columns = [c.replace(" ", "_") for c in df.columns]
    
    return df


def make_dataframe_dictionary (file_name, subset_cols=[], exclude_cols=[], nrows=None, lowercase_col_names=True,
                               replace_spaces=True, file_type="tsv", delimiter="\t", sheet_name=0,
                               file_archive_name=""):
    """
    Builds a dictionary based on the structure of the pandas dataframe generated from the designated file.
    The dictionary is oriented for records.
    E.g.:
      [
        {
          'col1': 1, 
          'col2': 0.5
        }, 
        {
          'col1': 2, 
          'col2': 0.75
        }
      ]

    Essentially, this function is a shortcut for calling make_dataframe() and then transforming the result into a dictionary. 
    E.g.:
      df = make_dataframe(file_name)
      dictdf = dictdf = df.to_dict(orient="records")
    
    
    Args:
        file_name: The name of the file containing the data for the dataframe. If the file is not in the same directory, then specify the path as part of the file name.
        subset_cols: Specifies a specific of subset of columns to be included in the dataframe.
        exclude_cols: Specifies a specific of subset of columns to be excluded from the dataframe.
        nrows: Specifies the number of rows to be returned in the dataframe (useful for testing).
        lowercase_col_names: If true, the column names are converted to lower case.
        replace_spaces: If true, spaces in column names are replaced with spaces.
        file_type: Speicfies the type of file. Current acceptable file types are tsv, csv, and excel. Note that when using excel, you may need to specify a sheet name.
        delimiter: Specifies the delimiter character used between fields.
        sheet_name: If the files is an Excel spreadsheet, this parameter specifies a particular sheet.
        archive_name: If the file_name is contained in an zip or file, this is the name of archive file.
    Returns:
        Dictionary built from a Pandas dataframe.
    """
    df = make_dataframe(file_name, subset_cols=[], exclude_cols=[], nrows=None, lowercase_col_names=True, \
                        replace_spaces=True, file_type="tsv", delimiter=delimiter, sheet_name=sheet_name,
                        file_archive_name=file_archive_name)
    return df.to_dict(orient="records")


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


def convert_dict_list_to_json_list (dict_list):
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


def make_lat_lon (latitude, longitude):
    # latitude = "" if pds.isnull(latitude) else str(latitude).strip().replace('\n', '')
    # longitude = "" if pds.isnull(longitude) else str(longitude).strip().replace('\n', '')
    latitude = None if pds.isnull(latitude) else float(latitude)
    longitude = None if pds.isnull(longitude) else float(longitude)

    if (not (latitude is None)) and (not (longitude is None)):
        return f"{latitude} {longitude}".strip()
    else:
        return None


def make_nmdc_dict_list (dictionary,
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

    def map_slot_to_entity (slot_map, record):
        """
        Connects a slot to an entity whose type is specified in a map/dict. 
        Example 2, the map: 
            {'part_of': project_gold_ids'}
        specifies that the part_of slot connects to the record's project_ids values.

        Example 1, the map:
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


    def make_constructor_args (constructor_map, record):
        ## for every mapping between a key and data field create a dict
        ## of the parameters needed to instantiate the class
        constructor_dict = {}
        for key, field in constructor_map.items():
            ## if the fields is a tuple, index 0 is param dict, index 1 is the class
            ## e.g., lat_lon': ('lat_lon', nmdc.GeolocationValue)
            if type(()) == type(field):
                params = \
                    {
                        key: "" if pds.isnull(record[value]) else record[value] # we don't want null/NaN to be a value in the constructor
                        for key, value in  field[0].items()
                    }
                constructor_obj = field[1](**params)
                constructor_obj.type = field[1].class_class_curie
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
            if not hasattr(nmdc_class, af): setattr(nmdc_class, af, None)
            ## TODO ! throw a a warning

        if attribute_map:
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
            if (not pds.isnull(item)) and ('' != item) and not (item is None) and (key in attribute_fields):
                av = make_attribute_value(item)

                ## check if attribute has been mapped to a mixs term
                if attribute_map:
                    if key in attribute_map.keys():
                        mapped_attr = attribute_map[key]
                        setattr(obj, mapped_attr, av)
                    else:
                        setattr(obj, key, av)
                else:
                    setattr(obj, key, av)
        
        ## go though the attribute list and link slots to entities specified in slot map/dict
        ## for example: {'part_of': ({'id': 'project_gold_ids'}, nmdc.OmicsProcessing)}
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


def save_json_string_list (file_name, json_list):
    """
    Saves a list of json strings to a file.
    Args:
        file_name: The name of the file containing the data for the dataframe. If the file is not in the same directory, then specify the path as part of the file name.
        json_list: The list of json strings to be saved to file.
    Returns:
        Nothing.
    """
    ## merge json list into a single string
    json_str = "[\n" + ", ".join(json_list) + "\n]"
    
    with open(file_name, "w") as f:
        f.write(json_str)


def load_dict_from_json_file (file_name):
    """
    Creates and returns from a json file.
    Args:
      file_name: The name of the file containing the json formated data.
    Returns:
      A dict object containing the JSON dta.
    """
    with open(file_name, "r") as json_file:
        return json.load(json_file)


def make_dataframe_from_spec_file (data_spec_file, nrows=None):
    def make_df_from_file (data_source, nrows):
        file_type = data_source.file_type
        fname = data_source.file_name
        
        if 'file_archive_name' in data_source.keys():
            farchive = data_source.file_archive_name
            df = make_dataframe(fname, file_archive_name=farchive, file_type=file_type, nrows=nrows)
        else:
            df = make_dataframe(fname, file_type=file_type, nrows=nrows)
        
        return df
    
    def make_df (source, source_type='file_name'):
        name = source[0]
        data = source[1]
        data_source = source[1].data_source
        
        if source_type not in data_source.keys():
            return None
        
        ## get data from file
        if 'file_name' in data_source.keys():
            df = make_df_from_file(data_source, nrows=nrows)
        
        ## add extra columns
        if 'append_columns' in data.keys():
            for col in data.append_columns: df[col.name] = col.value
        
        ## rename columns
        if 'rename_slots' in data.keys():
            for slot in data.rename_slots: df.rename(columns={slot.old_name:slot.new_name}, inplace=True)
        
        ## filter rows by specific values
        if 'filters' in data.keys():
            for fltr in data.filters: df = df[df[fltr.field].isin(fltr.values)]
        
        ## select a subset of the columns
        if 'subset_cols' in data.keys():
            df = df[data.subset_cols]
        
        ## add 'nmdc_record_id' as a primary key
        if 'id_key' in data.keys():
            df['nmdc_record_id'] = df[data.id_key]
            df['nmdc_record_id'] = df['nmdc_record_id'].astype(str)  # ensure all keys are strings
        else:
            df.index.name = 'nmdc_record_id'  # rename the current index
            df.reset_index(inplace=True)  # turn index into a column
            df['nmdc_record_id'] = df['nmdc_record_id'].astype(str)  # ensure all keys are strings
        
        return df
    
    with open(data_spec_file, 'r') as input_file:
        spec = DottedDict(yaml.load(input_file, Loader=Loader))
    
    Data_source = namedtuple('Data_source', 'data name')
    
    dataframes = []
    for source in spec.data_sources.items():
        df = make_df(source)
        ds = Data_source(df, source[0])
        dataframes.append(ds)
    
    merged_df = merge_dataframes(dataframes)
    return merged_df


def merge_dataframes (dataframes, data_source_names=[]):
    merged_df = pds.DataFrame(columns=['nmdc_data_source', 'nmdc_record_id', 'attribute', 'value'])
    
    for idx, df in enumerate(dataframes):
        if 'pandas.core.frame.DataFrame' == type(df):
            data_source_name = data_source_names[idx]
            data = df
        else:
            data_source_name = df.name
            data = df.data
        
        ## convert data into an EAV structure
        eavdf = data.melt(id_vars=['nmdc_record_id'], var_name='attribute')
        eavdf['nmdc_data_source'] = data_source_name
        
        #merged_df = merged_df.append(eavdf, ignore_index=True)
        merged_df = merged_df.append(eavdf, ignore_index=True)
    
    return merged_df


def unpivot_dataframe (df, index='nmdc_record_id', columns='attribute', value='value',
                       splice=['nmdc_record_id', 'attribute', 'value']):
    ## reshape eav structure to row-column structure
    ## see: https://www.journaldev.com/33398/pandas-melt-unmelt-pivot-function
    if len(splice) > 0:
        df = df[splice].pivot(index=index, columns=columns)
    else:
        df = df.pivot(index=index, columns=columns)
    
    if len(df) > 0: df = df[value].reset_index()  # drop value hierarchical index
    df.columns.name = None  # remove column name attribute
    
    return df


def extract_table (merged_df, table_name):
    df = unpivot_dataframe(merged_df[merged_df.nmdc_data_source == table_name])

    ## replace an NaN values with None
    df = df.where(pds.notnull(df), None)
    return df


def make_gold_to_mixs_list(source_list, dataframe, table_name):
    target_list = []
    for item in source_list:
        ## check for special condition fo using dicts for linking objects
        if type({}) != type(item):
            ## check for gold to mixs mapping
            target_item = \
                get_mapped_term(dataframe, database='gold', table_name=table_name, source_field=item, target_field='mixs_term')
            
            if len(target_item) > 0:
                target_list.append(target_item)
            else:
                target_list.append(item)
    
    return target_list


def make_gold_to_mixs_map(source_list, dataframe, table_name):
    gold_to_mixs = {}
    for item in source_list:
        ## check for special condition fo using dicts for linking objects
        if type({}) != type(item):
            ## check for gold to mixs mapping
            mapped_item = \
                get_mapped_term(dataframe, database='gold', table_name=table_name, source_field=item, target_field='mixs_term')
            
            if len(mapped_item) > 0:
                gold_to_mixs[item] = mapped_item
            
    return gold_to_mixs


def get_gold_biosample_mixs_term(dataframe, source_field):
    return get_mapped_term(dataframe, 'gold', 'biosample',source_field, 'mixs_term')


def get_mapped_term(dataframe, database, table_name, source_field, target_field):
    return_val = \
        dataframe[(dataframe['database'].str.lower() == database.lower())
                   & (dataframe['table'].str.lower() == table_name.lower())
                   & (dataframe['field'].str.lower() == source_field.lower())]
    
    if len(return_val) > 0:
        return return_val[target_field].values[0] # if more than one match is found, only the first is returned
    else:
        return ""
    
    
def make_collection_date(year_val, month_val, day_val, hour_val="", minute_val=""):
    def pad_value(val, pad_len=2):
        s = str(val)
        return s.zfill(pad_len)
    
    return_val = ""
    year_val = year_val.strip()
    month_val = month_val.strip()
    day_val = day_val.strip()
    hour_val = hour_val.strip()
    minute_val = minute_val.strip()
    return_val = ""
    
    ## if a year isn't provided simply return the empty string
    if len(year_val) < 1:
        return ""
    else:
        return_val = pad_value(year_val, 4)
    
    if len(month_val) > 0:
        return_val = return_val + "-" + pad_value(month_val)
    
    ## we only days that have months assocated with them
    if (len(month_val) > 0) and (len(day_val) > 0):
        return_val = return_val + "-" + pad_value(day_val)

    ## we only want times with months and days associated with them
    if (len(month_val) > 0) and (len(day_val) > 0):
        if (len(hour_val) > 0) and (len(minute_val) > 0):
            return_val = return_val + "T" + pad_value(hour_val) + ":" + minute_val
        elif len(hour_val) > 0:
            return_val = return_val + "T" + pad_value(hour_val) + "00" # case for when no minute val is given
    
    return return_val


def make_study_dataframe (study_table, contact_table, proposals_table, result_cols=[]):
    ## subset dataframes
    contact_table_splice = contact_table[['contact_id', 'principal_investigator_name']].copy()
    proposals_table_splice = proposals_table[['gold_study', 'doi']].copy()
    
    ## left join data from contact
    temp1_df = pds.merge(study_table.copy(), contact_table_splice, how='left', on='contact_id')
    
    ## left join data from proposals
    temp2_df = pds.merge(temp1_df, proposals_table_splice, how='left', left_on='gold_id', right_on='gold_study')
    
    ## add prefix
    temp2_df.gold_id = "gold:" + temp2_df.gold_id
    temp2_df.gold_study = "gold:" + temp2_df.gold_study
    
    if len(result_cols) > 0:
        return temp2_df[result_cols]
    else:
        return temp2_df


def make_project_dataframe (project_table, study_table, contact_table, data_object_table=None, result_cols=[]):
    ## subset data
    study_table_splice = study_table[['study_id', 'gold_id']].copy()
    contact_table_splice = contact_table[['contact_id', 'principal_investigator_name']].copy()
  
    ## rename study.gold_id to study_gold_id
    study_table_splice.rename(columns={'gold_id': 'study_gold_id'}, inplace=True)
    
    ## inner join on study (project must be part of study)
    temp1_df = pds.merge(project_table, study_table_splice, how='inner', left_on='master_study_id', right_on='study_id')
    
    ## left join contact data
    temp2_df = pds.merge(temp1_df, contact_table_splice, how='left', left_on='pi_id', right_on='contact_id')
    
    ## add prefix
    temp2_df.gold_id = "gold:" + temp2_df.gold_id
    temp2_df.study_gold_id = "gold:" + temp2_df.study_gold_id

    if not (data_object_table is None):
        ## make copy and add prefix
        data_object_table = data_object_table.copy()
        data_object_table.gold_project_id = \
            data_object_table.gold_project_id.map(lambda x: x if 'gold:' == x[0:5] else 'gold:' + x)
        
        ## create a group concat for all file ids in the data objects
        groups = data_object_table.groupby('gold_project_id')['file_id']
        output_files = \
            pds.DataFrame(groups.apply(lambda x: ','.join(filter(None, x)))).drop_duplicates().reset_index()
        output_files.rename(columns={'file_id': 'output_file_ids'}, inplace=True)
        output_files['output_file_ids'] = output_files['output_file_ids'].astype(str)
        
        ## join project and output files
        temp2_df = pds.merge(temp2_df, output_files, how='left', left_on='gold_id', right_on='gold_project_id')
    
    if len(result_cols) > 0:
        return temp2_df[result_cols]
    else:
        return temp2_df


def make_biosample_dataframe (biosample_table, project_biosample_table, project_table, result_cols=[]):
    def make_collection_date_from_row(row):
        def _format_date_part_value(val):
            if pds.isnull(val): return ""
            
            if type("") == type(val):
                if '.' in val:
                    return val[0: val.find('.')].strip()
                else:
                    return val.strip()
            else:
                return str(int(val)).strip()
            
        year_val = _format_date_part_value(row['sample_collection_year'])
        month_val = _format_date_part_value(row['sample_collection_month'])
        day_val = _format_date_part_value(row['sample_collection_day'])
        hour_val = _format_date_part_value(row['sample_collection_hour'])
        minute_val = _format_date_part_value(row['sample_collection_minute'])
        
        return make_collection_date(year_val, month_val, day_val, hour_val, minute_val)
        
    ## subset data
    project_biosample_table_splice = project_biosample_table[['biosample_id', 'project_id']].copy()
    project_table_splice = project_table[['project_id', 'gold_id']].copy()
    
    ## add prefix
    project_table_splice.gold_id = "gold:" + project_table_splice.gold_id
    
    ## rename columns
    project_table_splice.rename(columns={'gold_id': 'project_gold_id'}, inplace=True)
    
    ## inner join on project_biosample and project; i.e., biosamples must be linked to project
    temp1_df = pds.merge(biosample_table, project_biosample_table_splice, how='inner', on='biosample_id')
    temp2_df = pds.merge(temp1_df, project_table_splice, how='inner', on='project_id')
    
    ## add collection date and lat_lon columns
    temp2_df['collection_date'] = temp2_df.apply(lambda row: make_collection_date_from_row(row), axis=1)
    temp2_df['lat_lon'] = temp2_df.apply(lambda row: make_lat_lon(row.latitude, row.longitude), axis=1)
    
    ## convert latitude and longitute columns to floats
    temp2_df['latitude'] = temp2_df['latitude'].map(lambda x: None if pds.isnull(x) else float(x))
    temp2_df['longitude'] = temp2_df['longitude'].map(lambda x: None if pds.isnull(x) else float(x))
    
    ## add gold prefix
    temp2_df['gold_id'] = 'gold:' + temp2_df['gold_id']
    
    ## biosample might belong to more than one project; so do the equivalent of a group_cat
    ## see: https://queirozf.com/entries/pandas-dataframe-groupby-examples
    ## see: https://stackoverflow.com/questions/18138693/replicating-group-concat-for-pandas-dataframe
    groups = \
        temp2_df.groupby('biosample_id')['project_gold_id'].apply(lambda pid:','.join(filter(None, pid))).reset_index()
    groups.rename(columns={'project_gold_id':'project_gold_ids'}, inplace=True)
    
    # join concat groups to dataframe
    temp3_df = pds.merge(temp2_df, groups, how='left', on='biosample_id')
    
    ## remove uneeded columns & drop dups
    temp3_df.drop(columns=['project_gold_id'], inplace=True)
    temp3_df.drop_duplicates(inplace=True)
    
    if len(result_cols) > 0:
        return temp3_df[result_cols]
    else:
        return temp3_df


def  make_jgi_emsl_dataframe(jgi_emsl_table, study_table, result_cols=[]):
    ## subset data
    study_table_splice = study_table[['study_id', 'gold_id']].copy()
    
    ## inner join jgi-emsl data on study (must be part of study)
    temp1_df = pds.merge(jgi_emsl_table, study_table_splice, how='inner', left_on='gold_study_id', right_on='gold_id')

    ## add prefix
    temp1_df.gold_id = "gold:" + temp1_df.gold_id
    temp1_df.gold_study_id = "gold:" + temp1_df.gold_study_id

    if len(result_cols) > 0:
        return temp1_df[result_cols]
    else:
        return temp1_df


def make_emsl_dataframe (emsl_table, jgi_emsl_table, study_table, result_cols=[]):
    ## subset data
    study_table_splice = study_table[['study_id', 'gold_id']].copy()
    jgi_emsl_table_splice = jgi_emsl_table[['gold_study_id', 'emsl_proposal_id']]
    
    ## inner join jgi-emsl data on study (must be part of study)
    temp1_df = \
        pds.merge(jgi_emsl_table_splice, study_table_splice, how='inner', left_on='gold_study_id', right_on='gold_id')
    
    ## inner join emsl data on jgi-emsl proposal ids
    temp2_df = pds.merge(emsl_table, temp1_df, how='inner', on='emsl_proposal_id')
    
    ## add data obect id column
    temp2_df["data_object_id"] = "output_"
    temp2_df["data_object_id"] = temp2_df["data_object_id"] + temp2_df["dataset_id"].map(str) # build data object id
    
    ## add data object name column
    temp2_df["data_object_name"] = "output: "
    temp2_df["data_object_name"] = temp2_df["data_object_name"] + temp2_df["dataset_name"].map(str)  # build data object id
    
    ## add prefix
    temp2_df.gold_id = "gold:" + temp2_df.gold_id
    temp2_df.gold_study_id = "gold:" + temp2_df.gold_study_id
    temp2_df.dataset_id = "emsl:" + temp2_df.dataset_id
    temp2_df.data_object_id = "emsl:" + temp2_df.data_object_id
    
    if len(result_cols) > 0:
        return temp2_df[result_cols]
    else:
        return temp2_df


def make_data_objects_dataframe (faa_table, fna_table, fastq_table, project_table, result_cols=[]):
    ## subset data
    project_table_splice = project_table[['gold_id']].copy()
    
    ## copy tables
    faa_df = faa_table.copy()
    fna_df = fna_table.copy()
    fastq_df = fastq_table.copy()

    ## add prefixes for faa, fna, and fastq files
    faa_df.file_id = "nmdc:" + faa_df.file_id 
    fna_df.file_id = "nmdc:" + fna_df.file_id 
    fastq_df.file_id = "jgi:" + fastq_df.file_id

    ## merge tables
    data_objects = pds.concat([faa_df, fna_df, fastq_df], axis=0)
    
    ## inner joing data objects (e.g., faa, fna, fasq) to projects
    temp1_df = \
        pds.merge(data_objects, project_table_splice, how='inner', left_on='gold_project_id', right_on='gold_id')
    
    ## add prefix for gold
    temp1_df.gold_project_id = "gold:" + temp1_df.gold_project_id
    temp1_df.gold_id = "gold:" + temp1_df.gold_id
    
    if len(result_cols) > 0:
        return temp1_df[result_cols]
    else:
        return temp1_df[data_objects.columns]
