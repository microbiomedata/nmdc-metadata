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


def align_data_object(file_path):
    ## load json
    with open(file_path, 'r') as in_file:
        json_list =  json.load(in_file)

    ## change file size bytes to int
    for item in json_list:
        val = int(item['file_size_bytes']['has_raw_value'])
        item['file_size_bytes'] = val

    ## save json with changed data types
    with open(file_path, 'w') as out_file:
        json.dump(json_list, out_file, indent=2)

def align_emsl_data_object():
    align_data_object('output/nmdc_etl/emsl_data_objects.json')

def align_jgi_data_object():
    align_data_object('output/nmdc_etl/faa_fna_fastq_data_objects.json')

def main():
    pass


if __name__ == '__main__':
    main()