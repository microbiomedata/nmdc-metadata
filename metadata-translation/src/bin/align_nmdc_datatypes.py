import os, sys
sys.path.append(os.path.abspath('../../../schema')) # add path nmdc schema files and modules

import yaml
import json
from yaml import CLoader as Loader, CDumper as Dumper
from collections import namedtuple
from pprint import pprint
import pandas as pds
import jsonasobj
import nmdc
import lib.data_operations as dop

# TODO: convert triad value in complex object; convert depth the measurement unit ("meters")

def get_json(file_path):
    ## load json
    with open(file_path, 'r') as in_file:
        json_list =  json.load(in_file)
    return json_list

def save_json(json_list, file_path):
    ## save json with changed data types
    with open(file_path, 'w') as out_file:
        json.dump(json_list, out_file, indent=2)
    return json_list

def convert_env_triad(attribute_value):
    ## replace '_' with ':' in curie
    curie_val = attribute_value_to_string(attribute_value)
    curie_val = curie_val.replace('_', ':')
    
    return nmdc.ControlledTermValue(curie_val)

def attribute_value_to_datatype(attribute_value, data_type='string'):
    val = attribute_value['has_raw_value']
    if data_type == 'integer':
        return int(val)
    else:
        return str(val)

def attribute_value_to_int(attribute_value):
    return attribute_value_to_datatype(attribute_value, 'integer')

def attribute_value_to_string(attribute_value):
    return attribute_value_to_datatype(attribute_value, 'string')

def align_data_object(file_path):
    json_list = get_json(file_path) # load json

    ## change file size bytes to int
    for item in json_list:
        item['file_size_bytes'] = attribute_value_to_int(item['file_size_bytes'])

    save_json(json_list, file_path) # save json
    
def align_emsl_data_object():
    align_data_object('output/nmdc_etl/emsl_data_objects.json')

def align_jgi_data_object():
    align_data_object('output/nmdc_etl/faa_fna_fastq_data_objects.json')

def align_biosample(file_path):
    json_list = get_json(file_path) # load json

    ## change file size bytes to int
    for item in json_list:
        item['env_broad_scale'] = convert_env_triad(item['env_broad_scale'])
        print(item['env_broad_scale'])

    save_json(json_list, file_path) # save json

def align_gold_biosample():
    align_biosample('output/nmdc_etl/gold_biosample.json')


def main():
    pass


if __name__ == '__main__':
    main()